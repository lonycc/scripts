# 设计模式, 解决某类问题的最佳实践

## 单例模式: 创建型模式,它会限制应用程序,使其只能创建某一特定类类型的一个单一的实例,需要用静态定义属性和方法
```
class Singleton
{
  static private $_instance = NULL;
  private function __construct(){}  //这样就能限制new一个实例
  static function getInstance(){
     if(self::$_instance == NULL){
         self::$_instance = new Singleton();
     }
     return self::$_instance;
   }
}
$obj = Singleton::getInstance();
$obj2 = Singleton::getInstance(); //这里$obj2和$obj指向了Singleton的同一个实例
```

## 工厂模式: 用于创建多种不同类型的类的多个对象

```
abstract class Factory{
    static function Crate($type)
    {
        //Validate $type
        return new Factory();
    }
}
```

## 组合模式: 一个类的类型可以由另外一些类的类型组合

```
abstract class WorkUnit{
   abstract function add(WorkUnit $obj);
   abstract function remove(WorkUnit $obj);
   ...
}
class E1 extends WorkUnit{
    private $_elements = array();
    function add(WorkUnit $obj){
         $this->$_elements[] = $obj;
    }
}
clas E2 extends WorkUnit{
     function add(WorkUnit $obj){
          return $obj;   //or return false
      }
}
$obj = new E1();
$obj2 = new E2();
$obj->add($obj2);
```

## 策略模式: 一个接口, 多个类关联

```
interface Filter{ function filter($str); }
class Filter1 implements Filter{ function filter($str){ return $str; }
class Filter2 implements Filter{ function filter($str){ return $str; }
class Formdate {
    private $_data = NULL;
    function __construct($input){
           $this->_data = $input;
     }
     function process(Filter $type){
            $this->_data = $type->filter($this->_data);
      }
}
```

<br/><br/>

```
class A
{
   public static function get_self()
   {
       return new self();
   }
   public static function get_static()
   {
       return new static();
   }
}
class B extends A {}   //B继承A,self绑定A，因为它在A中定义，static绑定被引用类
echo get_class(B::get_self());  //A
echo get_class(B::get_static());  //B
echo get_class(A::get_static());  //A

class A
{
   public function create1()
   {
       $class = get_class($this);
       return new $class();
   }
   public function create2()
   {
        return new static();
   }
}
class B extends A {}
$b = new B();
var_dump(get_class($b->create1()),get_class($b->create2()));
```


> this,self,parent

> this是在实例化的时候来确定指向谁.

> self指向类本身,不指向任何已经实例化的对象，一般self用来指向类中的静态变量.

> parent指向父类的指针，一般用于调用父类的构造函数.


## 单例类
```
//final关键字防止类被继承
final class Danli
{
    private static $_instance;
    private function __construct()
    {
        //防止外部实例化对象
        $this->num = mt_rand(10000,99999);
    }
    private function __clone()
    {
        //防止对象被复制
        trigger_error('clone is not allowed!',E_USER_ERROR);
    }
    //单例方法,用于访问实例的公共静态方法
    public static function getInstance(){
        //常用getInstance()进行实例化单例类,通过instanceof操作符检测类是否已经实例化
        if ( !(self::$_instance instanceof self) )
        {
            self::$_instance = new self;
        }
        return self::$_instance;
    }
    public function test()
    {
        echo 'succeed';
    }
}
$danli = Danli::getInstanceof();
$danli->test();
$danli_clone = clone $danli; //复制对象会导致E_USER_ERROR错误
```

`uniqid(prefix, more_entropy);`  //基于以微妙计的当前时间，生成一个唯一的ID。

`get_class();`  //获取类

`get_class_methods();` //获取方法

`get_object_vars();` //获取变量

`var_dump($a instanceof A);`  //对象$a是否类A的一个实例

`error_reporting(E_ALL & ~E_WARNING & ~E_NOTICE & ~E_STRICT );` //忽略警告、提示、严格模式

`set_time_limit(0);` //不限运行时间

`date_default_timezone_set(timezone);`  //设置默认时区

`·join("!",array);` //将数组组合成一个字符串, 用!分隔数组元素, 同`implode('!', array);`

