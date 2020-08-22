#Import statements
import serial
import os
import time
import sys
from serial_reader import serial_reader
from open_random_file_mp3 import open_file


#Opening the serial port COM3 at 9600 baud
COM3 = serial.Serial(port="COM3", baudrate=9600, timeout=1)


while True:
    distance_value = serial_reader(COM3)
    if (distance_value > 10):
        open_file("D:\\Code\\Special_Projects\\Moaner\\music_files\\", "vlc.exe")
        time.sleep(2)
        COM3.reset_input_buffer()
        while True:
            distance_value = serial_reader(COM3)
            if (distance_value > 10):
                COM3.reset_input_buffer()
                continue
            else:
                break

    else:
        continue
    