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

水平分页线标签


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
