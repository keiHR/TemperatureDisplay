#!/usr/bin/python 
# coding:utf-8 
import time
import RPi.GPIO as GPIO
import os

pin=31
GPIO.setmode(GPIO.BOARD)

#GPIO31pinを入力モードとし、pull upに設定
GPIO.setup(pin, GPIO.IN, pull_up_down = GPIO.PUD_UP)

# 長押し検知用フラッグ　長押し検知でFalseになる
flag = True

while flag:
    #GPIO31ピンの立ち下がりエッジ検出
    GPIO.wait_for_edge(pin, GPIO.FALLING)
    sw_counter = 0
    
    while True:
        sw_status = GPIO.input(pin) # スイッチ押下で0になる
        if sw_status == 0:
            sw_counter += 1
            if sw_counter >= 100:
                # print('長押しを検知')
                flag = False
                break
        else:
            # print('短押しを検知')
            break
        
        time.sleep(0.01)
    
    # print(sw_counter)

GPIO.cleanup()
os.system("sudo shutdown -h now")
# print('終了します')
