from tkinter import *
import datetime
root = Tk()
root.title('Daily average spend')
#Get variables from files

with open('spend.txt') as f:
    spend = int(f.read().strip())
with open('spend-new.txt') as f:
    last = int(f.read().strip())


# Get the current date
today = datetime.datetime.now()

# Get the number of days since the start of the year
day_of_year = (today - datetime.datetime(today.year, 1, 1)).days + 1

#the day limit i set is starting from 260. day of 2022.
#so i will add  105 to day_of_year.

day = float(day_of_year + 105)



myLabel1 = Label(root, text="Your total spend %d " %spend)
myLabel1.grid(row=0, column=0)
myLabel2 = Label(root, text="Your last spend %d " %last)
myLabel2.grid(row=1, column=0)

e = Entry(root, width=50, borderwidth=5)
e.grid(row=2, column=0)
e.insert(0, "Enter todays spend")

def myClick():
    global e_get
    global hello
    e_get = int(e.get())
    hello=  spend + int(e.get())
    myLabel = Label(root,text="Your new total spend: %d" %hello)
    myLabel.grid(row=5, column=0)
    avg= hello/day
    myLabel3 = Label(root,text="%d days have passed since the start." %day)
    myLabel2 = Label(root,text="Your daily average spend is %.2f lira. " %avg)
    myLabel2.grid(row=6, column=0)
    myLabel3.grid(row=7, column=0)
    
    "%d days have passed since the start." %day
    
    

#creating label
myButton = Button(root, text="Click", command=myClick)
#shoving label on to screen
myButton.grid(row=4, column=0)


    
root.mainloop()

if e_get != None:
    with open('spend-new.txt', 'w') as fi:
        fi.write(str(e_get))
        
with open('spend.txt', 'w') as f:
    f.write(str(hello))