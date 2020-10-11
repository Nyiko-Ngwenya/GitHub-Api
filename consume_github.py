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

