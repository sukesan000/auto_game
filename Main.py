import Game_module as gModule
from time import sleep
from subprocess import run, PIPE
import subprocess


def main():
    mod = gModule.Game_module()
    # Nox起動
    subprocess.Popen('"D:\\Program Files\\Nox\\bin\\Nox.exe" -clone:Nox_4')
    print ("wait for app...")
    sleep(50)

    # アプリ起動
    mod.start_app()

    # スクリーンショット
    mod.screencap()
    
    if(mod.chkImg('D:\\Program Files\\Nox\\bin\\pics\\syotoka.png'))
        sleep(3)

    # 見本と比較
    # x, y = Module.chkImg('./img/Home.png')
    # print(x + y)

if __name__ == '__main__':
     main()