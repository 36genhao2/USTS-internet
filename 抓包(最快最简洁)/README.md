# Dr.COM 校园网自动登录脚本

这是一个用于 Dr.COM 认证系统的校园网自动登录脚本，支持校园网、中国移动、中国联通、中国电信等多种运营商。通过模拟浏览器 POST 请求完成登录，适合在命令行环境中快速联网。

## 依赖

- Python 3.x
- requests 库（如未安装，请执行 `pip install requests`）

## 配置步骤

打开脚本，找到以下变量并填写你的账号和密码：
  ```python
  username = ""  # 例如：20231145
  password = ""  # 例如：123456
选择运营商：脚本中已列出四种后缀，请只保留你需要的行（去掉行首的 #），其他行请保持注释状态：
  ```python
   # carrier_suffix = "@keda"      # 校园网
   # carrier_suffix = "@cmcc"      # 中国移动 (CMCC)
   carrier_suffix = "@unicom"      # 中国联通
   # carrier_suffix = "@telecom"    # 中国电信
默认启用的是 中国联通，如需更改请相应调整。

保存脚本（例如保存为 login.py）。
