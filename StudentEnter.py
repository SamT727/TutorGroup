import csv

def login():
    correct_username = "Leeman" #case sensitive so "leeman" would not work
    correct_password = "123"  #put in f for username and password and it correctly came out with incorrect details
    
    while True:
        entered_username = input("Enter username: ")
        entered_password = input("Enter password: ")
        
        if entered_username == correct_username and entered_password == correct_password:
            print("Login successful!")
            return True
        else:
            print("Incorrect username or password. Please try again.") #worked(see line 4)

def enter_student_details():
    with open("Students.csv", mode='a', newline='') as file:
        writer = csv.writer(file)
        print("\nEnter student details:")
        unique_id = input("Enter unique ID number: ")
        surname = input("Entr surname: ")
        forename = input("Enter forename: ")
        dob = input("Enter date of birth (Day/Month/year): ")
        address = input("Enter home address: ")
        phone_number = input("Enter home phone number: ")
        gender = input("Enter gender: ")
        tutor_group = input("Enter tutor group: ")
        
        writer.writerow([unique_id, surname, forename, dob, address, phone_number, gender, tutor_group])
        print("Student details added successfully.")  #Adding details worked, however, you can add anything you want here and it would still be added. 

def view_student_details():
    try:
        with open("Students.csv", mode='r') as file:
            reader = csv.reader(file)
            print("\nStudent details:")
            for row in reader:
                print(row)
    except FileNotFoundError:
        print("No student details found.")

def main():
    if login():
        while True:
            print("\nMenu:")
            print("1. Enter student details")
            print("2. View student details") #typing 2 to view details showed it correctly after adding a student
            print("3. Logout") #ends code, worked.
            choice = input("Enter your choice (1/2/3): ")
            
            if choice == "1":
                enter_student_details()
            elif choice == "2":
                view_student_details()
            elif choice == "3":
                print("Logged out.")
                break
            else:
                print("Invalid choice. Please enter 1, 2, or 3.") #put in 4 and this showed up, working as intended.

if __name__ == "__main__":
    main()
