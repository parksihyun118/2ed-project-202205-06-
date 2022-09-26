from bs4 import BeautifulSoup
import requests
import datetime
import time
import pandas as pd
import csv


headers = {'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Mobile Safari/537.36', 
           'Content-type':'application/x-www-form-urlencoded;charset=UTF-8;', 
           'origin':'https://www.mobileindex.com'
           }
url = "https://proxy-insight.mobileindex.com/chart/global_rank_v2"

target_dt = '20190101'
date = datetime.datetime.strptime(target_dt, '%Y%m%d')
days = 0

# request 접속
def bs(url,payload):
    #10번 시도
    for i in range(10):
        time.sleep(1)
        try:
            response = requests.post(url,headers=headers, data=payload)
            return response.json()

        # except requests.exceptions.Timeout as errd:
        #     print("Timeout Error : ", errd)
        #     continue
        
        # except requests.exceptions.ConnectionError as errc:
        #     print("Error Connecting : ", errc)
            
        # except requests.exceptions.HTTPError as errb:
        #     print("Http Error : ", errb)

        # # Any Error except upper exception
        # except requests.exceptions.RequestException as erra:
        #     print("AnyException : ", erra)
        except:
            continue
        
    return False

while date.strftime('%Y%m%d') != datetime.datetime.now().strftime('%Y%m%d'):

    date = (datetime.datetime.strptime(target_dt, '%Y%m%d') +datetime.timedelta(days))
    day = date.strftime('%Y%m%d')
    days +=1
    payload = {'market': 'all',
                'country': 'kr',
                'rankType': 'gross',
                'appType': 'game',
                'date': day,
                'startRank': '1',
                'endRank': '200'
                }

    # print(payload)
    # time.sleep(1)   
    dic = bs(url, payload)
    if not dic:
        print(day)
        break
    df = pd.DataFrame(dic)
    df.to_csv('app_game_ranking.csv', mode='a', index=False, header=None)

# 받아온 데이터( json, 딕셔너리 형식 )



# 키 확인
# keys = dic.keys()
# for i in keys:
#     print(i, dic[i])


# 랭킹정보 데이터
# data = dic['data']
# {'rank': 1, 'country_name': 'kr', 'market_name': 'google', 'rank_type': 'gross', 'app_name': '리니지W', 'publisher_name': 'NCSOFT', \
# 'icon_url': 'http~//지움', 'market_appid': 'com.ncsoft.lineagew', 'package_name': 'com.ncsoft.lineagew'}



# one_list=[]
# google_list=[]
# apple_list=[]

# market_name에 따라 다른 리스트에 입력함


# def switch(dic):
#     key = dic['market_name']
    
#     market = {"one": one_list,
#               "google" : google_list,
#               "apple" : apple_list
#               }
#     market[key].append(dic)



# for j in data:
#     switch(j)

    
