# 参考资料

 [马哥在线网站PSD效果图](https://www.123pan.com/s/A7oDVv-DyY4H) 

 [马哥在线网站](http://mayw.host3v.club/mageOnline/)
***

# 在线文档
  
  [bootstap中文文档](https://www.bootstrap.cn/doc/read/94) 
  
  [vue文档](https://cn.vuejs.org/)

  [express中文文档](https://nodejs.cn/express/starter/)

  [axios中文网](https://axios.nodejs.cn/docs/intro)

## vue快速入门：服务于web动态网站
  ```html
     <!DOCTYPE html>
      <html lang="en">
          <head>
              <meta charset="UTF-8">
              <title>马老师讲前端</title>
          </head>
          <body>
              
              <div id="app">
                  {{ age }}

                  <textarea name="" id="" cols="30" rows="10" ref="area" v-model="content" 
                  v-on:keydown.enter="getTextareaCon()"></textarea>

                  <hr>
                  <ul>
                      <li v-for="item in arr">  {{item}} </li>
                  </ul>
              </div>
          
              <div id="box"></div>
          </body>
      </html>
      <script src="https://unpkg.com/vue@3/dist/vue.global.js"></script>

      <script>

      const { createApp } = Vue


      const app = createApp({
          data(){
              return {
                  age :39,
                  content :'',
                  arr : []
              }
          } ,

          methods:{
              getTextareaCon(e){
                this.arr.push(this.content) 
                console.log(this.arr)
                this.content = ''
                //让当前元素输入框，失去焦点
                this.$refs.area.blur()
              }
          }

      })

      app.mount('#app')

      </script>
  ```


# 软件安装
[MySQL8 （安装版）教程](https://malaoshi.feishu.cn/docx/doxcn8yWT5lVNSPjbI18TSAHA9f)

[navicat安装步骤](https://malaoshi.feishu.cn/docx/doxcnCYDWKREgRhaBfQ3gu9xLWd)

[node安装步骤](https://malaoshi.feishu.cn/docx/N99sdLaPOoS1DVx9PqYclqRmnhc)
---

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
