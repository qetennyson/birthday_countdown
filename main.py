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

def compute_days_between_dates():
    pass

def print_bday_info():
    pass

def main():
    print_header()
    bday = get_user_birthday()
    now = None
    num_days = compute_days_between_dates(bday, now)
    print_bday_info(num_days)

main()


