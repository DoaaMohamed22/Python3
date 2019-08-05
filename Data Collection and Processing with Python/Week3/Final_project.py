import requests
import json
def get_movies_from_tastedive(movie):
    dic={"q":movie,"type":"movies","limit":5,"k":"enter_your_key"}
    url ="https://tastedive.com/api/similar"
    page=requests.get(url,params=dic)
    page_dict=json.loads(page.text)
    return(page_dict['Similar']['Results'])
lst_0=get_movies_from_tastedive("Black Panther")
lst_1=get_movies_from_tastedive("Tony Bennett")

##qu2
movies_name=[]
def extract_movie_titles(lst_moves):
    for item in lst_moves:
        movies_name.append(item['Name'])
    return(movies_name)    

##print("Black Panther similar mocies:: ",extract_movie_titles(lst_0))
##print("Tony Bennett similar mocies:: ",extract_movie_titles(lst_1))
titles_0 = extract_movie_titles(lst_0)
titles_1 = extract_movie_titles(lst_1)
##print(len(titles_0))
##print(len(titles_1))

lst=[]

def get_related_titles(title):
    for items in title:
        if type(items)is list:
            for item in items:
                if item not in lst:
                    lst.append(item)
        else:
            for item in items:
                if item not in lst:
                    lst.append(item)                


    return(lst)      


print('=====Part2=====')

def get_movie_data(name_movie):
    url='http://www.omdbapi.com/'
    dic ={'t':name_movie,'r':'json','apikey':"enter_your_key"}
    page =requests.get(url,params=dic)
    page_dict=json.loads(page.text)
    return(page_dict)
Venom=get_movie_data("Venom")
Baby_Mama=get_movie_data("Baby Mama")
Deadpool_2=get_movie_data("Deadpool 2")

##print(movie1)
lst_rating=[]
rating_sort=[]
int_rating=[]
def get_movie_rating(movie):
    lst_movies = movie['Ratings']
      
    for items in lst_movies:
        if items['Source'] !='Rotten Tomatoes':
            lst_rating.append('0')

        elif items['Source'] =='Rotten Tomatoes':
            lst_rating.append(items['Value'])

    rating_sort=sorted(lst_rating,reverse=True)
    for items in rating_sort:
        int_rating.append(int(items.split('%')[0]))
            
    return(int_rating[0])        
print(get_movie_rating(movie1))
print(get_movie_rating(movie2))
