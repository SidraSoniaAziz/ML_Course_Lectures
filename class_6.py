#Date: Oct 14,2022
#recap
# def fun1():
#     dict = {
#         'car':['car1','car2','car3']
#     }
#     print(dict)
# fun1()
#para,eterized functions
# def add(a,b,c):
#     addition = a+b+c
#     return addition
# a = int(input("Enter a : "))
# b = int(input("Enter b : "))
# c = int(input("Enter c : "))
# addition = add(a,b,c)
# print("addition: ",addition)
#condition checking for number
# def number_checker(num):
#     if num > 0:
#         print("number is positive")
#     elif num < 0:
#         print("number is negative")
#     else:
#         print("number is zero")
# num = int(input("Enter a number: "))
# number_checker(num)
# num1 = int(input("Enter a number1: "))
# num = int(input("Enter a number2: "))
# print("Prime numbers are : ")
# for i in range(num1,num+1):
#     if i > 1:
#         for j in range(2,i):
#             if (i%j) ==0:
#                 break
#             else:
#                 print(i)
# def tri_recursion(k):
#   if(k>0):
#     result = k+tri_recursion(k-1)
#     print(result)
#   else:
#     result = 0
#   return result
#
# print("\n\nRecursion Example Results")
# tri_recursion(6)
# def recursion(k):
#     if (k>0):
#         res = k + recursion(k-1)
#         print(res)
#     else:
#         res = 0
#     return res
# print("Recursion examples: ")
# recursion(6)
# def factorial(num):
#     fac = 1
#     if num < 0:
#         print("Factorial does not exist")
#     elif num == 0:
#         print("Factorial of number 0 is 1.")
#     else:
#         for i in range(1,num+1):
#             fac = fac * i
#             print("The factorial of ",i,"is ",fac)
# num = int(input("Enter a number to find factorial: "))
# factorial(num)
##################### Machine Learning #####################
# Features : input (independentt variables)
# Label/target : output (dependent variables)
########### 1. supervised learning
# supervision : Jesy kisi supervision m seekhna
# Jesy dog ko samjha ty h based on reward
# Jesy bachy ko seekhaty h chair , table etc
# iss m features, label dono hotey h
#-----> classification:
# label: in the form of classes. classify kr rehy.
# For example: male/female, fruit/vegetable, cat/dog
#-----> regression
# label: in the form of number
# predicting continuous number
# For example : predicting house prices
########### 2. Unsupervised learning
# machine khud learn krti h from past experiences
# iss m sarif features hotey h
########### 3. Reinforcement learning
# iss m 2, 3 objects hotey h, aik agent hota h , aik environment hota h , aik reward/penalty hoti h
# rat wali example , uss ko phely food miley gae , at the end ussey issi tarah capture kiya jay ega.
# na label sy baat ki. aik khula environment dy dia. agent : rat h , reward: food
### Intelligent path finding-----> shortest distance
### different distaces calcuate kr k shortest path find krty h .ye reinforcement laerning m ata.
# machine environmnt sy learn krti h.
# bias = loss
#  Weather Forecasting
# Used past data
# Use of Sensors
# Important thing is "data"
# Give data to machine , machine learn, then give output
# Data Platforms
# 1. Kaggle --> https://www.kaggle.com/datasets
# 2. Uci ml dataset repository ----> https://archive.ics.uci.edu/ml/index.php
## Google collab



