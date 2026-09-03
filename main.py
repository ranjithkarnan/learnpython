# product = { 
#     "name" : "T-shirt",
#     "price": 799,
#     "stock": 20
# }

# product ['category'] = "MensWear"
# product ['stock'] = 15

# print(product["name"])
# print(product["price"])
# print(product["stock"])
# print(product["category"])


# Python Day 2 — Q6: List of Dictionaries ⭐⭐⭐

# students = [
#     {
#         "name": "Ravi",
#         "course": "Python",
#         "score": 85
#     },
#     {
#         "name": "Priya",
#         "course": "RAG",
#         "score": 92
#     },
#     {
#         "name": "Arun",
#         "course": "LLM APIs",
#         "score": 88
#     }
# ]


# print(f"First Student: {students[0] ["name"]}")
# print(f"Second Student: {students[1] ["course"]}")
# print(f"Third Student: {students[2] ["score"]}")
# print(f"Total students : {len(students)}")

# Day 1  & Day 2 Revision

# Q1 — Employee Profile ⭐
# name = str(input("Enter your Name :"))
# age = input("Enter your Age :")
# city = input("Enter your city :")
# profession = input("Enter your Profession:")

# print(f"Name : " + name)
# print(f"age :" +age)
# print(f"city : " +city)
# print(f"profession : " + profession)

# Q2 — Project Cost Calculator ⭐⭐

# development = int(input("Development Cost : "))
# domain = int(input("Domain Cost :"))
# hosting =int(input("Hosting Cost :"))
# monthly_maintenance = int(input("Monthly Maintenance :"))

# intial_project_cost = development + domain + hosting
# anual_maintenance = monthly_maintenance * 12
# total_first_year_cost = intial_project_cost +  anual_maintenance

# print(f"Initial Project Cost : {intial_project_cost}")
# print(f"Annual Maintenance : {anual_maintenance}")
# print(f"Total First Year Cost : {total_first_year_cost}")

# Q3 — GST Product Bill ⭐⭐⭐

# product = str(input("Enter the Product Name :"))
# price = int(input("Enter amount price :"))
# quantity = int(input("Enter the Quantity :"))
# gst_percentage = float(input("Enter the percentage :"))

# subtotal = price * quantity
# gst_amount = subtotal * gst_percentage / 100
# total_amount = subtotal + gst_amount

# print(f"Product: {product}")
# print(f"Subtotal: {subtotal}")
# print(f"GST Amount: {gst_amount}")
# print(f"Total Amount:{total_amount}")

# Q4 — AI Learning Courses ⭐⭐

# courses = [
#     "Python",
#     "LLM APIs",
#     "Embeddings",
#     "Vector DB",
#     "RAG"
# ]

# # Add "LangChain"

# courses.append("Langchain")
# courses["Vector DB"] = "PGVector"
# courses.remove("Embeddings")

# print(f"First Course: {courses[0]}")
# print(f"Third Course: {courses[2]}")
# print(f"Last Course: {courses[4]}")
# print(f"Total Courses:{len(courses)}")

# Q5 — Remove Duplicate Skills ⭐⭐


# skills = [
#     "Python",
#     "React",
#     "Python",
#     "RAG",
#     "React",
#     "PostgreSQL",
#     "RAG"
# ]

# unique_skills =set(skills);
# unique_skills.add("Langchain")
# unique_skills.remove("React")
# print(f"Unique skils : {unique_skills}")
# print(f"total_number of unique skill: {len(unique_skills)}")

# Q6 — AI Course Dictionary ⭐⭐⭐

# course =  { 
#     "course_name" : "Python",
#     "level" : "Beginner",
#     "completed" : "False",
#     "progress" : 60
# }

# print(f"course Name : {course["course_name"]}")
# print(f"progress : {str(course["progress"])}")
# # these are typically wrong, i need to get idea about this.
# print(f"change progress : {str(course[3] [80])}")
# print(f"completeed : {bool(course[2])}")

# course["next_course"] = "LLM Apis"
# print(f"complete_courses : {course}")

# Q7 — Customer Product Dictionary ⭐⭐⭐

# product = {
#     "name": "Running Shoes",
#     "price": 2499,
#     "stock": 25
# }

# # i have doubt here also.
# print(f"Product Name : {product[0]}")
# print(f"Product Price : {product[1]}")

# product.add({ 
#     "catergory": "Footwear",
#     "available": True
# })

# print(product)


# Q8 — List of Dictionaries ⭐⭐⭐⭐

# courses = [
#     {
#         "name": "Python",
#         "duration": 30,
#         "completed": True
#     },
#     {
#         "name": "LLM APIs",
#         "duration": 15,
#         "completed": False
#     },
#     {
#         "name": "RAG",
#         "duration": 25,
#         "completed": False
#     }
# ]

# print(f"First Course : {courses[0]["name"]}")
# print(f"Second Course Duration:{str(courses[1]["duration"])}")
# print(f"RAG Completed:{bool(courses[2] ["completed"])}")
# print(f"Total Courses:{len(courses)}")

# how to change dictionary values

# RAG completed False → True


# Final Revision Challenge — AI Learning Tracker ⭐⭐⭐⭐⭐

# learning = {
#     "student": "Ranjith",
#     "current_course": "Python",
#     "completed_courses": ["Claude 101", "Python Day 1"],
#     "skills": {"HTML", "CSS", "JavaScript", "Python"}
# }

# # 1.Print student name
# print(f"Student Name :{learning["student"]}")
# print(f"current course : {learning['current_course']}")
# # print(f"first_completed course : {learning[2]["completed_course"]}")

# # 4. Add "Python Day 2" to completed_courses
# # I have no idea how to do this

