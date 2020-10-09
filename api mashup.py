
# coding: utf-8

# In[14]:


import requests
import json


def get_movies_from_tastedive(name):
    res= requests.get('https://tastedive.com/api/similar',params={'q':name,'type':'movies','limit':5})
    return res.json()
def extract_movie_titles(ret):
    titles=[]
    for key in ret['Similar']['Results']:
        titles.append(key['Name'])
    return titles
def get_related_titles(lst):
    list_titles=[]
    if lst==[]:
        return []
    else:
        for i in lst:
            full_det=get_movies_from_tastedive(i)
            titles_lst=extract_movie_titles(full_det)
            for i in titles_lst:
                if i not in list_titles:
                    list_titles.append(i)
        return list_titles
def get_movie_data(name):
    res=requests.get('http://www.omdbapi.com/?i=tt3896198&apikey=b88b07cd',params={'t':name,'r':'json'})
    return res.json()
def get_movie_rating(resp):
    for i in resp['Ratings']:
        if i['Source']=='Rotten Tomatoes':
            return int(i['Value'].replace('%',''))
    return 0
def get_sorted_recommendations(lste):
    x=get_related_titles(lste)
    rating=[]
    for i in x:
        y=get_movie_data(i)
        z=get_movie_rating(y)
        rating.append(z)
    total=zip(rating,x)
    return sorted(total,key=lambda x:x[0],reverse=True)
print('WORKING OF get_movies_from_tastedive(movie_name)------------------------\n')
x=get_movies_from_tastedive('venom')
print(f'{x}\n')
print('WORKING OF extract_movie_titles()-----------------------------\n')
y=extract_movie_titles(x)
print(f'{extract_movie_titles(x)}\n') 
print('WORKING OF get_related_titles()-------------------------------\n')
print(f'{get_related_titles(y)}\n')
print('-----------------------------------------------------------------\n')
print('WORKING OF get_movie_data()-------------------------------\n')
z=get_movie_data('venom')
print(get_movie_data('venom'))
print('\n\n')
print('WORKING OF get_movie_rating(r)-------------------------------\n')
print(f'{get_movie_rating(z)}\n')
print('WORKING OF get_sorted_recommendations()-------------------------------\n')
print(f'{get_sorted_recommendations(y)}')


# In[ ]:




    

