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


# Recall Question 1 — Variables + Input 🟢

# Real-world scenario: Employee Registration

# employee_name = input("Employee Name :")
# job_role = input("Job Role :")
# experiance = int(input("Year of Experience :"))

# print(employee_name)
# print(job_role)
# print(experiance)


# project_name = input("Project Name : ")
# hours = int(input("Number of Hours : "))
# cost_hour = int(input("Cost per Hour :"))

# total_cost = hours * cost_hour

# print(f"project :{ project_name}")
# print(f"Total Hours : {hours}")
# print(f"total Cost : ${total_cost}")

# # Recall Question 3 — Percentage Calculation 🟡

# current_salary = int(input("Enter the current Salary :"))
# percentage = int(input("Enter the percentage :"))

# increment_amount = current_salary * percentage / 100

# new_salary = current_salary + increment_amount

# print(f"Current Salary : ${current_salary}")
# print(f"increment Amount : ${increment_amount}")
# print(f"new Salary : ${new_salary}")


# skills = ["Python", "SQL", "Postman", "Jira"]

# print(f"first Skill : {skills[0]}")
# print(f"last skill : {skills[-1]}")
# skills.append("git")
# print(skills)
# skills.remove("Jira")
# print(skills)
# skills[2] = "API Testing"
# print(skills)
# print(f"total skils : {len(skills)}")
# print(f"final skilss are : {skills}")


# Recall Question 5 — Sets 🟡

# technologies = {"Python", "PostgreSQL", "React", "Jira"}

# technologies.add("Git")
# print(technologies)
# technologies.add("Python")
# technologies.remove("Jira")
# print(technologies)
# print(f"total number of tech : {len(technologies)}")
# print(technologies)

# Recall Question 6 — Dictionary 🟡

# employee = {
#     "name": "Arun",
#     "role": "QA Engineer",
#     "experience": 3,
#     "location": "Chennai"
# }

# print(f"Employee name : {employee['name']}")
# print(f"Employee role : {employee['role']}")
# employee["experience"] = "4"
# print(f"Employee experience : {employee['experience']}")
# employee["skill"] = "Python"
# print(employee)
# employee["role"] = "AI QA Engineer"
# print(employee)

# Recall Question 7 — Nested Dictionary + List 🟠

# student = {
#     "name": "Ravi",
#     "current_course": "Python",
#     "completed_courses": ["Manual Testing", "API Testing"],
#     "skills": {"Postman", "SQL", "Jira"}
# }

# print(f"Student Name : {student['name']}")
# print(f"first completed course : {student['completed_courses'][0]}")
# student["completed_courses"].append("python basics")
# student["skills"].add("Git")
# student["skills"].remove("Jira")
# student["current_course"] = "LLM API's"
# print(f"number of completed course : {len(student['completed_courses'])}")
# print(f"number of skills : {len(student['skills'])}")
# print(student)


# Recall Question 8 — Basic for Loop + len()

# models = [
#     "GPT",
#     "Claude",
#     "Gemini",
#     "Llama"
# ]

# for model in models :
#     print(f"Testing Model {model}")
# print(f"total models :{len(models)}")

# Recall Question 9 — Loop + Accumulator 🟡

# token_usage = [
#     1200,
#     850,
#     1500,
#     950
# ]

# total = 0
# for token in token_usage :
#     print(f"Tokens Used : {token}")
#     total = total + token

# print(f"total token :{len(token_usage)}")

# print(f"token used : {total}")

# Recall Question 10 — Loop + List of Dictionaries 🟠

# test_results = [
#     {
#         "test_name": "Login Test",
#         "status": "Passed",
#         "execution_time": 5
#     },
#     {
#         "test_name": "API Test",
#         "status": "Passed",
#         "execution_time": 8
#     },
#     {
#         "test_name": "Payment Test",
#         "status": "Failed",
#         "execution_time": 12
#     }
# ]

# total = 0 
# test_time = 0
# for test_result in test_results:
#     print(f"test_name : {test_result}")
# print(test_results)

# test_results = [
#     {"test_name": "Login Test", "status": "Passed", "execution_time": 5},
#     {"test_name": "API Test", "status": "Passed", "execution_time": 8},
#     {"test_name": "Payment Test", "status": "Failed", "execution_time": 12}
# ]

