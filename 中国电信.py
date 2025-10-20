from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import os
import time


def telecom_login():
    print("正在启动Edge浏览器进行中国电信登录...")

    # 配置浏览器选项
    options = webdriver.EdgeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')

    driver = webdriver.Edge(options=options)

    # 实际登录页面URL
    login_url = "http://10.160.63.9/"

    print(f"正在访问: {login_url}")
    driver.get(login_url)

    try:
        # 使用显式等待
        wait = WebDriverWait(driver, 0.5)

        # 等待页面完全加载
        print("等待页面加载...")
        wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))

        # 检查当前页面URL
        print(f"当前页面: {driver.current_url}")

        # 读取账号密码
        desktop_path = os.path.join(os.path.expanduser("~"), "Desktop", "账号.txt")
        print(f"读取账号文件: {desktop_path}")

        with open(desktop_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            username = lines[0].strip()
            password = lines[1].strip() if len(lines) > 1 else ""

        print(f"账号: {username}")

        # 专门选择中国电信运营商
        print("选择中国电信运营商...")
        time.sleep(2)

        # 使用Select类选择中国电信
        try:
            # 找到运营商选择下拉框
            isp_select = wait.until(
                EC.presence_of_element_located((By.NAME, "ISP_select"))
            )

            # 创建Select对象
            select = Select(isp_select)

            # 选择中国电信 (value="@telecom")
            select.select_by_value("@telecom")
            print("✓ 已选择中国电信")

            # 验证选择是否成功
            selected_option = select.first_selected_option
            if selected_option.get_attribute("value") == "@telecom":
                print("✓ 中国电信选择确认成功")
            else:
                print("⚠ 运营商选择可能未生效，尝试备用方法")
                # 备用方法
                select.select_by_visible_text("中国电信")

        except Exception as e:
            print(f"运营商选择失败: {e}")
            return False

        # 填写账号
        username_selectors = [
            'input[name="DDDDD"]',
            'input[name="username"]',
            'input[type="text"]',
            '#username',
            '.username'
        ]

        username_filled = False
        for selector in username_selectors:
            try:
                username_input = wait.until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, selector))
                )
                username_input.clear()
                username_input.send_keys(username)
                print(f"✓ 已填写账号: {username}")
                username_filled = True
                break
            except:
                continue

        # 填写密码
        password_selectors = [
            'input[name="upass"]',
            'input[name="password"]',
            'input[type="password"]',
            '#password',
            '.password'
        ]

        password_filled = False
        for selector in password_selectors:
            try:
                password_input = wait.until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, selector))
                )
                password_input.clear()
                password_input.send_keys(password)
                print("✓ 已填写密码")
                password_filled = True
                break
            except:
                continue

        # 尝试点击登录按钮
        login_button_selectors = [
            'input[type="submit"]',
            'button[type="submit"]',
            '.login-btn',
            '#loginBtn',
            'input[value="登录"]'
        ]

        login_clicked = False
        for selector in login_button_selectors:
            try:
                login_button = wait.until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, selector))
                )
                driver.execute_script("arguments[0].click();", login_button)
                print("✓ 已点击登录按钮")
                login_clicked = True

                # 等待登录结果
                print("等待登录结果...")
                time.sleep(5)

                # 检查是否登录成功
                current_url = driver.current_url
                print(f"登录后页面: {current_url}")

                if "success" in current_url.lower() or "3.htm" in current_url:
                    print("🎉 中国电信登录成功！")
                    return True
                else:
                    print("⚠ 登录状态未知，请检查页面")
                    return False

                break
            except Exception as e:
                continue

        if not username_filled or not password_filled:
            print("❌ 未找到输入框，请手动填写")
            print("请在页面中手动填写账号密码后按回车继续...")
            input()
        elif not login_clicked:
            print("❌ 未找到登录按钮，请手动点击登录")
            input("请手动点击登录按钮后按回车继续...")

        return False

    except Exception as e:
        print(f"❌ 发生错误: {e}")
        input("按回车键退出...")
        return False

    finally:
        # 保持浏览器打开以便查看结果
        print("浏览器将保持打开状态，请手动关闭...")
        input("按回车键退出程序...")
        driver.quit()


if __name__ == "__main__":
    success = telecom_login()
    if success:
        print("✅ 中国电信自动登录流程完成")
    else:
        print("❌ 中国电信自动登录失败")