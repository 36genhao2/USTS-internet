# Dr.COM 校园网自动登录脚本

这是一个用于 Dr.COM 认证系统的校园网自动登录脚本，支持校园网、中国移动、中国联通、中国电信等多种运营商。通过模拟浏览器 POST 请求完成登录，适合在命令行环境中快速联网。

## 依赖

- Python 3.x
- requests 库（如未安装，请执行 `pip install requests`）

## 配置步骤

1. **打开脚本**，找到以下变量并填写你的账号和密码：
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

## 运行
在终端（命令行）中进入脚本所在目录，执行：

bash
python login.py

## 注意事项
认证页面地址默认设为 http://10.160.63.9:801/eportal/?c=ACSetting&a=Login，如果你的校园网使用不同的 IP 或端口，请修改脚本中的 login_url 变量。

如果登录失败，可以取消脚本最后几行的注释（删除 # print(response.text) 前的 #），重新运行以查看服务器返回的原始内容，便于排查问题。

脚本采用 GB2312 编码解析返回内容，若出现乱码可尝试修改 response.encoding 为 'utf-8' 或 'gbk'。

请确保运行脚本的设备已连接到校园网（通常需要先连接 Wi-Fi 或网线）。
