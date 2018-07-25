
**进程之间通信(IPC)方式, 管道(命名/匿名)、消息队列、信号量、共享内存和socket**

**可以通过posix_mkfifo()创建命名管道, 创建后就是一个文件; 多个进程可以对这个管道读写**

## 消息队列

```
// 使用ftok创建一个键名，注意这个函数的第二个参数“需要一个字符的字符串”
$key = ftok( __DIR__, 'a' );

// 然后使用msg_get_queue创建一个消息队列
$queue = msg_get_queue( $key, 0666 );

// 使用msg_stat_queue函数可以查看这个消息队列的信息，而使用msg_set_queue函数则可以修改这些信息
//var_dump( msg_stat_queue( $queue ) );

// fork进程
$pid = pcntl_fork();
if( $pid < 0 ){
  exit( 'fork error'.PHP_EOL );
} else if( $pid > 0 ) {
  // 在父进程中
  
  // 使用msg_receive()函数获取消息
  msg_receive( $queue, 0, $msgtype, 1024, $message );
  
  echo $message.PHP_EOL;
  
  // 用完了记得清理删除消息队列
  msg_remove_queue( $queue );
  pcnlt_wait( $status );
} else if( 0 == $pid ) {
  // 在子进程中
  
  // 向消息队列中写入消息
  // 使用msg_send()向消息队列中写入消息，具体可以参考文档内容
  msg_send( $queue, 1, "helloword" );
  
  exit;
}
```


**共享内存和信号量**

> 当前进程获取将使用的共享内存的信号量

> 如果信号量大于0，那么就表示这块儿共享资源可以使用，然后进程将信号量减1

> 如果信号量为0，则进程进入休眠状态一直到信号量大于0，进程唤醒开始从1
 
```
$sem_key = ftok( __FILE__, 'b' );
$sem_id = sem_get( $sem_key );
// shm key
$shm_key = ftok( __FILE__, 'm' );
$shm_id = shm_attach( $shm_key, 1024, 0666 );
const SHM_VAR = 1;
$child_pid = [];
// fork 2 child process
for( $i = 1; $i <= 2; $i++ ){
  $pid = pcntl_fork();
  if( $pid < 0 ){
    exit();
  } else if( 0 == $pid ) {
  // 获取锁
  sem_acquire( $sem_id );
  if( shm_has_var( $shm_id, SHM_VAR ) ){
    $counter = shm_get_var( $shm_id, SHM_VAR );
    $counter += 1;
    shm_put_var( $shm_id, SHM_VAR, $counter );
  } else {
    $counter = 1;
    shm_put_var( $shm_id, SHM_VAR, $counter );
  }
  // 释放锁，一定要记得释放，不然就一直会被阻锁死
  sem_release( $sem_id );
  exit;
  } else if( $pid > 0 ) {
    $child_pid[] = $pid;
  }
}
while( !empty( $child_pid ) ){
  foreach( $child_pid as $pid_key => $pid_item ){
    pcntl_waitpid( $pid_item, $status, WNOHANG );
  unset( $child_pid[ $pid_key ] );
  }
}
// 休眠2秒钟，2个子进程都执行完毕了
sleep( 2 );
echo '最终结果'.shm_get_var( $shm_id, SHM_VAR ).PHP_EOL;
// 记得删除共享内存数据，删除共享内存是有顺序的，先remove后detach，顺序反过来php可能会报错
shm_remove( $shm_id );
shm_detach( $shm_id );
```

**socket实现, fork指定个数子进程**

```
$host = '0.0.0.0';
$port = 9999;
// 创建一个tcp socket
$listen_socket = socket_create( AF_INET, SOCK_STREAM, SOL_TCP );
// 将socket bind到IP：port上
socket_bind( $listen_socket, $host, $port );
// 开始监听socket
socket_listen( $listen_socket );
// 给主进程换个名字
cli_set_process_title( 'phpserver master process' );
// 按照数量fork出固定个数子进程
for( $i = 1; $i <= 10; $i++ ){
  $pid = pcntl_fork();
  if( 0 == $pid ){
    cli_set_process_title( 'phpserver worker process' );
    while( true ){
    $conn_socket = socket_accept( $listen_socket );
    $msg = "helloworld\r\n";
    socket_write( $conn_socket, $msg, strlen( $msg ) );
    socket_close( $conn_socket );
  }
  }
}
// 主进程不可以退出，代码演示比较粗暴，为了不保证退出直接走while循环，休眠一秒钟
// 实际上，主进程真正该做的应该是收集子进程pid，监控各个子进程的状态等等
while( true ){
  sleep( 1 );
}
socket_close( $connection_socket );
```

**IO多路复用, 依然是同步通信方式; select/poll/epoll三种方案, epoll解决了c10k问题;**

```
$base = new EventBase();
echo "特性：".PHP_EOL;
$features = $base->getFeatures();
// 看不到这个判断条件的，请反思自己“位运算”相关欠缺
if( $features & EventConfig::FEATURE_ET ){
  echo "边缘触发".PHP_EOL;
}
if( $features & EventConfig::FEATURE_O1 ){
  echo "O1添加删除事件".PHP_EOL;
}
if( $features & EventConfig::FEATURE_FDS ){
  echo "任意文件描述符，不光socket".PHP_EOL;
}
```
