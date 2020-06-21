# Some lists for word inserts

ADJECTIVES = [
	[""],
	["awful", "terrible", "terrific", "terrifying", "horrible", "horrific", "horrendous", "horrifying", "atrocious", "appalling", "detestable", "vile", "feral"],
	["bad", "not recommendable"],
	["underwhelming", "meh", "improvable"],
	["good", "recommendable"],
	["excellent", "top tier"]
]


# Function for getting game title names

def get_string(mandatory, title_case):
	# Loop that will continue if the user inputs invalid text
	while True:
		# Get text
		string = input().strip()
		# Convert the name to title case if required to
		if title_case:
			string = string.title()
		# Make the user re enter text if the field is blank
		if mandatory and string == "":
			print("This field is required.")
			continue
		# If everything is valid then return
		return string


# Function for getting the star ratings

def get_star_rating(mandatory):
	# Loop that will continue if the user inputs a invalid number
	while True:
		# Get text
		number = input()
		# Make the user re enter text if the field is blank
		if number == "":
			if not mandatory:
				return 0
			else:
				print("This field is required.")
				continue
		# Attempt to convert the string to an integer
		try:
			number = int(number)
		# If it is not a valid integer then make the user re enter text
		except ValueError:
			print("This is not a valid integer (whole number).")
			continue
		# If the number is out of range the make the user re enter text
		if number < 1 or number > 5:
			print("This number is out of range (must be between 1 and 5)")
			continue
		# If everything is valid then return
		return number


# Function that allows the user to select a word from a list or type in their own word

def get_word_insert(rating, array, mandatory):
	# Print out the list
	out = "(0)" + array[rating][0].title()
	for item in range(1, len(array[rating])):
		out = out + ", (" + str(item) + ")" + array[rating][item].title()
	print(out)
	# Loop that will continue if the user inputs a invalid string
	while True:
		# Get string
		string = input().strip()
		# Make the user re enter text if the field is blank
		if string == "" and mandatory:
			print("This field cannot be blank")
			continue
		# Check if the string is a valid integer in range
		try:
			number = int(string)
			if number < 0:
				print("This number is less then 0, it must be at least 0")
				continue
			# Return appropriate insert if so
			return array[rating][number]
		# If the user entered a valid string then return that
		except ValueError:
			# But making sure that it is not a floating point number
			try:
				float(string)
				print("This number must be a integer (Whole Number)")
				continue
			except ValueError:
				return string.lower()
		# If the user enters a number that is too big then make the user re enter text
		except IndexError:
			print("That number is bigger then {}, the size of the list".format(len(array[rating]) - 1))
			continue
		# If everything is valid then return
		print("Error")


# Main body of the code

# Print the review generator help

print("""Welcome to the Game Review Generator.
In order to generate a review; we will need to ask you some questions. These will help us create a review.
Some questions will require will a yes/no, a rating between 0 and 5 or just require you to enter some text.
Most questions will need to be answered and are marked by an astrix (*), however some are not and can be left blank.
""")

#print("Game Name*:")
#name = get_string(True, True)
#print("\nName: " + name)

#print("")
#print("How much did you enjoy the game* (1 - 5)?")
#enjoyment = get_star_rating(True)
#print("\nEnjoyment: " + str(enjoyment))

print("")
print("Choose a adjective that best decries the game*:")
adjective1 = get_word_insert(1, ADJECTIVES, True)
print(adjective1)