# total =0

# for test in test_results:
#     print(f"test name : {test["test_name"]}")
#     print(f"status : {test["status"]}")
#     print(f"execution time : {test["execution_time"]}")
#     total = total + test["execution_time"]
# print(f"total test : {len(test_results)}")
# print(f"total execution time : {total}")


# Recall Question 12 — Inside or Outside the Loop?

# response_times = [2, 4, 3, 6, 5]

# total = 0

# for response in response_times:
#     print(f"Response Time: {response} seconds")
#     total = total + response
#     avg_response = total / len(response_times)
# print(f"Total Tests : {len(response_times)} ")
# print(f"Total Response Time: {total} seconds")
# print(f"Average Response Time: {avg_response} seconds")


# Day 3 — Question 1

# score = int(input("Enter your Score : "))


# if score >= 50:
#     print(f"your test is passed and the score is {score}")
# else:
#     print(f"your test is failed and the score is {score}")

# print(score)


# Day 3 — Question 2: QA Bug Check

# Bugs = int(input("Enter the number of bugs :"))

# if Bugs == 0:
#     print(f"No Bugs found - Testing passed")
# else:
#     print("Bugs found - Testing Failed")


# score = int(input("Enter your score : "))

# if score >= 80:
#     print(f"Your Score {score} - its Execellent")
# elif score >=50:
#     print(f"Your Score {score} - its Passed")
# else:
#     print(f"your score {score} - its failed")


# Day 3 — Question 4: Condition Order


# score = int(input("Enter severity score: "))

# if score >= 8: 
#     print("its Critical")
# elif score >= 5:
#     print("its Major")
# elif score >= 1:
#     print("its minor")
# else: 
#     print("no bugs")

# Day 3 — Question 5: One step harder

# api_response = int(input("Enter API response code: "))

# if api_response == 200:
#     print("Test Passed")
# elif api_response == 400:
#     print("Bad request")
# elif api_response == 401:
#     print("unathurized")
# elif api_response == 404:
#     print("not found")
# elif api_response == 500:
#     print("unexpected response")
# else:
#     print("not valid response")


# Day 3 — Question 6: API Performance Check


# response = int(input("Enter API response time (ms): "))

# if response < 500:
#     print("Excellent Performance")
# elif response >=500 and response <=1000:
#     print("Acceptable Performance")
# else:
#     print("Slow Performance")


# Day 3 — Question 7: Practice !=

# status = int(input("Enter actual status code:"))

# if status == 200:
#     print("its acceptable response received")
# if status != 200:
#     print("its not acceptable response received")


# Day 3 — Question 8: < and <=

# tests = int(input("Enter number of failed tests:"))

# if tests ==0:
#     print("Test passed")
# elif tests >=1 and tests <=3:
#     print("test with warining")
# else:
#     print("test failed")


# Day 3 topic: Logical Operators.

# Day 3 — Question 9: Practice and



# username = input("Enter username:")
# password = input("Enter password:")

# if username =="admin" and password == "python123":
#     print("Login Successful")
# else:
#     print("Login Failed")


# Day 3 — Question 10: One more and practice


# passed_test = int(input("Enter number of passed tests:"))
# critical_bug = int(input("Enter number of critical bugs:"))

# if passed_test >=95 and critical_bug ==0:
#     print("Ready for Release")
# else:
#     print(" Not Ready for Release")


# Day 3 — Question 11: Practice or

# failed_testcases = int(input("Enter number of failed tests:"))
# critical_bugs = int(input("Enter number of critical bugs:"))

# if failed_testcases > 5 or critical_bugs > 0 :
#     print("Needs Investigation")
# else:
#     print("Build looks stable")

# One more or practice — Question 12

# role = input("Enter your role:")

# if role=="admin" or role=="manager":
#     print("Access Granted")
# else:
#     print("Access Denied")


# Next: Logical operator not
# Day 3 — Question 13: Practice not


# system_online = True

# if not system_online:
#     print("System is offline")
# else:
#     print("System is online")


# Day 3 — Question 14: Combine what you've learned


# test_passed = True
# critical_bugs = 0
# environment_unavailable = False

# if not environment_unavailable and test_passed == True and critical_bugs ==0:
#     print("Ready for deployemnent")

# else:
#     print("not ready for deployement")


