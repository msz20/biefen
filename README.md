# 在线笔记
[HTML笔记](https://www.yuque.com/myw/mps0hv)

[CSS笔记](https://www.yuque.com/myw/css)

[H5C3阶段](https://www.yuque.com/myw/di8gqh)

[JavaScript基础](https://www.yuque.com/myw/javascriptbasic)

[JavaScript-Web APIS](https://www.yuque.com/myw/hpkan9)

[JavaScript高级](https://www.yuque.com/myw/hpkan9)

[ajax](https://malaoshi.feishu.cn/drive/folder/fldcn09fMgibeWqEvCUpplfNpAh)


[bootStrap5框架](https://malaoshi.feishu.cn/drive/folder/fldcnnMfYzqc0yUCr6CIMq2AwQf)

[node](https://malaoshi.feishu.cn/drive/folder/fldcnoGTRNHim2vTzdmx3FSmInc)

[vue](https://malaoshi.feishu.cn/drive/folder/fldcniDngiRjKlgjf2rwLjBttwh)



[马老师笔记-多学科](https://www.yuque.com/myw)

---

# 软件安装
[MySQL8 （安装版）教程](https://malaoshi.feishu.cn/docx/doxcn8yWT5lVNSPjbI18TSAHA9f)

# git协同用法
1. 安装git软件
2. 拉去项目到本地
  1. 找一个存放代码的目录。
  2. Cmd ： git clone https://gitee.com/mayuanwei/summer-program.git
  3. 拉去云平台代码到本地： git pull
  4. 创建自己代码目录，编写代码。
  5. 上传自己的代码到gitee。

    1.  标记当前目录代码已经被自己修改过了：git add .

    2. 查看项目状态（可以省略）： git status  可以看到有自己更新过文件，变绿色。

    3. 提交代码到本地仓库： git commit -m '注释内容解释说明这次提交的意义'。如果是首次提交，需要设置用户名和邮箱

    4. 推送本地仓库代码到云端：git push。此时云端发生改变。如果是首次提交，需要登录用户名和密码

---

# 随堂笔记
计划完成内容
1. 前端
  1. Html
  2. Css
  3. Js
2. 后端
  1. Python
  2. Java
  3. Php 
  4. node
3. 数据库
  1. mysql
---
1. 网页
1. 元素：文字、音视频、链接。。。html : 结构
  1. 样式：将元素排版。。。。css：  化妆
2. 交互: 动态效果+校验。。。。js  ： 动作
  1. 数据：从服务端获取的内容：  灵魂
[静态网站效果](http://jdd93.host3v.club/mddshopping/)

2. HTML
1. 默认结构，自动生成
2. 元素都由标签的形式体现
  1. 双标签
  2. 单标签
  3. 理解标签属性
    1. 属性名
    2. 属性值
    3. 成对组成
3. 常见标签
  1. 标题
  2. 图片
    1. 路径问题
    2. 尺寸问题
    3. alt
    4. id属性：标识，当前网页，唯一性。
  3. id属性
    1. 所有元素都可以加这个id标识。
  4. 列表标签
    1. 有序列表
    2. 无序列表:ul>li
    3. 自定义列表
  5. div : 没有语义化的块级容器
  6. span：没有语义化的行内元素
  7. a：超链接
    1. href属性
  8. 表单标签
    1. 表单属性：
      1. action：决定跳转到哪里
      2. method:提交方式
    2. 表单元素
      1. 文本输入框
      2. 密码输入框
      3. 单选框: name属性必须添加，相同的name属性表示同一组单选框，具备互斥效果
      4. 多选框：name属性必须添加，相同的name属性表示同一组多选框
      5. 文本域
      6. 下拉选框
      7. 提交按钮
      8. 重置按钮
    3. 表单属性
      1. value：对于单选框和多选框，value用来传递点击或者勾选的数据
      2. name: 必须给。用户输入框或者密码框或者文本域这种数据需要通过name传递。
      3. placeholder
      4. checked ： 属性名和属性值相同时，可以简写。建议写全。
4. 元素的显示模式
  1. 块级元素：独占一行，可以直接设置尺寸
    1. 标题
    2. p段落
  2. 行内元素：一行内显示：不可以直接设置尺寸
    1. Span
  3. 行内块：可以一行显示，但是可以设置宽高尺寸

3. Css
1. 入门
  1. css存放位置
css代码要放在 style 标签中
 style  标签要放在 head 标签中
  2. 语法
选中要求改的元素{
    属性名1 : 属性值1;
    属性名2 : 属性值2;
    ....
}
  1. 代码示例
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>样式入门：基本样式</title>

    <style>
        h1{
            /* 修改文字大小 */
            font-size: 30px;
            /* 字体粗细 */
            font-weight: 400;
            /* 字体风格 */
            font-style: normal;
            /* 字体样式：宋体、楷体、微软雅黑等，取决于C:\Windows\Fonts 中有哪些可用字体*/
            font-family: 华文行楷;
            /* 字体其他样式如何自学：https://developer.mozilla.org/zh-CN/  */

            /* 修改文字颜色 */
            color: aqua;
        }
    </style>
</head>
<body>
    
    <h1>
        落花流水春去也
    </h1>
</body>
</html>
2. css代码位置，样式和结构分离。

  1. 将css代码单独封装到第三方文件  sty.css 

  2. 在需要用到的页面中引入 

```html
<link rel="stylesheet" href="./sty.css">
```

3. 选择器:如何选中元素
1. 基础选择器

  1. 元素选择器

  2. id选择器

  3. 类名选择器

  4. 通配符选择器

2. 复合选择器
  1. 后代

  2. 儿子

  3. 兄弟

  4. 并集

  5. nth-child()

  6. ...