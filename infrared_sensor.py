# 赤外線障害物センサー
from machine import Pin  # type: ignore
import time

infrared_sensor = Pin(16, Pin.IN)

while True:
    infrared_sensor_value = infrared_sensor.value()

    # 障害物なし
    if infrared_sensor_value == 1:
        print("Without obstacle")

    # 障害物あり
    else:
        print("Obstacle exists!")

    time.sleep(1)
