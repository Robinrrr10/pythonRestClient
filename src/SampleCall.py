import requests

print("Goodbye, World!")
class SampleRestClient():
    def makeGetCall(self):
        print("Making GET Rest call")
        urlwithpath = "https://reqres.in/api/user/1"
        print("Trying to hit with url:", urlwithpath)
        response = requests.get(url = urlwithpath)
        print("Body is:", response.content)
        print("body 2 is", response.text)
        responseJson = response.json()
        print("Response is:", responseJson)
        print("name is", responseJson['data']['name'])
        
    def makePostCall(self):
        print("Making POST Rest call")
        urlwithpath = "https://reqres.in/api/users"
        requestBody = {"name": "morpheus333","job": "leader"}
        response = requests.post(url = urlwithpath, data = requestBody)
        print("Body is:", response.content)
        print("body 2 is", response.text)
        responseJson = response.json()
        print("Response is:", responseJson)
        print("new id is", responseJson['id'])
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            

client = SampleRestClient()
client.makeGetCall()
client.makePostCall()
   