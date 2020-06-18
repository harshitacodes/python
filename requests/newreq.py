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
	course_id = id_list[user_id]
	print("course id is",course_id)
	print(course_name[user_id])


	callApi = "https://saral.navgurukul.org/api/courses" + "/" +str(id_list[user_id])+ "/" + "exercises"


	if path.exists("coExercise/course"+(str(user_id))+".json"):
		with open("coExercise/course"+(str(user_id))+".json","r") as data_file:
			readfile = json.load(data_file)	
			dic_type = json.loads(readfile)
	else:
		restext = courses_api(callApi)
		with open("coExercise/course"+(str(user_id))+".json","w") as filedata:
			json.dump(restext,filedata)                        
			dic_type = json.loads(restext)
	return ([dic_type['data'],id_list[user_id]])


idlistdata = courseId()
id_listdata = (idlistdata[0])
user_id = (idlistdata[1])

    
def parentchildExercise():
	index = 0
	while index < len(id_listdata):
		parent_Exercise = id_listdata[index]['name']
		childExerciseslist = id_listdata[index]['childExercises']
		print(index,parent_Exercise)
		index1 = 0
		while index1 < len(childExerciseslist):
			if "parent_exercise_id" in childExerciseslist[index1]:
				print(5*" ", index1,"-", childExerciseslist[index1]['name'])
			index1 = index1 + 1
		index = index + 1                                                                                                                                                                                                            
parentchildExercise()	



exercise = int(input("enter the exercise no: "))


def id_single_data():
	exercise_index = 0
	while exercise_index < len(id_listdata):
		parent_Exercise = id_listdata [exercise]['name']
		childExerciseslist = id_listdata [exercise]['childExercises']
		print(exercise_index,parent_Exercise)
		child_index2 = 0
		while child_index2 < len(childExerciseslist):
			if "parent_exercise_id" in childExerciseslist[child_index2]:
				print(5*" ",child_index2+1,"-", childExerciseslist[child_index2]['name'])
			child_index2 = child_index2 + 1
		break
		exercise_index = exercise_index + 1
id_single_data()


def child_exercise_slug():
	slug_list = []
	child_list =[]
	parent_slug_index = 0
	while parent_slug_index < len(id_listdata):
		childExerciseslist = id_listdata[parent_slug_index]['childExercises']
		child_slug = id_listdata[parent_slug_index]['slug']
		child_list.append(childExerciseslist)
		slug_list.append(child_slug)
		parent_slug_index = parent_slug_index + 1
	content = int(input("enter the exercise no to get the content: "))
	
	if (child_list[exercise]==[]):
		third_api = "http://saral.navgurukul.org/api/courses/" + str(user_id) + "/" + "exercise/getBySlug?slug=" + str(slug_list[exercise])
	else:
		third_api = "http://saral.navgurukul.org/api/courses/" + str(user_id) + "/" + "exercise/getBySlug?slug=" + str(child_list[exercise][content]["slug"])
	text_content = courses_api(third_api)
	# path = "slugdata/childslug_"+ str(child_list[exercise][content]["slug"])
	# os.mkdir(path)
	# print(os.getcwd())
	# path = ""

	os.mkdir("slugdata/childslug_" + str(slug_list[content]))

	with open("childSlug/child_"+ str(slug_list[content])+".json","w") as p:
		json.dump(text_content,p)
		d_type = json.loads(text_content)
	# print(d_type['slug'])
	print(d_type['content'])
	
child_exercise_slug()






# slug_api = "http://saral.navgurukul.org/api/courses/" + str(exercise) + "/" + "exercise/getBySlug?slug=requests__using-json"
# if path.exists("courseSlug/slug_"+(str(exercise))+".json"):
# 	with open("courseSlug/slug_"+(str(exercise))+".json","r") as d:
# 		r_data = json.load(d)	
# 		dictype = json.loads(r_data)
# else:
# 	r_text = courses_api(slug_api)
# 	with open("courseSlug/slug_"+(str(exercise))+".json","w") as K:
# 		json.dump(r_text,K)
# 		# while dumping the data from file in response_text it might change the type string
# 		dictype = json.loads(r_text)