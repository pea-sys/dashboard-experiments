import requests

OECD_ROOT_URL = 'http://stats.oecd.org/sdmx-json/data'

def make_OECD_request(dsname, dimensions, params=None, root_dir=OECD_ROOT_URL):
    if params is None:
        params = {}
    
    dim_args = ['+'.join(d) for d in dimensions]
    dim_str = '.'.join(dim_args)

    url = root_dir + '/' + dsname + '/' + dim_str + '/all'
    print('Requesting URL: ' + url)
    return requests.get(url,  params=params)


response = make_OECD_request('QNA',(('USA','AUS'),('GDP', 'B1_GE'),('CUR','VOBARSA'),('Q')),{'startTime':'2009-Q1', 'endTime':'2010-Q1'})

if response.status_code == 200:
    json=response.json()
    print(json.keys())