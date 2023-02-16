from datetime import datetime

def n_times_day(bday1, bday2, n=2):
    age_diff=bday2-bday1
    Day=bday2+age_diff/(n-1)


    # TODO_B4

    return Day

def main():
    today=datetime.now()
    print("Lab03 B-1")
    
    # TODO_B1
    print("Today's date and the day of the week:")
    print(today,'\n',today.strftime("%A"))
    # Your output should be like:
    # 2020-08-03 20:19:19.806211
    # Monday

    print("Lab03 B-2")
    s = input('Enter your birthday in mm/dd/yyyy format: ') #'01/15/1997'
    birth_month=int(s[0:2])
    birth_day=int(s[3:5])
    birth_year=int(s[6:])
    
    if(today.month>birth_month):
        next_birthday=datetime.strptime(s[0:6]+str(today.year+1),"%m/%d/%Y")
        #Today=datetime.strptime(today,)
        duration=(next_birthday-today)
        age=today.year-birth_year
    else:
        next_birthday=datetime.strptime(s[0:6]+str(today.year),"%m/%d/%Y")
        duration=(next_birthday-today)
        age=today.year-birth_year-1
    print("Time until your next birthday and your current age are:")
    print(duration,"\n",age)
    
    # TODO_B2

    # Your output should be like:
    # 280 days, 3:40:40.193789
    # 22


    print("Lab03 B-3")
    print("For people born on these dates:")
    bday1 = datetime(day=15, month=1, year=1997)
    bday2 = datetime(day=11, month=10, year=2003)
    print("Double Day is")
    age_diff=bday2-bday1
    double_day=bday2+age_diff
    print(double_day)

    # TODO_B3

    # Your output should be like:
    # 2020-01-01 00:00:00 (this is not the correct answer!)

    print("Lab03 B-4")
    print("Triple Day is ", n_times_day(bday1, bday2, n=3))

if __name__ == '__main__':
    main()