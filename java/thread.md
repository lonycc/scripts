# java 线程与锁

```
public class Test {
    public static void main(String[] args) throws InterruptedException {
        Thread myThread = new Thread() {
            public void run() {
                System.out.println("hello from new thread");
            }
        };
        myThread.start();
        //Thread.yield();  //当前线程让出对处理器的占用, 若没有这句, 几乎main线程总是先执行
        //Thread.sleep(1); //当前线程睡眠, 有这句几乎总是new线程先执行
        System.out.println("hello from main thread");
        myThread.interrupt();  //中断myThread
        myThread.join();  //等待myThread线程结束
    }
 }
 ```
 
> 竞态条件, 由于多个线程同时使用共享内存, 它们往往"打成一片". 可以用java对象原生的内置锁(synchronized)来同步.

```
class Counter {
  private int count = 0;
  public synchronized void increment() { ++count; }
  public synchorized int getCount() { return count; }
}
```

- 编译器的静态优化可能打乱代码执行顺序;
- JVM的动态优化也会打乱代码的执行顺序;
- 硬件可通过乱序执行优化其性能;

> 死锁, 使用多把锁, 线程之间发生死锁.

```
class Philosopher extends Thread {
    private Object first, second;
    private Random random;

    public Philosopher(Object left, Object right) {
        if (System.identityHashCode(left) < System.identityHashCode(right)) {
            first = left;
            second = right;
        } else {
            first = right;
            second = left;
        }
        random = new Random();
    }

    public void run() {
        try {
            while(true) {
                Thread.sleep(random.nextInt(1000));
                synchronized (first) { //获取first对象的内置锁
                    synchronized (second) {
                        Thread.sleep(random.nextInt(1000));
                    }
                }
            }
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }
}
```

> 来自 Alien Method 方法的危害, 可能会产生死锁, 需要进行 defensive copy

