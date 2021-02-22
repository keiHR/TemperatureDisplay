#coding: utf-8
import RPi.GPIO as GPIO
import dht11
import time
from LCDscreen import LCD
import serial
import re



# ---------------------------------------
# GPIOの初期化
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.cleanup()
# ---------------------------------------

# ---------------------------------------
# DHT11で使用する変数
dht_pin = 8
dht = dht11.DHT11(pin = 8)
# ---------------------------------------

# ---------------------------------------
# DHT11で温湿度を取得する関数
def read_DHT11():
    read = dht.read()
    temp = read.temperature
    humi = read.humidity
    result = [temp, humi]
    return result
# ---------------------------------------

# -------------------------------------------------------------------
# bme280（外気温湿度）に使用する変数
baudrate_O = 115200 # ボーレート
timeout_O = 0 # タイムアウトの時間
port_O = "COM6" # ポート番号
sleeptime_O = 0.1 # データ取得間隔
# -------------------------------------------------------------------

# -------------------------------------------------------------------
# bme280（外気温湿度）を取得する変数
def read_bme280():
    flag = True # データを取得できるまで繰り返す
    while flag:
        bme280 = serial.Serial("/dev/ttyUSB0", baudrate_O) # bme280に接続
        data = bme280.readline() # 1行取得
        m = re.search(br"tm=(\-?\d+):hu=(\-?\d+)", data)
        if (m):
            temp = round(int(m.group(1))/100, 1) # 取得データは×100されているため100で割る＆小数点第二位で四捨五入
            humi = round(int(m.group(2))/100, 1) # 取得データは×100されているため100で割る＆小数点第二位で四捨五入
            flag = False # データを取得できたので終了
            result = [temp, humi]
            bme280.close()
    return result
# -------------------------------------------------------------------


if __name__ == '__main__':
    lcd = LCD() # LCDをインスタンス化
    cnt = 0
    try:
        while True:
            i_result = read_DHT11() # 室内温度＆湿度測定
            type = "inner" # 室内の識別子
            lcd.main(i_result, type) # 室内温度＆湿度の表示
            time.sleep(30) # 30秒の待機
            o_result = read_bme280() # 室外温度＆湿度測定
            type = "uoter" # 室外の識別子
            lcd.main(o_result, type) # 室外温度＆湿度測定の表示
            time.sleep(30) # 30秒の待機
    except KeyboardInterrupt:
        lcd.finish()
        pass
            
print("FINISH")
lcd.finish()