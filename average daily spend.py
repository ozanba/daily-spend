import datetime

# Get the current date
today = datetime.datetime.now()

# Get the number of days since the start of the year
day_of_year = (today - datetime.datetime(today.year, 1, 1)).days + 1

#the day limit i set is starting from 260. day of 2022.
#so i will add  105 to day_of_year.

day = float(day_of_year + 105)


#get spend 

with open('spend.txt') as f:
    spend = int(f.read().strip())
print('Your spend until today is: ',spend)

with open('spend-new.txt') as f:
    last = int(f.read().strip())
print('Your last spend: ',last)


# Get the todays spend from user
today_spend = int(input('Enter your spending today: '))

with open('spend-new.txt', 'w') as f:
    
    f.write(str(today_spend))


# Add the two integers
sum = spend + today_spend
avg = sum/day
# Open the file in write mode and write the sum to it
with open('spend.txt', 'w') as f:
    f.write(str(sum))

print("%d days have passed since the start." %day)
print("and your daily average spend is %f lira." %avg)
    