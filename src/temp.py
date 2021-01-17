# coding:utf-8
import os
from datetime import datetime
import time
import serial
import sys

"""
参考: pyserial公式ドキュメント
[1]サイトトップ http://pythonhosted.org/pyserial/
[2]API一覧 http://pythonhosted.org/pyserial/pyserial_api.html
[3]イントロダクション http://pythonhosted.org/pyserial/shortintro.html
"""


# -------------------------------------------------------------------
# 現在日時を取得する関数
def getNow():
    now = datetime.now()
    date = "{:%Y-%m-%d %H:%M:%S}".format(now)
    hour = now.hour
    min = now.minute
    return now, date, hour, min
# -------------------------------------------------------------------


# -------------------------------------------------------------------
# 加速度を取得する関数
def readSerial(baudrate, timeout, port, sleeptime): # 引数はボーレート、タイムアウトの時間、ポート番号、データ取得間隔
    ser = serial.Serial()
    ser.baudrate = baudrate  # ボーレート設定
    ser.timeout = timeout  # タイムアウトの時間設定
    ser.port = port  # ポート番号設定

    # ポートの開通確認
    try:
        ser.open()
        print("open " + ser.port)
    except:
        print("can't open" + ser.port)
        sys.exit(0)

    # ちゃんと開けていたらループに入る
    while ser.is_open:
        s = ser.readline()
        if s != "":
            data = s.decode('utf-8')  # sはbyte型なのでdecode関数で文字列に変換
            data = data.rstrip('\r\n')  # 末尾の改行記号を削除
            data_list = data.split(":")
            if len(data_list) == 13:  # 出力データの要素数は空白２こ＋データ１１こ
                data_list.remove('')  # 先頭の空欄を削除
                data_list.remove('')  # 先頭の空欄を削除
                print(data_list[8] + ' ' + data_list[9] + ' ' + data_list[10])

        else:
            print(".")
        time.sleep(sleeptime)  # データ取得間隔設定

# -------------------------------------------------------------------


# -------------------------------------------------------------------
# 使用する変数
baudrate = 115200 # ボーレート
timeout = 0 # タイムアウトの時間
port = "COM5" # ポート番号
sleeptime = 0.1 # データ取得間隔
# -------------------------------------------------------------------


# -------------------------------------------------------------------
# main関数
def main():
    readSerial(baudrate, timeout, port, sleeptime)
# -------------------------------------------------------------------


try:
    now, date, hour, min = getNow()
    print(date)
    main()

except KeyboardInterrupt:
    print("serial connection closed")