`function func_name($arg1, $arg2){}`  //参数的传递，值传递$a不会改变函数外部的值，引用传递&$a可用于修改参数值。

`int func_num_args(void)`  //获得传递给函数的参数个数

`mixed func_get_arg(int $arg_num)`  //获得指定索引号的参数

`array func_get_args(void)`  //获得数组形式的函数参数列表

`array get_extension_funcs(string $module_name)` //根据模块名返回函数

`bool dl(string $library)`   //载入制定参数library的php扩展

`bool extension_loaded(string $name)`   //检查一个扩展是否加载

`string get_class([ object $obj])`  //返回对象实例obj所属类的名字

`bool is_callable(callable $name [, bool $syntax_only = false [, string &$callable_name]])`  //验证变量的内容能否作为函数调用

`mixed var_export(mixed $expr [, bool $return ])`  //返回一个变量的字符串表示

`function foo(){echo "a";}  $a='foo'; $a();`  //可变函数

`$foo=new Obj(); $func="vari"; $foo->$func();` //调用一个对象的方法

`bool spl_autoload_register( [ callback $autoload_func] )` //注册__autoload()函数

`function __autoload($class_name){require_once $class_name . '.php';}`  //使用尚未被定义的类时自动调用, __autoload()应该被放置在实例化对象的脚本中

`void spl_autoload(string $class_name [, string $file_extensions ])`   //__autoload(）函数的默认实现


## 函数的引用返回
```
function &test()
{
    static $b = 0; //定义静态变量
    $b = $b+1;
    echo $b;
    return $b;
}
$a = test(); //输出$b的值为1，这只是普通的函数调用
$a = 5; $a = test(); //输出$b的值为2
$a = &test(); //输出$b的值为3，将return $b中的$b变量的内存地址与$a变量的内存地址指向了同一个地方，即$a = &$b，所以改变了$a的值，同时也改变了$b的值
$a = 5; $a = test(); //输出$b的值为6,因为$a和$b两个变量指向同一个内存地址,$a值改变了，$b值也改变了
```

## 对象的引用
```
class A{}
$b = new A;
$c = $b; //对象的复制通过引用来实现，等效于 $c = &$b;
//若你希望建立一个对象的副本，用__clone来实现。
$c = null; //清除一个对象引用
```

## 取消引用
```
$a = 1;
$b = &$a;
unset($b); //不会unset $a
//unset只是删除引用，引用的内容还在
```

## 全局变量

`global $var;`  //相当于`$var = &$GLOBALS['var'];`, `unset($var)`不会unset全局变量


## php引用&

`$a = "ABC";`

`$b = &$a;`

> $a和$b都指向"ABC", 两者有一个变化另一个也变化

`function test(&$a);` //这里是函数的引用参数


## 匿名函数

> 允许临时创建一个没有指定名称的函数, 经常用于回调函数的参数值, 匿名函数通过Closure类来实现.

`$greet = function($name){}; $greet('abc');`

```
break语句
break n; 跳出n重循环
goto语句
用于直接跳到标志处
goto end;
end:
...;
continue语句
用于跳出本重循环后面代码

declare语句
declare(encoding='ISO-8859-1');


返回值
return -1; 一般表示执行不成功
return 0;一般表示执行成功

return 0;表示假
return 1;表示真
```


## 扩展PHP内置的异常类
```
class Exception
{
    protected $message = 'Unknown exception';  //异常信息
    protected $code = 0;   // 用户自定义异常代码
    protected $file;     // 发生异常的文件名
    protected $line;     // 发生异常的代码行号

    function __construct($message = null, $code = 0);

    final function getMessage();  // 返回异常信息
    final function getCode();     // 返回异常代码
    final function getFile();     // 返回发生异常的文件名
    final function getLine();     // 返回发生异常的代码行号
    final function getTrace();    // backtrace() 数组
    final function getTraceAsString(); // 已格成化成字符串的 getTrace() 信息

    /* 可重载的方法 */
    function __toString();       // 可输出的字符串
}
```

> 自定义的类extends内置异常处理类，如果要重新定义构造函数，建议使用parent::construct($message,$code)来检查所有变量是否已赋值。



## 迭代器Iterator

> 一般我们用`foreach`来遍历数组, 如果要用`foreach`遍历对象, 那这个对象的类就要实现`Iterator`接口.

`$dir = new DirectoryIterator('.');`

```
Iterator extends Traversable {       //迭代器接口
    abstract public mixed current(void)  //返回当前元素
    abstract public scalar key(void)    //返回当前元素的key
    abstract public void next(void)     //下移一个元素
    abstract public void rewind(void)   //移到首元素
    abstract public boolean valid(void)  //判断是否还有后续元素
}
```

`$item instanceof Traversable;` #判断是否可迭代

> 可以用`IteratorAggregate`接口以替代实现所有的`Iterator`方法, `IteratorAggregate`只需要实现一个方法`IteratorAggregate::getIterator()`, 其返回一个实现了`Iterator`的类的实例.


## 生成器Generator, 实现了Iterator接口

```php
Generator implements Iterator {
    /* Methods */
    public mixed current ( void )
    public mixed key ( void )
    public void next ( void )
    public void rewind ( void )
    public mixed send ( mixed $value )
    public mixed throw ( Exception $exception )
    public bool valid ( void )
    public void __wakeup ( void )
}

function xrange($start, $end, $step = 1) {
    for ($i = $start; $i <= $end; $i += $step) {
        yield $i;
        $j = (yield $i);
    }
}

$n = 100000;
$startTime = microtime(true);
$startMemory = memory_get_usage();
$array = range(1, $n);

foreach($array as $a) {
}

echo memory_get_usage() - $startMemory, " bytes\n";
echo microtime(true) - $startTime. " ms\n";

$startTime = microtime(true);
$startMemory = memory_get_usage();
$g = xrange(1,$n);

foreach($g as $i) {
}

echo memory_get_usage() - $startMemory, " bytes\n";
echo microtime(true) - $startTime. " ms\n";
```

> Generator对象的中可迭代的元素就是所有yield语句返回的值的集合, 类似数组但不是数组, 遍历Generator对象的每次迭代都只会执行前一次yield语句之后的代码，而且碰到yield语句就会返回一个值, 相当于从generator函数中返回.
这有点像挂起一个进程（线程）的执行, 然后又启动它继续执行, 周而复始直到进程（线程）执行中止.



## 自动加载类
```
function class_loader($class)
{
    require($class.'.php');
}
```

`spl_autoload_register('class_loader');`


## 类与对象

> 当一个方法活属性在类定义内部被调用时, 有一个可用的伪变量$this.

> 面向对象两大原则：模块化(抽象)/封装(访问控制/可见性).

> 类的定义: `$var = new ClassA();`

> 类的属性和方法, 对象操作符. `$var->propertyName;  $var->methodName();`

> 删除对象 `unset($var);`

> 注意：类名不区分大小写, 类的方法也不区分. 也可以用`$var = new classa();` 在类定义内部, 可以用`new self`和`new parent`创建新对象.


**类常量**

`const a = 'acfun';` //能被类的全部实例访问

`$obj = new ClassA();`

`$obj::a;`  //实例访问

`ClassA::a;`  //a可以为属性或方法,但a中不能有`$this`

`self::a;`  //在类内部引用常量

**构造函数和析构函数**

`void __construct([ mixed $args [, $...]] )`  //一般用于对象的初始化，用new创建类的一个实例时，构造函数自动调用。

`parent::construct`  //从父类继承构造方法

`void __destruct(void)`  //在某个对象的所有引用都被删除或者当对象被显式销毁时执行。

`unset($obj);`  //这会调用析构函数

> 注意: php总是调用刚刚被实例化的类的构造函数.

**访问控制（可见性）**

- `public`    公有, 可在任何地方访问, 可被修改

- `protected`  受保护, 可在自身以及子类和父类中访问, 不能在类之外访问

- `private`    私有, 只能在受定义的类中访问


> `var`定义的变量默认为`public`; 未加关键字定义的方法, 默认为`public`

**对象继承**

> 父类的 `public` 和 `protected` 属性和方法被继承

> `class A extends B`  对父类方法重写, 称为"多态"

> 方法重写, 方法名和参数必须完全一致


**范围解析操作符（::）**

