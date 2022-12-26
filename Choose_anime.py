# -*- coding: utf-8 -*-
"""
Created on Fri Jun 10 14:39:53 2022

@author: Tarun
"""

import requests
import random


#Use this function to get my plan to watch list from MyAnimeList
#update:
    #originally I thought they would give the whole list at once but I need to keep pulling the data
def getAnimeList():
    CLIENT_ID = 'a460179b988e3a3141f712207a76360d'

    url = 'https://api.myanimelist.net/v2/users/RUN4urlfe/animelist?status=plan_to_watch'

    #x-mal-client-id line needed to go around authenticating user
    response = requests.get(url, headers = {
        'X-MAL-CLIENT-ID': CLIENT_ID
        })
    
    response.raise_for_status()
    anime_list = response.json()
    response.close()
    
    titles = []
    #grab the first 10 titles
    titles = getTitles(anime_list,titles)
    
    #theres more to the list so going to make a loop that keeps pulling the next 10 anime entries
    while('next' in anime_list['paging'].keys()):
        #get url for next request
        url = anime_list['paging'].get('next')
        #get response
        response = requests.get(url, headers = {
            'X-MAL-CLIENT-ID': CLIENT_ID
            })
        
        response.raise_for_status()
        anime_list = response.json()
        response.close()
        
        titles = getTitles(anime_list,titles)
    
    return titles


#this iterates through the anime list dictionary and pulls the titles
def getTitles(anime_list,titles):
    length = len(anime_list['data'])
    for i in range(0,length):
        titles.append(anime_list['data'][i].get('node').get('title'))
    return titles

def main():
    go = 'y'
    while(go == 'y' or go == 'Y'):
        rep = input("Anime(1) or Manga(2)\n")
        if(int(rep) == 1):
            plan_to_watch = getAnimeList()
            print("Ok Tarun, go watch", random.choice(plan_to_watch))
        elif(int(rep) == 2):
            print("working on it")
        go = input("Want another suggestion? y/n \n")
if __name__== "__main__" :
    main()   
    
