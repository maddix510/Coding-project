name = input("What's your name? ")
age = input("How old are you? ")

print ("Hi", name, ", glad to see you")
mood = input("How was your day? (good, okay, bad) ")

if mood.lower() == "good":
    print("Awesome! Keep it up!")
elif mood.lower() == "okay":
    print("Not bad, tomorrow could be better!")
elif mood.lower() == "bad":
    print("Don't worry, things will improve")

rating = input("What would you rate your day on a scale from 1-10 (please enter answer in a number) ")
rating_number = int(rating)

if rating_number in [8, 9, 10]:
    print("Looks like a great day!")
elif rating_number in [5, 6, 7]:
    print("A decent day, huh?")
elif rating_number in [1, 2, 3, 4]:
    print("Tough day, hang in there!")
else:
    print("Please enter a valid number between 1-10")

print("To summarize, your name is", name, ", you are", age, "years old, and you rated your day a", rating_number)