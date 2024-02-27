#!/usr/binenv python3

import time
import winsound

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

# Define a function to play a click sound with a given duration and frequency
def play_click(duration, frequency):
    winsound.Beep(int(frequency), int(duration * 1000))

# Define a function to run the metronome
def metronome(tempo, subdivision, sound):
    # Calculate the duration of one beat in seconds
    beat_duration = 60.0 / tempo

    # Calculate the duration of each subdivision in seconds
    subdivision_duration = beat_duration / float(subdivision)

    # Load the selected click sound
    click_sound = click_sounds[sound]

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

# Define a function to run the metronome based on user input
def main():
    print('Welcome to the metronome!')
    while True:
        tempo, subdivision, sound = get_user_input()
        print(f'\nTempo: {tempo} BPM\nSubdivision: {subdivision}\nClick sound: {sound}\n')
        metronome(tempo, note_values[subdivision], sound)
        print('Metronome stopped.\n')

if __name__ == '__main__':
    main()
