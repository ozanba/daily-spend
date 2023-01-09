from tkinter import *
import datetime
from tkinter import messagebox
root = Tk()
root.title('Daily average spend')
#Get variables from files

with open('/Users/ozan/Desktop/daily_spend/spend.txt') as f:
    spend = int(f.read().strip())
with open('/Users/ozan/Desktop/daily_spend/spend-new.txt') as f:
    last = int(f.read().strip())


# Get the current date
today = datetime.datetime.now()

# Get the number of days since the start of the year
day_of_year = (today - datetime.datetime(today.year, 1, 1)).days + 1

#top
total_spend = Label(root, text="Your total spend %d " %spend)
total_spend.grid(row=0, column=0,columnspan=3)
last_spend = Label(root, text="Your last spend %d " %last)
last_spend.grid(row=1, column=0,columnspan=3)
#entry
e = Entry(root, width=50, borderwidth=5)
e.grid(row=2, column=0, columnspan=3)
e.insert(0, "Enter  spend")

def myClick():
    global e_get
    global spend_total_new
    global total_spend
    global last_spend
    global e
    global clickButton
    
    with open('/Users/ozan/Desktop/daily_spend/spend.txt') as f:
        spend = int(f.read().strip())
    
    day = getDate()
    day = int(day)
    
    
    #entry
 
    if e.get()=='Enter  spend' or e.get()==None:
        messagebox.showwarning("ERROR","Enter a value")
    elif int(e.get())<=0 :
        messagebox.showwarning("ERROR","Value must be positive")
    else:
        e_get = int(e.get())  
        #bottom part
        
        spend_total_new=  spend + e_get
        
        new_total_spend = Label(root,text="Your new total spend: %d" %spend_total_new)
        new_total_spend.grid(row=5, column=0,columnspan=3)
        
        last_spend.grid_forget()
        last_spend = Label(root, text="Your last spend %d " %int(e.get()))
        last_spend.grid(row=1, column=0,columnspan=3)
        
        avg= spend_total_new/day
        day_passed = Label(root,text="%d days have passed since the start." %day)
        daily_average = Label(root,text="Your daily average spend is %.2f lira. " %avg)
        
        total_spend.grid_forget()
        total_spend= Label(root, text="Your total spend %d " %spend_total_new)
        total_spend.grid(row=0, column=0,columnspan=3)
        
        daily_average.grid(row=6, column=0,columnspan=3)
        day_passed.grid(row=7, column=0,columnspan=3)
        myClick.counter +=1
        clickButton.grid_forget()
        clickButton = Button(root, text="Click for %d. spend"% myClick.counter ,command=myClick)
    
        clickButton.grid(row=4, column=0, columnspan=3)
        
        spend_count =+ 1
        with open('/Users/ozan/Desktop/daily_spend/spend.txt', 'w') as f:
            f.write(str(spend_total_new))
        with open('/Users/ozan/Desktop/daily_spend/spend-new.txt', 'w') as fi:
            fi.write(str(e_get))
        
        e.delete(0, 'end')
            
myClick.counter = 1

def date_chance():
    global day_clicked
    global month_clicked
    global year_clicked
    day_list= list(range(1,32))
    
    #day
    global day_option
    global day_text
    day_clicked =  IntVar()
    day_clicked.set(25)
    day_text = Label(text="Day")
    day_text.grid(row=9, column=0)
    day_option = OptionMenu(root, day_clicked,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31)
    day_option.grid(row=10, column=0)
    
    #month
    global month_option
    global month_text
    month_clicked =  IntVar()
    month_clicked.set(9)
    month_text = Label(text="Month")
    month_text.grid(row=9, column=1)
    month_option = OptionMenu(root, month_clicked,1,2,3,4,5,6,7,8,9,10,11,12)
    month_option.grid(row=10, column=1)
    
    #year
    global year_option
    global year_text
    year_clicked =  IntVar()
    year_clicked.set(2022)
    year_text = Label(text="year")
    year_text.grid(row=9, column=2)
    year_option = OptionMenu(root, year_clicked,2020,2021,2022,2023)
    year_option.grid(row=10, column=2)
    
    
    clickButton.grid_forget()
    global date_button
    date_button = Button(root, text="change", command=call_back)
    date_button.grid(row=11, column=0)
    
 
def getDate():
    
    if date_b_callback== 1:
        
        date = datetime.datetime(year_clicked.get(), month_clicked.get(), day_clicked.get())
        dayF = int(days_since(date))
    else:
        dayF = int(day_of_year + 105)
        
        
    return dayF  

date_b_callback = 0
def call_back():
    global date_b_callback 
    
    date_b_callback = 1
    clickButton = Button(root, text="Click", command=myClick)
    
    clickButton.grid(row=4, column=0, columnspan=3)
    #delete date chance items
    year_option.grid_forget()
    month_option.grid_forget()
    day_option.grid_forget()
    day_text.grid_forget()
    month_text.grid_forget()
    year_text.grid_forget()
    date_button.grid_forget()
    
    date = Label(root, text='New starting: %d/%d/%d'% (day_clicked.get(),month_clicked.get(),year_clicked.get()))
    date.grid(row=11, column=2)
    

def days_since(date):
    # Calculate the difference between the given date and the current date
    diff = datetime.datetime.now() - date

    # Return the number of days as an integer
    return diff.days       

# buttons
clickButton = Button(root, text="Click", command=myClick)
clickButton.grid(row=4, column=0, columnspan=3)
button_quit = Button(root, text="Exit", command=root.quit)
button_quit.grid(row= 8,column=0)

button_date = Button(root, text="Chance strating date", command=date_chance)
button_date.grid(row= 8,column=2)

 
def days_since(date):
    # Calculate the difference between the given date and the current date
    diff = datetime.datetime.now() - date

    # Return the number of days as an integer
    return diff.days

root.mainloop()
