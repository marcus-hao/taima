#!/usr/bin/env python3
import argparse
import time
import winsound

parser = argparse.ArgumentParser()
parser.add_argument('-t', '--time', default=25, 
                    help='Duration in minutes', type=float)
parser.add_argument('-n', '--task-name', default='*\\0/*',
                    help='Task description', type=str)
parser.add_argument('-fa', '--audio-file', default='impomu.wav',
                    help='Audio file(.wav) for \ notification sound', type=str)
args = parser.parse_args()

time_elapsed = int(args.time * 60)
print(args.task_name)
while time_elapsed:
    minutes, seconds = divmod(time_elapsed, 60)
    print(f'\r{minutes:02d}:{seconds:02d}', end='', flush=True)
    time.sleep(1)
    time_elapsed -= 1
print('\rTime\'s up!')
winsound.PlaySound(args.audio_file, winsound.SND_FILENAME)