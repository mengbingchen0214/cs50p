# ask user's name
name = input("What's your name? ").strip().title()

# remove whitespace from str and capitalize user's name (each word will be titlecased)
#name = name.strip().title()

# split user's name into first and second name
first, last = name.split(" ")

# say hello to user
print(f"hello, {first}")
# print ("hello, " + name)



