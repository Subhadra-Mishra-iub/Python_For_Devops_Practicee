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

url = "https://api.github.com/repos/subhadra-mishra/Python_For_Devops_Practicee/Day 11/real_life_example.py"
response = requests.get(url)
print(response.json())

#Now, we will be using the Kubernates module to deploy our application on kubernetes cluster.
#So, we will be using the kubernetes module.
#So, first we need to install the kubernetes module.
#So, in the terminal, first install the kubernetes module by using the command: pip install kubernetes.
#Then write a python program that will use the kubernetes module.
#So, here is the code:


