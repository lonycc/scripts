<?php
/**（1）、静态属性不需要实例化即可调用。因为静态属性存放的位置是在类里，调用方法为"类名::属性名", 类内部 "self::属性名"；
 * （2）、静态方法不需要实例化即可调用。同上
 * （3）、静态方法不能调用非静态属性。因为非静态属性需要实例化后，存放在对象里；
 * （4）、静态方法可以调用非静态方法，使用 self 关键词。php里，一个方法被self:: 后，它就自动转变为静态方法；
 * （5）、静态方法在类外调用方式 "实例名::方法名 或 实例名->方法名 或 类名::方法名"
 * （6）、非静态方法在类外调用方式 "实例名->方法名", 若用 "实例名::方法名 或 类名::方法名" 尽管在方法内没有$this情况下不报错, 但不建议
 */
 
// 自动加载类, 会自动加载需要的文件
function __autoload($class_name)
{
    require_once $class . '.php';
}

class User
{
	private $gender;
	private $country;
	
	// 公有静态属性, 类和实例都能通过::操作符访问 ::$a
	public static $a = 'fuck';
	
	// 公有属性, 只有实例能通过->操作符访问 ->b
	public $b = 'suruo';
	
	// 对于常量, 类和实例都能通过::操作符访问 ::c
	const c = 'this is const';
 
	// 定义为静态方法, 方法体内部不能用$this变量; 可用self::来访问常量
	public static function static_method()
	{
		echo self::c . ' call static method ' . User::c;
	}
 
	// 普通方法, 只能通过->操作符调用
	function normal_method()
	{
		echo $this->name . ' - ' . $this->gender . ' - ' . self::c;
	}
	
	// 构造函数, 在实例化类的时候执行
	function __construct($name='tony', $age=25)
	{
		$this->name = $name;
		$this->age = $age;
		echo '执行了__construct()方法';
	}
	
	// __set()方法设置私有属性
	function __set($property_name, $value)
	{
		echo '在直接设置私有属性值时, 自动调用了__set()方法为其赋值';
		$this->property_name = $value;
	}
	
	// __get()方法获取私有属性
	function __get($property_name)
	{
		echo '在直接获取私有属性值时, 自动调用了__get()方法';
		if ( isset($this->property_name) )
			return $this->property_name;
		return null;
	}
	
	// 析构函数, 在注销类的实例时执行
	function __destruct()
	{
		echo '执行了__destruct()方法';
	}
	
	// 该方法在打印对象实例的时候调用 $user = new User(); echo $user;
	function __toString()
	{
		return $this->name."\n";
	}
	
	// 魔术方法, 在执行unserialize()方法之前执行
	public function __wakeup()
	{
		$this->name = '我回来了';
		echo '__wakeup\n';
	}
	
	// 魔术方法, 在执行serialize()方法序列化实例之前执行
	public function __sleep()
	{
		$this->name = '不告诉你';
		echo '执行了__sleep()方法';
		return array('name', 'age');
	}
	
	// __clone方法仅在克隆对象时被执行
	public function __clone()
	{
		$this->name = 'name changed via clone';
	}
	
	// 该方法仅在被调用的方法不存在时执行
	public function __call($function_name, $args)
	{
		echo '你调用的方法: '.$function_name .'(参数:<br/>';
		var_dump($args);
		echo ') 不存在';
	}
}


$obj1 = new User();
$obj2 = clone $obj1;  //浅复制, 所有的引用属性仍是原来$obj1的引用



/**
 * 观察者模式举例, 依赖注入举例
 */ 
 
// car类, 实现了car的基础方法
class car implements SplSubject
{
  //车的类型
  private $carName;
  //车的状态，0为关闭，1这启动车子
  private $carState = 0;
  //初始化车的速度表值
  private $carSpeed = 0;
  //各项车的性能观察对象
  private $Observers;

  public function __construct($Name)
  {
    $this->carName   = $Name;
    $this->Observers = new SplObjectStorage;
  }

  //启动
  public function start()
  {
    $this->carState = 1;
    $this->notify();
  }

  //停车
  public function stop()
  {
    $this->carState = 0;
    $this->carSpeed = 0;
    $this->notify();
  }

  //加速
  public function accelerate($Acceleration)
  {
    if (0 === $this->carState) {
      throw new Exception('先踩油门，不然车怎走啊!!!');
    }
    if (!is_int($Acceleration) || $Acceleration < 0) {
      throw new Exception('加速值错了啊');
    }
    $this->carSpeed += $Acceleration;
    $this->notify();
  }

  //增加监测对象
  public function attach(SplObserver $observer)
  {
    if ( ! $this->Observers->contains($observer) ) {
      $this->Observers->attach($observer);
    }
    return true;
  }

  //删除监测对象
  public function detach(SplObserver $observer)
  {
    if ( ! $this->Observers->contains($observer) ) {
      return false;
    }
    $this->Observers->detach($observer);
    return true;
  }

  //传送对象
  public function notify()
  {
    foreach ($this->Observers as $observer) {
      $observer->update($this);
    }
  }
  
  public function __get($Prop)
  {
    switch ($Prop) {
      case 'STATE':
        return $this->carState;
        break;
      case 'SPEED':
        return $this->carSpeed;
        break;
      case 'NAME':
        return $this->carName;
        break;
      default:
        throw new Exception($Prop . 'cannotberead');
    }
  }

  public function __set($Prop, $Val)
  {
    throw new Exception($Prop . 'cannotbeset');
  }
}

// carStateObserver类, 汽车状态观察者
class carStateObserver implements SplObserver
{
    private $SubjectState;
    public function update(SplSubject $subject)
    {
        switch ($subject->STATE) {
            case 0:
                if (is_null($this->SubjectState)) {
                    echo $subject->NAME . '没有启动呢' . "<br/>";
                } else {
                    echo $subject->NAME . '熄火了' . "<br/>";
                }
                $this->SubjectState = 0;
                break;
            case 1:
                if (1 !== $this->SubjectState) {
                    echo $subject->NAME . '启动了' . "<br/>";
                    $this->SubjectState = 1;
                }
                break;
            default:
                throw new Exception('UnexpectederrorincarStateObserver::update()');
        }
    }
}

// carSpeedObserver类, 汽车速度观察者
class carSpeedObserver implements SplObserver
{
    public function update(SplSubject $subject)
    {
        if (0 !== $subject->STATE) {
            echo $subject->NAME . '目前速度为' . $subject->SPEED . 'Kmh' . "<br/>";
        }
    }
}

// carOversppedObserver, 汽车超速观察者
class carOverspeedObserver implements SplObserver
{
    public function update(SplSubject $subject)
    {
        if ($subject->SPEED > 130) {
            throw new Exception('加速限制在130以内,你违规了!' . "<br/>");
        }
    }
}


try {
    $driver  = new car('AUDIA4');
    $driverObserver1  = new carStateObserver;
    $driverObserver2  = new carSpeedObserver;
    $drivesrObserver3 = new carOverspeedObserver;
    $driver->attach($driverObserver1);
    $driver->attach($driverObserver2);
    $driver->attach($drivesrObserver3);
    $driver->start();
    $driver->accelerate(10);
    $driver->accelerate(30);
    $driver->stop();
    $driver->start();
    $driver->accelerate(50);
    $driver->accelerate(70);
    $driver->accelerate(100);
    $driver->accelerate(150);
} catch (Exception $e) {
    echo $e->getMessage();
}