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
#open file
try:
    fid = open('WeatherDataWindows.csv','r')
except FileNotFoundError:
    print('no file')
#initialize variables
num = 0
total_prec = 0
jan_max = 0
jan_min = 100
max_num = 0
min_num = 100
press_inc = 0
press_dec = 0
humid = 0
prev_press = 0
# open csv file
with open('WeatherDataWindows.csv', newline='') as myFile:  
    reader = csv.reader(myFile)
    for row in reader: # loop for each row in the file
        if row[1] == 'Temp High': # skip the header
            continue
        elif float(row[1]) > max_num: #finding the max temp
            max_num = float(row[1])
        elif float(row[3]) < min_num: #finding the min temp
            min_num = float(row[3])
        elif row[0] == '1/8/2015' or row[0] == '1/8/2016' or row[0] == '1/8/2017': 
            if float(row[1]) > jan_max: # max temp for jan 8
                jan_max = float(row[1])
            if float(row[3]) < jan_min: # min temp for jan 8
                jan_min = float(row[3])
        if (float(row[10]) - prev_press) > 0: # calculate press diff
            press_inc += 1 #increse in press
        if (float(row[10]) - prev_press) < 0:
            press_dec += 1 #decrease in press
        if float(row[7]) > 95: # calulate number of times humidity above 95
            humid += 1
        #variables that iterate in for loop
        total_prec += float(row[-1])
        num += 1
        prev_press = float(row[10])
        percent = (humid / num) * 100
#variable that iterates outside for loop
avg_prec = total_prec / num
#print statements       
print('The hottest temperature:', max_num)
print('The coolest temperature:', min_num)
print('The average daily precepitation:', avg_prec)
print('The hottest temp on Janurary 8:', jan_max)
print('The cooleset temp on Janurary 8:', jan_min)
print('pressure increased',press_inc, 'times')
print('pressure decreased',press_dec,'times')
print('The percent of days when humidity is above 95%:', str(percent) + '%') 

        
