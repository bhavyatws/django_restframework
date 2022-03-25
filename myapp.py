
import json
import requests
'''###Getting Data####
URL='http://127.0.0.1:8000/api/students/'

r = requests.get(url=URL)

data=r.json()

print(data)


#Creating Data
URL='http://127.0.0.1:8000/api/student-create/'
data={
    'id':3,
    'name':'Majnu',
    'roll':12,
    'city':'Khanna'
}
json_data=json.dumps(data)#Converting python native data to json data

r = requests.post(url=URL,data=json_data)
data=r.json()
print(data)

'''
#Getting Student Data by this app
# URL='http://127.0.0.1:8000/api/get-student/'
#Class Based URL for getstudent
# URL='http://127.0.0.1:8000/api/get-student-class-based-view/'
#Using ModelSerializor
# URL='http://127.0.0.1:8000/modelserializor/get-student-class-based-view/'
#using api_view() function based
# URL='http://127.0.0.1:8000/modelserializor/hello-world/'
# URL='http://127.0.0.1:8000/modelserializor/student-api-view/'
URL='http://127.0.0.1:8000/modelserializor/student-api-view-pk/'

def get_data(id=None):
    data={} 
    id=2
    if id is not None:
        data={'id':id} 
    #'detail': 'Unsupported media type "text/plain" in request. error to avoid this write pass headers
    headers={'content-type':'application/json'}
    json_data=json.dumps(data)#Converting python native data to json data
    r = requests.get(url=URL,data=json_data,headers=headers)
    data=r.json()
    print(data)
get_data()
#Add Data
def post_data():
    data={
        
        'name':'Rohit',
        'city':'Chandragiri',
        'roll':13
    }
    #'detail': 'Unsupported media type "text/plain" in request. error to avoid this write pass headers
    headers={'content-type':'application/json'}
    json_data=json.dumps(data)#converting python native to json data
    r=requests.post(url=URL,headers=headers,data=json_data)
    data=r.json()
    print(data)
# post_data()

#Partial Update Data
def partial_update_data():
    data={
        'id':2,
        'name':'Hohit',
        'city':'Rancho',
        
    }
    #'detail': 'Unsupported media type "text/plain" in request. error to avoid this write pass headers
    headers={'content-type':'application/json'}#if we donot pass headers then error come in api_view
    #partial update as roll is not there in data
    json_data=json.dumps(data)#converting python native to json data
    r=requests.put(url=URL,headers=headers,data=json_data)
    data=r.json()
    print(data)
# partial_update_data()

#Complete Update Data
def complete_update_data():
    data={
        'id':4,
        'name':'Rohit',
        'city':'Ranchi',
        'roll':90
        
    }
    #'detail': 'Unsupported media type "text/plain" in request. error to avoid this write pass headers
    headers={'content-type':'application/json'}#if we donot pass headers then error come in api_view
    #complete update as all fields are there
    json_data=json.dumps(data)#converting python native to json data
    r=requests.patch(url=URL,headers=headers,data=json_data)
    data=r.json()
    print(data)
# complete_update_data()

#Delete Data
def delete_data():
    data={
        'id':4,
        }
    #Deleting Data
    json_data=json.dumps(data)#converting python native to json data
    #'detail': 'Unsupported media type "text/plain" in request. error to avoid this write pass headers
    headers={'content-type':'application/json'}
    r=requests.delete(url=URL,data=json_data,headers=headers)
    data=r.json()
    print(data)
# delete_data()
    


