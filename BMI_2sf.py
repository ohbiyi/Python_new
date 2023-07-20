#!/usr/bin/python3

import time
 
t = time.localtime(time.time())
localtime = time.asctime(t)
str = "Current Time:" + time.asctime(t)
 
print(str);

height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

height1 = float(height)
weight1 = int(weight)

height2 = height1 **2
BMI = round(weight1 / height2, 2)
print(BMI)

if BMI < 18.5:
 print("you are underweight")
elif BMI < 25:
 print("you are normal weight")
elif BMI < 30:
 print("you are overweight")
elif BMI < 35:
 print("you are obese")
elif BMI > 35:
 print("you are clinically obese")
    