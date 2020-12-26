# def greeting():
#     print("Hello")

# def greeting(name):
#     print("Hello " + name)

# def greeting(name, greeting):
#      print(greeting + " " + name)

# def greeting(name, greeting="Hello"):
#      print(greeting + " " + name)

def student_info(*args, **kwargs):
    print(args)
    print(kwargs)

 
student_info("Rom","Negrillo","CpE","2014106058", course="Computer Engineering", year_level="4")

student_personal_info = ["Rom","Negrillo","CpE","2014106058"]
student_course_info = {"course": "Computer Engineering", "year_level":4}

student_info(*student_personal_info, **student_course_info)