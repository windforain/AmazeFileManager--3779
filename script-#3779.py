# bug reproduction script for bug #3779 of AFM
import sys
import time
import uiautomator2 as u2

def wait(seconds=2):
    for i in range(0, seconds):
        print("wait 1 second ..")
        time.sleep(1)

if __name__ == '__main__':
    avd_serial = sys.argv[1]
    server_ip = sys.argv[2]
    share_path = sys.argv[3]
    username = sys.argv[4]
    password = sys.argv[5]
    d = u2.connect(avd_serial)
    d.app_start("com.amaze.filemanager")


    out = d(resourceId="com.amaze.filemanager:id/sd_main_fab").click()
    if not out:
        print("Success: 点击右下角加号 ")
    wait()

    out = d(resourceId="com.amaze.filemanager:id/sd_label", text="网盘").click()
    if not out:
        print("Success: 点击网盘 ")
    wait()

    out = d(text="SMB 共享连接").click()
    if not out:
        print("Success: 点击 SMB共享连接 ")
    wait()

    out = d(resourceId="com.amaze.filemanager:id/md_buttonDefaultPositive").click()
    if not out:
        print("Success: 点击 使用自定义IP ")
    wait()

    out = d(text="服务器 IP 地址 *").set_text(text=server_ip)
    if not out:
        print("Success: 输入SMB服务端IP ")
    wait()

    out = d(text="分享路径").set_text(text=share_path)
    if not out:
        print("Success: 输入SMB服务端文件夹存储位置 ")
    wait()

    width, height = d.window_size()
    d.swipe(0.5 * width, 0.8 * height, 0.5 * width, 0.3 * height, 0.5)

    out = d(text="用户名 *").set_text(text=username)
    if not out:
        print("Success: 输入SMB服务端用户名 ")
    wait()

    out = d(text="密码 *").set_text(text=password)
    if not out:
        print("Success: 输入SMB服务端密码 ")
    wait()

    out = d(resourceId="com.amaze.filemanager:id/md_buttonDefaultPositive").click()
    if not out:
        print("Success: 点击新建 ")
    wait()

    out = d(description="转到上一层级").click()
    if not out:
        print("Success: 打开竖导航栏 ")
    wait()


    out = d(text="SMB 共享连接").click()
    if not out:
        print("Success: 打开SMB连接 ")
    wait()

    out = d.xpath('//*[@resource-id="com.amaze.filemanager:id/scroll1"]/android.widget.LinearLayout[1]').click()
    if not out:
        print("Success: 点开上侧路径栏 ")
    wait()

    out = d.xpath('//*[@resource-id="com.amaze.filemanager:id/buttons"]/android.widget.ImageButton[1]').click()
    if not out:
        print("Success: 点击安卓LOGO ")
    wait()
