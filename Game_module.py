import subprocess
from subprocess import run, PIPE
import cv2
import numpy as np

class Game_module:
    def chkImg(self, dir_temp):
        self.matchTemplate()
        

    def matchTemplate(self)
    dir_input = "D:/Program Files/Nox/bin/pics/_capture.png"
        _THRESHOLD = 0.9 #類似度
        
        # キャプチャ画像
        _input = cv2.imread(dir_input)
        # 見本画像
        _temp = cv2.imread(dir_temp)

        gray = cv2.cvtColor(_input, cv2.COLOR_RGB2GRAY)
        temp = cv2.cvtColor(_temp, cv2.COLOR_RGB2GRAY)

        print(temp.shape)
        _h, _w = temp.shape

        _match = cv2.matchTemplate(_input, _temp, cv2.TM_CCOEFF_NORMED)
        _loc = np.where(_match >= _THRESHOLD)
        # 類似度が0.9以下であればfalse　0.9以上であれば続行
        try:
            _x = _loc[1][0]
            _y = _loc[0][0]
            #ここでタッチメソッド

            #returnでtrueを返す
            return _x + _w / 2, _y + _h / 2
        except IndexError as e:
            return -1, -1

    def screencap(self):
        _cmd = "nox_adb shell screencap -p /sdcard/_capture.png"
        self.send_cmd_to_adb(_cmd)
        _cmd = "nox_adb pull /sdcard/_capture.png pics"
        self.send_cmd_to_adb(_cmd)

    def self.start_app():
        _cmd = "nox_adb shell am start -n jp.co.cygames.umamusume/jp.co.cygames.umamusume_activity.UmamusumeActivity"
        self.send_cmd_to_adb(_cmd)


    def tap(self, x, y):
        _cmd = "nox_adb shell input touchscreen tap " + str(x) + " " + str(y)
        self.send_cmd_to_adb(_cmd)

    def send_cmd_to_adb(self, cmd):
        _dir = "D:\\Program Files\\Nox\\bin"
        return self.doscmd(_dir, cmd)

    def doscmd(self, directory, command):
        completed_process = run(command, stdout=PIPE, shell=True, cwd=directory, universal_newlines=True, timeout=10)
        return completed_process.stdout
        