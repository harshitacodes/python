import requests
import json
print("##########---WELCOME TO SARAL--##############")

url = "http://saral.navgurukul.org/api/courses"



def get_saral_url(link):
	res = requests.get(link)
	return res.text
response_text = get_saral_url(url)


with open("coursesExersise.json","w") as file:
		json.dump(response_text,file)
		dictionary_type = json.loads(response_text)
coursesList = (dictionary_type['availableCourses'])


def list_of_courses():
	i = 0
	while i < len(coursesList):
		cousre_name = coursesList[i]["name"]
		courses_id = coursesList[i]["id"]
		print(i,cousre_name,courses_id)
		i = i + 1
list_of_courses()

print("\n")
print("#################----------Welcom to the exercise-----------###################")
print("\n")


def saral_course_id():
	id_list = []
	course_name = []
	j = 0  
	while j < len(coursesList):
		id_list.append(coursesList[j]['id'])
		course_name.append(coursesList[j]['name'])
		j = j + 1
	user_id = int(input("enter the id no: "))
	courseid = id_list[user_id]
	print("your course id is ",courseid)
	print(course_name[user_id])
	callApi = "https://saral.navgurukul.org/api/courses" + "/" +str(id_list[user_id])+ "/" + "exercises"
	restext = get_saral_url(callApi)
	with open("courses_Exercise/course_"+(str(user_id))+".json","w") as filedata:
		json.dump(restext,filedata)
		dic_type = json.loads(restext)
	return (dic_type["data"])
id_listdata = saral_course_id()


def parentchildExercise(list_data):
	parent_index = 0
	while parent_index < len(list_data):
		parent_Exercise = list_data[parent_index]['name']
		childExerciseslist = list_data[parent_index]['childExercises']
		child_slug = list_data[parent_index]['slug']
		print(parent_index,parent_Exercise)
		child_index = 0
		while child_index < len(childExerciseslist):
			if "parent_exercise_id" in childExerciseslist[child_index]:
				print(5*" ", child_index,"-", childExerciseslist[child_index]['name'])
			child_index = child_index + 1
		parent_index = parent_index + 1                                                                                                                                                                                                                                             
parentchildExercise(id_listdata )	

exercise = int(input("enter the exercise no"))

	














