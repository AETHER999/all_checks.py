# Calendar of 2023 with scheduling feature

import calendar

# Create a calendar object
cal = calendar.Calendar()

# Get all the days in 2023
days_in_year = cal.yeardatescalendar(2023)

# Create a dictionary to store special days
special_days = {}

# Function to add a special day to the calendar
def add_special_day():
    date = input("Enter the date (in MM/DD/YYYY format): ")
    event = input("Enter the event: ")
    special_days[date] = event

# Function to view special days on a given date
def view_special_days():
    date = input("Enter the date (in MM/DD/YYYY format): ")
    if date in special_days:
        print(f"Special days on {date}: {special_days[date]}")
    else:
        print("No special days on this date")

# Function to display the calendar
def display_calendar():
    print("\nCALENDAR OF 2023\n")
    for month in days_in_year:
        for week in month:
            for day in week:
                if day.month == 1:
                    print(calendar.month_name[1])
                    print(calendar.weekheader(3))
                if day.month == 1 and day.day == 1:
                    print("\n")
                if day.month == 1 and day.day == 1 and day.weekday() != 0:
                    print(" " * (day.weekday() * 3), end="")
                if day.month == 12 and day.day == 31 and day.weekday() != 6:
                    print(day.day, end="")
                    print(" " * ((6 - day.weekday()) * 3), end="")
                    print("\n")
                else:
                    print(day.day, end="")
                    print(" " * 2, end="")
            print("\n")

# Main function to run the calendar
def main():
    while True:
        print("\n1. View Calendar\n2. Add Special Day\n3. View Special Days\n4. Quit\n")
        choice = input("Enter your choice: ")
        if choice == '1':
            display_calendar()
        elif choice == '2':
            add_special_day()
        elif choice == '3':
            view_special_days()
        elif choice == '4':
            break
        else:
            print("Invalid input. Try again.")

if __name__ == '__main__':
    main()
