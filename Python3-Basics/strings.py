greeting = "Hello"
name = "Rom"

print(name)
print(name[0])
print(name[-1])
print(name.upper())
print(name.lower())

message = greeting + ", " + name + ". Welcome!"

print(message)

message = "{}, {}. Welcome!".format(greeting, name)

print(message)

message_with_single_quotes = "Rom's Resolve"
print(message_with_single_quotes)

message_with_double_quotes = '"Great things takes time" - Saying'
print(message_with_double_quotes)

multiline_message = """
"Rom"
'is'
serious!
"""

print(multiline_message)

message.replace("Rom", "Ryouta")

print(message)

new_message = message.replace("Rom", "Ryouta")
print(new_message)