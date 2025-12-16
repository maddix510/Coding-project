name = input("What's your name? ")
age = input("How old are you? ")

print ("Hi", name, ", glad to see you")
mood = input("How was your day? (good, okay, bad) ")

if mood.lower() == "good":
    print("Awesome! Keep it up!")
elif mood.lower() == "okay":
    print("Not bad, tomorrow could be better!")
elif mood.lower() == "bad":
    print("Don't worry, tings will improve")

rating = input("What would you rate your day on a scale from 1-10 (please enter answer in a number) ")

if int(rating) in [8, 9, 10]:
    print("Looks like a great day!")
elif int(rating) in [5, 6, 7]:
    print("A decent day, huh?")
elif int(rating) in [1, 2, 3, 4]:
    print("Tough day, hang in there!")
else:
    print("Please enter a valid number between 1-10")