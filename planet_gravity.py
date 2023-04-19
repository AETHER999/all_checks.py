planet_gravity = {
    'Mercury': 0.38,
    'Venus': 0.91,
    'Earth': 1.0,
    'Mars': 0.38,
    'Jupiter': 2.34,
    'Saturn': 1.06,
    'Uranus': 0.92,
    'Neptune': 1.19
}

while True:
    try:
        weight_on_earth = float(input('Enter your weight on Earth (in pounds): '))
        if weight_on_earth <= 0:
            raise ValueError
        break
    except ValueError:
        print('Invalid input. Please enter a positive number.')

print('\nYour weight on each planet:')
for planet, gravity in planet_gravity.items():
    weight_on_planet = weight_on_earth * gravity
    print(f'{planet}: {weight_on_planet:.2f} pounds')
