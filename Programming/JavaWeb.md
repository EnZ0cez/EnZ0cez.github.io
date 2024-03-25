# JavaWeb

## HTML&CSS

HTML: Hypertext Markup Language

CSS: Cascading Style Sheet

### HTML快速入门

HTML页面的基础结构标签：

```html
<html>
 	<head>
 		<title> </title>
	</head>
	<body>
        
        
	</body>
</html>
```

HTML中的标签特点：

1. HTML标签不区分大小写
2. HTML标签的属性值，采用单引号、双引号都可以
3. HTML语法相对比较松散 (建议大家编写HTML标签的时候尽量严谨一些)

### 新浪新闻

#### 标题实现

![image-20240311191222511](./_media/image-20240311191222511.png)

1. 图片，用到HTML中的图片标签来实现。
2. 标题，用HTML中的标题标签来实现。
3. 两条水平分割线，用HTML中的标签来定义分割线

##### 标签

图片标签 img

```html
A. 图片标签: <img>
B. 常见属性:
 src: 指定图像的url (可以指定 绝对路径 , 也可以指定 相对路径)
 width: 图像的宽度 (像素 / 百分比 , 相对于父元素的百分比)
 height: 图像的高度 (像素 / 百分比 , 相对于父元素的百分比)
 
 备注: 一般width 和 height 我们只会指定一个，另外一个会自动的等比例缩放。
 
C. 路径书写方式:
 绝对路径:
 1. 绝对磁盘路径:
C:\Users\Administrator\Desktop\HTML\img\news_logo.png
 <img src="C:\Users\Administrator\Desktop\HTML\img\news_logo.png">
 2. 绝对网络路径:
https://i2.sinaimg.cn/dy/deco/2012/0613/yocc20120613img01/news_logo.png
<img src="https://i2.sinaimg.cn/dy/deco/2012/0613/yocc20120613img01/news_logo.png">
 相对路径:
 ./ : 当前目录 , ./ 可以省略的
 ../: 上一级目录
```

标题标签h

```html
A. 标题标签: <h1> - <h6>
 <h1>111111111111</h1>
 <h2>111111111111</h2>
 <h3>111111111111</h3>
 <h4>111111111111</h4>
 <h5>111111111111</h5>
 <h6>111111111111</h6>
 
B. 效果 : h1为一级标题，字体也是最大的 ； h6为六级标题，字体是最小的。
```

水平分页线标签 <hr>


```html
<p>This is some content above the horizontal rule.</p>
<hr>
<p>This is some content below the horizontal rule.</p>
```

#### 标题样式

##### CSS引入方式

| 名称     | 语法描述                                     | 示例                                        |
| -------- | -------------------------------------------- | ------------------------------------------- |
| 行内样式 | 在标签内使用style属性，属性值是css属性键值对 | <h1 style="xxx:xxx;">中国新闻网</h1>        |
| 内嵌样式 | 定义<style>标签，在标签内部定义css样式       | <style> h1 {...} </style>                   |
| 外联样式 | 定义<link>标签，通过href属性引入外部css文件  | <link rel="stylesheet" href="css/news.css"> |

内部样式，通过定义css选择器，让样式作用于当前页面的指定的标签上。

外部样式，html和css实现了完全的分离，企业开发常用方式。

#### 颜色表示

| **表示方式**   | **表示含义**                      | **取值**                                    |
| -------------- | --------------------------------- | ------------------------------------------- |
| 关键字         | 预定义的颜色名                    | red、green、blue...                         |
| rgb表示法      | 红绿蓝三原色，每项取值范围：0-255 | rgb(0,0,0)、rgb(255,255,255)、rgb(255,0,0)  |
| 十六进制表示法 | #开头，将数字转换成十六进制表示   | #000000、#ff0000、#cccccc，简写：#000、#ccc |

#### CSS选择器

选择器是选取需设置样式的元素（标签）

**选择器通用语法如下**：

```css
选择器名   {
    css样式名：css样式值;
    css样式名：css样式值;
}
```



