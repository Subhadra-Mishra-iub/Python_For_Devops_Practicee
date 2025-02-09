#Get pull requests information on a repo using python?

#using Kubernates

#here we will be talking to github through apis.
#So, we will be using the requests module 

#Steps: 
#1. requests(----)
#2. API(----) for pull requests
#3. JSON(----) Dictonary
#4. print(----)

#We dont know the API for the pull requests.
# So, what to do first is to search github api docs in google
# So, there we hav eREST API lists and we need to search what we need.
# Then we find the link in the right
# Then we go to the link and we find the list of all the apis
# Then we find the api for pull requests

#Steps to implement:
#In the terminal, first install the requests module by using the command: pip install requests.
#Then write a python program that will use the API for pull requests.
#So, here is the code:
import requests
#Why am i still getting error?

#url = "api.github.com/repos/kubernetes/kubernetes/pulls"
#list of dictionaries: can check by go to browser and put the url and see the json format
#then doing requests.get(url) will give the same as going to the browser and stuff

response = requests.get("https://api.github.com/repos/kubernetes/kubernetes/pulls")
#print(response.json()) :  This automatically converts to dictonary
#Just say that we just want to have users name

complete_details = response.json()

#Name of the first user who has made a pull request on kubernetes repo:
print(complete_details[0]["user"]["login"])

#Complete Data:
for i in range(len(complete_details)):
    print(complete_details[i]["user"]["login"])

#Now, if we want to have say number of pull requests along with the user name
#Then we can do the following:
