UITcloudServer
####  项目名称
###### UI云测平台后端代码

####  项目目录
- v1
    请进入到v1目录中查看！

####  功能包含
- appium功能相关
    - 支持通过配置File Browser APK链接来下载安装测试应用
    - 使用python库click在命令行中调用Appium执行UI自动化测试
    - 使用pytest+allure来作为单元测试框架与生成测试报告
    - 使用python库logbook来记录操作日志
    
####  工程版本
- v1
    - 命令行方式
        - 本地使用
            - 功能1：进行Appium UI测试
                - Terminal进入到v1目录中，输入命令：
                   python manage.py appiumtest
- v2(紧急进行中，暂时不可用)
    - web接口方式
        - 本地使用
            - Terminal进入到v2目录中，输入命令：
                uvicorn main:app --reload
        - 远程调用
            - 待开发
    
#### 环境安装
- 1.python相关依赖库的安装
    pip install -r requirements.txt -i https://pypi.douban.com/simple
- 2.appium环境安装
    - 详见《appium安装文档》
- 3.allure工具安装
    - 详见《allure安装文档》
    

#### 待解决问题
1. 将testlink中测试用例的名称与描述与cases中对应脚本匹配，并在Allure报告中展示
2. Apk包除了从共享文件夹中下载，同时支持使用本地包
3. 完善H5页面元素的定位方法
4. 后期抽离出逻辑层与数据层
5. 执行失败的情况下会自动截图


#### 更新日志：
##### 2020-5-10 
1.完成页面元素数据分离到elements.yaml文件中，可以方便测试同学更好的维护页面元素 。具体实现：