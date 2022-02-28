# 运行python
1. 右键开始
2. Powershell（管理员身份）
3. 修改安全策略，允许修改：Set-ExecutionPolicy -ExecutionPolicy RemoteSigned（来源：https://blog.csdn.net/z_dmsd/article/details/107394983）
4. 返回结果如下，应该是ok了
尝试新的跨平台 PowerShell https://aka.ms/pscore6

加载个人及系统配置文件用了 4236 毫秒。
(base) PS D:\My docsify\docs> conda activate py38
(py38) PS D:\My docsify\docs> & D:/Anaconda/envs/py38/python.exe
Python 3.8.8 (default, Apr 13 2021, 15:08:03) [MSC v.1916 64 bit (AMD64)] :: Anaconda, Inc. on win32
Type "help", "copyright", "credits" or "license" for more information.

# 设置settings.json
python3.8对应的环境地址是：D:/Anaconda/envs/py38/python.exe
手动配置python解释器的路径到settings.json里
    左下角齿轮-设置
    搜索python path
    设置Python: Default Interpreter Path



这样就不需要修改powershell安全策略了，更安全（见上一条）
来源：https://blog.csdn.net/gwzz1228/article/details/105449843
