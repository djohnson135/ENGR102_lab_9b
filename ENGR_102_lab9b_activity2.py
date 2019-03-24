"""
Name : Dathan Johnson
Section : 409
Assignment : lab 9b - 2
Date : 3-23-19
By submitting this assignment, I agree to the following:
“Aggies do not lie, cheat, or steal, or tolerate those who do”
“I have not given or received any unauthorized aid on this assignment”
"""

#open celsius file
try:
    fid = open('Celsius.txt','r')
except FileNotFoundError:
    print('no file')
#create a new file for fahrenheit
farenfile = 'Fahrenheit.txt'
faren = open(farenfile, 'w') #open the file on W

#initialize list
data = []
#make a list for celsius
x = fid.readlines()
#loop to append values to list
for i in x:
    val = int(i)
    data.append(val)
#loop to convert values to fahrenheit
for i in data:
    fahrenheit = (i * (9/5)) + 32
    faren.write(str(fahrenheit) + '\n' )


#close files
fid.close()
faren.close()
