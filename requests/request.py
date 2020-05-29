import requests,json
from os import path


print("---------------- welcome to the saral courses ---------------")


print("\n")
# this is the url where api will hit the request
saral_url = "http://saral.navgurukul.org/api/courses"
def request_api(url):
	response = requests.get(url)
	return(response.text)


if path.exists("courses.json"):
	with open("courses.json","r") as data:
		# print(type(data)) 
		# coverting the data into string from _io.TextIoWrapper
		read_file = json.load(data)
		# data is converting from string to dictionary  
		dictionary_type = json.loads(read_file)
else:
	response_text = request_api(saral_url)
	with open("courses.json","w") as file:
		json.dump(response_text,file)
		 # while dumping the data from file in response_text it might change the type string
		dictionary_type = json.loads(response_text)


#  this main list contain the data in dictionary format
courses_list = ((dictionary_type['availableCourses']))
# loop will run in courses list
counter = 1
for i in courses_list:
	# data will access by key
	print ("{0}.   {1}".format(str(counter),i['name']))
	counter = counter + 1