1. **元素（标签）选择器**：

- 选择器的名字必须是标签的名字
- 作用：选择器中的样式会作用于所有同名的标签上

~~~
元素名称 {
    css样式名:css样式值；
}
~~~

例子如下：

~~~css
 div{
     color: red;
 }
~~~



**2.id选择器:**

- 选择器的名字前面需要加上#
- 作用：选择器中的样式会作用于指定id的标签上，而且有且只有一个标签（由于id是唯一的）

~~~
#id属性值 {
    css样式名:css样式值；
}
~~~

例子如下：

~~~css
#did {
    color: blue;
}
~~~



**3.类选择器：**

- 选择器的名字前面需要加上 .
- 作用：选择器中的样式会作用于所有class的属性值和该名字一样的标签上，可以是多个

~~~
.class属性值 {
    css样式名:css样式值；
}
~~~

例子如下：

~~~css
.cls{
     color: green;
 }
~~~

![image-20240325203747194](./_media/image-20240325203747194.png)

#### 超链接

* 标签: &lt;a href="..." target="...">央视网</a>
* 属性：
	* href: 指定资源访问的url
	* target: 指定在何处打开资源链接
		* _self: 默认值，在当前页面打开
		* _blank: 在空白页面打开

#### 正文实现

##### 正文排班

整个正文部分的排版，主要分为这么四个部分：

1). 视频 (当前这种新闻页面,可能也会存在音频)

2). 文字段落

3). 字体加粗

4). 图片

##### 标签

1. **视频、音频标签**

- 视频标签: &lt;video>
	- 属性: 
		- src: 规定视频的url
		- controls: 显示播放控件
		- width: 播放器的宽度
		- height: 播放器的高度

- 音频标签: &lt;audio>
	- 属性:
		- src: 规定音频的url
		- controls: 显示播放控件

2. **段落标签**

- 换行标签: &lt;br>
	- 注意: 在HTML页面中,我们在编辑器中通过回车实现的换行, 仅仅在文本编辑器中会看到换行效果, 浏览器是不会解析的, HTML中换行需要通过br标签

- 段落标签: &lt;p>
	- 如: &lt;p> 这是一个段落 &lt;/p>

3. **文本格式标签**

| 效果   | 标签 | 标签(强调) |
| ------ | ---- | ---------- |
| 加粗   | b    | strong     |
| 倾斜   | i    | em         |
| 下划线 | u    | ins        |
| 删除线 | s    | del        |

前面的标签 b、i、u、s 就仅仅是实现加粗、倾斜、下划线、删除线的效果，是没有强调语义的。 而后面的strong、em、ins、del在实现加粗、倾斜、下划线、删除线的效果的同时，还带有强调语义。

几个CSS属性：

- text-indent: 设置段落的首行缩进 
- line-height: 设置行高
- text-align: 设置对齐方式, 可取值为 left / center / right

#### 页面布局

##### 盒子模型

- 盒子：页面中所有的元素（标签），都可以看做是一个 盒子，由盒子将页面中的元素包含在一个矩形区域内，通过盒子的视角更方便的进行页面布局

- 盒子模型组成：内容区域（content）、内边距区域（padding）、边框区域（border）、外边距区域（margin）

![image-20240325205624726](./_media/image-20240325205624726.png)

CSS盒子模型，其实和日常生活中的包装盒是非常类似的，就比如：

![image-20240325205659085](./_media/image-20240325205659085.png)

盒子的大小，其实就包括三个部分： border、padding、content，而margin外边距是不包括在盒子之内的。

##### 布局实现

在实现新闻页面的布局时，我们需要做两部操作：

- 第一步：需要将body中的新闻标题部分、正文部分使用一个 div 布局标签将其包裹起来，方便通过css设置内容占用的宽度，比如：65%。
- 第二步：通过css为该div设置外边距，左右的外边距分别为：17.5%，上下外边距靠边展示即可，为：0%。

### 表格标签

