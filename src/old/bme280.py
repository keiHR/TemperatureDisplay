text = '::rc=80000000:lq=141:ct=0001:ed=810BDC17:id=0:ba=3210:a1=1468:a2=0993:tm=1705:hu=5010:at=1012'
import serial
import re

# -------------------------------------------------------------------
# bme280（外気温湿度）に使用する変数
baudrate_O = 115200 # ボーレート
timeout_O = 0 # タイムアウトの時間
port_O = "COM6" # ポート番号
sleeptime_O = 0.1 # データ取得間隔
# -------------------------------------------------------------------

"""
# -------------------------------------------------------------------
# bme280（外気温湿度）を取得する変数
bme280 = serial.Serial(port_O, baudrate_O)

while True:
    data = bme280.readline() # 1行取得
    # row = str(data).split(":")
    m = re.search(br"tm=(\-?\d+):hu=(\-?\d+)", data)
    if (m):
        tm = round(int(m.group(1))/100, 1) # 取得データは×100されているため100で割る＆小数点第二位で四捨五入
        hu = round(int(m.group(2))/100, 1) # 取得データは×100されているため100で割る＆小数点第二位で四捨五入

bme280.close()
# -------------------------------------------------------------------
"""

m = re.search("tm=(\-?\d+):hu=(\-?\d+)", text)
if (m):
    tm = round(int(m.group(1))/100,1)
    hu = round(int(m.group(2))/100,1)
    print(tm)
    print(hu)
