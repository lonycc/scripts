```
<?php

// mongodb
$mongo = new Mongo( "127.0.0.1:27017" ); //连接mongodb
$db = $mongo->test;  // 选择数据库test
$collection = $db->person;  // 选择person集合
$obj = $collection->findOne();   // 查询集合里面一条文档
var_dump( $obj );


// memcache
$memcache = memcache_connect('localhost', 11211) or die(memcache_error());
$memcache->set("str_key", "String to store in memcached");
$memcache->set("num_key", 123);

$object = new StdClass;
$object->attribute = 'test';
$memcache->set("obj_key", $object);
$array = Array('assoc'=>123, 345, 567);
$memcache->set("arr_key", $array);

var_dump($memcache->get('str_key'));
var_dump($memcache->get('num_key'));
var_dump($memcache->get('obj_key'));
var_dump($memcache->get('arr_key'));
$memcache->flush();  //清除所有数据
$memcache->close();  //关闭连接


// SQLite单文件，单机，零配置，无用户管理，适合嵌入式应用。
// php接口
class MyDB extends SQLite3{
   function __construct(){
       $this->open('test.db');
   }
}
$db = new MyDB();  //实例化一个SQLite3对象
// 事务性操作，如create、insert、update、delete，则使用$db->exec($sql);
// 查询操作，select，使用$db->query($sql);
while ( $row = $result->fetchArray(SQLITE3_ASSOC) )
{
    $row['column_name'];
}
$db->changes(void);  //返回最近一次sql改变数据表的行
$db->close(void);   //关闭数据库连接
$db->escapeString(string $value);  //返回一个转义后的字符串
$db->lastErrorMsg(void);     //返回最近一次失败的SQLite请求信息
$db->lastErrorCode(void);   //返回最近一次失败的SQLite请求代码
public void SQLite3::open(filename,flags,encryption_key){}  //打开一个SQLite3连接，如果filename赋值为':memory'，那么将在ram中创建一个内存数据库，只在当前session中有效。flags可选，用于判断是否打开SQLite数据库，默认使用SQLITE3_OPEN_READWRITE | SQLITE3_OPEN_CREATE时打开。


// pdo_oci 连接 oracle
$tns="(DESCRIPTION = (ADDRESS_LIST = (ADDRESS = (PROTOCOL = TCP)(HOST = 192.168.x.x)(PORT = 1521)))(CONNECT_DATA = (SID = domain)))";
$oracleUser = 'username';
$oraclePass = 'password';
try {
    $oracle = new PDO("oci:dbname=".$tns, $oracleUser, $oraclePass, array(PDO::ATTR_PERSISTENT => TRUE));
    $oracle->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
    $oracle->setAttribute(PDO::ATTR_CASE,  PDO::CASE_LOWER);
	echo 'good';
} catch (PDOException $e) {
    echo 'Connection failed: ' . $e->getMessage();
}
