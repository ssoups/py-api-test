import math
import os
import requests as req


debugmode = False

os.system('cls')
user = input("Enter your tetrio username!\n").lower()

def userinfo(json):
    
    print("Username: " + json['username'])
    print("Country: " + json['country'])
    print("Role: " + json['role'])
    print("Games played: " + str(json['gamesplayed']))
    print("Games won: " + str(json['gameswon']))
    print("WLR: " + str(round((json['gameswon']/json['gamesplayed'])*1000)/10) + "%")
    
def leagueinfo(json):
    
    print("Rank: " + json['rank'])
    print("League Games Played: " + str(json['gamesplayed']))
    print("Games Won : " + str(json['gameswon']))
    print("League WLR : " + str(round((json['gameswon']/json['gamesplayed'])*1000)/10) + "%")
    print("Avg. apm: " + str(json['apm']))
    print("Avg. ppm: " + str(json['pps']))
    print("Percentile: " + str(round(json['percentile'] * 1000)/100) + "%")



def options(json): 
    os.system('cls')
    option = input('Please pick any following option: \n- All \n- User Info \n- League Info \n- Rank Info\n').lower()

    if option == "all": # Runs all functions
        os.system('cls')
        userinfo(json['data']['user'])
        leagueinfo(json['data']['user']['league'])

    elif option == "user info":
        os.system('cls')
        userinfo(json['data']['user'])

    elif option == "league info":
        os.system('cls')
        leagueinfo(json['data']['user']['league'])
    elif option == "json":
        print(json)
    else:
        os.system('cls')
        print("Option not found.")
    


res = req.get("https://ch.tetr.io/api/users/" + user).json()
if res['success'] == False: 
    print('Your username could not be found.')
else:
    options(res)


    