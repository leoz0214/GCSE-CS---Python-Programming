# 6.1e - Time calculator


def validate_time(time):
    try:
        split_time = time.split(":")
        if len(split_time) != 3:
            return False
        days, hours, minutes = split_time
        for time in split_time:
            if not time.isnumeric():
                return False
        if len(days) < 2 or int(days) < 0:
            return False
        if len(hours) != 2 or not (0 <= int(hours) < 24):
            return False
        if len(minutes) != 2 or not (0 <= int(minutes) < 60):
            return False 
    except Exception:
        return False
    return True


def validate_times(*times):
    valid = True
    for time in times:
        if not validate_time(time):
            print(f"{time} is an invalid time... ensure it is definitely in the format DD:HH:MM and makes sense.")
            valid = False
    return valid 
    

def simplify_time(days, hours, minutes):
    total_minutes = days*1440 + hours*60 + minutes
    new_days = str(total_minutes//1440)
    new_hours = str((total_minutes%1440)//60)
    new_minutes = str(total_minutes%60)
    return f"{new_days if len(new_days) >= 2 else '0'+new_days}:{new_hours if len(new_hours) == 2 else '0'+new_hours}:{new_minutes if len(new_minutes) == 2 else '0'+new_minutes}"


def add_times(time_1, time_2):
    if validate_times(time_1, time_2):
        days_1, hours_1, minutes_1 = tuple(map(int, time_1.split(":")))
        days_2, hours_2, minutes_2 = tuple(map(int, time_2.split(":")))
        return simplify_time(days_1+days_2, hours_1+hours_2, minutes_1+minutes_2)


def time_difference(time_1, time_2):
    if validate_times(time_1, time_2):
        days_1, hours_1, minutes_1 = tuple(map(int, time_1.split(":")))
        days_2, hours_2, minutes_2 = tuple(map(int, time_2.split(":")))
        return simplify_time(days_1-days_2, hours_1-hours_2, minutes_1-minutes_2) 

    
def arithmetic_mode():
    while True:
        print("""Time Calculator - Arithmetic Mode
    1 - Add 2 times
    2 - Find the difference between 2 times
    8 - Conversion mode
    9 - Exit""")
        option = input("Enter an option: ").strip()
        if option == "1":
            time_1 = input("Enter time 1 (DD:HH:MM): ")
            time_2 = input("Enter time 2 (DD:HH:MM): ")
            total_time = add_times(time_1, time_2)
            if total_time:
                print(f"Total time: {total_time}")
        elif option == "2":
            time_1 = input("Enter time 1 (DD:HH:MM): ")
            time_2 = input("Enter time 2 (DD:HH:MM): ")
            difference = time_difference(time_1, time_2)
            if difference:
                print(f"Time difference: {difference}")
        elif option == "8":
            return conversion_mode()
        elif option == "9":
            print("Program terminated")
            break
        else:
            print("Invalid option")
        print("\n")


def time_to_days(time):
    if validate_times(time):
        total_days = round(time_to_minutes(time)/1440, 5)
        return total_days


def time_to_hours(time):
    if validate_times(time):
        total_hours = round(time_to_minutes(time)/60, 5)
        return total_hours


def time_to_minutes(time):
    if validate_times(time):
        days, hours, minutes = tuple(map(int, time.split(":")))
        total_minutes = days*1440 + hours*60 + minutes
        return total_minutes 


def minutes_to_time(minutes):
    new_days = str(minutes//1440)
    new_hours = str((minutes%1440)//60)
    new_minutes = str(minutes%60)
    return f"{new_days if len(new_days) >= 2 else '0'+new_days}:{new_hours if len(new_hours) == 2 else '0'+new_hours}:{new_minutes if len(new_minutes) == 2 else '0'+new_minutes}"
    

def conversion_mode():
    while True:
        print("""Time Calculator - Conversion Mode
    1 - Convert Time to Days
    2 - Convert Time to Hours
    3 - Convert Time to Minutes
    4 - Convert Minutes to Time
    5 - Convert Hours to Time
    6 - Convert Days to Time
    8 - Arithmetic Mode
    9 - Exit""")
        option = input("Enter an option: ").strip()
        if option in ("1", "2", "3"):
            time = input("Enter time (DD:HH:MM): ")
        if option == "1":
            days = time_to_days(time)
            print(f"Days: {days}")
        elif option == "2":
            hours = time_to_hours(time)
            print(f"Hours: {hours}")
        elif option == "3":
            minutes = time_to_minutes(time)
            print(f"Minutes: {minutes}")
        elif option == "4":
            minutes = int(input("Enter number of minutes (int): "))
            if minutes < 0:
                print("Minutes must be greater than or equal to 0")
            else:
                time = minutes_to_time(minutes)
                print(time)
        elif option == "5":
            hours = int(input("Enter number of hours (int): "))
            if hours < 0:
                print("Hours must be greater than or equal to 0")
            else:
                time = minutes_to_time(hours*60)
                print(time)
        elif option == "6":
            days = int(input("Enter number of days (int): "))
            if days < 0:
                print("Days must be greater than or equal to 0")
            else:
                time = minutes_to_time(days*1440)
                print(time)
        elif option == "8":
            return arithmetic_mode()
        elif option == "9":
            print("Program terminated")
            break
        else:
            print("Invalid option")
        print("\n")

        
if __name__ == "__main__":
    arithmetic_mode()
    
