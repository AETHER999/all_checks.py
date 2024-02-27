#!/usr/bin/env python3

import time
import pygame

# Define a dictionary of note values and their corresponding duration in seconds
note_values = {
    '1/1': 4.0,
    '1/2': 2.0,
    '1/4': 1.0,
    '1/8': 0.5,
    '1/16': 0.25,
    '1/32': 0.125,
}

# Define a dictionary of different click sounds
click_sounds = {
    'beep': 'click1.wav',
    'woodblock': 'click2.wav',
    'cowbell': 'click3.wav',
}

# Initialize pygame mixer
pygame.mixer.init()

# Define a function to play a click sound with a given duration and frequency
def play_click(duration, frequency):
    pygame.mixer.Sound.play(click_sound)

def metronome(tempo, subdivision, sound):
    # Convertir subdivision a un número entero
    subdivision = int(subdivision)
    # Cálculo de duraciones de nota
    beat_duration = 60 / tempo
    subdivision_duration = beat_duration / subdivision

    # Load the selected click sound
    click_sound = pygame.mixer.Sound(click_sounds[sound])

    # Play the metronome
    while True:
        for i in range(subdivision):
            if i == 0:
                # Play the accented click on the first subdivision
                play_click(beat_duration * 0.7, 1000)
            else:
                # Play the regular click on all other subdivisions
                play_click(subdivision_duration * 0.7, 700)
            time.sleep(subdivision_duration - subdivision_duration * 0.7)

# Define a function to get the tempo, subdivision, and sound from the user
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
        sound = input('Choose a click sound (beep, woodblock, cowbell): ')
        if sound in click_sounds:
            break
        else:
            print('Invalid input. Try again.')

    return tempo, subdivision, sound

def main():
    print("Welcome to the metronome!")
    tempo, subdivision, sound = get_user_input()

    print("\nTempo:", tempo, "BPM")
    print("Subdivision:", subdivision)
    print("Click sound:", sound, "\n")

    metronome(tempo, note_values[subdivision], sound)

if __name__ == '__main__':
    main()
