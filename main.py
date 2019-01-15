import datetime

def print_header():
    print('--------------------------------------------------')
    print(' CONGRATULATIONS ON ANOTHER YEAR OF LIFE HUMAN')
    print('--------------------------------------------------')

def get_user_birthday():
    print("When were you born? ")
    year = int(input("Year [YYYY]: "))
    month = int(input("Month [MM]: "))
    day = int(input("Day [DD]: "))

    # We're trying to compare days, not moments in time, but we can do that too :)
    birthday = datetime.date(year, month, day)
    return birthday

def compute_days_between_dates(original_date, target_date):
    this_year = datetime.date(target_date.year, original_date.month, original_date.day)
    days_between = this_year - target_date
    return days_between.days

def print_bday_info(days):
    if days < 0:
        print(f"You had your birthday {days} days ago this year")
    elif days > 0:
        print(f"Your birthday is in {days} days!")
    else:
        print("Today is your birthday!")

def main():
    print_header()
    bday = get_user_birthday()
    today = datetime.date.today()
    num_days = compute_days_between_dates(bday, today)
    print_bday_info(num_days)

main()


