student = {
    "name": "Rom", 
    "age": 25, 
    "courses": ["Math", "ComSci"],
  
}

student["phone"] = "555-5555"
student["name"] = "Jane"

student.update({"name": "Ryouta", "phone": "999-9999"})

print(student["name"])
print(student.get("phone", "Not found"))

#del student["age"]
age = student.pop("age")

print(student)
print(age)

print(len(student))
print(student.keys())
print(student.values())
print(student.items())