# # 5. Add "RAG" to skills
# learning["skills"] = "RAG"

# # Remove "CSS" from skills
# # I have no idea how to do this

# # 7. Change current_course from "Python" → "LLM APIs"
# # I have no idea how to do this

# # 8. Print total completed courses
# print(f"completed course: {len(learning)}")

# # Print total skills
# print(f"total skills : {learning[len("skills")]}")

# # 10. Print the complete learning dictionary
# print(learning)


# learning = {
#     "student": "Ranjith",
#     "current_course": "Python",
#     "completed_courses": ["Claude 101", "Python Day 1"],
#     "skills": {"HTML", "CSS", "JavaScript", "Python"}
# }

# # Print student name.
# print(f"Student Name : {learning['student']}")

# # Print current course.
# print(f"Current Course : {learning['current_course']}")

# # Print first completed course.
# print(f"firstCompletedcourse: {learning['completed_courses'][0]}")

# # Add "Python Day 2" to completed_courses
# print(f"Python Day 2 to completed_courses : {learning["completed_courses"].append("python day 2")}")

# # Add "RAG" to skills.
# print(f"adding rag to skills: { learning['skills'].add["RAG"]}")

# # Remove "CSS" from skills.
# print(f"Remove CSS from skills : {learning['skills'].remove [1]}")

# # Change current_course to "LLM APIs".
# print(f"remove current_course : {learning['current_course'] = 'LLM Api'}")

# # Print the total completed courses.
# print(f"total completed course : {len(learning['completed_courses'])}")

# # Print the total skills.
# print(f"printtotalskills : {len(learning['skills'])}")

# # Print learning.
# print(f"total learning : {len(learning)}")



# Revision Challenge — Developer Learning Tracker ⭐⭐⭐⭐

# developer = {
#     "name": "Arun",
#     "current_skill": "Python",
#     "completed_topics": ["Variables", "Lists"],
#     "technologies": {"HTML", "CSS", "JavaScript"}
# }

# # Print the developer's name.
# print(f"developerName : {developer['name']}")

# # Print the current skill.
# print(f"current_skill : {developer['current_skill']}")

# # Print the first completed topic.
# print(f"firstcompletedtask : {developer['completed_topics'][0]}")

# # Add "Dictionaries" to completed_topics.
# developer["completed_topics"].append("Dictionaries")

# developer["technologies"].add("Python")

# developer["technologies"].remove("CSS")

# developer["current_skill"] = "LLM APIs"

# print(f"total number completed topics : {len(developer['completed_topics'])}")

# print(f"total number skills : {len(developer['technologies'])}")

# print(developer)


      


# # Real-World Interview Scenario — Employee Training Tracker ⭐⭐⭐⭐

# employee = {
#     "employee_name": "Karthik",
#     "department": "QA",
#     "current_training": "Python",
#     "completed_trainings": ["Manual Testing", "API Testing"],
#     "technical_skills": {"Postman", "SQL", "Jira", "Python"}
# }

# # Print the employee name.
# print(f"EmployeeName : {employee['employee_name']}")

# # Print the department.
# print(f"department : {employee['department']}")

# # Print the second completed training.

# print(f"second_completed_training : {employee['completed_trainings'][1]}")

# # Add "Python Basics" to completed_trainings.

# employee["completed_trainings"].append("Python Basics")

# # Add "Git" to technical_skills.

# employee["technical_skills"].add("Git")

# # Remove "Jira" from technical_skills.

# employee["technical_skills"].remove("Jira")

# # Change current_training from "Python" to "LLM APIs".

# employee["current_training"] = "LLM APIs"

# # Print the updated current training.

# print(f"current_training_updated : {employee['current_training']}")

# # Print the total number of completed trainings.
# print(f"total_completed_trainings : {len(employee['completed_trainings'])}")

# # Print the total number of technical skills
# print(f"total_technical_skills : {len(employee['technical_skills'])}")

# # Print the complete updated employee dictionary.

# print(employee)




# Next Stage:

# Q7 — for Loop ⭐⭐⭐

# courses = ["Python", "LLM APIs", "Embeddings", "RAG"]

# for course in courses:
#     print(f"course:{course}")

# print("all courses are displyed")


# Q7 — Your First Practice

# skills = [
#     "Python",
#     "JavaScript",
#     "React",
#     "PostgreSQL",
#     "RAG"
# ]

# # Task 1 Using one for loop, print:

# for skill in skills:
#     print(f"skill:{skill}")
# print(f"total skills: {len(skills)}")


# Q7 Practice 2 — Customer Orders ⭐⭐
# 

# orders = [
#     "T-Shirt",
#     "Jeans",
#     "Shoes",
#     "Jacket",
#     "Watch"
# ]

# for order in orders:
#     print(f"Ordered Product : {order}")

# print(f"total number of order : {len(orders)}")



# loop with calculation challange

# prices = [799, 1299, 2499, 999]

# total = 0

# for price in prices:
    
#     print(f"procuct price : {price}")
#     total = total + price
    
# print(f"Total Bill: {total}")



# 🧑‍💻 Interview Scenario — Monthly Business Expenses ⭐⭐⭐⭐

# expenses = [
#     1500,
#     2500,
#     799,
#     1200,
#     3500
# ]

# total = 0

# for expense in expenses:
#     print(f"Expense Amount: {expense}")
#     total = expense + total

# print(f"Total number of transaction : {len(expenses)}")
# print(f"total amount : {total}")


# sales = [
#     1200,
#     850,
#     2300,
#     1500,
#     950
# ]

# total = 0

# for sale in sales:
#     print(f"Sale Amount: {sale}")
#     total = sale + total

# print(f"total number of sale: {len(sales)}")

# print(f"total sale :{total}")