> 用于访问静态成员/类变量, 或者覆盖类中的属性或方法, 可以用于类内部或外部.

> 类中静态方法和静态属性, 用范围解析操作符来引用, 不用实例化即可引用

`parent::func_name();`  //在子类中继承父类的方法

`class_name::class;`  //获取类class_name的完全限定名称

`parent::$var;`  //对父类变量$var进行访问

`self::$var;`    //对自身变量$var进行访问

`static::$var;`   //对父类或自身静态$var进行访问

**static关键字**

`public static $count = 0;`  //声明类属性或方法为`static`, 就可以不实例化类而直接访问.

`ClassName::$var;`

`ClassNmme:func();`

`$obj::func();`

> 静态方法中不能用伪变量`$this`.

**abstract抽象类**

> 定义为抽象的类不能被实例化, 抽象类中至少有一个抽象方法. 继承一个抽象类时, 子类必须定义父类中的所有抽象方法, 且访问控制和父类一样或大于父类.

`abstract class A{ abstract protected function getValue(); }` //抽象类中的方法一般只定义接口, 不定义实现

`class B extends A{protected function getValue(){return "fuck";} }`  //扩展类继承抽象类, 定义具体实现

`__toString()`   //当一个类的对象实例用作string类型时就会自动调用这个方法.


**对象接口**

> 接口中所有方法都是`public`, 所有方法都为空的. 可实现多个接口, 用逗号隔开, 接口也可用`extends`实现继承, 实现接口的类必须定义接口中的方法.

```
interface template{
    public function a($name,$var);
    public function b($temp);
}
class itemp implements template
{
	//关联
    public function a($name,$var){}
    public function b($temp){}
}
```

`interface b extends a{}`

`inteface a{const b=’fuck’;} echo a::b;`  //接口常量

**代码复用trait**

`class base {}`

`trait a {//定义属性和方法};`

`class son extends base {use a;}`

> 对于类son, 从base中继承的成员被trait方法覆盖, 而trait方法被自身方法覆盖. 对于多个trait, 在use声明列出, 用逗号分隔.

> 若两个trait插入了一个同名的方法, 则可能会产生冲突. 解决冲突的方法:

`use A, B { B::sTalk insteadof A; A::bTalk insteadof B; B::sTalk as talk; }`

as也可用于修改方法的访问属性,

`use A { sTalk as protected; }`

`use B { bTalk as private talk; }`

> trait中也可使用trait, 为了对使用的类施加强制要求, trait支持抽象方法的使用

> 静态成员可以被trait的方法引用, 但不能被trait定义, trait能够为使用的类定义静态方法

> trait可以定义属性, 使用trait的类不能定义同名属性

**类型提示**

```
class ClassA
{
    function doThis(ClassB $var){}   //$var将是一个ClassB类型的对象
}
```

**重载**

> 动态地创建类属性和方法, 通过魔术方法（这些魔术方法的参数不能通过引用传递）实现. 当调用当前环境下未定义或不可见的类属性或方法时, 重载方法会被调用. 所有重载方法必须被声明为`public`.

> 属性重载: 只能在对象中进行, 静态方法中不可调用.

`public void __set(string $name, mixed $value){$this->$name=$value; }`  //在给不可访问属性赋值时, `__set()`会被调用

`public mixed __get(string $name){return $value; }`  //读取不可访问属性的值时, `__get()`会被调用

`public bool __isset(string $name){return isset($this->$name); }`   //当对不可访问属性调用`isset()`或`empty()`时, `__isset()`会被调用

`public void __unset(string $name){unset($this->$name);}`   //当对不可访问属性调用`unset()`时, `__unset()`会被调用

**方法重载**

`public mixed __call(string $name, array $args)`  //在对象中调用一个不可访问的方法时, `__call()`会被调用

`public static mixed __callStatic(string $name, array $args)`  //用静态方式调用一个不可访问的方法时, `__callStatic()`会被调用


**魔术方法**

> 魔术方法在类中需要重新声明方法体.

`public array __sleep(void)`   //用于提交未提交的数据, 或清理对象等

`public __wakeup(void)`     //用于反序列操作中, 如重新建立数据库连接等

