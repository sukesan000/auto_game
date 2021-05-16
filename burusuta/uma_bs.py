from os import P_OVERLAY
import bs_module as bsModule  
from time import sleep
import pyautogui
import sys

bs = bsModule.bs_module()
class uma_bs:
    
    def auto(self):
        ssrCnt = 0
        module_name = "umamusume_BS"
        self.setName(module_name)

        bs.callName()

        print("タイトル")
        bs.screenChk(275, 820, "logo")
        sleep(1)

        print("利用規約")
        bs.screenChk(405, 960, "riyo")
        sleep(1.5)

        print("ポリ")
        bs.screenChk(405, 960, "policy")
        sleep(1)

        print("google")
        bs.screenChk(100, 690, "google")
        sleep(1)

        print("アカウント連携")
        bs.screenChk(150, 690, "renkei")
        sleep(1)

        print("チュートリアル")
        bs.screenChk(390, 680, "tuto")

        print("トレーナー登録")
        bs.screenChk(295, 485, "traner")    
        sleep(1)
        pyautogui.write('aaa', interval=0.25)
        sleep(1)
        pyautogui.click(287, 685)

        print("登録")
        bs.screenChk(275, 680, "toroku")

        print("OK")
        bs.screenChk(400, 680, "OK")

        # お知らせが出るまでタップ
        print("skip")
        bs.continuous_tap(505, 985, "message")

        print("お知らせ")
        bs.screenChk(275, 955, "message")

        print("メインストーリー")
        bs.screenChk(280, 680, "main")

        print("ストーリー解放")
        bs.screenChk(280, 950, "story")
        sleep(2)

        print("プレゼント")
        pyautogui.click(505, 745)

        print("受け取り")
        bs.screenChk(405, 955, "uketori")

        print("閉じる")
        bs.screenChk(275, 955, "tojiru")

        print("閉じる")
        bs.screenChk(150, 955, "tojiru")

        print("ガチャ")
        bs.screenChk(500, 985, "gacha")

        print("右へタップ")
        bs.screenChk(500, 640, "kokan")

        print("サポガチャ")
        bs.screenChk(445, 830, "10kai")

        print("ガチャ確認")
        bs.screenChk(400, 680, "kakunin")

        print("skip")
        bs.continuous_tap(505, 985, "kekka")

        print("ガチャ結果")
        bs.screenChk(400, 970, "kekka")

        while True:
            sleep(1)
            bs.screencap()
            if bs.chkImg('C:\\Users\\kousuke\\Pictures\\uma\\BS\\hiku.PNG'):
                pyautogui.click(395, 680)
                print("skip")
                bs.continuous_tap(505, 985, "kekka")
                print("ガチャ結果")
                bs.screenChk(400, 970, "kekka")
                sleep(1)
            else:
                print('キャンセル')
                pyautogui.click(155, 680)
                break

        print("戻る")
        bs.screenChk(160, 960, "modoru")

        print("強化編成")
        bs.screenChk(55, 995, "kyoka")

        print("サポートカード")
        bs.screenChk(390, 700, "support")

        print("一覧")
        bs.screenChk(155, 800, "itiran")

        print("スクショ１")
        sleep(2)
        bs.gacha_screencap("1")
        path = "C:\\Users\\kousuke\\Pictures\\uma\\BS\\gacha1.PNG"
        # SSRの数を数える
        ssrCnt += bs.multi_chkImg(path)

        print("戻る")
        bs.screenChk(60, 875, "modoru1")

        if ssrCnt > 3:
            print("保管室")
            bs.screenChk(385, 700, "hokan")

            print("閉じる")
            bs.screenChk(270, 980, "tojiru")

            print("チェック")
            bs.screenChk(180, 815, "check")
            sleep(1)

            print("レアリティ")
            bs.screenChk(375, 750, "rare")
            
            print("所持数")
            bs.screenChk(70, 400, "syoji")
            sleep(1)

            print("絞り込み")
            bs.screenChk(405, 140, "shibo")
            
            print("SSR")
            bs.screenChk(435, 250, "ssr_check")

            print("OK")
            bs.screenChk(400, 950, "ok1")
            sleep(1)

            if bs.chkImg('C:\\Users\\kousuke\\Pictures\\uma\\BS\\ok1.PNG'):
                pyautogui.click(160, 950)
            print("スクショ2")
            sleep(1)
            bs.gacha_screencap("2")
            path = "C:\\Users\\kousuke\\Pictures\\uma\\BS\\gacha2.PNG"
            # SSRの数を数える
            ssrCnt += bs.multi_chkImg(path)

            print("戻る")
            bs.screenChk(60, 870, "modoru1")

        print("SSR: "+ str(ssrCnt) + "枚")
        # 結果をラインに送信
        bs.line_message(ssrCnt, 'C:\\Users\\kousuke\\Pictures\\uma\\BS\\gacha1.PNG')

        if ssrCnt >= 6:
            sys.exit()

        print("メニュー")
        bs.continuous_tap(500, 90, "menu")
        sleep(1)

        print("タイトルへ")
        pyautogui.moveTo(270,630)
        pyautogui.dragTo(270, 350, 0.5)
        bs.screenChk(145, 855, "title")

        print("ハンバーガー")
        bs.screenChk(515, 990, "han")

        print("ユーザデータ削除1")
        bs.screenChk(200, 830, "user_deleat")

        print("ユーザデータ削除2")
        bs.screenChk(400, 680, "user_deleat1")

        print("ユーザデータ削除3")
        bs.screenChk(400, 680, "user_deleat2")

        print("ユーザデータ削除4")
        bs.screenChk(275, 680, "user_deleat3")

        self.auto()

    def setName(self, name):
        bs.setName(name)
 

