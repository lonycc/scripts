## java 泛型

> 泛型本质就是参数化类型, 提供了编译时类型安全检测机制.

List<String> list = new ArrayList<>();


**泛型方法**

```
public static <E> void printArray(E[] inArray)
{
  for (E ele : inArray) {
    System.out.printf("%s", ele);
  }
}

public static void main(String args[])
{
  Integer[] intArray = { 1, 2, 3, 4, 5 };
  Double[] doubleArray = { 1.1, 2.2, 3.3, 4.4 };
  Character[] charArray = { 'H', 'E', 'L', 'L', 'O' };
  
  printArray(intArray);
  printArray(doubleArray);
  printArray(charArray);
}
```


**泛型类**

```
class DataHolder<T>
{
  T item;
    
  public void setData(T t)
  {
    this.item = t;
  }
    
  public T getData()
  {
    return this.item;
  }

  public <E> void print(E e)
  {
    System.out.println(e)
  }
}

DataHolder<String> dataHolder = new DataHolder<>();
dataHolder.print(123);
dataHolder.print("ABC");
dataHolder.print(1.23f);
```

**类型通配符**

```
public static void getData(List<?> data) {}  // 接受List<Integer>/<String>/<Number>/<Double>类型data

public static void getData(List<? extends Number> data) {}  // 限定了参数泛型上限为Number

public static void getData(List<? super Number> data) {} // 限定了参数泛型下限, Number及其三层父类类型
```

**泛型interface**

```
public interface Generator<T>
{
  public T next();
}


class FruitGenerator<T> implements Generator<T>
{
  @Override
  public T next()
  {
    return null;
  }
}

// 传入类型参数, 实现该泛型接口的实现类
class DataHandler implements Generator<String>
{
  @Override
  public String next()
  {
    return null;
  }
}
```

**泛型擦除**

```
Class<?> c1 = new ArrayList<String>().getClass();
Class<?> c2 = new ArrayList<Integer>().getClass();
c1.equals(c2);   // 都是java.util.ArrayList
```
