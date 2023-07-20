#!/usr/bin/python3

import time
 
t = time.localtime(time.time())
localtime = time.asctime(t)
str = "Current Time:" + time.asctime(t)
 
print(str);

print("Welcome to the roller coaster ")
height = int(input("enter your height in cm: "))

if height > 120:
 print("ticket for roller coaster ride")
else:
 print("no ticket allocated")
