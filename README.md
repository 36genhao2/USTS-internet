# 校园网自动连接脚本

## 简介
本项目旨在通过自动化脚本实现校园网的自动登录。针对使用哆点（Dr.COM）认证系统的校园网络，通过Selenium模拟浏览器操作，脚本能够自动选择运营商（如中国联通）、读取本地存储的账号密码并完成登录。
## 使用方法

### 1. 配置账号信息
在桌面上创建 `账号.txt` 文件，按以下格式输入账号和密码：

账号

密码

注意：账号和密码之间使用换行分隔。

### 2. 运行环境
建议使用 PyCharm 运行此脚本，便于安装和管理所需的库。

### 3. 运行脚本
直接运行主Python文件即可开始自动连接流程。

## 注意事项

### 浏览器相关问题
- 如果 Microsoft Edge 浏览器打开较慢，请先手动打开一次浏览器，然后再运行脚本。
- 如果打开网页后未自动选择运营商，请打开Python文件，找到以下代码：
  ```python
  wait = WebDriverWait(driver, 0.5)
将 0.5 改为更大的数值（如 1、5、10），以增加等待时间。

### 元素定位说明
代码通过查找页面元素来定位操作位置，由于JavaScript动态加载或页面结构变化，元素定位可能不准确。

在运营商选择环节，正常的radio和label元素可能无法被正常识别，脚本使用了CSS选择器

### 测试信息
当前测试环境使用中国联通，其他三个运营商（中国移动、中国电信、校园网）理论上都能正常填入。

如果在使用过程中遇到问题，请及时反馈。

### 依赖库
运行此脚本需要安装以下Python库：

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import os
import time
