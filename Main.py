import Game_module as gModule
from time import sleep
from subprocess import run, PIPE
import subprocess


def main():

    mod = gModule.Game_module()
    mode = 0
    stackCnt = 0
    ssrCnt = 0
    imageCnt = 1
    waitCnt = 0
    # Nox起動
    # subprocess.Popen('"D:\\Program Files\\Nox\\bin\\Nox.exe" -clone:Nox_4')
    # print ("wait for app...")
    # sleep(50)

    while True:
        # スクリーンショット
        mod.screencap()
        print('スクショ')

        #ローディング中は3秒待機
        if mod.chkImg('D:\\Program Files\\Nox\\bin\\pics\\loding.png', False):
            sleep(3)

        # 早送りボタンは常にタップ
        elif mod.chkImg('D:\\Program Files\\Nox\\bin\\pics\\hayaokuri.png', True):
            sleep(0.5)
            mod.tap(655, 1255)

        # 同意をタップ
        elif mod.chkImg('D:\\Program Files\\Nox\\bin\\pics\\doui.png', True):
            sleep(0.01)

        # Google Playダイアログが出たら、キャンセルの位置をタップ
        elif mod.chkImg('D:\\Program Files\\Nox\\bin\\pics\\google.png', False):
            mod.tap(200, 830)

        # アカウント連携ダイアログが出たら、後でするの位置をタップ
        elif mod.chkImg('D:\\Program Files\\Nox\\bin\\pics\\account.png', False):
            #result = mod.chkImg('D:\\Program Files\\Nox\\bin\\pics\\cansel.png')
            mod.tap(200, 830)

        # チュートリアルダイアログが出たら、スキップの位置をタップ
        elif mod.chkImg('D:\\Program Files\\Nox\\bin\\pics\\tutorial.png', False):
            mod.tap(520, 830)    

        # トレーナー登録ダイアログが出たら、
        elif mod.chkImg('D:\\Program Files\\Nox\\bin\\pics\\touroku.png', False):
            # トレーナー名入力の位置をタップ
            mod.tap(230, 570)
            sleep(1)
            # abc と入力
            mod.inputText('abc')
            sleep(1)
            # 登録ボタンの位置をタップ1
            mod.tap(360, 835)
            sleep(1)
            # 登録ボタンの位置をタップ2
            mod.tap(360, 835)
            sleep(1)
            # OKボタンの位置をタップ
            mod.tap(515, 835)

        if mode == 0:
            # タイトルをタップ
            if mod.chkImg('D:\\Program Files\\Nox\\bin\\pics\\logo.png', False):
                mod.tap(300, 835)

            # お知らせ
            elif mod.chkImg('D:\\Program Files\\Nox\\bin\\pics\\oshirase.png', False):
                mod.tap(360, 1180)
                sleep(1)
                mod.tap(360, 835)
                sleep(1)
                mod.tap(360, 1180)

            # プレゼントを受け取っていない場合
            elif mod.chkImg('D:\\Program Files\\Nox\\bin\\pics\\present1.png', False) and mode == 0:
                # プレゼントボタンタップ
                mod.tap(680, 905)
                sleep(1)
                # 一括受取
                mod.tap(520, 1185)
                sleep(1)
                # 閉じる
                mod.tap(360, 1180)
                sleep(1)
                # 閉じる
                mod.tap(200, 1180)
                mode = 1

        if mode == 1:
            # プレゼントを受け取っている場合
            if mod.chkImg('D:\\Program Files\\Nox\\bin\\pics\\present2.png', False):
                sleep(1)
                mod.tap(640, 1250)
                sleep(2)
                mod.tap(640, 800)

            # 10回引く
            elif mod.chkImg('D:\\Program Files\\Nox\\bin\\pics\\10Kai.png', False):
                mod.tap(580, 1030)        

            # ガチャを引く
            elif mod.chkImg('D:\\Program Files\\Nox\\bin\\pics\\hiku.png', True):
                sleep(0.01)

            # お知らせダイアログが出たら、閉じるの位置をタップ
            elif mod.chkImg('D:\\Program Files\\Nox\\bin\\pics\\close.png', False):
                mod.tap(360, 1180)
                sleep(1)   
                mod.tap(360, 835)
                sleep(1)
                mod.tap(360, 1180)

            # ガチャ結果
            elif mod.chkImg('D:\\Program Files\\Nox\\bin\\pics\\kekka.png', False):
                sleep(0.5)
                # もう一回引く
                mod.tap(515, 1200)
                sleep(1)
                mod.screencap()
                sleep(2)
                if mod.chkImg('D:\\Program Files\\Nox\\bin\\pics\\hiku.png', True):
                    sleep(1)
                else:
                    print('キャンセル')
                    mod.tap(200, 835)
                    sleep(2)
                    print('もどる')
                    mod.tap(205, 1200)
                    mode = 2

            elif mod.chkImg('D:\\Program Files\\Nox\\bin\\pics\\kekka.png', False):
            

        # ガチャ確認
        elif mod.chkImg('D:\\Program Files\\Nox\\bin\\pics\\kyoka.png', False) and mode == 2:
            # 強化編成
            mod.tap(100, 1230)
            sleep(1)
            # サポートカード
            mod.tap(500, 840)
            sleep(1)
            # 一覧
            mod.tap(310, 980)
            sleep(1)
            mod.gacha_screencap(imageCnt)
            sleep(3)
            path = 'D:\\Program Files\\Nox\\bin\\pics\\gacha_kekka' + str(imageCnt) + '.png'
            print(path)
            # SSRの数を数える
            ssrCnt += mod.multi_matchTemplate(path)
            imageCnt += 1
            # 戻る
            mod.tap(80, 1080)
            mode = 3
            
        # 保管室
        elif mod.chkImg('D:\\Program Files\\Nox\\bin\\pics\\hokan.png', True) and mode == 3:
            sleep(1)
            # 閉じるボタン
            mod.tap(360, 1205)
            sleep(1)
            # チェックする
            mod.tap(220, 1000)
            sleep(2)
            # レアリティ
            mod.tap(500, 920)
            sleep(2)
            # 所持数
            mod.tap(135, 475)
            sleep(1)
            # 絞り込み
            mod.tap(530, 135)
            # SSRチェック
            sleep(2)
            mod.tap(525, 275)
            # OK
            mod.tap(515, 1180)
            sleep(1)
            mod.screencap()
            sleep(2)
            if mod.chkImg('D:\\Program Files\\Nox\\bin\\pics\\cansel.png', True):
                # mod.tap(,)
                sleep(1)
            mod.gacha_screencap(imageCnt)
            sleep(2)
            path = 'D:\\Program Files\\Nox\\bin\\pics\\gacha_kekka' + str(imageCnt) + '.png'
            # SSRの数を数える
            ssrCnt += mod.multi_matchTemplate(path)
            imageCnt += 1
            # 結果をラインに送信
            mod.line_message(ssrCnt, 'D:\\Program Files\\Nox\\bin\\pics\\gacha_kekka1.png')
            # SSRが五枚以上なら終了
            print('計' + str(ssrCnt) + '枚')
            if ssrCnt >= 6:
                ssrCnt = 0
                break
            ssrCnt = 0
            # 戻る
            mod.tap(80, 1080)
            sleep(1)
            # メニュー
            mod.tap(660, 75)
            mode = 4

        if mode == 4:
            # タイトルに戻る
            if mod.chkImg('D:\\Program Files\\Nox\\bin\\pics\\menu2.png', False):
                # スワイプ
                mod.swipe(100, 1000, 850, 700, 1)
                # sleep(3)
                # mod.screencap()
                # sleep(3)
                # mod.chkImg('D:\\Program Files\\Nox\\bin\\pics\\title.png', False)
                # タイトル
                sleep(2)
                mod.tap(205, 1060)

            # アカウント削除
            elif mod.chkImg('D:\\Program Files\\Nox\\bin\\pics\\hanba-ga-.png', True):
                sleep(2)
                # ユーザデータ削除
                mod.tap(155, 990)
                sleep(1)
                # 削除しますか？
                mod.tap(520, 835)
                sleep(1)
                # 本当に削除しますか？
                mod.tap(520, 835)
                sleep(1)
                mod.tap(360, 835)
                mode = 0

        # 強制終了した場合
        elif mod.chkImg('D:\\Program Files\\Nox\\bin\\pics\\home.png', False):
            # アプリ起動
            mod.start_app('jp.co.cygames.umamusume/jp.co.cygames.umamusume_activity.UmamusumeActivity')
            sleep(10)
            # タイトルをタップ
            if mod.chkImg('D:\\Program Files\\Nox\\bin\\pics\\logo.png', False):
                mod.tap(300, 835)

        # メインストーリー開放ダイアログが出たら、閉じるの位置をタップ
        # elif mod.chkImg('D:\\Program Files\\Nox\\bin\\pics\\umamusume-syosai.png'):
        #     mod.touchPos(270, 630)
        #     mod.sleep(1)     

         # プレゼントが届いている場合
        # elif mod.touchImg('./umamusume/present1.png'):
        #     # タップ出来たら待機
        #     mod.sleep(1)
        #     # 一括受取の位置をタップ
        #     mod.touchPos(405, 890)
        #     mod.sleep(1)
        #     # 閉じるの位置をタップ1
        #     mod.touchPos(270, 890)
        #     mod.sleep(1)
        #     # 閉じるの位置をタップ2
        #     mod.touchPos(135, 890)
        #     mod.sleep(1)

        else:
            print('確認できず')
            waitCnt += 1
            if waitCnt >= 10:
                if mod.chkImg('D:\\Program Files\\Nox\\bin\\pics\\logo.png', True):
                    sleep(0.5)

        # スタックした場合
        if mod.chkImg('D:\\Program Files\\Nox\\bin\\pics\\stack.png', False):
            stackCnt += 1
            if stackCnt >= 3:
                mod.stop_app('jp.co.cygames.umamusume')
                sleep(3)
                mod.start_app('jp.co.cygames.umamusume/jp.co.cygames.umamusume_activity.UmamusumeActivity')
                stackCnt = 0
        else:
            stackCnt = 0 


    # if mod.chkImg('D:\\Program Files\\Nox\\bin\\pics\\syotoka.png'):
    #     print('成功！')
    #     #sleep(3)

    # 見本と比較
    # x, y = Module.chkImg('./img/Home.png')
    # print(x + y)

if __name__ == '__main__':
     main()