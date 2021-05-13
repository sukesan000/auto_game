import subprocess
from subprocess import run, PIPE
import cv2
import numpy as np
from matplotlib import pyplot as plt
import requests

class Game_module:
    minVal = 0
    maxVal = 0
    minLoc = []
    maxLoc = []
    # id = ''

    # LINE
    url = "https://notify-api.line.me/api/notify"
    access_token = '1mWfffgRMzwVgHRYPB71czaDify4QkQ4F7zq7t4zyQE'
    headers = {'Authorization': 'Bearer ' + access_token}

    #類似度の設定(0~1)
    threshold = 0.85
    
    def setId(self, noxId):
        self.id = noxId

    def chkImg(self, dir_temp, isTap):
        result =self.matchTemplate(dir_temp, isTap)
        return result
        

    def matchTemplate(self, dir_temp, isTap):
        dir_input = "D:/Program Files/Nox/bin/pics/No1/_capture1.png"
        
        # キャプチャ画像
        _input = cv2.imread(dir_input)
        # 見本画像
        _temp = cv2.imread(dir_temp)

        gray = cv2.cvtColor(_input, cv2.COLOR_RGB2GRAY)
        temp = cv2.cvtColor(_temp, cv2.COLOR_RGB2GRAY)

        _h, _w = temp.shape

        _match = cv2.matchTemplate(_input, _temp, cv2.TM_CCOEFF_NORMED)
        # 最も類似度が高い位置と低い位置を取得します
        self.minVal, self.maxVal, self.minLoc, self.maxLoc = cv2.minMaxLoc(_match)
        
        if self.threshold < self.maxVal:
            result = True
        else:
            result = False
        
        print(self.maxVal)

        _loc = np.where(_match >= self.threshold)
        
        if result == True:
            try:
                _x = _loc[1][0]
                _y = _loc[0][0]
                x =  _x + _w / 2
                y =  _y + _h / 2
                print(x)
                print(y)
                if isTap == True:
                    self.tap(x + _w / 2, _y + _h / 2)
                return True
            except IndexError as e:
                return False

        else:
            return False

    def multi_matchTemplate(self, dir_temp):
        dir_input = "D:/Program Files/Nox/bin/pics/ssr.png"
        img_rgb = cv2.imread(dir_temp)
        img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
        template = cv2.imread(dir_input, 0)
        w, h = template.shape[::-1]
        cnt = 0

        res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
        self.minVal, self.maxVal, self.minLoc, self.maxLoc = cv2.minMaxLoc(res)
        print(self.maxVal)
        threshold = 0.8
        loc = np.where( res >= threshold)
        print(loc)
        for pt in zip(*loc[::-1]):
            cnt += 1
            cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
        cv2.imwrite('D:/Program Files/Nox/bin/pics/No1/res.png',img_rgb)
        print('SSRの数' + str(cnt))
        return cnt

    def hokan_matchTemplate(self, dir_temp):
        dir_input = [
            "D:/Program Files/Nox/bin/pics/kakeru2.png",
            "D:/Program Files/Nox/bin/pics/kakeru3.png",
            ]
        cnt = 0

        for i in dir_input:
            img_rgb = cv2.imread(dir_temp)
            img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
            template = cv2.imread(i, 0)
            w, h = template.shape[::-1]

            res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
            self.minVal, self.maxVal, self.minLoc, self.maxLoc = cv2.minMaxLoc(res)
            print(self.maxVal)
            threshold = 0.8
            loc = np.where( res >= threshold)
            print(loc)
            if self.threshold < self.maxVal:
                for pt in zip(*loc[::-1]):
                    if i == "D:/Program Files/Nox/bin/pics/kakeru2.png":
                        cnt += 2
                        print('2')
                    elif i == "D:/Program Files/Nox/bin/pics/kakeru3.png":
                        cnt += 3
                        print('3')
        return cnt

    def screencap(self):
        _cmd = "nox_adb shell screencap -p /sdcard/_capture1.png"
        self.send_cmd_to_adb(_cmd)
        _cmd = "nox_adb pull /sdcard/_capture1.png pics/No1"
        self.send_cmd_to_adb(_cmd)

    def gacha_screencap(self, imageCnt):
        _cmd = "nox_adb shell screencap -p /sdcard/gacha_kekka1_" + str(imageCnt)+ ".png"
        self.send_cmd_to_adb(_cmd)
        _cmd = "nox_adb pull /sdcard/gacha_kekka1_" + str(imageCnt) + ".png" + " pics/No1"
        self.send_cmd_to_adb(_cmd)

    def start_app(self, x):
        _cmd = "nox_adb shell am start -n " + str(x)
        self.send_cmd_to_adb(_cmd)

    def stop_app(self, x):
        _cmd = "nox_adb shell am force-stop " + str(x)
        self.send_cmd_to_adb(_cmd)

    def inputText(self, message):
        _cmd = "nox_adb shell input text " + str(message)
        self.send_cmd_to_adb(_cmd)

    def judgeMatching(self):
        if self.threshold < self.maxVal:
            return True
        else:
            return False

    def line_message(self, ssr, image):
        message = 'SSRの数:' + str(ssr)
        payload = {'message': message}
        if ssr >= 6:
            files = {'imageFile': open(image, 'rb')}
            requests.post(self.url, headers = self.headers, params = payload, files = files)
        else:
            requests.post(self.url, headers = self.headers, params = payload)
        
    def swipe(self, x1, y1, x2, y2, seconds):
        _millis = seconds * 1000
        _cmd = "nox_adb shell input touchscreen swipe " + str(x1) + " " + str(y1) + " " + str(x2) + " " + str(y2) + " " + str(_millis)
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

        