`string serialize(mixed $value)`   //序列化对象/数组, 返回一个包含了表示value的字节流的字符串. `serialize()`会检查类中是否存在`__sleep()`方法; 若存在, 先调用`__sleep()`方法, 再执行序列化操作

`mixed unserialize(string $str)`  //反序列化, 转换回php的值. `unserialize()`会检查是否存在一个`__wakeup()`方法，若存在，先调用`__wakeup()`方法, 预先准备对象所需资源

`public string __toString(void)`  //用于将类转为字符串

`mixed __invoke([$... ])`   //当尝试以调用函数的方式调用一个对象时, `__invoke()`方法会被自动调用. `$obj = new classA(); $obj(3);`

`static object __set_state(array $properties)`  //调用var_export()导出类时, 该方法被调用

**final关键字**

> 如果父类中方法定义为`final`, 则子类无法覆盖. 如果一个类定义为`final`, 则不能被继承. `final public function func_name(){}` / `final class classA {}`

**对象复制**

`$a = new Class();`

`$a->val = 1;`

`$b = $a;`

`$b->val =2;`

`echo $a->val;`  //2, 因为两个变量指向同一块内存地址

`$c = clone $a;`

`$c->val = 3;`  //这不会改变`$a->val`的值, 因为两个对象独立

`$obj1 = clone $obj2;`

`void __clone(void)`  //当复制完成时, 如果类中定义了`__clone()`方法, 则新创建的对象中的`__clone()`方法会被调用, 可用于修改属性的值.

**对象比较**

> 当使用比较运算符`==`比较两个对象变量时, 比较原则是: 如果两个对象的属性和属性值都相等, 而且两个对象是同一个类的实例, 那么这两个对象变量相等.

> 当使用全等运算符`===`时, 这两个对象变量一定要指向某个类的同一个实例(即同一个对象)

**类型约束**

> 函数的参数指定必须为对象/接口/数组或`callable`, 如果使用`NULL`作为参数的默认值, 那么在调用函数的时候仍可使用`NULL`作为实参.

`public function a(array $arr)`

**后期静态绑定**

> 使用`static::`不再被解析为定义当前方法所在的类, 而是在实际运行时计算的.

> 使用`self::`或者`__CLASS__`对当前类的静态引用, 取决于定义当前方法所在的类.

> 静态调用使用`self::`或`parent::`, 将转发调用信息.

**引用和对象**

> php的引用时别名, 就是两个变量名字指向相同的内容. 一个对象变量不保存整个对象的值, 只保存一个标识符来访问真正的对象内容. 当对象作为参数传递, 作为结果返回, 或者赋值给另外一个变量, 另外一个变量跟原来的不是引用的关系, 只是他们都保存着同一个标识符的拷贝, 这个标识符指向同一个对象的真正内容.

`$a = new A; $b = $a;`  //$a/$b都是同一个标识符的拷贝, ($a)=($b)=<id>

`$c = new A; $d = &$c;`  //$c/$d是引用, ($c, $d)=<id>

`$e = new A; function foo($obj){} foo($e);`   //($obj)=($e)=<id>

**对象序列化**

> 序列化一个对象将会保存对象的所有变量, 但不会保存对象的方法, 只会保存类的名字.

`$a = new A; $s= serialize($a);  file_put_contents('a.txt', $s);`   //序列化并保存在a.txt

`$s = file_get_contents('a.txt');  $a=unserialize($s);`    //从a.txt读入字符串并解序列化

<br/><br/>

## 命名空间

> 是一种封装事物的方法, 提供了一种将相关的类/接口/函数/常量组合到一起的途径, 避免了命名冲突.

```
declare(encoding='UTF-8');
namespace MyProject;    //命名空间必须在所有代码之前, 除declare外.
const OK = 1;
class Connection{...}
function connection(){...}

//同一个命名空间可以定义在多个文件中, 引用方式
require('namespace.php');
$obj = new \MyProject\Connection();


namespace MyProject\Sub\Level;   //层次化方式定义命名空间
const OK = 1;
clss Connection{...}
function connection(){...}

//引用方式
require('User.php');
$obj = new \MyProject\Sub\Level\User();
```

```
namespace MyProject {}

namespace AnotherProject {}
```

