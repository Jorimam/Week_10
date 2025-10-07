
data_option = input("Select data borrow option\n")
if data_option == "1":
	phone_number = input("Enter phone number\n")
	print(f"{phone_number} subscribed with 1gb worth of data")
elif data_option == "2":
	phone_number = input("Enter phone number\n")
	print(f"{phone_number} subscribed with 2gb worth of data")
elif data_option == "3":
	phone_number = input("Enter phone number\n")
	print(f"{phone_number} subscribed with 3gb worth of data")
else:
	print("Error")


