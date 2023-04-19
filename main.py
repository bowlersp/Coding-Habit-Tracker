import requests

USERNAME = "xxxxx"
TOKEN = "yyyyy"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

user_params_response = requests.post(url=pixela_endpoint, json=user_params)


graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Coding Tracker Graph",
    "unit": "Hours",
    "type": "float",
    "color": "sora",
}

headers = {
    "X-USER-TOKEN": TOKEN
}
graph_config_response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
print(graph_config_response.text)


#### Post to Graph Program ####

final_graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1"


date = input("please enter the date you coded (FORMAT = yyyyMMdd)\n")
quantity = input("please enter the length of time in hours you coded\n")

date_and_quantity = {
    "date": date,
    "quantity": quantity
}

post_to_graph = requests.post(url=final_graph_endpoint, json=date_and_quantity, headers=headers)
print(post_to_graph.text)
