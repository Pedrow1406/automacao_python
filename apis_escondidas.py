import requests
import pandas as pd
from tabulate import tabulate
headers = {
    'authority': 'api.catarse.me',
    'accept': 'application/json, text/*',
    'accept-language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
    'origin': 'https://www.catarse.me',
    'prefer': 'count=none',
    'range': '0-0',
    'range-unit': 'items',
    'referer': 'https://www.catarse.me/',
    'sec-ch-ua': '^\\^Not',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '^\\^Windows^\\^',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
}

params = (
    ('project_id', 'eq.130712'),
)

response = requests.get('https://api.catarse.me/project_details', headers=headers, params=params)

def show_table(table):
    print(tabulate(table,  headers= 'keys', tablefmt='fancy_grid'))

catarse = pd.json_normalize(response.json())
# print(catarse.loc[0])
# print(catarse.columns)
# print(catarse[['project_id','name', 'headline','goal','pledged']])


import requests

headers = {
    'authority': 'www1.folha.uol.com.br',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
    'cookie': '_cb_folha=6OZKhBMpYtuDkWzH_; folha_ga_userType=not_logged; folha_ga_loginType=folha; folha_ga_userGroup=none; folha_ga_swgt=none; _gcl_au=1.1.1383230389.1707064487; _gid=GA1.3.1043249090.1707064487; BTCTL=23; _sp_ses.8894=*; _matheriSegs=MATHER_U9_INSTANTMET2_20200701; _matherSegments=MATHER_U9_INSTANTMET2_20200701; nav23947=13f9f8d243e4e514dc26f4221710^|2_36; _scor_uid=d03fe40f3bf74484baa3d30a2ac3d49d; _cb_svref_folha=https^%^3A^%^2F^%^2Fwww.folha.uol.com.br^%^2F; tt_c_vmt=1707064520; tt_c_c=referral; tt_c_s=referral; tt_c_m=referral; tt.u=0100007FB646BE65D906F00802F6B03C; tt.nprf=; _gat_uolMain=1; _ga=GA1.1.1178663288.1707064487; _chartbeat2_folha=.1707064485821.1707064590094.1.CCI-ll9hFisT-rTBDhzcVVB7H9nL.3; _ttuu.s=1707064590477; _sp_id.8894=42d44904-0e2d-4c9b-a323-5f72c1f18729.1707064489.1.1707064603.1707064489; _chartbeat4_folha=t=C9M33BDjgpOpDFxPoJCEqrqVCdR0Ff&E=10&x=0&c=0.35&y=1799&w=695; _ga_RY1LTN28TR=GS1.1.1707064487.1.1.1707064611.36.0.0',
    'referer': 'https://www1.folha.uol.com.br/maispopulares/',
    'sec-ch-ua': '^\\^Not',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '^\\^Windows^\\^',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
}

params = (
    ('qs', '2024141336'),
)

response = requests.get('https://www1.folha.uol.com.br/virtual/spiffy/mais-lidas/home-1.0.0.json', headers=headers, params=params)

folha_df = pd.DataFrame(response.json())
# print(folha_df[['cover_date', 'title', 'url']])


import requests