**场景：**在网页中以表格（行、列）形式整齐展示数据，我们在一些管理类的系统中，会看到数据通常都是以表格的形式呈现出来的，比如：班级表、学生表、课程表、成绩表等等。

**标签：**

- &lt;table> : 用于定义整个表格, 可以包裹多个 &lt;tr>， 常用属性如下： 
	- border：规定表格边框的宽度
	- width：规定表格的宽度
	- cellspacing: 规定单元之间的空间

- &lt;tr> : 表格的行，可以包裹多个 &lt;td>  
- &lt;td> : 表格单元格(普通)，可以包裹内容 , 如果是表头单元格，可以替换为 &lt;th>  

### 表单标签

#### 表单

- 表单场景: 表单就是在网页中负责数据采集功能的，如：注册、登录的表单。 

- 表单标签: &lt;form>
- 表单属性:
	- action: 规定表单提交时，向何处发送表单数据，表单提交的URL。
	- method: 规定用于发送表单数据的方式，常见为： GET、POST。
		- GET：表单数据是拼接在url后面的， 如： xxxxxxxxxxx?username=Tom&age=12，url中能携带的表单数据大小是有限制的。
		- POST： 表单数据是在请求体（消息体）中携带的，大小没有限制。

- 表单项标签: 不同类型的input元素、下拉列表、文本域等。
	- input: 定义表单项，通过type属性控制输入形式
	- select: 定义下拉列表
	- textarea: 定义文本域

![image-20240325212148765](./_media/image-20240325212148765.png)

#### 表单项

 在一个表单中，可以存在很多的表单项，而虽然表单项的形式各式各样，但是表单项的标签其实就只有三个，分别是：

- &lt;input>: 表单项 , 通过type属性控制输入形式。

	| type取值                 | **描述**                             |
	| ------------------------ | ------------------------------------ |
	| text                     | 默认值，定义单行的输入字段           |
	| password                 | 定义密码字段                         |
	| radio                    | 定义单选按钮                         |
	| checkbox                 | 定义复选框                           |
	| file                     | 定义文件上传按钮                     |
	| date/time/datetime-local | 定义日期/时间/日期时间               |
	| number                   | 定义数字输入框                       |
	| email                    | 定义邮件输入框                       |
	| hidden                   | 定义隐藏域                           |
	| submit / reset / button  | 定义提交按钮 / 重置按钮 / 可点击按钮 |

- &lt;select>: 定义下拉列表, &lt;option> 定义列表项

- &lt;textarea>: 文本域

```html
    <form action="" method="post">
        姓名: <input type="text" name="name"> <br><br>
        密码: <input type="password" name="password"> <br><br> 
        性别: <input type="radio" name="gender" value="1"> 男
             <label><input type="radio" name="gender" value="2"> 女 </label> <br><br>
        爱好: <label><input type="checkbox" name="hobby" value="java"> java </label>
             <label><input type="checkbox" name="hobby" value="game"> game </label>
             <label><input type="checkbox" name="hobby" value="sing"> sing </label> <br><br>
        图像: <input type="file" name="image">  <br><br>
        生日: <input type="date" name="birthday"> <br><br>
        时间: <input type="time" name="time"> <br><br>
        日期时间: <input type="datetime-local" name="datetime"> <br><br>
        邮箱: <input type="email" name="email"> <br><br>
        年龄: <input type="number" name="age"> <br><br>
        学历: <select name="degree">
                  <option value="">----------- 请选择 -----------</option>
                  <option value="1">大专</option>
                  <option value="2">本科</option>
                  <option value="3">硕士</option>
                  <option value="4">博士</option>
             </select>  <br><br>
        描述: <textarea name="description" cols="30" rows="10"></textarea>  <br><br>
        <input type="hidden" name="id" value="1">
            
        <!-- 表单常见按钮 -->
        <input type="button" value="按钮">
        <input type="reset" value="重置"> 
        <input type="submit" value="提交">   
        <br>
    </form>
```

![image-20240325212913114](./_media/image-20240325212913114.png)

###  文档查阅

文档地址: https://www.w3school.com.cn/index.html
