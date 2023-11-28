# Python from Runoob

## 基础语法

### 基本数据类型

Python 中的变量不需要声明。每个变量在使用前都必须赋值，变量赋值以后该变量才会被创建。

在 Python 中，变量就是变量，它没有类型，我们所说的"类型"是变量所指的内存中对象的类型。

常见的数据类型：

1. Number(数字)：**int、float、bool、complex（复数）**。

   在Python 3里，只有一种整数类型 int，表示为长整型，没有 python2 中的 Long。

2. String（字符串）：

   Python中的字符串用单引号 **'** 或双引号 **"** 括起来，同时使用反斜杠 **\** 转义特殊字符。

3. bool（布尔类型）

4. List（列表）：

   列表可以完成大多数集合类的数据结构实现。列表中元素的类型可以不相同，它支持数字，字符串甚至可以包含列表（所谓嵌套）。

   列表是写在方括号 **[]** 之间、用逗号分隔开的元素列表。

5. Tuple（元组）：

   元组（tuple）与列表类似，不同之处在于元组的元素不能修改。元组写在小括号 **()** 里，元素之间用逗号隔开。

   元组中的元素类型也可以不相同

6. Set（集合）：

   Python 中的集合（Set）是一种无序、可变的数据类型，用于存储唯一的元素。

   集合中的元素不会重复，并且可以进行交集、并集、差集等常见的集合操作。

   在 Python 中，集合使用大括号 **{}** 表示，元素之间用逗号 **,** 分隔。

   另外，也可以使用 **set()** 函数创建集合。

7. Dictionary（字典）：

   字典（dictionary）是Python中另一个非常有用的内置数据类型。

   列表是有序的对象集合，字典是无序的对象集合。两者之间的区别在于：字典当中的元素是通过键来存取的，而不是通过偏移存取。

   字典是一种映射类型，字典用 **{ }** 标识，它是一个无序的 **键(key) : 值(value)** 的集合。

   键(key)必须使用不可变类型。

   在同一个字典中，键(key)必须是唯一的。

### 数据类型转换

* 隐式类型转换 - 自动完成

	在隐式类型转换中，Python 会自动将一种数据类型转换为另一种数据类型，不需要我们去干预。较低数据类型（整数）就会转换为较高数据类型（浮点数）以避免数据丢失。

* 显式类型转换 - 需要使用类型函数来转换

	在显式类型转换中，用户将对象的数据类型转换为所需的数据类型。 我们使用 int()、float()、str() 等预定义函数来执行显式类型转换。

以下几个内置的函数可以执行数据类型之间的转换。这些函数返回一个新的对象，表示转换的值。

