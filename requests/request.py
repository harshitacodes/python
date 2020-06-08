import os.path 
from os import path
import requests
import json
print("##########---WELCOME TO SARAL COURSES---##############")

url = "http://saral.navgurukul.org/api/courses"

def get_saral_url(link):
	res = requests.get(link)
	return res.text


exists = path.exists("/home/Documents/python/requests/files.json")
if exists:
	with open("files.json") as f:
		var=json.load(f)
		
else:
	res_text = get_saral_url(url)
	# r=requests.get("http://saral.navgurukul.org/api/courses")
	# a=r.text
	with open("files.json","w+") as f:
		var = json.loads(res_text)
		f.write(json.dumps(var, sort_keys=True, indent=4))
		var=json.loads(res_text)
		

def list_of_courses():
	i = 0
	# loop will run in courses list
	while i < len(var["availableCourses"]):
		cousre_name = var["availableCourses"][i]["name"]
		courses_id = var["availableCourses"][i]["id"]
		print(i,cousre_name,courses_id)
		i = i + 1
list_of_courses()

def course_id():
	id_list = []
	course_name = []
	j = 0  
	while j < len(var["availableCourses"]):
	# for j in courses_list:
		id_list.append(var["availableCourses"][j]['id'])
		course_name.append(var["availableCourses"][j]['name'])
		# id_list.append([j]['id'])
		j = j + 1
	user_id = int(input("enter the id: "))
	courseid = id_list[user_id]
	# print(courseid)
	print(course_name[user_id])
	callApi = get_saral_url("https://saral.navgurukul.org/api/courses" + "/" +str(id_list[user_id])+ "/" + "exercises")
	dict_type = json.loads(callApi)
	# print(type(callApi))
	
	return (dict_type["data"])

id_listdata = course_id()

def parentchildExercise(list_data):

	index = 0
	while index < len(list_data):
		parent_Exercise = list_data[index]['name']
		childExerciseslist = list_data[index]['childExercises']
		
		# print(childExerciseslist)
		print(index,parent_Exercise)
		index1 = 0
		while index1 < len(childExerciseslist):
			if "parent_exercise_id" in childExerciseslist[index1]:
				print(5*" ", index1,"-", childExerciseslist[index1]['name'])
			index1 = index1 + 1
		index = index + 1                                                                                                                                                                                                                                             
parentchildExercise(id_listdata )	

choice = input("enter the 'up' if you want again all exercises or 'exercise no 'to get the exercise content:")
if choice == "up":
	print(list_of_courses())
else:
	print(parentchildExercise(id_listdata))

	




# 	i = 0
# 	# loop will run in courses list
# 	while i < len(courses_list):
# 		cousre_name = courses_list[i]['name']
# 		courses_id = courses_list[i]['id']
# 		print(i,cousre_name,courses_id)
# 		i = i + 1
# courses_name()



# url = "http://saral.navgurukul.org/api/courses"
# # print(url)
# def course(link):
# 	res = requests.get(link)
# 	# response_type = res.text
# 	# pprint(response_type)
# 	print(res.text)
# course(url)

# url2 = url + "/" + "courses"
# full_couses = course(url2)
# pprint(url2)
# print("---------------- welcome to the saral courses ---------------")


# print("\n")
# # this is the url where api will hit the request
# get_saral_url = "http://saral.navgurukul.org/api/courses"
# print(get_saral_url)
# def request_api(url):
# 	response = requests.get(url)
# 	return(response.text)


# if path.exists("courses.json"):
# 	with open("courses.json","r") as data:
# 		# print(type(data)) 
# 		# coverting the data into string from _io.TextIoWrapper
# 		read_file = json.load(data)
# 		# data is converting from string to dictionary  
# 		dictionary_type = json.loads(read_file)
# else:
# 	response_text = request_api(get_saral_url)
# 	with open("courses.json","w") as file:
# 		json.dump(response_text,file)
# 		 # while dumping the data from file in response_text it might change the type string
# 		dictionary_type = json.loads(response_text)
# #  this main list contain the data in dictionary format
# courses_list = ((dictionary_type['availableCourses']))
# print(type(courses_list))


# def courses_name():
# 	i = 0
# 	# loop will run in courses list
# 	while i < len(courses_list):
# 		cousre_name = courses_list[i]['name']
# 		courses_id = courses_list[i]['id']
# 		print(i,cousre_name,courses_id)
# 		i = i + 1
# courses_name()

# id_list = [] #taking the whole id of courses
# def courses_id():
# 	j = 0
# 	while j < len(courses_list):
# 	# for j in courses_list:
# 		id_list.append(courses_list[j]['id'])
# 		# id_list.append([j]['id'])
# 		j = j + 1
# 	return id_list
# 	# user_id = int(input("enter the id: "))
# 	# if user_id == id_list[j]:
# 	# 	# print(id_list[1])
# 	# 	print(courses_list[j]['name'])
# 	# 	# print(courses_name())	
# courses_id()
# for i in courses_list:
# 	# data will access by key
# 	# print ("{0}.   {1}".format(str(counter),i['name'],i['id']))
# 	print(i['name'],i['id'])