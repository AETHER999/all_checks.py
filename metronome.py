#!/usr/bin/env python3

import time
import subprocess

# Define a dictionary of note values and their corresponding duration in seconds
note_values = {
    '1/1': 4.0,
    '1/2': 2.0,
    '1/4': 1.0,
    '1/8': 0.5,
    '1/16': 0.25,
    '1/32': 0.125,
}

def play_click(duration, sound):
    subprocess.run(["cvlc", "--play-and-exit", sound])

def metronome(tempo, subdivision, sound):
    beat_duration = 60 / tempo
    subdivision_duration = beat_duration / subdivision

    while True:
        for i in range(int(subdivision)):
            if i == 0:
                play_click(beat_duration * 0.7, sound)
            else:
                play_click(subdivision_duration * 0.7, sound)
            time.sleep(subdivision_duration - subdivision_duration * 0.7)

def get_user_input():
    while True:
        try:
            tempo = int(input('Enter the tempo (BPM): '))
            if tempo <= 0:
                raise ValueError
            break
        except ValueError:
            print('Invalid input. Try again.')

    while True:
        subdivision = input('Enter the subdivision (1/1, 1/2, 1/4, 1/8, 1/16, 1/32): ')
        if subdivision in note_values:
            break
        else:
            print('Invalid input. Try again.')

    while True:
        sound = input('Enter the path to the click sound file: ')
        try:
            with open(sound, 'rb') as f:
                f.read(1)
            break
        except FileNotFoundError:
            print('File not found. Try again.')

    return tempo, note_values[subdivision], sound

def main():
    print("Welcome to the metronome!")
    tempo, subdivision, sound = get_user_input()

    print("\nTempo:", tempo, "BPM")
    print("Subdivision:", subdivision)
    print("Click sound:", sound, "\n")

    metronome(tempo, subdivision, sound)

if __name__ == '__main__':
    main()