| 函数                                                         | 描述                                                |
| :----------------------------------------------------------- | :-------------------------------------------------- |
| int(x [,base])]                                              | 将x转换为一个整数                                   |
| [float(x)](https://www.runoob.com/python3/python-func-float.html) | 将x转换到一个浮点数                                 |
| complex(real [,imag])]                                       | 创建一个复数                                        |
| [str(x)](https://www.runoob.com/python3/python-func-str.html) | 将对象 x 转换为字符串                               |
| [repr(x)](https://www.runoob.com/python3/python-func-repr.html) | 将对象 x 转换为表达式字符串                         |
| [eval(str)](https://www.runoob.com/python3/python-func-eval.html) | 用来计算在字符串中的有效Python表达式,并返回一个对象 |
| [tuple(s)](https://www.runoob.com/python3/python3-func-tuple.html) | 将序列 s 转换为一个元组                             |
| [list(s)](https://www.runoob.com/python3/python3-att-list-list.html) | 将序列 s 转换为一个列表                             |
| [set(s)](https://www.runoob.com/python3/python-func-set.html) | 转换为可变集合                                      |
| [dict(d)](https://www.runoob.com/python3/python-func-dict.html) | 创建一个字典。d 必须是一个 (key, value)元组序列。   |
| [frozenset(s)](https://www.runoob.com/python3/python-func-frozenset.html) | 转换为不可变集合                                    |
| [chr(x)](https://www.runoob.com/python3/python-func-chr.html) | 将一个整数转换为一个字符                            |
| [ord(x)](https://www.runoob.com/python3/python-func-ord.html) | 将一个字符转换为它的整数值                          |
| [hex(x)](https://www.runoob.com/python3/python-func-hex.html) | 将一个整数转换为一个十六进制字符串                  |
| [oct(x)](https://www.runoob.com/python3/python-func-oct.html) | 将一个整数转换为一个八进制字符串                    |

## 解释器

可以在cmd窗口中输入“Python”命令来启动Python解释器

### 交互式编程

我们可以在命令提示符中输入"Python"命令来启动Python解释器：

```python
$ python3
```

执行以上命令后，出现如下窗口信息：

```python
$ python3
Python 3.4.0 (default, Apr 11 2014, 13:05:11) 
[GCC 4.8.2] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> 
```

### 脚本式编程

创建一个hello.py文件

在cmd中通过以下命令执行该脚本

```python
python3 hello.py
```

## Python3注释

Python 中的注释有单行注释和多行注释。

Python 中单行注释以 # 开头，例如：

```python
# 这是一个注释
print("Hello, World!")
```

多行注释：

1. 单引号(‘’‘)

	```python
	#!/usr/bin/python3 
	'''
	这是多行注释，用三个单引号
	这是多行注释，用三个单引号 
	这是多行注释，用三个单引号
	'''
	print("Hello, World!")
	```

	

2. 双引号(“”“)

	```python
	#!/usr/bin/python3 
	"""
	这是多行注释，用三个双引号
	这是多行注释，用三个双引号 
	这是多行注释，用三个双引号
	"""
	print("Hello, World!")
	```

## Python3运算符

### 算术运算符

| 运算符 | 描述                                            | 实例               |
| :----- | :---------------------------------------------- | :----------------- |
| +      | 加 - 两个对象相加                               | a + b 输出结果 31  |
| -      | 减 - 得到负数或是一个数减去另一个数             | a - b 输出结果 -11 |
| *      | 乘 - 两个数相乘或是返回一个被重复若干次的字符串 | a * b 输出结果 210 |
| /      | 除 - x 除以 y                                   | b / a 输出结果 2.1 |
| %      | 取模 - 返回除法的余数                           | b % a 输出结果 1   |
| **     | 幂 - 返回x的y次幂                               | a**b 为10的21次方  |
| //     | 取整除 - 往小的方向取整数                       |                    |

### 比较运算符

| 运算符 | 描述                                                         | 实例                  |
| :----- | :----------------------------------------------------------- | :-------------------- |
| ==     | 等于 - 比较对象是否相等                                      | (a == b) 返回 False。 |
| !=     | 不等于 - 比较两个对象是否不相等                              | (a != b) 返回 True。  |
| >      | 大于 - 返回x是否大于y                                        | (a > b) 返回 False。  |
| <      | 小于 - 返回x是否小于y。所有比较运算符返回1表示真，返回0表示假。这分别与特殊的变量True和False等价。注意，这些变量名的大写。 | (a < b) 返回 True。   |
| >=     | 大于等于 - 返回x是否大于等于y。                              | (a >= b) 返回 False。 |
| <=     | 小于等于 - 返回x是否小于等于y。                              | (a <= b) 返回 True。  |

### 赋值运算符

| 运算符 | 描述                                                         | 实例                                                         |
| :----- | :----------------------------------------------------------- | :----------------------------------------------------------- |
| =      | 简单的赋值运算符                                             | c = a + b 将 a + b 的运算结果赋值为 c                        |
| +=     | 加法赋值运算符                                               | c += a 等效于 c = c + a                                      |
| -=     | 减法赋值运算符                                               | c -= a 等效于 c = c - a                                      |
| *=     | 乘法赋值运算符                                               | c *= a 等效于 c = c * a                                      |
| /=     | 除法赋值运算符                                               | c /= a 等效于 c = c / a                                      |
| %=     | 取模赋值运算符                                               | c %= a 等效于 c = c % a                                      |
| **=    | 幂赋值运算符                                                 | c **= a 等效于 c = c ** a                                    |
| //=    | 取整除赋值运算符                                             | c //= a 等效于 c = c // a                                    |
| :=     | 海象运算符，可在表达式内部为变量赋值。**Python3.8 版本新增运算符**。 | 在这个示例中，赋值表达式可以避免调用 len() 两次:`if (n := len(a)) > 10:    print(f"List is too long ({n} elements, expected <= 10)")` |
