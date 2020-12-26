courses = ["History", "Math", "Physics", "ComSci"]
courses_2 = ["Art", 'Education']


print(courses)
print(len(courses))

print(courses[0:2])
print(courses[:2])
print(courses[2:])

print(courses[-1])

courses.append("Art")
print(courses)

courses = ["History", "Math", "Physics"]
courses_2 = ["Art", 'Education']

courses.append(courses_2)
print(courses)


courses = ["History", "Math", "Physics"]
courses_2 = ["Art", 'Education']

courses.extend(courses_2)
print(courses)

courses.remove("Math")
print(courses)

popped = courses.pop()
print(courses)
print(popped)

courses.reverse()

print(courses)

courses.sort()

print(courses)

num = [1,3,6,3,5,4]
num.sort()
print(num)

num.sort(reverse=True)
print(num)

num = [1,3,6,3,5,4]
num_sorted = sorted(num)

print(num)
print(num_sorted)

print(min(num))
print(max(num))
print(sum(num))

 
courses = ["History", "Math", "Physics", "ComSci"]
print(courses.index("ComSci"))

#print(courses.index("Art"))

print("Art" in courses)
print("Math" in courses)

for index,course in enumerate(courses, start=1):
    print(index, course)


courses = ["History", "Math", "Physics", "ComSci"]
course_str = " - ".join(courses)

new_list = course_str.split(" - ")

print(course_str)
print(new_list)