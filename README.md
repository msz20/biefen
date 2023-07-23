# 参考网站
[马老师在线课堂](http://mayw.host3v.club/mageOnline/)

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
## 1. 网页

    1. 元素：文字、音视频、链接。。。html : 结构

      1. 样式：将元素排版。。。。css：  化妆

    2. 交互: 动态效果+校验。。。。js  ： 动作

      1. 数据：从服务端获取的内容：  灵魂
      
    [静态网站效果](http://jdd93.host3v.club/mddshopping/)

## 2. HTML

    1. 默认结构，自动生成

    2. 元素都由标签的形式体现

      1. 双标签

      2. 单标签

      3. 理解标签属性

        1. 属性名

        2. 属性值

        3. 成对组成

## 3. 常见标签

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

## 4. 元素的显示模式

      1. 块级元素：独占一行，可以直接设置尺寸

        1. 标题

        2. p段落

      2. 行内元素：一行内显示：不可以直接设置尺寸

        1. Span

      3. 行内块：可以一行显示，但是可以设置宽高尺寸


# 3. Css

    ## 1. 入门
        1. css存放位置

          css代码要放在 style 标签中
          style  标签要放在 head 标签中
          
        2. 语法
        ```css
          选中要求改的元素{
              属性名1 : 属性值1;
              属性名2 : 属性值2;
              ....
          }
        ```

      代码示例
      ```html
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
      ```

  ## 2. css代码位置，样式和结构分离。

      1. 将css代码单独封装到第三方文件  sty.css 

      2. 在需要用到的页面中引入 

    ```html
    <link rel="stylesheet" href="./sty.css">
    ```

  ## 3. 选择器:如何选中元素
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

# 盒子模型
  ## 1. 盒子类型：
    内容盒子
    边框盒子（CSS3的盒子或者IE的怪异盒子）
  ## 2. 尺寸+边框
  ## 3. 内边距
  ## 4. 外边距
  ## 5. 文字水平居中 + 文字垂直居中 + 盒子水平居中 

# 布局知识

  ## 常见设置
  ```css
            /* 清除内外边距 设置盒子模型 */
            *{
                padding: 0;
                margin: 0;
                box-sizing: border-box;
            }

/* 取消li的小圆点 */
list-style: none;

/* 超出盒子内容隐藏起来 */
overflow: hidden; 
/* 左浮动 */
 float: left;








  ```
  ## 布局技巧
    1. 使得块级元素一行内显示的时候，不要使用行内块。因为自带缝隙，不方便处理。
    2. 使用浮动或者flex

# flex布局
  1. 容器： display: flex;
  2.  主轴方向          
   ```css
         
            /* 设置主轴方向 ： 在容器中，子元素的排列方向*/
            /* 设置主轴为 x 轴 */
            flex-direction: row;
            
            /* 设置主轴为 x 轴 逆向  用的极少*/
            flex-direction: row-reverse;

            /* 设置主轴为 y 轴 */
            flex-direction: column;

             /* 设置主轴为 y 轴 逆向  用的极少*/
            flex-direction: column-reverse;
   ```            
  3. 观察子盒子弹性效果。是否换行。
  ```css
              /* 子元素是否换行显示：
                flex-wrap该属性记得是加在父容器身上，控制子项换行方式。
                    nowrap : 默认，不换行，当子项总尺寸超过父容器的时候，也不换行，而是弹性挤压子项的尺寸。
                    wrap： 换行，不挤压子项尺寸，装不下就换行。
            */
            flex-wrap: nowrap;
            flex-wrap: wrap;
  
  ```
  4. 主轴位置
  ```css
    /* 在主轴排列方式 
            justify-content:控制主轴排列方式
                flex-start：默认值，从前往后。
                flex-end: 靠主轴末端。
                center: 主轴居中
                space-around: 把主轴上子项没用完的剩余空间，平均分给主轴上子项的两侧。均分空间的意思。
                space-between : 主轴左右两侧贴边，中间的空间平分
            */
            justify-content: flex-start;
            justify-content: flex-end;
            justify-content: center;
            justify-content: space-around;
            justify-content: space-between;
  
  ```
  5. 侧轴位置
  ```css
               /* 
                在侧轴排列方式
                align-items: 控制侧轴排列
                    flex-start：默认，靠侧轴从前往后。
                    flex-end : 靠侧轴，从后往前
                    center : 侧轴居中显示
            */
            align-items: flex-start;
            align-items: flex-end;
            align-items: center;
  ```