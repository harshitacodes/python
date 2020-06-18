import requests
import json ,pprint

print("##########---WELCOME TO SARAL--##############")

url = "http://saral.navgurukul.org/api/courses"



def get_saral_url(link):
	res = requests.get(link)
	return res.text
response_text = get_saral_url(url)



dictionary_data = json.loads(response_text)
coursesList = (dictionary_data['availableCourses'])


def Available_courses():
	courses_index = 0
	while courses_index < len(coursesList):
		cousre_name = coursesList[courses_index]["name"]
		courses_id = coursesList[courses_index]["id"]
		print(courses_index +1,cousre_name,courses_id)
		courses_index = courses_index + 1
Available_courses()


print("\n")
print("#################----------Welcome to the exercise-----------###################")
print("\n")



def available_course_id():
	id_list = []
	course_name = []
	id_index = 0  
	while id_index < len(coursesList):
		id_list.append(coursesList[id_index]['id'])
		course_name.append(coursesList[id_index]['name'])
		id_index = id_index + 1

	user_id = int(input("enter the id no: ")) -1
	
	courseid = id_list[user_id]
	print("your course id is ",courseid)
	print(course_name[user_id])


	secondApi = "https://saral.navgurukul.org/api/courses" + "/" +str(id_list[user_id])+ "/" + "exercises"

	restext = get_saral_url(secondApi)
	dic_data = json.loads(restext)
	return ([dic_data["data"],id_list[user_id]])

idlistdata = available_course_id()
id_listdata = (idlistdata[0])
user_id = (idlistdata[1])




print("\n")


# choice = input("enter the choice for up write'up' and 'down' for down")
# if choice == "up":
# 	print(list_of_courses())
	
def parentchildExercise(list_data):
	parent_index = 0
	while parent_index < len(list_data):
		parent_Exercise = list_data[parent_index]['name']
		childExerciseslist = list_data[parent_index]['childExercises']
		print(parent_index+1,parent_Exercise)
		child_index = 0
		while child_index < len(childExerciseslist):
			if "parent_exercise_id" in childExerciseslist[child_index]:
				print(5*" ", child_index+1,"-", childExerciseslist[child_index]['name'])
			child_index = child_index + 1
		parent_index = parent_index + 1                                                                                                                                                                                                                                             
parentchildExercise(id_listdata )	


print("\n")

exercise = int(input("enter the exercise no: "))-1

print("\n")


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


print("\n")

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

		
	content = int(input("enter the exercise no to get the content: "))-1




	if (child_list[exercise]==[]):
		third_api = "http://saral.navgurukul.org/api/courses/" + str(user_id) + "/" + "exercise/getBySlug?slug=" + str(slug_list[exercise])
		text_content = get_saral_url(third_api)
		dict_type_slug = json.loads(text_content)
		print(dict_type_slug['content'])


	else:
		third_api = "http://saral.navgurukul.org/api/courses/" + str(user_id) + "/" + "exercise/getBySlug?slug=" + str(child_list[exercise][content]["slug"])
		text_content = get_saral_url(third_api)
		dict_type_slug = json.loads(text_content)
		print(dict_type_slug['content'])

	

child_exercise_slug()

