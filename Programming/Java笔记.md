# Java笔记

## Lambda表达式



## API基础语法

Lambda表达式基本上是一个匿名函数。它由三个部分组成：

- 参数列表
- 箭头（->）
- 函数体

语法如下：

```java
(parameters) -> { expression; }
```

或者如果函数体只包含一个语句，可以省略大括号：

```java
(parameters) -> expression
```

### 示例

假设我们有一个字符串列表，并且我们想对它进行排序。不使用lambda表达式，我们可能需要这样写：

```java
Collections.sort(list, new Comparator<String>() {
    public int compare(String s1, String s2) {
        return s1.compareTo(s2);
    }
});
```

使用lambda表达式，我们可以这样写：

```
Collections.sort(list, (String s1, String s2) -> s1.compareTo(s2));
```

如果编译器能从上下文推断出参数类型，那么类型声明也可以省略：

```
Collections.sort(list, (s1, s2) -> s1.compareTo(s2));
```

### 使用场景

Lambda表达式在Java中最常见的使用场景包括：

- 使用在集合上的内置函数式接口，如 `Consumer`, `Supplier`, `Function`, `Predicate` 等。
- 创建简洁的事件监听器。
- 简化线程的创建。

### 函数式接口

Lambda表达式通常与函数式接口一起使用，这是只有一个抽象方法的接口。Java API中定义了许多函数式接口。例如，`Runnable`, `Callable`, `Comparator`, `Consumer` 等。

```java
// 使用 Runnable 和 lambda 表达式创建一个线程
new Thread(() -> System.out.println("Hello from a thread")).start();
javaCopy code// 使用 Consumer 函数式接口处理列表中的每个元素
List<String> names = Arrays.asList("John", "Doe", "Jane");
names.forEach(name -> System.out.println(name));
```

### 作用域和闭包

Lambda表达式可以访问其外部作用域的变量。但是，与匿名内部类一样，它们受到某些限制。Lambda可以捕获静态变量、实例变量和effectively final的局部变量（即，一旦赋值后就不再改变的变量）。

### 1、Math类

![image-20231211162036972](./_media/image-20231211162036972.png)

在API文档中没有体现可用的构造方法，因此我们就不能直接通过new关键字去创建Math类的对象。同时我们发现Math类中的方法都是静态的，因此在使用的时候我们可以直接通过类名去调用。在Math类中

####  常见方法

```java
public static int abs(int a)					// 返回参数的绝对值
public static double ceil(double a)				// 返回大于或等于参数的最小整数
public static double floor(double a)			// 返回小于或等于参数的最大整数
public static int round(float a)				// 按照四舍五入返回最接近参数的int类型的值
public static int max(int a,int b)				// 获取两个int值中的较大值
public static int min(int a,int b)				// 获取两个int值中的较小值
public static double pow (double a,double b)	// 计算a的b次幂的值
public static double random()					// 返回一个[0.0,1.0)的随机值
```

### 2、System类

System类所在包为java.lang包，因此在使用的时候不需要进行导包。并且System类被final修饰了，因此该类是不能被继承的。

System包含了系统操作的一些常用的方法。比如获取当前时间所对应的毫秒值，再比如终止当前JVM等等。

System类中的方法都是静态的，因此在使用的时候我们可以直接通过类名去调用。

`````java
public static long currentTimeMillis()			// 获取当前时间所对应的毫秒值（当前时间为0时区所对应的时间即就是英国格林尼治天文台旧址所在位置）
public static void exit(int status)				// 终止当前正在运行的Java虚拟机，0表示正常退出，非零表示异常退出
public static native void arraycopy(Object src,  int  srcPos, Object dest, int destPos, int length); // 进行数值元素copy 
//src：源数组，要复制的数组。
//srcPos：源数组中开始复制的位置。
//dest：目标数组，复制的目标。
//destPos：目标数组中开始粘贴的位置。
//length：要复制的元素数量。
`````

### 3、Date类

简单来说：使用无参构造，可以自动设置当前系统时间的毫秒时刻；指定long类型的构造参数，可以自定义毫秒时刻。例如：

```java
import java.util.Date;

public class Demo01Date {
    public static void main(String[] args) {
        // 创建日期对象，把当前的时间
        System.out.println(new Date()); // Tue Jan 16 14:37:35 CST 2020
        // 创建日期对象，把当前的毫秒值转成日期对象
        System.out.println(new Date(0L)); // Thu Jan 01 08:00:00 CST 1970
    }
}
```

