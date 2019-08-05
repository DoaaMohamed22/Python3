##part1

nested = [['dog', 'cat', 'horse'], ['frog', 'turtle', 'snake', 'gecko'], ['hamster', 'gerbil', 'rat', 'ferret']]
output=nested[1][2]
print(output)

##part2


lst = [['apple', 'orange', 'banana'], [5, 6, 7, 8, 9.9, 10], ['green', 'yellow', 'purple', 'red']]

#Test to see if 'yellow' is in the third list of lst. Save to variable ``yellow``

for lsts in lst:
    for item in lsts:
        if item=='yellow':
            yellow= True
            print(yellow)
    
#Test to see if 4 is in the second list of lst. Save to variable ``four``
for lsts in lst:
    for item in lsts:
        if item==4:
            four=True
            print(four)
        else:
            four=False
            print(four)

#Test to see if 'orange' is in the first element of lst. Save to variable ``orange``

for lsts in lst:
    for item in lsts:
        if item=='orange':
            orange=True
            print(orange)

##part3

L = [[5, 8, 7], ['hello', 'hi', 'hola'], [6.6, 1.54, 3.99], ['small', 'large']]

# Test if 'hola' is in the list L. Save to variable name test1
for lst in L:
    for item in lst:
        if item=='hola':
            test1= True
            print(test1)
        else:
            test1=False
            print(test1)
            
# Test if [5, 8, 7] is in the list L. Save to variable name test2
for lst in L:
        if lst==[5, 8, 7]:
            test2= True
            print(test2)

# Test if 6.6 is in the third element of list L. Save to variable name test3

for lst in L:
    for item in lst:
        if item==6.6:
            test3= True
            print(test3)


##PArt4
            
nested = {'data': ['finding', 23, ['exercises', 'hangout', 34]], 'window': ['part', 'whole', [], 'sum', ['math', 'calculus', 'algebra', 'geometry', 'statistics',['physics', 'chemistry', 'biology']]]}

# Check to see if the string data is a key in nested, if it is, assign True to the variable data, otherwise assign False.
for key, items in nested.items():
    if(key=='data'):
        data=True
        print(data)
        
# Check to see if the integer 24 is in the value of the key data, if it is then assign to the variable twentyfour the value of True, otherwise False.
for key, items in nested.items():
    if key =='data':
        if type(items) is list:
            for lst in items:
                if lst == 24:
                    twentyfour= True
                    print(twentyfour)
                else:
                    twentyfour=False
                    print(twentyfour)
       
        else:
            if lst == 24:
                twentyfour= True
                print(twentyfour)
            else:
                twentyfour=False
                print(twentyfour)
                 
               
                
        
    
# Check to see that the string 'whole' is not in the value of the key window. If it's not, then assign to the variable whole the value of True, otherwise False.
for key, items in nested.items():
    if key =='window':
        if type(items) is list:
            for lst in items:
                if lst == 'whole':
                    whole= True
                    print(whole)
                else:
                    whole=False
                    print(whole)
       
        else:
            if lst == 'whole':
                whole= True
                print(whole)
            else:
                whole=False
                print(whole)
                 


# Check to see if the string 'physics' is a key in the dictionary nested. If it is, assign to the variable physics, the value of True, otherwise False.

for key, items in nested.items():
    if key=='physics':
        physics=True
        print(physics)
    else:
        physics = False
        print(physics)
##part5


nested_d = {'Beijing':{'China':51, 'USA':36, 'Russia':22, 'Great Britain':19}, 'London':{'USA':46, 'China':38, 'Great Britain':29, 'Russia':22}, 'Rio':{'USA':35, 'Great Britain':22, 'China':20, 'Germany':13}}
london_gold =[]
for keys, items_dic in nested_d.items():
    for keys_2, items_2 in items_dic.items():
        if keys_2 =='Great Britain':
            london_gold.append(items_2)
london_gold=sorted(london_gold,reverse=True)[0]            
print(london_gold)


##part6

sports = {'swimming': ['butterfly', 'breaststroke', 'backstroke', 'freestyle'], 'diving': ['springboard', 'platform', 'synchronized'], 'track': ['sprint', 'distance', 'jumps', 'throws'], 'gymnastics': {'women':['vault', 'floor', 'uneven bars', 'balance beam'], 'men': ['vault', 'parallel bars', 'floor', 'rings']}}

# Assign the string 'backstroke' to the name v1
for keys, items in sports.items():
    for lst in items:
        if lst =='backstroke':
            v1=lst
            print(v1)
        

# Assign the string 'platform' to the name v2
for keys, items in sports.items():
    for lst in items:
        if lst =='platform':
            v2=lst
            print(v2)


# Assign the list ['vault', 'floor', 'uneven bars', 'balance beam'] to the name v3
for keys, items_dict in sports.items():
    if type(items_dict) is dict:
        for keys_2, items in items_dict.items():
            if items ==['vault', 'floor', 'uneven bars', 'balance beam']:
                v3 =items
                print(v3)

          

# Assign the string 'rings' to the name v4
for keys, items_dict in sports.items():
    for lst in items_dict:
        if lst =='rings':
            v4=lst
            print(v4)
        else:
            v4=False
            print(v4)
    if type(items_dict) is dict:
        for keys_2, items in items_dict.items():
            for lsts in items:
                if lsts =='rings':
                    v4=lsts
                    print(v4)
                else:
                    v4=False

                
        

##part7

nested_d = {'Beijing':{'China':51, 'USA':36, 'Russia':22, 'Great Britain':19}, 'London':{'USA':46, 'China':38, 'Great Britain':29, 'Russia':22}, 'Rio':{'USA':35, 'Great Britain':22, 'China':20, 'Germany':13}}

US_count = []
for keys, items_dic in nested_d.items():
    for keys_2, items_2 in items_dic.items():
        if keys_2 =='USA':
            US_count.append(items_2)
print(US_count)


##part8

l_of_l = [['purple', 'mauve', 'blue'], ['red', 'maroon', 'blood orange', 'crimson'], ['sea green', 'cornflower', 'lavender', 'indigo'], ['yellow', 'amarillo', 'mac n cheese', 'golden rod']]
third=[]
for lsts in l_of_l:
    third.append(lsts[2])        
print(third)        


#part9

athletes = [['Phelps', 'Lochte', 'Schooling', 'Ledecky', 'Franklin'], ['Felix', 'Bolt', 'Gardner', 'Eaton'], ['Biles', 'Douglas', 'Hamm', 'Raisman', 'Mikulak', 'Dalton']]
t= []
other=[]
for lsts in athletes:
    for lst in lsts:
        if 't' in lst:
            t.append(lst)
        else:
            other.append(lst)
print(t)
print(other)

