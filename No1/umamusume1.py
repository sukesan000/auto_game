import Game_module as gModule
from time import sleep
from subprocess import run, PIPE
import subprocess
from multiprocessing import Process


def main():
    mod = gModule.Game_module()
    mode = 0
    stackCnt = 0
    ssrCnt = 0
    imageCnt = 1
    waitCnt = 0
    # NOXウィンドウのID
    noxId = '127.0.0.1:62028'
    mod.setId(noxId)
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
            print('ローディング中')
            sleep(3)

        # 早送りボタンは常にタップ
        elif mod.chkImg('D:\\Program Files\\Nox\\bin\\pics\\skip.png', True):
            print('早送り')
            sleep(0.1)

        # 同意をタップ
        elif mod.chkImg('D:\\Program Files\\Nox\\bin\\pics\\doui.png', True):
            print('同意')
            sleep(1)
            mod.tap(385, 885)
            sleep(2)

        # Google Playダイアログが出たら、キャンセルの位置をタップ
        elif mod.chkImg('D:\\Program Files\\Nox\\bin\\pics\\google.png', False):
            print('グーグル')
            # キャンセル
            mod.tap(150, 625)
            sleep(1)
            # 後でする
            mod.tap(150, 625)
            sleep(1)
            # スキップ
            mod.tap(380, 625)

        # # アカウント連携ダイアログが出たら、後でするの位置をタップ
        # elif mod.chkImg('D:\\Program Files\\Nox\\bin\\pics\\account.png', False):
        #     mod.chkImg('D:\\Program Files\\Nox\\bin\\pics\\atode.png', False)
        #     mod.tap(150, 630)

        # # チュートリアルダイアログが出たら、スキップの位置をタップ
        # elif mod.chkImg('D:\\Program Files\\Nox\\bin\\pics\\tutorial.png', False):
        #     mod.chkImg('D:\\Program Files\\Nox\\bin\\pics\\skipsuru.png', False)
        #     mod.tap(370, 625)    

        # トレーナー登録ダイアログが出たら、
        elif mod.chkImg('D:\\Program Files\\Nox\\bin\\pics\\touroku.png', False):
            print('名前入力')
            # トレーナー名入力の位置をタップ
            mod.tap(470, 435)
            sleep(0.5)
            # abc と入力
            mod.inputText('abc')
            sleep(0.5)
            # 登録ボタンの位置をタップ1
            mod.tap(245, 625)
            sleep(0.5)
            # 登録ボタンの位置をタップ2
            mod.tap(245, 625)
            sleep(0.5)
            # OKボタンの位置をタップ
            mod.tap(390, 625)

        # お知らせ
        elif mod.chkImg('D:\\Program Files\\Nox\\bin\\pics\\oshirase.png', False):
            print('お知らせ')
            mod.tap(270, 885)
            sleep(1)
            mod.tap(270, 625)
            sleep(1)
            mod.tap(270, 885)

        # プレゼントを受け取っていない場合 ※プレゼントの数が変わると編集する必要あり
        elif mod.chkImg('D:\\Program Files\\Nox\\bin\\pics\\present1.png', False):
            print('未受け取り')
            # プレゼントボタンタップ
            mod.tap(510, 665)
            sleep(1)
            # 一括受取
            mod.tap(365, 885)
            sleep(1)
            # 閉じる
            mod.tap(270, 885)
            sleep(1)
            # 閉じる
            mod.tap(150, 885)
        
        # プレゼントを受け取っている場合
        elif mod.chkImg('D:\\Program Files\\Nox\\bin\\pics\\present2.png', False):
            print('受け取った')
            # ガチャボタン
            mod.tap(485, 935)
            sleep(2)
            # サポートガチャに移動
            mod.tap(460, 590)

        # 10回引く
        elif mod.chkImg('D:\\Program Files\\Nox\\bin\\pics\\10Kai.png', False):
            print('10kai')
            mod.tap(430, 755)      
            sleep(1)  
            mod.screencap()
            sleep(1)
            # 購入ボタンが出たら強化編成へ
            if mod.chkImg('D:\\Program Files\\Nox\\bin\\pics\\konyu.png', False):
                mod.tap(150, 625)
                sleep(1)
                mod.tap(55, 920)
                sleep(1)
            else:
                mod.tap(390, 625) 

        # # ガチャを引く
        # elif mod.chkImg('D:\\Program Files\\Nox\\bin\\pics\\hiku.png', True):
        #     mod.tap(390, 625)

        # ガチャ結果
        elif mod.chkImg('D:\\Program Files\\Nox\\bin\\pics\\kekka.png', False):
            print('ガチャ結果')
            # もう一回引く
            mod.tap(385, 900)
            sleep(1)
            mod.screencap()
            sleep(1)
            if mod.chkImg('D:\\Program Files\\Nox\\bin\\pics\\hiku.png', True):
                sleep(1)
            else:
                mod.tap(150, 625)
                sleep(1)
                mod.tap(150, 900)

        # ガチャ確認
        elif mod.chkImg('D:\\Program Files\\Nox\\bin\\pics\\support.png', False):
            print('強化')
            # サポートカード
            mod.tap(370, 620)
            sleep(1)
            # 一覧
            mod.tap(170, 740)
            sleep(2)
            mod.gacha_screencap(imageCnt)
            sleep(1)
            path = 'D:\\Program Files\\Nox\\bin\\pics\\No1\\gacha_kekka1_' + str(imageCnt) + '.png'
            # SSRの数を数える
            ssrCnt += mod.multi_matchTemplate(path)
            imageCnt += 1
            # 戻る
            mod.tap(60, 810)

        # 保管室
        elif mod.chkImg('D:\\Program Files\\Nox\\bin\\pics\\hokan.png', False):
            print('保管室')
            # SSRが一枚以上あるなら保管室に入る
            if ssrCnt >= 1:
                mod.tap(380, 650)
                sleep(1)
                # 閉じるボタン
                mod.tap(270, 905)
                sleep(1)
                # チェックする
                sleep(1)
                mod.tap(175, 750)
                sleep(1.5)
                # レアリティ
                mod.tap(354, 695)
                sleep(1)
                # 所持数
                mod.tap(105, 355)
                sleep(1)
                # 絞り込み
                mod.tap(370, 100)
                # SSRチェック
                sleep(1)
                mod.tap(440, 210)
                # OK
                mod.tap(390, 885)
                sleep(1)
                mod.screencap()
                sleep(1)
                if mod.chkImg('D:\\Program Files\\Nox\\bin\\pics\\cansel.png', True):
                    sleep(1)
                mod.gacha_screencap(imageCnt)
                sleep(1)
                path = 'D:\\Program Files\\Nox\\bin\\pics\\No1\\gacha_kekka1_' + str(imageCnt) + '.png'
                # SSRの数を数える
                ssrCnt += mod.hokan_matchTemplate(path)
                imageCnt += 1
                # 結果をラインに送信
                mod.line_message(ssrCnt, 'D:\\Program Files\\Nox\\bin\\pics\\No1\\gacha_kekka1_1.png')
                # SSRが五枚以上なら終了
                print('計' + str(ssrCnt) + '枚')
                if ssrCnt >= 8:
                    ssrCnt = 0
                    break
                ssrCnt = 0
                # 戻る
                mod.tap(60, 810)
                sleep(1)
            # メニュー
            mod.tap(495, 55)
            sleep(1)

        # タイトルに戻る
        elif mod.chkImg('D:\\Program Files\\Nox\\bin\\pics\\menu2.png', False):
            print('タイトルに戻る')
            # スワイプ
            mod.swipe(200, 800, 850, 500, 1)
            # タイトル
            sleep(0.5)
            mod.tap(180, 795)
            mode = 1

        if mode == 1:
            print('削除')
            # アカウント削除
            if mod.chkImg('D:\\Program Files\\Nox\\bin\\pics\\hanba-ga-.png', True):
                sleep(0.5)
                # ユーザデータ削除
                mod.tap(98, 745)
                sleep(0.5)
                # 削除しますか？
                mod.tap(390, 625)
                sleep(0.5)
                # 本当に削除しますか？
                mod.tap(390, 625)
                sleep(0.5)
                mod.tap(270, 625)
                mode = 0
        
        # タイトルをタップ
        elif mod.chkImg('D:\\Program Files\\Nox\\bin\\pics\\logo.png', False):
            print('タイトル')
            mod.tap(230, 630)   

        # 強制終了した場合
        elif mod.chkImg('D:\\Program Files\\Nox\\bin\\pics\\home.png', False):
            # アプリ起動
            mod.start_app('jp.co.cygames.umamusume/jp.co.cygames.umamusume_activity.UmamusumeActivity')
            sleep(10)
            # タイトルをタップ
            if mod.chkImg('D:\\Program Files\\Nox\\bin\\pics\\logo.png', False):
                mod.tap(300, 835)

        # # メインストーリー開放ダイアログが出たら、閉じるの位置をタップ
        # # elif mod.chkImg('D:\\Program Files\\Nox\\bin\\pics\\umamusume-syosai.png'):
        # #     mod.touchPos(270, 630)
        # #     mod.sleep(1)     

        #  # プレゼントが届いている場合
        # # elif mod.touchImg('./umamusume/present1.png'):
        # #     # タップ出来たら待機
        # #     mod.sleep(1)
        # #     # 一括受取の位置をタップ
        # #     mod.touchPos(405, 890)
        # #     mod.sleep(1)
        # #     # 閉じるの位置をタップ1
        # #     mod.touchPos(270, 890)
        # #     mod.sleep(1)
        # #     # 閉じるの位置をタップ2
        # #     mod.touchPos(135, 890)
        # #     mod.sleep(1)

        else:
            print('確認できず')
            waitCnt += 1
            if waitCnt >= 10:
                if mod.chkImg('D:\\Program Files\\Nox\\bin\\pics\\close.png', True):
                    sleep(0.5)
                    waitCnt = 0

                elif mod.chkImg('D:\\Program Files\\Nox\\bin\\pics\\logo.png', True):
                    sleep(0.5)
                    waitCnt = 0

        # スタックした場合
        if mod.chkImg('D:\\Program Files\\Nox\\bin\\pics\\stack.png', False):
            stackCnt += 1
            if stackCnt >= 5:
                mod.stop_app('jp.co.cygames.umamusume')
                sleep(3)
                mod.start_app('jp.co.cygames.umamusume/jp.co.cygames.umamusume_activity.UmamusumeActivity')
                stackCnt = 0



    # if mod.chkImg('D:\\Program Files\\Nox\\bin\\pics\\syotoka.png'):
    #     print('成功！')
    #     #sleep(3)

    # 見本と比較
    # x, y = Module.chkImg('./img/Home.png')
    # print(x + y)

if __name__ == '__main__':
     main()