cookies = {
    'preferred_locale': 'pt-BR',
    '__Host-mons-sid': '137-7806914-5120950',
    'analytics_id': '0dc032b8-2e18-4934-ba4b-f0ec3c9c5b7b',
    'AMCVS_CCBC879D5572070E7F000101^%^40AdobeOrg': '1',
    'cwr_u': '55ea3a6f-e931-4f7f-a287-9ebc38f39ad0',
    'csm-sid': '549-0527000-4519141',
    's_lv_s': 'First^%^20Visit',
    's_cc': 'true',
    'AMCV_CCBC879D5572070E7F000101^%^40AdobeOrg': '-1124106680^%^7CMCIDTS^%^7C19758^%^7CMCMID^%^7C45581952408164671201820055064294109795^%^7CMCAAMLH-1707681717^%^7C4^%^7CMCAAMB-1707681717^%^7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y^%^7CMCOPTOUT-1707084118s^%^7CNONE^%^7CMCAID^%^7CNONE^%^7CvVersion^%^7C5.2.0',
    '__Host-mons-ubid': '134-7232880-0168944',
    'gpv': 'Amazon.jobs^%^20^%^7C^%^20Search',
    '__Host-mons-st': 'kAjX7bqOhHgLM/l0bfQSWZkOLJG/P9RK8BkSpMU0KVX58ZKGNuU92s2PMHRR/T0mnFJPZcZFOCNrstQZBeDk+jH9k7p9ibnsp+7Afaf9XRfw2bcH0v7yqORV7rtmEqLvtWFhriBH7GLOFoewCNnirFBLPpPaCXrHoTPawZ28OaqtLLjP+E4muU0dg1cukIy8weaVhtYUGjv7ztQpyc6fI4xZQRZGHkJBHhB2765oKG7KYmEHaCK7wTJzydwXlToTMe2e8cK0gSxbVVDNEVvv/0aD4+WJlWCS80nwPN9RdaWBavg65iWMchn7ExvdroXAmeQmSH4zLMSQBDZ9HYMSICIKtbXik0kG',
    's_lv': '1707078748341',
    's_nr30': '1707078748342-Repeat',
    's_ppvl': 'Amazon.jobs^%^2520^%^257C^%^2520Search^%^2C99^%^2C24^%^2C2895^%^2C1536^%^2C695^%^2C1536^%^2C864^%^2C1.25^%^2CP',
    's_ppv': 'Amazon.jobs^%^2520^%^257C^%^2520Search^%^2C20^%^2C20^%^2C695^%^2C1536^%^2C695^%^2C1536^%^2C864^%^2C1.25^%^2CP',
    's_sq': '^%^5B^%^5BB^%^5D^%^5D',
    'amazon_jobs_session': 'aHgvVDh4WjlubXhXWWpCckNTeittcUxuaFJhc29DTDBheFVOTjhXVlVJdWNZREVRK1NtUjRMZzRTR0hKR3gzNlB2SkFsR1luc3BybWhRVUk3SG9MVTBNeFh2QTlqUVNPZVpQYmRRTXo3VFR2UVhBUm1mTXhwaW53T3ovTnR6a3VDUWMvajJsYW5IbmVYTDFqQTRYQ0dLUlVrMm1KelNGWDlsaC9ydUpnVHg5bmR4OXdvRDlKRlk2Y05qcFVCTWdrajdRTnJ1L0FPcUhPZHFmN3ZUb2R2YitvendaeWFKWFpHZktJUFZtVXl4cHV4UUFJWUdvNGhqOWZDeGkyd3RrVElLQlRaait6bFI0MlhVQTd6K0dVcUR3MTAwWlNsRWJ0ZVR3MWJDcjdRN204YmZTcWUzNHdWQjAvRnJZUy9UUGsvV2UxQU1uQVpPWWZCYzIzREhsaWxqelRFWWRhcTkwbjA4czl0UkRxUk9vPS0tYnVld3MwaDE5d0RJcXhrWDhBcy9zdz09--2ec1812065cb39d84c86063ce1f173e4c5c61c3c',
    'cwr_s_a727750b-28d3-4e1d-81fe-8eece247d35b': 'eyJzZXNzaW9uSWQiOiJlMDVlOGFlOC0zMjhlLTRmYWEtYTY0OC1kY2M0NTg4NmYzYWIiLCJyZWNvcmQiOnRydWUsImV2ZW50Q291bnQiOjE2MCwicGFnZSI6eyJwYWdlSWQiOiIvcHQvc2VhcmNoIiwicGFyZW50UGFnZUlkIjoiL3B0L3NlYXJjaCIsImludGVyYWN0aW9uIjoxMSwic3RhcnQiOjE3MDcwNzg3NjU3NDd9fQ==',
}

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
    'Connection': 'keep-alive',
    'If-None-Match': 'W/^\\^d003fc2d309ce361857237a6f9d2bf0a^\\^',
    'Referer': 'https://amazon.jobs/pt/search?base_query=&loc_query=S^%^C3^%^A3o+Paulo^%^2C+S^%^C3^%^A3o+Paulo^%^2C+Brasil&latitude=-23.56287&longitude=-46.65469&loc_group_id=&invalid_location=false&country=BRA&city=Sao+Paulo&region=Sao+Paulo&county=',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
    'sec-ch-ua': '^\\^Not',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '^\\^Windows^\\^',
}

params = (
    ('radius', '24km'),
    ('facets^%^5B^%^5D', ['normalized_country_code', 'normalized_state_name', 'normalized_city_name', 'location', 'business_category', 'category', 'schedule_type_id', 'employee_class', 'normalized_location', 'job_function_id', 'is_manager', 'is_intern']),
    ('offset', '0'),
    ('result_limit', '20'),
    ('sort', 'relevant'),
    ('latitude', '-23.56287'),
    ('longitude', '-46.65469'),
    ('loc_group_id', ''),
    ('loc_query', 'S^%^C3^%^A3o^%^20Paulo^%^2C^%^20S^%^C3^%^A3o^%^20Paulo^%^2C^%^20Brasil'),
    ('base_query', ''),
    ('city', 'Sao^%^20Paulo'),
    ('country', 'BRA'),
    ('region', 'Sao^%^20Paulo'),
    ('county', ''),
    ('query_options', ''),
)

response = requests.get('https://amazon.jobs/pt/search.json', headers=headers, params=params, cookies=cookies)

#NB. Original query string below. It seems impossible to parse and
#reproduce query strings 100% accurately so the one below is given
#in case the reproduced version is not "correct".
# response = requests.get('https://amazon.jobs/pt/search.json?radius=24km&facets^%^5B^%^5D=normalized_country_code&facets^%^5B^%^5D=normalized_state_name&facets^%^5B^%^5D=normalized_city_name&facets^%^5B^%^5D=location&facets^%^5B^%^5D=business_category&facets^%^5B^%^5D=category&facets^%^5B^%^5D=schedule_type_id&facets^%^5B^%^5D=employee_class&facets^%^5B^%^5D=normalized_location&facets^%^5B^%^5D=job_function_id&facets^%^5B^%^5D=is_manager&facets^%^5B^%^5D=is_intern&offset=0&result_limit=10&sort=relevant&latitude=-23.56287&longitude=-46.65469&loc_group_id=&loc_query=S^%^C3^%^A3o^%^20Paulo^%^2C^%^20S^%^C3^%^A3o^%^20Paulo^%^2C^%^20Brasil&base_query=&city=Sao^%^20Paulo&country=BRA&region=Sao^%^20Paulo&county=&query_options=&', headers=headers, cookies=cookies)

print(response)
jobs_df = pd.DataFrame(response.json()['jobs'])
show_table(jobs_df[['title', 'city','posted_date']].drop_duplicates())
# print(jobs_df)