# empty list to add item in it
shop_list = []


# function to show Help
def help_me():
	print("""'Done' -> stop adding new thing
'Show ' -> showing your shop list
'Help ' -> helping you
'Del  ' -> delete what you want 
	""")


def delete_me():
	if not shop_list:
		print("Nothing do delete")
	else:
		try:
			for_del = input("what do you want to delete ? ").title()
			shop_list.remove(for_del)
		except ValueError:
			print("{} is not in your list! ".format(for_del))


# function to show what in list
def show_me():
	# number iteration what in list
	if not shop_list:
		print("Nothing for shop")
	else:
		i = 1
		for item in shop_list:
			print("{} - {}".format(i, item))
			i += 1


# main program for shopping list
while True:
	new_item = input("Enter what you need > ").title()
	if new_item == "Help":
		help_me()
		continue
	elif new_item == "Show":
		show_me()
		continue
	elif new_item == "Del":
		delete_me()
		continue
	elif new_item == "Done":
		break
	else:
		shop_list.append(new_item)
		print("""'{}' Added to list""".format(new_item))
# print whole list and what is in shopping list
print("your need these to shop : ")
i = 1
for item in shop_list:
	print("{} - {}".format(i, item))
	i += 1
