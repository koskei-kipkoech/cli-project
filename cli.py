import sys 
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, TM, Student

DATABSE_URL = "sqlite:///tms.db"

engine = create_engine(DATABSE_URL)
Session = sessionmaker(bind=engine)
session = Session()

def init_db():
    #initialize database
    Base.metadata.create_all(engine)
    print("Database initialized successfully.")

def create_tm():
    #create a new TM
    name = input("Enter the Tm Name: ")
    email = input("Enter the Tm Email: ")
    tm = TM(name=name, email=email)
    session.add(tm)
    session.commit()
    print(f"TM '{name}' with ID {tm.id} created successfully.")


def update_tm():
    tm_id = int(input("Enter the ID to update: "))
    tm = session.get(TM, tm_id)

    if not tm:
        print(f"TM with ID {tm_id} not found.")
        return
    tm.name =  input(f"Enter new name for TM (current : {tm.name}): ") or tm.name
    tm.email = input(f"Enter new email for TM (current : {tm.email}):") or tm.email
    session.commit()
    print(f"TM with ID {tm_id} updated successfully.")


def delete_tm():
    tm_id = int(input("Enter the TM ID to delete: "))
    tm = session.get(TM, tm_id)

    if not tm:
        print(f"TM with ID {tm_id} not found.")
        return
    session.delete(tm)
    session.commit()
    print(f"TM with ID {tm_id} deleted successfully.")

def create_student():
    #create a new student
    name = input("Enter the Student Name: ")
    age = int(input("Enter the Student Age: "))
    tm_id = int(input("Enter the TM ID: "))
    tm = session.get(TM, tm_id)

    if not tm:
        print(f"TM with ID {tm_id} not found.")
        return
    student = Student(name=name, age=age, tm_id=tm_id)
    session.add(student)
    session.commit()
    print(f"Student '{name}' with ID {student.id} created successfully and assigned to TM ID {tm_id}.")

def update_student():
    student_id = int(input("Enter the ID to update: "))
    student = session.get(Student, student_id)

    if not student:
        print(f"Student with ID {student_id} not found.")
        return
    student.name =  input(f"Enter new name for Student (current : {student.name}): ") or student.name
    student.age = input(f"Enter new age for Student (current : {student.age})): ") or student.age
    new_tm_id = input(f"Enter new TM ID for Student (current : {student.tm_id}): ") or student.tm_id
    if new_tm_id:
        new_tm = session.get(TM, int(new_tm_id))
        if not new_tm:
            print(f"TM with ID {new_tm_id} not found. Skipping update.")
        else:
            student.tm_id = new_tm_id
    session.commit()
    print(f"Student with ID {student_id} updated successfully.")

def delete_student():
    student_id = int(input("Enter the Student ID to delete: "))
    student = session.get(Student, student_id)

    if not student:
        print(f"Student with ID: {student_id} not found.")
        return
    session.delete(student)
    session.commit()
    print(f"Student with ID: {student_id} deleted successfully.")

def assign_student():
    student_id = int(input("Student with ID: "))
    tm_id = int(input("TM with ID: "))
    student = session.get(Student, student_id)
    tm = session.get(TM, tm_id)
    if not student or not tm:
        print("invalid Student ID  or TM  ID not found.")
        return
    student.tm_id = tm_id
    session.commit()
    print(f"Student with ID: {student_id} assigned to TM with ID: {tm_id} successfully.")

def list_tms():
    tms = session.query(TM).all()
    if not tms:
        print("No TM found.")
    for tm in tms:
        print(tm)

def list_students():
    students  = session.query(TM).all()
    if not students:
        print("No Student found.")
    for student in students:
        print(student)

def view_student_by_tm():
    tm_id  = input("Enter TM ID to view student: ")
    tm = session.get(tm_id)
    if not tm:
        print(f"TM with ID: {tm_id} not found.")
        return
    students = tm.students
    if not students:
        print(f"No Student found for TM with ID: {tm_id}")
        return
    print(f"Student belonging to TM '{tm.name}'  (id: {tm_id}")
    for student in students:
        print(student)

def main_menu():
    while True:
        print(" Welcome to  the Application. what would you like to do")
        print("1. Create TMs.")
        print("2. Update TMs.")
        print("3. Delete TMs.")
        print("4. Create Students.")
        print("5. Update Students.")
        print("6. Delete Students.")
        print("7. Assign Student to TM.")
        print("8. List all TMs.")
        print("9. List all Students.")
        print("10. View Students by TM.")
        print("11. Exit.")

        choice = input("Enter your choice: ")
        if choice == "1":
            create_tm()
        elif choice == "2":
            update_tm()
        elif choice == "3":
            delete_tm()
        elif choice == "4":
            create_student()
        elif choice == "5":
            update_student()
        elif choice == "6":
            delete_student()
        elif choice == "7":
            assign_student()
        elif choice == "8":
            list_tms()
        elif choice == "9":
            list_students()
        elif choice == "10":
            view_student_by_tm()
        elif choice == "11":
            print("Exiting the application..............")
            sys.exit()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    init_db()
    main_menu()