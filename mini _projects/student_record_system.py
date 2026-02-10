#student record management system 

student={
    "Amit": 85,
    "Neha": 95,
    "Anjali": 80,
    "Anil": 60,
    "Bipin": 76,
}
def add_student():
  name=input("Enter student name: ")
  marks=int(input("Enter marks: "))
  student[name]=marks
  print("student added successfully")

def view_student():
  if not student:
      print("no students record")
  else:
    print("student record")
    for name,marks in student.items():
      print(f"{name}:{marks}")

def search_student():
  name=input("Enter student name: ")
  if name in student:
    print(f"{name}scored{students[name]} marks")
  else:
    print("student not found")

def delete_student():
    name = input("Enter student name to delete: ")
    if name in student:
        del student[name]
        print(" student record delete successfully")
    else:
        print("student not found")
  

while True:
     print(" Students record menu")
     print("1. Add student")
     print("2. View student")
     print("3. Search student")
     print("4. delete student")
     print("5. Exit")

     choice = input("Enter your choice: ")

     if choice=="1":
         add_student()
     elif choice=="2":
          view_student()
     elif choice=="3":
           search_student()
     elif choice=="4":
            delete_student()
     elif choice=="5":
            print("Exiting program...")
            break
     else:
            print("Invalid choice, try again")
     
            