常用方法：

Date类中的多数方法已经过时，常用的方法有：

- `public long getTime()` 把日期对象转换成对应的时间毫秒值。
- `public void setTime(long time)` 把方法参数给定的毫秒值设置给日期对象

示例代码

```java
public class DateDemo02 {
    public static void main(String[] args) {
        //创建日期对象
        Date d = new Date();
        
        //public long getTime():获取的是日期对象从1970年1月1日 00:00:00到现在的毫秒值
        //System.out.println(d.getTime());
        //System.out.println(d.getTime() * 1.0 / 1000 / 60 / 60 / 24 / 365 + "年");

        //public void setTime(long time):设置时间，给的是毫秒值
        //long time = 1000*60*60;
        long time = System.currentTimeMillis();
        d.setTime(time);

        System.out.println(d);
    }
}
```

> 小结：Date表示特定的时间瞬间，我们可以使用Date对象对时间进行操作。

### 4、SimpleDateFormat类

`java.text.SimpleDateFormat` 是日期/时间格式化类，我们通过这个类可以帮我们完成日期和文本之间的转换,也就是可以在Date对象与String对象之间进行来回转换。





## 正则表达式

在Java中，我们经常需要验证一些字符串，例如：年龄必须是2位的数字、用户名必须是8位长度而且只能包含大小写字母、数字等。正则表达式就是用来验证各种字符串的规则。它内部描述了一些规则，我们可以验证用户输入的字符串是否匹配这个规则。



规则是从左到右一个一个比较的

#### 1、字符类(只匹配一个字符)

1. \[abc\]：代表a或者b，或者c字符中的一个。
2. \[^abc\]：代表除a,b,c以外的任何字符。
3. [a-z]：代表a-z的所有小写字符中的一个。
4. [A-Z]：代表A-Z的所有大写字符中的一个。
5. [0-9]：代表0-9之间的某一个数字字符。
6. [a-zA-Z0-9]：代表a-z或者A-Z或者0-9之间的任意一个字符。
7. [a-dm-p]：a 到 d 或 m 到 p之间的任意一个字符。 

### 2、预定义字符(只匹配一个字符)

1. "." ： 匹配任何字符。
2. "\d"：任何数字[0-9]的简写；
3. "\D"：任何非数字\[^0-9\]的简写；
4. "\s"： 空白字符：[ \t\n\x0B\f\r] 的简写
5. "\S"： 非空白字符：\[^\s\] 的简写
6. "\w"：单词字符：[a-zA-Z_0-9]的简写
7. "\W"：非单词字符：\[^\w\]

tips: \ 在java中表示转义的意思，就是改变后面那个字符原本的含义，可以用来打印分号，\\\前面的\是一个转义字符，改变了后面\原本的含义，把它变成了一个普通的\

### 3、数量词

1. X? : X出现0次或1次
2. X* : X出现0次到多次
3. X+ : X出现1次或多次
4. X{n} : X出现恰好n次
5. X{n,} : X出现至少n次
6. X{n,m}: X出现n到m次(n和m都是包含的)

以上内容不用背，可以通过查看Pattern类的API得知。

String中有一个方法matchs(String regex)，这个regex表示一个正则表达式，返回的是boolean类型，表示此字符是否匹配给定的正则表达式

## 集合

### Map集合

- Map集合概述

	```java
	interface Map<K,V>  K：键的类型；V：值的类型
	```

- Map集合的特点

	- 双列集合,一个键对应一个值
	- 键不可以重复,值可以重复


```java
Map map = new HashMap();
map.put(1,"cez");
map.put(2,"zjy");
map.put(3,"zyj");
System.out.println(map);
System.out.println(map.get(1));
```

方法介绍

| 方法名                              | 说明                                 |
| ----------------------------------- | ------------------------------------ |
| V   put(K key,V   value)            | 添加元素                             |
| V   remove(Object key)              | 根据键删除键值对元素                 |
| void   clear()                      | 移除所有的键值对元素                 |
| boolean containsKey(Object key)     | 判断集合是否包含指定的键             |
| boolean containsValue(Object value) | 判断集合是否包含指定的值             |
| boolean isEmpty()                   | 判断集合是否为空                     |
| int size()                          | 集合的长度，也就是集合中键值对的个数 |

