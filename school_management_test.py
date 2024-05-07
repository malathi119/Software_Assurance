import unittest
from school_management import SchoolManagementSystem

class TestSchoolManagementSystem(unittest.TestCase):
    def setUp(self):
        self.system = SchoolManagementSystem()

    def test_add_student(self):
        student_id = "S001"
        student_info = {"name": "John Doe", "class": "10A"}
        self.assertTrue(self.system.add_student(student_id, student_info))

        self.assertFalse(self.system.add_student(student_id, student_info))

    def test_update_student(self):
        student_id = "S001"
        updated_info = {"name": "Jane Doe", "class": "10B"}
        self.assertTrue(self.system.update_student(student_id, updated_info))

        self.assertFalse(self.system.update_student("S002", updated_info))

    def test_delete_student(self):
        student_id = "S001"
        self.assertTrue(self.system.delete_student(student_id))

        self.assertFalse(self.system.delete_student("S002"))

    def test_add_teacher(self):
        teacher_id = "T001"
        teacher_info = {"name": "Alice Smith", "subject": "Math"}
        self.assertTrue(self.system.add_teacher(teacher_id, teacher_info))

        self.assertFalse(self.system.add_teacher(teacher_id, teacher_info))

    def test_delete_teacher(self):
        teacher_id = "T001"
        self.assertTrue(self.system.delete_teacher(teacher_id))

        self.assertFalse(self.system.delete_teacher("T002"))
    
    def test_list_students(self):
        self.system.students = {}
        with self.assertRaises(SystemExit) as cm:
            self.system.list_students()
        self.assertEqual(cm.exception.code, None)

        self.system.students = {"S001": {"name": "John Doe", "class": "10A"}, "S002": {"name": "Jane Smith", "class": "10B"}}
        expected_output = "ID: S001, Info: {'name': 'John Doe', 'class': '10A'}\nID: S002, Info: {'name': 'Jane Smith', 'class': '10B'}\n"
        with self.assertLogs() as log:
            self.system.list_students()
        self.assertEqual(log.output[0], expected_output)

    def test_list_teachers(self):
        self.system.teachers = {}
        with self.assertRaises(SystemExit) as cm:
            self.system.list_teachers()
        self.assertEqual(cm.exception.code, None)

        self.system.teachers = {"T001": {"name": "Alice Smith", "subject": "Math"}, "T002": {"name": "Bob Johnson", "subject": "Science"}}
        expected_output = "ID: T001, Info: {'name': 'Alice Smith', 'subject': 'Math'}\nID: T002, Info: {'name': 'Bob Johnson', 'subject': 'Science'}\n"
        with self.assertLogs() as log:
            self.system.list_teachers()
        self.assertEqual(log.output[0], expected_output)

if __name__ == "__main__":
    unittest.main()