# # Next: for loop + if/else

# test_statuses = ["Passed", "Failed", "Passed", "Passed", "Failed"]

# for test_status in test_statuses:
#     if test_status == "Passed":
#         print("Test Passed")
#     else:
#         print("Test Failed")


# # Next — Question 15: Count Passed Tests

# test_statuses = ["Passed", "Failed", "Passed", "Passed", "Failed"]

# passed_count = 0
# for teststatus in test_statuses:
#     if teststatus == "Passed":
#         print("Test Passed")
#         passed_count = passed_count + 1
#     else:
#         print("Test Failed")
    

# print(f"total status {len(test_statuses)}")
# print(f"total passed status {passed_count}")


# # Question 16 — Counter Practice

# test_results = ["Passed", "Failed", "Failed", "Passed", "Failed", "Passed"]

# failedtest = 0
# for testresult in test_results:
#     if testresult == "Failed":
#         print(testresult)
#         failedtest = failedtest + 1
#     else:
#         print(testresult)

# print(f"Total test status {len(test_results)}")
# print(f"Total failed status {failedtest}")


# # Question 17 — Two Counters

# test_results = ["Passed", "Failed", "Passed", "Passed", "Failed", "Failed", "Passed"]

# passed_result = 0
# failed_result = 0
# for test_result in test_results:
#     if test_result == "Passed":
#         print(test_result)
#         passed_result = passed_result +1
#     else:
#         print(test_result)
#         failed_result = failed_result +1


# print(f"Total test result :{len(test_results)}")
# print(f"Total Passed result : {passed_result}")
# print(f"Total failed result : {failed_result}")


# Question 18 — List of Dictionaries + Conditions + Counters

# test_results = [
#     {"test_name": "Login Test", "status": "Passed"},
#     {"test_name": "API Test", "status": "Failed"},
#     {"test_name": "Payment Test", "status": "Passed"},
#     {"test_name": "Profile Test", "status": "Failed"},
#     {"test_name": "Logout Test", "status": "Passed"}
# ]
# passed_test = 0
# failed_test = 0

# for test_result in test_results:
#     if test_result["status"]== "Passed":
#         print(f"{test_result['test_name']} - {test_result['status']}")
#         passed_test = passed_test + 1
#     else:
#         print(f"{test_result['test_name']} - {test_result['status']}")
#         failed_test = failed_test + 1
# print(f"Total Test result :{len(test_results)}")
# print(f"total test passed :{passed_test}")
# print(f"total test failed :{failed_test}")


# # Question 19 — Same concept, different scenario

# employees = [
#     {"name": "Arun", "status": "Active"},
#     {"name": "Priya", "status": "Inactive"},
#     {"name": "Karthik", "status": "Active"},
#     {"name": "Divya", "status": "Active"},
#     {"name": "Vijay", "status": "Inactive"}
# ]

# active_count = 0
# inactive_count = 0

# for employee in employees:
#     if employee['status'] == "Active":
#         print(f"{employee['name']} -{employee['status']}")
#         active_count = active_count + 1
#     else:
#         print(f"{employee['name']} - {employee['status']}")
#         inactive_count = inactive_count + 1

# print(f"Total Employees {len(employees)}")
# print(f"Active Employee : {active_count}")
# print(f"Inactive Employee : {inactive_count}")


# # Question 20 — Add elif

# employees = [
#     {"name": "Arun", "status": "Active"},
#     {"name": "Priya", "status": "Inactive"},
#     {"name": "Karthik", "status": "On Leave"},
#     {"name": "Divya", "status": "Active"},
#     {"name": "Vijay", "status": "On Leave"}
# ]

# active_employee = 0
# inactive_employee = 0
# on_leave_employee = 0

# for employee in employees:
#     if employee["status"] == "Active":
#         print(f"{employee['name']} - {employee['status']}")
#         active_employee = active_employee + 1
#     elif employee["status"] == "On Leave":
#         print(f"{employee['name']} - {employee['status']}")
#         on_leave_employee = on_leave_employee + 1
#     else:
#         print(f"{employee['name']} - {employee['status']}")
#         inactive_employee = inactive_employee + 1

# print(f"Total Employees : {len(employees)}")
# print(f"Total active Employee {active_employee}")
# print(f"total on leave employee {on_leave_employee}")
# print(f"total inactive employees {inactive_employee}")


