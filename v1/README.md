#### V1工具使用指导

##### Page Object 设计模式
请阅读：https://confluence.sui.work/pages/viewpage.action?pageId=67798249


##### 目录结构
测试执行员需重点关注cases与pages这两个目录
- cases # 测试用例目录，层级应与pages层级保持一致
- pages # APP页面元素目录，收纳了每个页面的页面元素，测试用例需要从中获取页面对象
- config # 配置文件，测试员只需要关心 FILE_BROWSER_SHARE_URL为本次测试需要下载应用的链接地址
- core # 核心文件，封装了driver操作元素的API、调用adb的API、以及下载校验apk的API等
- log # 执行日志存放目录
- utls # 一些常用组件，如log、email等
- test # 单元测试集合，如果你需要调试，可以在这里面新建文件测试，不要破坏其他目录中进行调试


#### 页面元素维护人员如何使用指导

- 1.pages中录入页面元素
    
- 2.cases中写入测试用例
   
##### 测试用例与测试报告如何关联
- 1.不需要怎么关联，命名为test_开头的函数就可以了


##### 测试人员如何在命令行中使用工具

- 1.本地开启Appium Server

- 2.设置v1目录为项目根目录，设置方式：选中v1目录，鼠标右键选择Mark Directory as Root Directory

- 3.config/ssj.py与kn.py中FILE_BROWSER_SHARE_URL设置为http://10.201.5.161:7777中APK应用下载链接

- 4.在Pycharm Terminal中进入v1目录，根据下面的提示输入相应命令
    - 批量执行cases目录下所有测试用例
        - python manage.py appiumtest

    - 批量执行cases目录下随手记APP测试用例
        - python manage.py appiumtest --case_path ssj
    
    - 批量执行cases目录下卡牛APP测试用例
        - python manage.py appiumtest --case_path kn
   
#### 常见问题解答
- Appium相关问题
    - 1.Appium运行过程中在窗口中出现，导致AppiumServer长时间无反应的处理方法
        参考博客：https://blog.csdn.net/qq_42311568/article/details/84644533
        与重启手机
        如果上面操作没有效果，只有重启AppiumDesktop
    - 2.Appium Desktop定位元素参考博客：https://blog.csdn.net/zw1_csdn/article/details/95108233
        
    
- Pycharm中如何使用Pytest调试单一测试用例
    - 参考博客：https://www.cnblogs.com/yoyoketang/p/9366638.html