from os import P_OVERLAY
import bs_module as bsModule  
from time import sleep
import pyautogui

def main():
    bs = bsModule.bs_module()
    ssrCnt = 0

    print("タイトル")
    bs.screenChk(275, 820, "logo")
    sleep(1)

    print("利用規約")
    bs.screenChk(405, 960, "riyo")
    sleep(1)

    print("ポリ")
    bs.screenChk(405, 960, "policy")
    sleep(1)

    print("google")
    bs.screenChk(100, 690, "google")
    sleep(1.5)

    print("アカウント連携")
    bs.screenChk(150, 690, "renkei")
    sleep(1)

    print("チュートリアル")
    bs.screenChk(390, 680, "tuto")
    sleep(1)

    print("トレーナー登録")
    bs.screenChk(295, 485, "traner")    
    sleep(1)
    pyautogui.write('aaa', interval=0.25)
    sleep(2)
    pyautogui.click(287, 685)
    sleep(1)

    print("登録")
    bs.screenChk(275, 680, "toroku")
    sleep(1)

    print("OK")
    bs.screenChk(400, 680, "OK")
    sleep(1)

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
    bs.screenChk(405, 955, "present1")

    print("閉じる")
    bs.screenChk(275, 955, "tojiru")

    print("閉じる")
    bs.screenChk(150, 955, "present1")

    # while True:
    #     print("スクショ")
    #     bs.screencap()

    #     if bs.chkImg("C:\\Users\\kousuke\\Pictures\\uma\\BS\\skip.PNG"):
    #         print("スキップ")
    #         bs.
    #         pyautogui.click(510, 980)

    #     elif bs.chkImg("C:\\Users\\kousuke\\Pictures\\uma\\BS\\kekka.PNG"):
    #         print("ガチャ結果")
    #         pyautogui.click(400, 960)
    #         sleep(1)
    #         bs.screencap()
    #         sleep(0.5)
    #         if bs.chkImg("C:\\Users\\kousuke\\Pictures\\uma\\BS\\hiku.PNG"):
    #             pyautogui.click(390, 680)
    #             sleep(1)
    #         else:
    #             pyautogui.click(155, 680)
    #             sleep(1)
    #             pyautogui.click(155, 970)

    #     elif bs.chkImg("C:\\Users\\kousuke\\Pictures\\uma\\BS\\logo.PNG"):
    #         print("タイトル")
    #         pyautogui.click(275, 820)

    #     elif bs.chkImg("C:\\Users\\kousuke\\Pictures\\uma\\BS\\riyo.PNG"):
    #         print("利用規約")
    #         pyautogui.click(405, 960)
    #         sleep(1.5)
    #         # プライバシー
    #         pyautogui.click(405, 960)

    #     elif bs.chkImg("C:\\Users\\kousuke\\Pictures\\uma\\BS\\sinin.PNG"):
    #         print("サインイン")
    #         pyautogui.click(100, 690)
    #         sleep(1)
    #         # 連携
    #         pyautogui.click(100, 690)
    #         sleep(1)
    #         # チュートリアル
    #         pyautogui.click(405, 680)
    #         sleep(1)

    #     elif bs.chkImg("C:\\Users\\kousuke\\Pictures\\uma\\BS\\traner.PNG"):
    #         print("登録")
    #         pyautogui.click(300, 485)
    #         # 名前入力
    #         pyautogui.write('aaa', interval=0.25)
    #         sleep(0.5)
    #         pyautogui.click(275, 680)
    #         sleep(1)
    #         # 登録
    #         pyautogui.click(275, 680)
        
    #     elif bs.chkImg("C:\\Users\\kousuke\\Pictures\\uma\\BS\\renkei.PNG"):
    #         print("アカウント連携")
    #         pyautogui.click(265, 640)

    #     elif bs.chkImg("C:\\Users\\kousuke\\Pictures\\uma\\BS\\message.PNG"):
    #         print("お知らせ")
    #         # 閉じる
    #         pyautogui.click(275, 955)
        
    #     elif bs.chkImg("C:\\Users\\kousuke\\Pictures\\uma\\BS\\main.PNG"):
    #         print("メインストーリー")
    #         pyautogui.click(280, 680)
    #         sleep(1)
    #         # ストーリー解放
    #         pyautogui.click(280, 955)
    #         sleep(2)
    #         # プレゼント
    #         pyautogui.click(505, 740)

    #     elif bs.chkImg("C:\\Users\\kousuke\\Pictures\\uma\\BS\\present1.PNG"):
    #         # 一括受け取り
    #         pyautogui.click(410, 960)
    #         sleep(1)
    #         # 閉じる
    #         pyautogui.click(280, 960)
    #         sleep(1)
    #         # 閉じる
    #         pyautogui.click(160, 950)
    #         sleep(3)
    #         # ガチャ
    #         pyautogui.click(500, 990)
    #         sleep(1.5)
    #         # 右へ移動
    #         pyautogui.click(500, 640)
    #         sleep(1.5)

    #     elif bs.chkImg("C:\\Users\\kousuke\\Pictures\\uma\\BS\\10kai.PNG"):
    #         print("1o回引く")
    #         pyautogui.click(460, 825)
    #         sleep(1)
    #         bs.screencap()
    #         sleep(0.5)
    #         if bs.chkImg("C:\\Users\\kousuke\\Pictures\\uma\\BS\\hiku.PNG"):
    #             pyautogui.click(400, 680)
    #             sleep(1)
    #         else:
    #             pyautogui.click(160, 680)
    #             sleep(1)
    #             pyautogui.click(60, 990)
    #             sleep(1)


    #     elif bs.chkImg("C:\\Users\\kousuke\\Pictures\\uma\\BS\\support.PNG"):
    #         print("サポートカード")
    #         pyautogui.click(385, 700)
    #         sleep(1)
    #         # 一覧
    #         pyautogui.click(150, 805)
    #         sleep(1.5)
    #         bs.gacha_screencap("gacha_kekka")
    #         sleep(0.5)
    #         path = "C:\\Users\\kousuke\\Pictures\\uma\\BS\\gacha_kekka.PNG"
    #         ssrCnt += bs.multi_chkImg(path)
    #         # 戻る
    #         pyautogui.click(55, 875)

    #     elif bs.chkImg("C:\\Users\\kousuke\\Pictures\\uma\\BS\\hokan.PNG"):
    #         print("保管室")
    #         pyautogui.click(390, 710)
    #         sleep(2.5)
    #         # 閉じる
    #         pyautogui.click(275, 975)
    #         sleep(1)
    #         # チェック外す
    #         pyautogui.click(180, 815)
    #         sleep(1)
    #         # レアリティ
    #         pyautogui.click(380, 755)
    #         sleep(1)
    #         # 所持数
    #         pyautogui.click(70, 400)
    #         sleep(0.5)
    #         # 絞り込み
    #         pyautogui.click(410, 135)
    #         sleep(0.5)
    #         # SSR
    #         pyautogui.click(410, 250)
    #         sleep(0.5)
    #         # OK
    #         pyautogui.click(405, 960)
    #         sleep(1)
    #         bs.screencap()
    #         sleep(0.5)
    #         # もし表示設定画面のままならキャンセルボタンを押す
    #         if bs.chkImg("C:\\Users\\kousuke\\Pictures\\uma\\BS\\ok.PNG"):
    #             pyautogui.click(160, 950)
    #         sleep(1)
    #         bs.gacha_screencap("hokan_kekka")
    #         path = 'C:\\Users\\kousuke\\Pictures\\uma\\BS\\hokan_kekka.PNG'
    #         # SSRの数を数える
    #         ssrCnt += bs.hokan_matchTemplate(path)


if __name__ == '__main__':
     main()