# Question 21 — One more real QA scenario

# bugs = [
#     {"bug": "Login crash", "severity": "Critical"},
#     {"bug": "Button color", "severity": "Minor"},
#     {"bug": "Payment failure", "severity": "Critical"},
#     {"bug": "Profile issue", "severity": "Major"},
#     {"bug": "Font alignment", "severity": "Minor"},
#     {"bug": "API timeout", "severity": "Major"}
# ]

# for_critical = 0
# for_major = 0
# for_minor = 0

# for issue in bugs:
#     if issue["severity"] == "Critical":
#         print(f"{issue['bug']} - {issue['severity']}")
#         for_critical = for_critical + 1
#     elif issue["severity"] == "Major":
#         print(f"{issue['bug']} - {issue['severity']}")
#         for_major = for_major + 1
#     else:
#         print(f"{issue['bug']} - {issue['severity']}")
#         for_minor = for_minor + 1

# print(f"Total Bugs : {len(bugs)}")
# print(f"Total Cirtical Bug : {for_critical}")
# print(f"Total Major Bugs :{for_major}")
# print(f"Total Minor Bugs : {for_minor}")


# Question 22 — and Inside a Loop

# test_results = [
#     {"test_name": "Login Test", "status": "Passed", "execution_time": 3},
#     {"test_name": "API Test", "status": "Passed", "execution_time": 8},
#     {"test_name": "Payment Test", "status": "Failed", "execution_time": 4},
#     {"test_name": "Profile Test", "status": "Passed", "execution_time": 5},
#     {"test_name": "Logout Test", "status": "Failed", "execution_time": 2}
# ]


# for test_result in test_results:
#     if test_result["status"] == "Passed" and test_result["execution_time"] <= 5:
#         print(f"{test_result['test_name']} - Good")
#     else:
#         print(f"{test_result['test_name']} - Needs Review")


# Question 23 — or Inside a Loop

# test_results = [
#     {"test_name": "Login Test", "status": "Passed", "critical_bug": 0},
#     {"test_name": "API Test", "status": "Failed", "critical_bug": 0},
#     {"test_name": "Payment Test", "status": "Passed", "critical_bug": 1},
#     {"test_name": "Profile Test", "status": "Passed", "critical_bug": 0},
#     {"test_name": "Logout Test", "status": "Failed", "critical_bug": 2}
# ]

# for test_result in test_results:
#     if test_result["status"] == "Failed" or test_result["critical_bug"] > 0:
#         print(f"{test_result['test_name']} - Need Investigation")
#     else:
#         print(f"{test_result['test_name']} - Test Looks Good")


# # Question 24 — Combine and + or

# builds = [
#     {"build": "Build-101", "passed": 98, "critical_bugs": 0, "environment_ready": True},
#     {"build": "Build-102", "passed": 92, "critical_bugs": 0, "environment_ready": True},
#     {"build": "Build-103", "passed": 99, "critical_bugs": 1, "environment_ready": True},
#     {"build": "Build-104", "passed": 97, "critical_bugs": 0, "environment_ready": False}
# ]

# for test_build in builds:
#     if test_build["passed"] >= 95 and test_build["critical_bugs"] == 0 and test_build["environment_ready"] == True:
#         print(f"{test_build['build']} - Ready for Release")
#     else:
#         print(f"{test_build['build']} - Not ready for Release")


# Question 25 — Actual and + or Combination

# test_runs = [
#     {"test": "Login", "status": "Passed", "execution_time": 3, "critical_bug": 0},
#     {"test": "Payment", "status": "Passed", "execution_time": 9, "critical_bug": 0},
#     {"test": "API", "status": "Failed", "execution_time": 4, "critical_bug": 1},
#     {"test": "Profile", "status": "Failed", "execution_time": 3, "critical_bug": 0},
#     {"test": "Logout", "status": "Passed", "execution_time": 4, "critical_bug": 0}
# ]


# for test_run in test_runs:
#     if test_run["status"] != "Passed" and test_run['execution_time'] <= 5 or test_run['critical_bug'] > 0:
#         print(f"{test_run['test']} - Needs Attention")
#     else:
#         print(f"{test_run['test']} - Test looks good")