> 将全局的非命名空间中的代码与命名空间中的代码组合在一起, 全局代码用一个不带名字的namaspace语句加上{}.

> 文件系统中访问一个文件的三种方式：

- 1.相对文件名形式, 如a.txt. 解析为当前目录下的a.txt.

- 2.相对路径名形式, 如test/a.txt. 解析为当目录下的test目录下的a.txt.

- 3.绝对路径名形式, 如/main/a.txt. 解析为/main/a.txt.


`$a = new classA();   classA::foo();`

`$a = new subnamespace\classA();  subnamespace\classA::foo();`

`$a = new \root\classA();   \root\classA::foo();`

> 访问任意全局类/函数或常量, 都可以使用完全限定名称, 例如`\strlen`或`\Exception`或`\INI_ALL`.

```
namespace Foo;
function strlen() {}
const INI_ALL = 3;
class Exception {}
$a = \strlen('hi’);
$b = \INI_ALL;
$c = new \Exception('error’);
```

## 命名空间和动态语言特性

> 必须使用完全限定名称（包括命名空间前缀的类的名称）。前导反斜杠可以省略。

`$a = '\namespace1\classA';  $a = 'namespace1\classA'; $obj = new $a;`

> 注意：完全限定名称只能放在单引号内，否则\会被解析为转义字符。

> 常量__NAMESPACE__的值包含当前命名空间名称的字符串。若为全局的不带名字的命名空间，则返回空字符串。

> __NAMESPACE__动态创建名称

```
namespace acFun;
function get($class_name)
{
   $a= __NAMESPACE__ .’\\’ . $class_name;
   return new $a;
}

namespace\func();  //调用函数fun();
namespace\sub\func();   //调用函数sub\func();
namespace\cname::method();  //调用静态方法cname::method();
$a=new namespace\sub\cname();
$b=namespace\CONSTANT;
```

## 使用命名空间: 别名/导入

> 允许通过别名引用或导入外部的完全限定名称, 可以为类或命名空间使用别名, 别名通过操作符use来实现.

```
namespace foo;
use My\Full\Classname as Another;
// 下面的例子与 use My\Full\NSname as NSname 相同
use My\Full\NSname;

// 导入一个全局类
use \ArrayObject;

$obj = new namespace\Another; // 实例化 foo\Another 对象
$obj = new Another; // 实例化 My\Full\Classname　对象
NSname\subns\func(); //调用函数 My\Full\NSname\subns\func
$a = new ArrayObject(array(1)); //实例化 ArrayObject 对象
// 如果不使用 "use \ArrayObject" ，则实例化一个 foo\ArrayObject 对象
```

## 全局空间

> 如果没有定义任何命名空间, 所有的类与函数的定义都是在全局空间. 在名称前加上前缀'\'表示该名称是全局空间中的名称.

## 后备全局函数/常量
```
namespace A\B\C;
class Exception extends \Exception {}

$a=new Exception('hi'); //$a 是类A\B\C\Exception 的一个对象
$b=new \Exception('hi'); // $b 是类 Exception 的一个对象

$c = new ArrayObject; // 致命错误, 找不到 A\B\C\ArrayObject 类
```

