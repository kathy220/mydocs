# Docsify的学习笔记

## 安装说明

### 安装Nodejs
1. 教程：https://blog.csdn.net/muzidigbig/article/details/80493880
2. 安装路径：D:/nodejs/
3. 自动配置PATH环境变量
4. CMD测试安装成功：node --version和npm --version

### CMD - Nodejs - 安装Docsify
1. 检查是否安装过：docsify -v
2. 安装：npm i docsify-cli -g
3. 确认成功：docsify -v
4. 自定义路径：cd /d d:\My docsify
5. 初始化工程目录
    - docsify init ./docs
    - docsify serve ./docs

### 上手使用
1. 初始化成功后，docs文件夹下出现3个文件
2. index.html入口文件
3. README.md直接编辑就能更新网站内容
4..nojekyll阻止GitHub Pages会忽略掉下划线开头的文件
5. 每次启动
    - 定位到docs所在目录
      - 方法一：CMD -> cd /d d:\My docsify
      - 方法二：打开文件所在目录 -> 输入CMD
    - 启动
      - docsify serve ./docs
      - http://localhost:3000

### 后续完善
1. 设置封面、侧边栏/目录、导航栏、主题等
2. 参考材料
    - 官方文档 https://docsify.js.org/#/zh-cn/
    - 主题自定义 https://jhildenbiddle.github.io/docsify-themeable/#/
    - 各种emoji https://www.webfx.com/tools/emoji-cheat-sheet/



## 每次启动
1. 传统方式
   1. CMD - 任意一个prompt
   2. cd /d d:\My docsify
   3. doscify serve docs
   4. chrome打开docs（http://localhost:3000/）
2. 简化方式
   1. 写一个windows批处理文件
   2. 详见docsify_run
   3. 快捷方式到桌面，自定义图标
   4. 只需要双击桌面图标，即可以批量完成一系列操作
3. github同步（ipad等终端查看）
   1. 在PC端正常更新知识库
   2. 打开docs文件夹 -> 空白处右键 -> 点击git bash here -> git add ./ -> git commit -m "mydocs update" -> git push

## 基础设置
1. 多页文档、导航栏、封面等（官方文档：https://docsify.js.org/#/zh-cn/）
2. 加载搜索框、侧边栏的默认折叠层数（https://www.cnblogs.com/baby123/p/14361402.html）
3. stylesheet、index备注、copy code、pagination等（https://www.jianshu.com/p/94a07580a31f）
4. 任务列表、图片缩放（官方文档助手：https://docsify.js.org/#/zh-cn/helpers）
5. 

## markdown技巧
### 字体
**黑体**  
*斜体*  
~~删除线~~  
<mark>高亮</mark>  
`强调这几个字`  
<pre>Preformatted text 还原文本本来的样子，也可以用做文字背景?</pre>  
<small>一行很小的字</small>  

这是 <sub>下标</sub>  Eg. P<sub>i</sub>=10   

这是 <sup>上标</sup> Eg. 3<sup>2</sup>=9


### Blockquotes与Notices
> 这是一段引用

?> 这是普通提示  

!> 这是重要提示  
### 待办事项
我的To-do List
- [x] 磨咖啡豆 - 磨豆机
- [ ] 做浓缩 - 摩卡壶
- [ ] 热牛奶 - 微波炉
  - [ ] 拿铁
  - [ ] 美式

### 选项卡
<!-- tabs:start -->

#### **English**

Hello!

#### **French**

Bonjour!

#### **Italian**

Ciao!

<!-- tabs:end -->

### 表格
挺麻烦的，建议直接copy  

| Left Align | Center Align | Right Align | Non&#8209;Breaking&nbsp;Header |
| ---------- |:------------:| -----------:| ------------------------------ |
| A1         | A2           | A3          | A4                             |
| B1         | B2           | B3          | B4                             |
| C1         | C2           | C3          | C4                             |

### 分割线
---

### 图片
这是一张来自网络的图片  
![docsify_logo](https://docsify.js.org/_media/icon.svg ':size=20%')  

这是一张来自本地的图片  
![account_logo](./media/account_logo.jpg ':size=20%')

### 代码
这是一段Python代码

```python
import pandas as pd

df = pd.DataFrame()
df.to_csv('./data.csv')
```

### 自动编号
1. 修改css
   VSCode - “control+shift+p” - MPE自定义样式
2. 用counter-reset构建headings自动编号












