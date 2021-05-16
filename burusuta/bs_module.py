import pyautogui  
import cv2
import numpy as np
from time import sleep
import requests
import importlib
import autoGame as auto 

class bs_module:
    
    #類似度の設定(0~1)
    threshold = 0.85
    # LINE
    url = "https://notify-api.line.me/api/notify"
    access_token = '1mWfffgRMzwVgHRYPB71czaDify4QkQ4F7zq7t4zyQE'
    headers = {'Authorization': 'Bearer ' + access_token}
    moduleName = "test"


    def callName(self):
        print(self.moduleName)

    def setName(self, name):
        self.moduleName = name

    def reload(self):
        importlib.reload(self.moduleName)

    def screencap(self):
        screenshot = pyautogui.screenshot()
        screenshot.save('C:\\Users\\kousuke\\Pictures\\uma\\BS\\screen.PNG')

    def gacha_screencap(self, path):
        sleep(1)
        screenshot = pyautogui.screenshot()
        screenshot.save('C:\\Users\\kousuke\\Pictures\\uma\\BS\\gacha' + str(path) + '.PNG')

    def screenChk(self, x, y, path):
        judge = 0
        cnt = 0
        path = 'C:\\Users\\kousuke\\Pictures\\uma\\BS\\' + str(path) + '.PNG'
        for num in range(40):
            sleep(0.5)
            self.screencap()
            if cnt == 10:
                if self.chkImg('C:\\Users\\kousuke\\Pictures\\uma\\BS\\home.PNG'):
                    self.freezChk()
            judg = self.chkImg(path)
            cnt += 1
            if judg == True:
                pyautogui.click(x, y)
                break
        if judg == False:
            self.freezChk()

    def freezChk(self):
        pyautogui.click(580, 1015)
        print("フリーズ")
        sleep(1)
        # タブ消去
        pyautogui.click(500, 90)
        sleep(1)
        # アプリ起動
        pyautogui.click(445, 115)
        sleep(2)
        for num in range(5):
            sleep(10)
            self.screencap()
            if self.chkImg('C:\\Users\\kousuke\\Pictures\\uma\\BS\\stack.PNG'):
                self.freezChk()
            else:
                self.riset()


    def riset(self):
        path = 'C:\\Users\\kousuke\\Pictures\\uma\\BS\\han.PNG'
        judge = 0
        for num in range(30):
            sleep(1)
            self.screencap()
            judg = self.chkImg(path)
            if judg == True:
                print("リセットします")
                pyautogui.click(520, 995)
                sleep(1)
                pyautogui.click(230, 840)
                sleep(1)
                pyautogui.click(405, 680)
                sleep(1)
                pyautogui.click(405, 680)
                sleep(1)
                # 閉じる
                pyautogui.click(275, 685)
                sleep(1)
                auto.main()
        if judg == False:
            self.freezChk()

    def continuous_tap(self, x, y, path):
        path = 'C:\\Users\\kousuke\\Pictures\\uma\\BS\\' + str(path) + '.PNG'
        judge = 0
        for num in range(30):
            pyautogui.click(x, y)
            sleep(1)
            self.screencap()
            judge = self.chkImg(path)
            if judge == True:
                break
        
        if judge == False:
            self.freezChk()
            self.riset()


    def chkImg(self, temp):
        screen = "C:\\Users\\kousuke\\Pictures\\uma\\BS\\screen.PNG"
        
        # キャプチャ画像
        _input = cv2.imread(screen)
        # 見本画像
        _temp = cv2.imread(temp)

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
        return result

    def multi_chkImg(self, temp):
        input = "C:\\Users\\kousuke\\Pictures\\uma\\BS\\ssr.PNG"
        img_rgb = cv2.imread(temp)
        img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
        template = cv2.imread(input, 0)
        w, h = template.shape[::-1]
        cnt = 0

        res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
        self.minVal, self.maxVal, self.minLoc, self.maxLoc = cv2.minMaxLoc(res)
        print(self.maxVal)
        threshold = 0.8
        loc = np.where( res >= threshold)
        print(loc)
        for pt in zip(*loc[::-1]):
            cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
            cnt += 1
        cv2.imwrite('C:\\Users\\kousuke\\Pictures\\uma\\BS\\res.PNG',img_rgb)
        cnt -= 1
        print('SSRの数' + str(cnt))
        return cnt

    def hokan_matchTemplate(self, temp):
        input = [
            "D:/Program Files/Nox/bin/pics/kakeru2.png",
            "D:/Program Files/Nox/bin/pics/kakeru3.png",
            ]
        cnt = 0
        threshold = 0.8

        for i in input:
            img_rgb = cv2.imread(temp)
            img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
            template = cv2.imread(i, 0)
            w, h = template.shape[::-1]

            res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
            self.minVal, self.maxVal, self.minLoc, self.maxLoc = cv2.minMaxLoc(res)
            print(self.maxVal)
            loc = np.where( res >= threshold)
            print(loc)
            if self.threshold < self.maxVal:
                for pt in zip(*loc[::-1]):
                    if i == "D:/Program Files/Nox/bin/pics/kakeru2.png":
                        cnt += 2
                    elif i == "D:/Program Files/Nox/bin/pics/kakeru3.png":
                        cnt += 3
            cnt -= 1 

    def line_message(self, ssr, image):
        message = 'SSRの数:' + str(ssr)
        payload = {'message': message}
        if ssr >= 6:
            files = {'imageFile': open(image, 'rb')}
            requests.post(self.url, headers = self.headers, params = payload, files = files)
        else:
            requests.post(self.url, headers = self.headers, params = payload)
