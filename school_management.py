import json

class SchoolManagementSystem:
    def __init__(self):
        self.students = self.load_data('students.json')
        self.teachers = self.load_data('teachers.json')
        self.classes = self.load_data('classes.json')

    def load_data(self, filename):
        try:
            with open(filename, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return {}

    def save_data(self, data, filename):
        with open(filename, 'w') as file:
            json.dump(data, file, indent=4)

    def add_student(self, student_id, student_info):
        if student_id in self.students:
            print("Student already exists.")
            return False
        self.students[student_id] = student_info
        self.save_data(self.students, 'students.json')
        print("Student added successfully.")
        return True

    def update_student(self, student_id, student_info):
        if student_id not in self.students:
            print("Student does not exist.")
            return False
        self.students[student_id] = student_info
        self.save_data(self.students, 'students.json')
        print("Student updated successfully.")
        return True

    def delete_student(self, student_id):
        if student_id in self.students:
            del self.students[student_id]
            self.save_data(self.students, 'students.json')
            print("Student deleted successfully.")
            return True
        print("Student not found.")
        return False

    def add_teacher(self, teacher_id, teacher_info):
        if teacher_id in self.teachers:
            print("Teacher already exists.")
            return False
        self.teachers[teacher_id] = teacher_info
        self.save_data(self.teachers, 'teachers.json')
        print("Teacher added successfully.")
        return True

    def delete_teacher(self, teacher_id):
        if teacher_id in self.teachers:
            del self.teachers[teacher_id]
            self.save_data(self.teachers, 'teachers.json')
            print("Teacher deleted successfully.")
            return True
        print("Teacher not found.")
        return False

    def list_students(self):
        if not self.students:
            print("No students found.")
            return
        for id, info in self.students.items():
            print(f"ID: {id}, Info: {info}")

    def list_teachers(self):
        if not self.teachers:
            print("No teachers found.")
            return
        for id, info in self.teachers.items():
            print(f"ID: {id}, Info: {info}")

def main():
    system = SchoolManagementSystem()
    while True:
        print("\nSchool Management System Options:")
        print("1. Add Student")
        print("2. Update Student")
        print("3. Delete Student")
        print("4. List Students")
        print("5. Add Teacher")
        print("6. Delete Teacher")
        print("7. List Teachers")
        print("8. Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            student_id = input("Enter student ID: ")
            student_name = input("Enter student name: ")
            student_class = input("Enter student class: ")
            student_info = {'name': student_name, 'class': student_class}
            system.add_student(student_id, student_info)
        elif choice == '2':
            student_id = input("Enter student ID to update: ")
            student_name = input("Enter new student name: ")
            student_class = input("Enter new student class: ")
            student_info = {'name': student_name, 'class': student_class}
            system.update_student(student_id, student_info)
        elif choice == '3':
            student_id = input("Enter student ID to delete: ")
            system.delete_student(student_id)
        elif choice == '4':
            system.list_students()
        elif choice == '5':
            teacher_id = input("Enter teacher ID: ")
            teacher_name = input("Enter teacher name: ")
            teacher_subject = input("Enter teacher subject: ")
            teacher_info = {'name': teacher_name, 'subject': teacher_subject}
            system.add_teacher(teacher_id, teacher_info)
        elif choice == '6':
            teacher_id = input("Enter teacher ID to delete: ")
            system.delete_teacher(teacher_id)
        elif choice == '7':
            system.list_teachers()
        elif choice == '8':
            break
        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()