| 方法名                           | 说明                     |
| -------------------------------- | ------------------------ |
| V   get(Object key)              | 根据键获取值             |
| Set<K>   keySet()                | 获取所有键的集合         |
| Collection<V>   values()         | 获取所有值的集合         |
| Set<Map.Entry<K,V>>   entrySet() | 获取所有键值对对象的集合 |

#### Map集合的遍历方式

- 获取所有键的集合。用keySet()方法实现
- 遍历键的集合，获取到每一个键。用增强for实现  
- 根据键去找值。用get(Object key)方法实现

### HashMap集合

+ HashMap底层是哈希表结构的
+ 依赖hashCode方法和equals方法保证键的唯一
+ 如果键要存储的是自定义对象，需要重写hashCode和equals方法

### TreeMap集合

+ TreeMap底层是红黑树结构
+ 依赖自然排序或者比较器排序,对键进行排序
+ 如果键存储的是自定义对象,需要实现Comparable接口或者在创建TreeMap对象时候给出比较器排序规则

## 可变参数

在**JDK1.5**之后，如果我们定义一个方法需要接受多个参数，并且多个参数类型一致，我们可以对其简化.

**格式：**

```
修饰符 返回值类型 方法名(参数类型... 形参名){  }
```

**底层：**

​	其实就是一个数组

**好处：**

​	在传递数据的时候，省的我们自己创建数组并添加元素了，JDK底层帮我们自动创建数组并添加元素了

**代码演示:**

```java
  public class ChangeArgs {
    public static void main(String[] args) {
        int sum = getSum(6, 7, 2, 12, 2121);
        System.out.println(sum);
    }
    
    public static int getSum(int... arr) {
   		int sum = 0;
   	     for (int a : arr) {
         sum += a;
        }
   		 return sum;
    }
}
```

**注意：**

	1. 一个方法只能有一个可变参数
	1. 如果方法中有多个参数，可变参数要放到最后。

## Collection类

## Collections常用功能

- `java.utils.Collections`是集合工具类，用来对集合进行操作。

	常用方法如下：

- `public static void shuffle(List<?> list) `:打乱集合顺序。

- `public static <T> void sort(List<T> list)`:将集合中元素按照默认规则排序。

- `public static <T> void sort(List<T> list，Comparator<? super T> )`:将集合中元素按照指定规则排序。

## 不可变集合

是一个长度不可变，内容也无法修改的集合

### 不可变集合分类

* 不可变的list集合

```java
        //一旦创建完毕之后，是无法进行修改的，在下面的代码中，只能进行查询操作
        List<String> list = List.of("张三", "李四", "王五", "赵六");
		//Java 9及之后才有.of功能
```

* 不可变的set集合

```java
		//一旦创建完毕之后，是无法进行修改的，在下面的代码中，只能进行查询操作
        Set<String> set = Set.of("张三", "张三", "李四", "王五", "赵六");
		//Java 9及之后才有.of功能
```

* 不可变的map集合

```java
        //一旦创建完毕之后，是无法进行修改的，在下面的代码中，只能进行查询操作
        Map<String, String> map = Map.of("张三", "南京", "张三", "北京", "王五", "上海",
                "赵六", "广州", "孙七", "深圳", "周八", "杭州",
                "吴九", "宁波", "郑十", "苏州", "刘一", "无锡",
                "陈二", "嘉兴");
		//Java 9及之后才有.of功能
```



## Stream流

![image-20240326195146927](./_media/image-20240326195146927.png)

Stream流的三类方法

- 获取Stream流
	- 创建一条流水线,并把数据放到流水线上准备进行操作
- 中间方法
	- 流水线上的操作
	- 一次操作完毕之后,还可以继续进行其他操作
- 终结方法
	- 一个Stream流只能有一个终结方法
	- 是流水线上的最后一个操作

* 生成Stream流的方式

	- Collection体系集合

		使用默认方法stream()生成流， default Stream<E> stream()


	- Map体系集合

		把Map转成Set集合，间接的生成流


	- 数组

		通过Arrays中的静态方法stream生成流


	- 同种数据类型的多个数据

		通过Stream接口的静态方法of(T... values)生成流

