import time

from mutagen.mp3 import MP3
from pygame import mixer  # Load the popular external library

import com.dugj.hello.rolling_file as rolling_file


def play(file_list):
    if len(file_list) == 1:
        for times in range(10):
            mixer.init()
            mixer.music.load(file_list[0])
            mixer.music.play()
            print('playing ' + file_list[0])
            time.sleep(int(MP3(file_list[0]).info.length) + 5)
    else:
        for times in range(10 // len(file_list)):
            for path in file_list:
                mixer.init()
                mixer.music.load(path)
                mixer.music.play()
                print('playing ' + path)
                time.sleep(int(MP3(path).info.length) + 5)


last_file_path = ''
hours = ['11', '12', '14', '15', '16', '17']
while True:
    hour_str = time.strftime('%H', time.localtime(time.time()))
    if hour_str in hours and time.strftime('%M', time.localtime(time.time())) == '00':
        path_list = rolling_file.get_file_path(last_file_path)
        play(path_list)
        if hour_str == '17':
            last_file_path = path_list[len(path_list) - 1]
            print('last file :' + last_file_path + '\n')
    time.sleep(59)
