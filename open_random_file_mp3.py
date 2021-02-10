
import os
import time
import random
from mutagen.mp3 import MP3


def open_file(file_path, player_exe_name):
    '''
    This module opens a random mp3 file from a directory then closes the player after it's playtime.
    '''

    file_list = os.listdir(file_path)
    choice = random.choice(file_list)
    random_file_path = os.path.join(file_path, choice)
    mp3_obj = MP3(random_file_path)
    playtime = round(mp3_obj.info.length, 1)
    os.startfile(random_file_path)
    time.sleep(playtime)
    os.system("Taskkill /IM " + player_exe_name + " /F")