```java
        //Collection体系的集合可以使用默认方法stream()生成流
        List<String> list = new ArrayList<String>();
        Stream<String> listStream = list.stream();

        Set<String> set = new HashSet<String>();
        Stream<String> setStream = set.stream();

        //Map体系的集合间接的生成流
        Map<String,Integer> map = new HashMap<String, Integer>();
        Stream<String> keyStream = map.keySet().stream();
        Stream<Integer> valueStream = map.values().stream();
        Stream<Map.Entry<String, Integer>> entryStream = map.entrySet().stream();

        //数组可以通过Arrays中的静态方法stream生成流
        String[] strArray = {"hello","world","java"};
        Stream<String> strArrayStream = Arrays.stream(strArray);
      
      	//同种数据类型的多个数据可以通过Stream接口的静态方法of(T... values)生成流
        Stream<String> strArrayStream2 = Stream.of("hello", "world", "java");
        Stream<Integer> intStream = Stream.of(10, 20, 30);
```

### Stream流中间操作方法【应用】

- 概念

	中间操作的意思是,执行完此方法之后,Stream流依然可以继续执行其他操作

- 常见方法

	| 方法名                                          | 说明                                                       |
	| ----------------------------------------------- | ---------------------------------------------------------- |
	| Stream<T> filter(Predicate predicate)           | 用于对流中的数据进行过滤                                   |
	| Stream<T> limit(long maxSize)                   | 返回此流中的元素组成的流，截取前指定参数个数的数据         |
	| Stream<T> skip(long n)                          | 跳过指定参数个数的数据，返回由该流的剩余元素组成的流       |
	| static <T> Stream<T> concat(Stream a, Stream b) | 合并a和b两个流为一个流                                     |
	| Stream<T> distinct()                            | 返回由该流的不同元素（根据Object.equals(Object) ）组成的流 |

### Stream流终结操作方法【应用】

- 概念

	终结操作的意思是,执行完此方法之后,Stream流将不能再执行其他操作

- 常见方法

	| 方法名                        | 说明                     |
	| ----------------------------- | ------------------------ |
	| void forEach(Consumer action) | 对此流的每个元素执行操作 |
	| long count()                  | 返回此流中的元素数       |

### Stream流的收集操作【应用】

- 概念

	对数据使用Stream流的方式操作完毕后,可以把流中的数据收集到集合中

- 常用方法

	| 方法名                         | 说明               |
	| ------------------------------ | ------------------ |
	| R collect(Collector collector) | 把结果收集到集合中 |

- 工具类Collectors提供了具体的收集方式

	| 方法名                                                       | 说明                   |
	| ------------------------------------------------------------ | ---------------------- |
	| public static <T> Collector toList()                         | 把元素收集到List集合中 |
	| public static <T> Collector toSet()                          | 把元素收集到Set集合中  |
	| public static  Collector toMap(Function keyMapper,Function valueMapper) | 把元素收集到Map集合中  |

## 方法引用

- 方法引用符

	::  该符号为引用运算符，而它所在的表达式被称为方法引用

- 推导与省略

	- 如果使用Lambda，那么根据“可推导就是可省略”的原则，无需指定参数类型，也无需指定的重载形式，它们都将被自动推导
	- 如果使用方法引用，也是同样可以根据上下文进行推导
	- 方法引用是Lambda的孪生兄弟

### 引用类方法【应用】

引用类方法，其实就是引用类的静态方法

- 格式

	类名::静态方法

- 范例

	Integer::parseInt

	Integer类的方法：public static int parseInt(String s) 将此String转换为int类型数据

- 练习描述

	- 定义一个接口(Converter)，里面定义一个抽象方法 int convert(String s);
	- 定义一个测试类(ConverterDemo)，在测试类中提供两个方法
		- 一个方法是：useConverter(Converter c)
		- 一个方法是主方法，在主方法中调用useConverter方法

- 代码演示

	```java
	public interface Converter {
	    int convert(String s);
	}
	
	public class ConverterDemo {
	    public static void main(String[] args) {
	
			//Lambda写法
	        useConverter(s -> Integer.parseInt(s));
	
	        //引用类方法
	        useConverter(Integer::parseInt);
	
	    }
	
	    private static void useConverter(Converter c) {
	        int number = c.convert("666");
	        System.out.println(number);
	    }
	}
	```

- 使用说明

	Lambda表达式被类方法替代的时候，它的形式参数全部传递给静态方法作为参数
