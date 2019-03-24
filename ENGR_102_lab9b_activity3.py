"""
Name : Dathan Johnson
Section : 409
Assignment : lab 9b - 3
Date : 3-23-19
By submitting this assignment, I agree to the following:
“Aggies do not lie, cheat, or steal, or tolerate those who do”
“I have not given or received any unauthorized aid on this assignment”
"""
import csv
# inputs for values
loan = float(input('amount of loan: '))
intrate = float(input('annual interst rate: '))
monthdue = float(input('amount payed monthly: '))
name = input('name of file: ')
#name of file is name with the added by .csv
filename = name + '.csv'
fid = open(filename,'w')
#writer function for the .csv
writer = csv.writer(fid)
#create list to add to file
header = ['month', 'total interest', 'remaining loan amount']
writer.writerow(header)
#the initial values
start = ['0','0', str(loan)]
writer.writerow(start)
#initialize variables
total_int = 0
month = 0
#loop till loan is depleted
while loan > 0:
    if month == 30: #if the month is 30 break out of loop to avoid an infinite loop
        break
    else:
        loan -= monthdue #calculate loan
        preloan = loan
        loan += preloan * (intrate/100) * 1/12
        month += 1
        my_list = [str(month), str(total_int), str(loan)] #list of values
        writer.writerow(my_list)
        if (loan - preloan) < 0:
            break
        else:
            interest = loan - preloan
            total_int += interest #add the total interest
#close file
fid.close()
