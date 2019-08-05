##ex1

lst_check = ['plums', 'watermelon', 'kiwi', 'strawberries', 'blueberries', 'peaches', 'apples', 'mangos', 'papaya']
def add_fruit(lst):
    return('Fruit: '+lst)
    
map_testing =map(add_fruit,lst_check)

##ex2

countries = ['Canada', 'Mexico', 'Brazil', 'Chile', 'Denmark', 'Botswana', 'Spain', 'Britain', 'Portugal', 'Russia', 'Thailand', 'Bangladesh', 'Nigeria', 'Argentina', 'Belarus', 'Laos', 'Australia', 'Panama', 'Egypt', 'Morocco', 'Switzerland', 'Belgium']

b_countries = filter(lambda lst:'B'in lst ,countries )
print(b_countries)

##ex3

people = [('Snow', 'Jon'), ('Lannister', 'Cersei'), ('Stark', 'Arya'), ('Stark', 'Robb'), ('Lannister', 'Jamie'), ('Targaryen', 'Daenerys'), ('Stark', 'Sansa'), ('Tyrell', 'Margaery'), ('Stark', 'Eddard'), ('Lannister', 'Tyrion'), ('Baratheon', 'Joffrey'), ('Bolton', 'Ramsey'), ('Baelish', 'Peter')]
first_names= [lst[1] for lst in people]
print(first_names)

##ex4

lst = [["hi", "bye"], "hello", "goodbye", [9, 2], 4]
lst2 = [ lsts*2 for lsts in lst]
print(lst2)

## ex5

students = [('Tommy', 95), ('Linda', 63), ('Carl', 70), ('Bob', 100), ('Raymond', 50), ('Sue', 75)]

passed = [lst[0] for lst in students if lst[1] >= 70 ]
print(passed)

## ex6

l1 = ['left', 'up', 'front']
l2 = ['right', 'down', 'back']
lsts_zip= zip(l1,l2)
##opposites=[lst for lst in lsts_zip if len(lst[0]) > 2 and len(lst[1]) > 2]

opposites=filter(lambda value: len(value[0]) > 2 and len(value[1]) > 2 ,lsts_zip)
print(opposites)

## ex7


species = ['golden retriever', 'white tailed deer', 'black rhino', 'brown squirrel', 'field mouse', 'orangutan', 'sumatran elephant', 'rainbow trout', 'black bear', 'blue whale', 'water moccasin', 'giant panda', 'green turtle', 'blue jay', 'japanese beetle']

population = [10000, 90000, 1000, 2000000, 500000, 500, 1200, 8000, 12000, 2300, 7500, 100, 1800, 9500, 125000]

pop_info =zip(species,population)
##print(pop_info)
lst =filter(lambda value: value[1] < 2500,pop_info)
endangered=map(lambda value: value[0],lst)
print(endangered)            
            
#endangered =[value for value in pop_info if value[1] > 2500]
