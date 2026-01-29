#arthamatic operators
'''
arthamatic operators :- 4 types 
                        1)addition
                        2)substraction
                        3)multiplication
                        $)division.

'''
# example for arthamatic operators :-

a=45
b=18

print(a+b)
print(a-b)
print(a*b)
print(a/b)


#assignement operators 

a=4-2                       # assign 4-2 in a
print(a)                    #output is 2 

b=6                         #b value is already is 6
b+=3                        #increment b value by 3 , output is 9
print(b)

c=4                         #c assign value is 4
c-=3                        #decrement the 3 value in 4 
print(c)                    #output is 1 ,

'''
over all the assignement value is assign value , and using increment and decrement we sould be assigns the value
'''


#comparision operators:-
#(it s commonly output we saw TRUE OR either FALSE )



#1)equal to(==)

a=23
b=23
print(a==b , a!=b)


a=12
bn=90
print (a>b)



a=23
b=90
print(a>=b)

a=88
b=90
print(a<b , a<=b)


#example =
marks=70
if marks>=35:
           print("pass")

else:
      print("fail")

a=8

print(a<=8)

#logical operator:-
# 3 types:-1)AND, 2)OR , 3)NOT.

#truth table of " or"
print("True or False is" , True or False)
print("True or True is", True or False)
print("False or True is ", True or False)
print("False or False is", True or False)


#truth table of " AND"
print("True and False is" , True and False)
print("True and True is", True and False)
print("False and True is ", True and False)
print("False and False is", True and False)

#not operator simple true ko false banata yee 
#and false ko true banata ye bhai simple .
print(not(True))
print(not(False))