## 名称解析规则
```
namespace A;
use B\D, C\E as F;

// 函数调用

foo();      // 首先尝试调用定义在命名空间"A"中的函数foo()
            // 再尝试调用全局函数 "foo"

\foo();     // 调用全局空间函数 "foo"

my\foo();   // 调用定义在命名空间"A\my"中函数 "foo"

F();        // 首先尝试调用定义在命名空间"A"中的函数 "F"
            // 再尝试调用全局函数 "F"

// 类引用

new B();    // 创建命名空间 "A" 中定义的类 "B" 的一个对象
            // 如果未找到，则尝试自动装载类 "A\B"

new D();    // 使用导入规则，创建命名空间 "B" 中定义的类 "D" 的一个对象
            // 如果未找到，则尝试自动装载类 "B\D"

new F();    // 使用导入规则，创建命名空间 "C" 中定义的类 "E" 的一个对象
            // 如果未找到，则尝试自动装载类 "C\E"

new \B();   // 创建定义在全局空间中的类 "B" 的一个对象
            // 如果未发现，则尝试自动装载类 "B"

new \D();   // 创建定义在全局空间中的类 "D" 的一个对象
            // 如果未发现，则尝试自动装载类 "D"

new \F();   // 创建定义在全局空间中的类 "F" 的一个对象
            // 如果未发现，则尝试自动装载类 "F"

// 调用另一个命名空间中的静态方法或命名空间函数

B\foo();    // 调用命名空间 "A\B" 中函数 "foo"

B::foo();   // 调用命名空间 "A" 中定义的类 "B" 的 "foo" 方法
            // 如果未找到类 "A\B" ，则尝试自动装载类 "A\B"

D::foo();   // 使用导入规则，调用命名空间 "B" 中定义的类 "D" 的 "foo" 方法
            // 如果类 "B\D" 未找到，则尝试自动装载类 "B\D"

\B\foo();   // 调用命名空间 "B" 中的函数 "foo"

\B::foo();  // 调用全局空间中的类 "B" 的 "foo" 方法
            // 如果类 "B" 未找到，则尝试自动装载类 "B"

// 当前命名空间中的静态方法或函数

A\B::foo();   // 调用命名空间 "A\A" 中定义的类 "B" 的 "foo" 方法
              // 如果类 "A\A\B" 未找到，则尝试自动装载类 "A\A\B"

\A\B::foo();  // 调用命名空间 "A\B" 中定义的类 "B" 的 "foo" 方法
              // 如果类 "A\B" 未找到，则尝试自动装载类 "A\B"
```

## 关于引用&

`$a = &$b;` // `$a`和`$b`指向了同一个变量, `$a`或`$b`的改变是同步的

`function demo(&$var){}  demo($a)`  //引用传递, `$a`被创建并赋值`null`, 函数内部对`$var`的改变将作用到`$a`


```php

// 引用返回

class foo {
    public $value = 42;

    public function &getValue() {
        return $this->value;
    }
}

$obj = new foo;
$myValue = &$obj->getValue(); // $myValue is a reference to $obj->value, which is 42.
echo 'before' . $myValue . '<br/>';
$obj->value = 2;
echo 'after' . $myValue;                // prints the new value of $obj->value, i.e. 2.
```


**一些高阶方法**

`bool spl_autoload_register([callback $autoload_function])`  #注册`__autoload()`函数, 用于将Zend Engine中的`__autoload()`函数取代为`spl_autoload()`或`spl_autoload_call()`

`spl_autoload_register()`  #无参数时自动注册`autoload`的默认实现函数`spl_autoload()`, 自己实现`__autoload()`方法

`spl_autoload_register('autoload_function_name')`  #自己实现`autoload_function_name()`方法

`spl_autoload_register(array('class_name', 'method_name'))` #自己实现`class_name`类及其静态成员方法`method_name`

`bool spl_autoload_unregister([callback $autoload_function])`

`call_user_func(func_name, arg1[, arg2, ...])` #调用用户自定义方法

`call_user_func(array('class_name', 'method_name'), arg)` #调用`class_name`类中的`method_name`方法, 并传入参数`arg`

`call_user_func_array()`  #同`call_user_func`, 只不过参数部分用`array`组织

`array_walk_recursive ( array &$array , callable $callback [, mixed $userdata = NULL ] ) : bool`   # 对数组中的每个成员递归地应用用户函数



[php7 protobuf demo](https://segmentfault.com/a/1190000009389032)

1 下载pear

> curl -O http://pear.php.net/go-pear.phar

2 安装pear, 回车默认安装

> sudo php -d detect_unicode=0 go-pear.phar

> pear version

3 安装protobuf

> sudo pecl install protof-{VERSION}

4 配置开启protobuf扩展

> echo "extension=protobuf.so" >> php.ini

`composer require "google/protobuf"`

5 demo.proto

```
syntax = "proto3";

message SearchRequest {
  string query = 1;
  int32 page_number = 2;
  int32 result_per_page = 3;
}
```

6 执行命令生成php文件

`protoc --plugin=vendor/google/protobuf/php/generate_descriptor_protos.sh --php_out=src/ src/demo.proto`

**href/src匹配**

`preg_match_all('/(src|href)=("(.*?)"|\'(.*?)\')/i', $html, $rs)`
