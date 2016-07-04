
from uuid import uuid4
import datetime

### Define Today's Date
format = "%a %b %d %H:%M:%S %Y"
today = datetime.date.today()
tomorrow = datetime.date.today() + datetime.timedelta(days=1)
dayaftertomorrow = tomorrow + datetime.timedelta(days=1)
print (today)
print (tomorrow)
print (dayaftertomorrow)

### Generate a user id
userid = uuid4()
print (userid)

# Grab user's name
firstname = raw_input("Please enter your first name: ")
lastname = raw_input("Please enter your last name: ")
print ("Thanks for entering that in {}\n\n").format(firstname.strip() +" "+ lastname.strip())

print ("\n\nList 5 Things You Dream of Having (material wants) \nincluding but not limited to ex: (house, car, clothing etc.)")

having = []
having.append(raw_input("1. "))
having.append(raw_input("2. "))
having.append(raw_input("3. "))
having.append(raw_input("4. "))
having.append(raw_input("5. "))

print (having)

print ("\n\nList 5 Things You Dream of Being including but not limited to ex: (be a great cook, be fluent in Chinese etc.)")

being = []
being.append(raw_input("1. "))
being.append(raw_input("2. "))
being.append(raw_input("3. "))
being.append(raw_input("4. "))
being.append(raw_input("5. "))

print (being)

print ("\n\nList 5 Things You Dream of Doing including but not limited to ex: (visiting Thailand, tracing your roots overseas, racing ostriches)")

doing = []
doing.append(raw_input("1. "))
doing.append(raw_input("2. "))
doing.append(raw_input("3. "))
doing.append(raw_input("4. "))
doing.append(raw_input("5. "))

print (doing)

mergedlist = having + being + doing

num = 1

print "\n\n"

for i in mergedlist:
    print str(num)+": " + i
    num += 1

print "\n\n"

selected_dreams = []

print "Select 4 dreams by typing in their numbers below: "
selected_dreams.append(raw_input("Please enter your First selected dream: "))
selected_dreams.append(raw_input("Please enter your Second selected dream: "))
selected_dreams.append(raw_input("Please enter your Third selected dream: "))
selected_dreams.append(raw_input("Please enter your Fourth selected dream: "))
