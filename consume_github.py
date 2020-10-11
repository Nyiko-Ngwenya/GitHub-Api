import requests
import json
import datetime

def get_pull_requests(github_username,reporitory_name, start_date, end_date):
    headers = {
    'Accept': 'application/vnd.github.v3+json',
    }
    base_api = 'https://api.github.com'
    pulls_response = f'/repos/{github_username}/{reporitory_name}/pulls'
    endpoint = base_api+pulls_response
    response = requests.get(endpoint , headers=headers ,params = {'state': 'all'} )
    data = response.json()
    pull_requests =[]
    if len(data) >0:
        pull_requests =[]
        for pr in data:
            for date_object in ['created_at','updated_at','merged_at','closed_at']:
                if pr[date_object] != None:
                    date = datetime.datetime.strptime(pr[date_object][:10], '%Y-%m-%d')
                    if (date >= start_date) and (date <= end_date):
                        pull_requests.append(pr)
                        break
        return pull_requests
    else:
        return pull_requests , 'No pull requests on this repo at all '


# date1 = datetime.datetime(2020, 10, 5)
# date2 = datetime.datetime(2021, 1, 30)
# print(len(get_pull_requests('Nyiko-Ngwenya','Testing-',date1,date2)))


