import os.path 
from os import path
import requests
import json

print("---------------- welcome to the saral courses ---------------")


print("\n")
# this is the url where api will hit the request
get_saral_url = "http://saral.navgurukul.org/api/courses"
# print(get_saral_url)
def courses_api(url):
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
	response_text = courses_api(get_saral_url)
	with open("courses.json","w") as file:
		json.dump(response_text,file)
		 # while dumping the data from file in response_text it might change the type string
		dictionary_type = json.loads(response_text)
#  this main list contain the data in dictionary format
courses_list = (dictionary_type['availableCourses'])
# print(type(courses_list))


def courses_name():
	i = 0
	# loop will run in courses list
	while i < len(courses_list):
		cousre_name = courses_list[i]['name']
		courses_id = courses_list[i]['id']
		print(i,"-",cousre_name,courses_id)
		i = i + 1
courses_name()




def courseId():
	id_list = []
	course_name = []
	j = 0
	while j < len(courses_list):
		id_list.append(courses_list[j]['id'])
		course_name.append(courses_list[j]['name'])
		j = j + 1
	user_id = int(input("enter the course id: "))
	# user_id = user_id-1
	course_id = id_list[user_id]
	print("course id is",course_id)
	print(course_name[user_id])


	callApi = "https://saral.navgurukul.org/api/courses" + "/" +str(id_list[user_id])+ "/" + "exercises"


	if path.exists("courses_Exercise/course_"+(str(user_id))+".json"):
		with open("courses_Exercise/course_"+(str(user_id))+".json","r") as data_file:
			readfile = json.load(data_file)	
			dic_type = json.loads(readfile)
	else:
		restext = courses_api(callApi)
		with open("courses_Exercise/course_"+(str(user_id))+".json","w") as filedata:
			json.dump(restext,filedata)
			# while dumping the data from file in response_text it might change the type string
			dic_type = json.loads(restext)
	return dic_type['data']	
id_listdata = courseId()


    
def parentchildExercise(list_data):
	index = 0
	while index < len(list_data):
		parent_Exercise = list_data[index]['name']
		childExerciseslist = list_data[index]['childExercises']
		print(index,parent_Exercise)
		index1 = 0
		while index1 < len(childExerciseslist):
			if "parent_exercise_id" in childExerciseslist[index1]:
				print(5*" ", index1,"-", childExerciseslist[index1]['name'])
			index1 = index1 + 1
		index = index + 1                                                                                                                                                                                                            
parentchildExercise(id_listdata)	





exercise = int(input("enter the exercise "))

slug_api = "http://saral.navgurukul.org/api/courses/" + str(exercise) + "/" + "exercise/getBySlug?slug=requests__using-json"
if path.exists("courseSlug/slug_"+(str(exercise))+".json"):
	with open("courseSlug/slug_"+(str(exercise))+".json","r") as d:
		r_data = json.load(d)	
		dictype = json.loads(r_data)
else:
	r_text = courses_api(slug_api)
	with open("courseSlug/slug_"+(str(exercise))+".json","w") as K:
		json.dump(r_text,K)
		# while dumping the data from file in response_text it might change the type string
		dictype = json.loads(r_text)