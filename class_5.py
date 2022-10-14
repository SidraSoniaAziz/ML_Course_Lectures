
# list  = [1,2,3,4,5,6,7]
# list = []
# num = int(input("Enter number: "))
# list = list.append(num)
# j = 0
# for i in range(len(list)):
#     j =i+j
#     print("Sum is :",j)
# list = []
# sum = 0
# for i in range(6):
#     num = int(input("Enter number: "))
#     list[i] = list.append(num)
#     for j in range(i):
#         j =  sum + j
#         print
#prime number
#While Loop
# i = 0
# while i <= 5:
#     print("i: " , i)
#     if i == 3:
#         break
#     i = i + 1
# https://bobbyhadz.com/blog/python-add-user-input-to-list
#Functions
#built-in function e.g sum()
#User defined functions
def fun():
    print("Introduction to functions")
fun()
def math_operations(num1,num2):
    sum  = num1+num2
    sub = num1 - num2
    mul = num1 * num2
    div = num1 / num2
    return sum,sub,mul,div

sum,sub,mul,div = math_operations(2,3)
print("sum is : ",sum)
print("sub is : ", sub)
print("mul is : ", mul)
print("div is : ", div)
