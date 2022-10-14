from datetime import datetime
import collections
# random_list = ['A', 'A', 'B', 'C', 'B', 'D', 'D', 'A', 'B']
date = datetime.now()
import math
print("Today : ",date)
# print("list built-in methods")
# new_list = [7,4,88,32,11,1,2,2,2,2,2,2,2,]
# print(max(new_list))
# print(min(new_list))
# num = new_list.count(2)
# print(num)
# using Counter to find frequency of elements
# frequency = collections.Counter(new_list)
# printing the frequency
# print(frequency)
#Use of dctionary
# dict = {
#     'name':'Sidra Sonia Aziz',
#     'roll_no':'2019-CE-8'
# }
# print(dict)
# print(dict.keys())
# print(dict.values())
# print(dict['roll_no'])
# for  i in dict:
#     print("key: ",i,"values: ",dict[i])
# dict = {
#     'fruits':['apple','orange','banana'],
#     'veg':['potato','tomato','cucumber'],
#     'cars':['honda','bmw','mercedies']
# }
# print(dict)
# print(dict.keys())
# print(dict.values())
# print(dict['veg'])
# print(dict['veg'][2])
# for  i in dict:
#     print("key: ",i,",values: ",dict[i],"\n")
# print("Sidra "*5)
#Loops
#fOR LOOP USS WAQAT USE KREY GY K JB PATA HO GA K FINITE TIME LOOP CHLY GA
#for loop(know in advance, how many times repeat)
#while loop(not know in advance)
# C
# for i in range(0,10):
#     print("pAK",i)
# for i in range(len(new_list)):
#     print(new_list[i])
print("For loop using list")
new_list = [7,4,88,32,11,1,2,2,2,2,2,2,2,]
for i in range(len(new_list)):
    print(new_list[i])
print("For loop using dictionary")
dict = {
    'fruits':['apple','orange','banana'],
    'veg':['potato','tomato','cucumber'],
    'cars':['honda','bmw','mercedies']
}
for i in dict:
    print(i, dict[i])