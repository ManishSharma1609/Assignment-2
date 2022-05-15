print('Q U E S T I O N  1')
input_str=str('Python is a case sensitive language')
print('the input string is:',input_str)
print('PART_a')
#finding length of input string
str1_length=len(input_str)
print('the length of input string is:', str1_length)

print('PART_b')
#printing input string in reverse order
str1_reverse=input_str[::-1]
print('reverse of input string:',str1_reverse)

print('PART_c')
#slicing input string
str2=input_str[10:26]
#printing the new string
print(str2)

print('PART_d')
#making replacement in the new string
new_string=input_str.replace('a case sensitive','object oriented')
print('new string after replacement is:',new_string)

print('PART_e')
#finding index of "a" in the input string
str_index=input_str.find('a')
print('index of "a" in input string is:', str_index)

print('PART_f')
#removing white spaces from the input string
str_combine=input_str.replace(' ','')
print('input string after removing all white spaces:',str_combine)

print('Q U E S T I O N  2')
#initializing variables
name=str('Manish')
sid=int(21102048)
department_name=str('civil')
cgpa=float(9.9)
#printing required data
print('Hey,%s'%(name),'Here!\nMY SID is %d'%(sid),'\nI am from %s'%(department_name),'department and my CGPA is %1.1f'%(cgpa))


print('Q U E S T I O N  3')
a=56
b=10
print('a=',a,'b=',b)

print('PART_a')
print('a&b=',a&b)

print('PART_b')
print('a|b=',a|b)

print('PART_c')
print('a^b=',a^b)

print('PART_d')
print('left shifting a with 2 bits:a<<2=',a<<2)
print('left shifting b with 2 bits:b<<2=',b<<2)

print('PART_e')
print('right shifting a with 2 bits:a>>2=',a>>2)
print('right shifting b with 2 bits:b>>2=',b>>2)



print('Q U E S T I O N  4')
print("Please Enter a string :")
char = str(input())
x = char.find('name')
if x == -1 :
    print("No")
else :
    print("Yes")


print('Q U E S T I O N  5')
a = int(input("Please enter the length of side 1 : "))
b = int(input("Please enter the length of side 2 : "))
c = int(input("Please enter the length of side 3 : "))
while ((a+b)>c) and ((a+c)>b) and ((b+c)>a):
    print("Yes")
    break
while ((a+b)<c) or ((a+c)<b) or ((b+c)<a):
    print("No")
    break

print('Q U E S T I O N  6')
print ("enter 1st number")
number_1=int(input())

print ("enter 2nd number")
number_2=int(input())

ex_or=number_1^number_2
bin_exor=bin(ex_or)
check_string= str(bin_exor)

a=check_string.count('1')
print(a)