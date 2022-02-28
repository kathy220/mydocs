# Docsify的安装说明

- **安装Nodejs**
    - 教程：https://blog.csdn.net/muzidigbig/article/details/80493880
    - 安装路径：D:/nodejs/
    - 自动配置PATH环境变量
    - CMD测试安装成功：node --version和npm --version

- **CMD - Nodejs - 安装Docsify**
    - 检查是否安装过：docsify -v
    - 安装：npm i docsify-cli -g
    - 确认成功：docsify -v
    - 自定义路径：cd /d d:\My docsify
    - 初始化工程目录
        - docsify init ./docs
        - docsify serve ./docs

- **上手使用**
    - 初始化成功后，docs文件夹下出现3个文件
        - index.html入口文件
        - README.md直接编辑就能更新网站内容
        - .nojekyll阻止GitHub Pages会忽略掉下划线开头的文件
    - 每次启动
        - 定位到docs所在目录
            - 方法一：CMD -> cd /d d:\My docsify
            - 方法二：打开文件所在目录 -> 输入CMD
        - 启动
            - docsify serve ./docs
            - http://localhost:3000

- **后续完善**
    - 设置封面、侧边栏/目录、导航栏、主题等
    - 参考材料
        - 官方文档 https://docsify.js.org/#/zh-cn/
        - 主题自定义 https://jhildenbiddle.github.io/docsify-themeable/#/
        - 各种emoji https://www.webfx.com/tools/emoji-cheat-sheet/