# for test_run in test_runs:
#     if test_run["status"] == "Failed" or (test_run["execution_time"] > 5 and test_run["critical_bug"] > 0):
#         print(f"{test_run['test']} - Needs Attentions")
#     else:
#         print(f"{test_run['test']} - test looks good")


# Question 26 — not Inside a Loop

# environments = [
#     {"name": "QA Server", "unavailable": False},
#     {"name": "Payment Server", "unavailable": True},
#     {"name": "API Server", "unavailable": False},
#     {"name": "Database Server", "unavailable": True}
# ]

# for environment in environments:
#     if not environment['unavailable']:
#         print(f"{environment['name']} - Ready for Testing")
#     else:
#         print(f"{environment['name']} - Environment Unavailable")


# # Question 27 — Day 3 Mixed Challenge

# test_cases = [
#     {"name": "Login Test", "status": "Passed", "critical_bug": 0, "environment_ready": True},
#     {"name": "Payment Test", "status": "Failed", "critical_bug": 1, "environment_ready": True},
#     {"name": "API Test", "status": "Passed", "critical_bug": 0, "environment_ready": False},
#     {"name": "Profile Test", "status": "Passed", "critical_bug": 0, "environment_ready": True},
#     {"name": "Logout Test", "status": "Failed", "critical_bug": 0, "environment_ready": True}
# ]


# ready_test = 0
# not_ready = 0
# for test_case in test_cases:
#     if test_case["status"] == "Passed" and test_case['critical_bug'] == 0 and test_case['environment_ready'] :
#         print(f"{test_case['name']} - Ready")
#         ready_test = ready_test + 1
#     else:
#         print(f"{test_case['name']} - Not Ready")
#         not_ready = not_ready + 1
# print(f"total Tests : {len(test_cases)}")
# print(f"Ready Tests : {ready_test}")
# print(f"Not Ready tests : {not_ready}")



# # Day 3 — Interview Question #1

# api_tests = [
#     {"api": "Login API", "status": "Passed", "response_time": 320, "critical_bug": False},
#     {"api": "Payment API", "status": "Passed", "response_time": 850, "critical_bug": False},
#     {"api": "Profile API", "status": "Failed", "response_time": 450, "critical_bug": True},
#     {"api": "Order API", "status": "Passed", "response_time": 490, "critical_bug": False},
#     {"api": "Logout API", "status": "Failed", "response_time": 280, "critical_bug": False}
# ]

# good_api=0
# review_api = 0
# for api_test in api_tests:
#     if api_test['status'] == "Passed" and api_test['response_time'] <= 500 and not api_test['critical_bug']:
#         print(f"{api_test['api']} - Good")
#         good_api = good_api + 1

#     else:
#         print(f"{api_test['api']} - Need Review")
#         review_api=review_api+1

# print(f"total Apis : {len(api_tests)}")
# print(f"Good Apis : {good_api}")
# print(f"Need review : {review_api}")

# if good_api == len(api_tests):
#     print("Build Status: READY")
# else:
#     print("Build Status: NOT READY")

# Interview Question #2 — Bug Release Decision


# bugs = [
#     {"bug_id": "BUG-101", "severity": "Minor", "status": "Open"},
#     {"bug_id": "BUG-102", "severity": "Critical", "status": "Closed"},
#     {"bug_id": "BUG-103", "severity": "Major", "status": "Open"},
#     {"bug_id": "BUG-104", "severity": "Critical", "status": "Open"},
#     {"bug_id": "BUG-105", "severity": "Minor", "status": "Closed"},
#     {"bug_id": "BUG-106", "severity": "Major", "status": "Closed"}
# ]


# open_bugs = 0
# open_critical_bugs = 0
# for test_bug in bugs:
#     print(f"{test_bug['bug_id']} - {test_bug['severity'] }- {test_bug['status']}")

#     if test_bug['status'] == "Open":
#         open_bugs = open_bugs + 1

#     if test_bug['status'] == "Open" and test_bug["severity"] == "Critical" :
#         open_critical_bugs = open_critical_bugs + 1

# print(f"total Bugs : {len(bugs)}")
# print(f"Open Bugs : {open_bugs}")
# print(f"Open Critical bugs : {open_critical_bugs}")

# if open_critical_bugs == 0 and open_bugs <= 3:
#     print("Ready of Release")
# else:
#     print("not for release")