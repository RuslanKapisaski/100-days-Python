import requests
import datetime

#-----------------/CREATE PIXELA PROFILE\-----------------
pixela_endpoint = "https://pixe.la/v1/users"

TOKEN = "jsia7238481pDFAAuhe;ow1p9wpsas"
USERNAME = "ruslan2026"

user_params = {
    "token": TOKEN ,
    "username": USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes",
}
#response = requests.post(url=pixela_endpoint, json=user_params)


#-----------------/CREATE PIXELA GRAPH\-----------------
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
GRAPH_ID = "graph1"

graph_config ={
    "id":GRAPH_ID,
    "name":"Running Graph",
    "unit":"Km",
    "type":"float",
    "color":"shibafu",
}

headers ={
    "X-USER-TOKEN":TOKEN
}


#-----------------/ADD PIXELA PIXEL\-----------------
post_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.date.today()
yesterday = today - datetime.timedelta(days=1)

post_data ={
    "date":yesterday.strftime("%Y%m%d"),
    "quantity":"8"
}
#response = requests.post(url=post_endpoint,  json=post_data,headers=headers)


#-----------------/UPDATE PIXELA PIXEL\-----------------
put_data ={
    "quantity":"20"
}

put_endpoint =f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

response = requests.put(url=put_endpoint, json=put_data,headers=headers)
print(response.text)