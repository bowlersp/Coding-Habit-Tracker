import requests

USERNAME = "bowlersp"
TOKEN = "1qaz!QAZ"
headers = {
    "X-USER-TOKEN": TOKEN
}
pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

#user_params_response = requests.post(url=pixela_endpoint, json=user_params)



### CREATING THE GRAPH ###

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Coding Tracker Graph",
    "unit": "Hours",
    "type": "float",
    "color": "sora",
}

#graph_config_response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
#print(graph_config_response.text)


#### Post to Graph ####

def new():
    date = input("NEW ENTRY SELECTED. please enter the date you coded (FORMAT = yyyyMMdd)\n")
    quantity = input("please enter the length of time in hours you coded\n")

    date_and_quantity = {
        "date": date,
        "quantity": quantity
    }
    final_graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1"
    post_to_graph = requests.post(url=final_graph_endpoint, json=date_and_quantity, headers=headers)
    print(post_to_graph.text)


#### Update to Graph ####

def update():
    date = input("UPDATE ENTRY SELECTED. please enter the date you coded that you want to update (FORMAT = yyyyMMdd)\n")
    quantity = input("please enter the length of time in hours you coded\n")

    quantity = {
        "quantity": quantity
    }
    put_graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1/{date}"
    put_to_graph = requests.put(url=put_graph_endpoint, json=quantity, headers=headers)
    print(put_to_graph.text)

#### Delete to Graph ####

def delete():
    date = input("DELETE ENTRY SELECTED. please enter the date you coded that you want to delete (FORMAT = yyyyMMdd)\n")

    delete_graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1/{date}"
    delete_to_graph = requests.delete(url=delete_graph_endpoint, headers=headers)
    print(delete_to_graph.text)

### Initial User Interface ###

Mode_Selection = input("Greetings, Please choose to add/update or delete an entry.\n "
        "For a new entry type 'new', to update a previous entry type 'update' and to delete an entry type 'delete'\n")

if Mode_Selection == 'new':
    new()
elif Mode_Selection == 'update':
    update()
elif Mode_Selection == 'delete':
    delete()

