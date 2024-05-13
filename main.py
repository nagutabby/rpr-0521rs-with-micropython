from machine import Pin, I2C
import time

# I2Cのピン設定
bus = I2C(0, scl=Pin(33), sda=Pin(32), freq=400000)

# RPR0521RSのI2Cアドレス
RPR_ADDR = 0x38

# 初期化
def rpr_SYSTEM_CONTROL():
    bus.writeto(RPR_ADDR, bytes([0x40, 0x80]))
    
def rpr_MODE_CONTROL():
    bus.writeto(RPR_ADDR, bytes([0x41, 0x8a]))

def rpr_ALS_CONTROL(): #Gainの調整　
    bus.writeto(RPR_ADDR, bytes([0x42, 0x02]))

# 光センサーからデータを読み取る
def READ_ALS_DATA():
    # レジスタからデータを読み取り
    bus.writeto(RPR_ADDR, bytes([0x46, 0x01]))
    data = bus.readfrom(RPR_ADDR, 2)
    als_value = (data[1] << 8) | data[0]
    return als_value

def main():
    rpr_SYSTEM_CONTROL()
    rpr_MODE_CONTROL()
    rpr_ALS_CONTROL()
    count = 0
    while count < 15:
        # 光センサーからデータを読み取る
        time.sleep(1) 
        als_value = READ_ALS_DATA()
        print("ALS Reading: {} lux".format(als_value))
        time.sleep(1)
        count += 1

if __name__ == "__main__":
    main()

