class Student:
    def __init__(self, full_name, age, grade, student_id):
        self.full_name = full_name
        self.age = age
        self.grade = grade
        self.student_id = student_id
        self.scores = []

    def show_info(self):
        print("*****Student Details*****")
        print(f"  Full Name: {self.full_name}")
        print(f"  Age: {self.age}")
        print(f"  Grade: {self.grade}")
        print(f"  Student ID: {self.student_id}")
        print("-------------------------------------")

    def add_score(self, score):
        self.scores.append(score)
        print(f"  Score {score} has been added to {self.full_name}'s scores")

    def show_scores(self):
        if not self.scores:
            print(f"  {self.full_name} has no scores yet.")
        else:
            print(f"  Scores: {self.scores}")

    def average_score(self):
        if not self.scores:
            print(f"  {self.full_name} has no scores yet.")
        return sum(self.scores) / len(self.scores)
    
    def change_grade(self, new_grade):
        self.grade = new_grade 
        print(f"  Grade changed to {self.grade} for student {self.full_name}")

class Teacher:
    def __init__(self, full_name, subject):
        self.full_name = full_name
        self.subject = subject
        self.students = []

    def add_student(self, student):
        if student not in self.students:
            self.students.append(student)
        else:
            print(f"  Student {student.full_name} already exists for this teacher.")

    def remove_student(self, student):
        if student in self.students:
            self.students.remove(student)
        else:
            print(f"  Student {student.full_name} not found for this teacher.")

    def show_students(self):
        if not self.students:
            print("No students assigned to this teacher.")
        else:
            for s in self.students:
                print(f"- {s.full_name} (ID: {s.student_id})")

class Classroom:
    def __init__(self, class_name):
        self.class_name = class_name
        self.teacher = None
        self.students = []

    def set_teacher(self, teacher):
        self.teacher = teacher
        if teacher:
            for student in self.students:
                teacher.add_student(student)

    def add_student(self, student):
        if student not in self.students:
            self.students.append(student)
            if self.teacher:
                 self.teacher.add_student(student)

    def remove_student(self, student):
        if student in self.students:
            self.students.remove(student)
            if self.teacher:
                self.teacher.remove_student(student)

    def show_class_info(self):
        teacher_name = self.teacher.full_name if self.teacher else "No teacher assigned yet"
        return f"Class: {self.class_name}, Teacher: {teacher_name}, Students count: {len(self.students)}"
    
    def show_students(self):
        if not self.students:
            return "No students in this class"
        student_names = [s.full_name for s in self.students]
        return student_names
    
class School:
    def __init__(self, name):
        self.name = name
        self.teachers = []
        self.students = []
        self.classrooms = []

    def add_student(self, student):
        for s in self.students:
            if s.student_id == student.student_id:
                print("Student with this ID already exists.")
                return
        self.students.append(student)
        print(f"Student {student.full_name} added to the school.")

    def add_teacher(self, teacher):
        for t in self.students:
            if t.full_name == teacher.full_name and t.subject == teacher.subject:
                print("Teacher with this name and subject already exists.")
        self.teachers.append(teacher)
        print(f"Teacher {teacher.full_name} added to the school.")

    def add_classroom(self, classroom):
        for c in self.classrooms:
            if c.class_name == classroom.name:
                print("Classroom with this name already exists.")
        self.classrooms.append(classroom) 
        print(f"Classroom {classroom.class_name} added to the school.")

    def assign_teacher_to_classroom(self, teacher, classroom):
        if teacher in self.teachers and classroom in self.classrooms:
            classroom.set_teacher(teacher)
            print(f"Teacher {teacher.full_name} assigned to {classroom.class_name}.")
        else:
            print("Teacher or classroom not found in the school.")

    def assign_student_to_classroom(self, student, classroom):
        if student in self.students and classroom in self.classrooms:
            if student not in classroom.students:
                classroom.add_student(student)
                print(f"Student {student.full_name} assigned to {classroom.class_name}.")
            else:
                print(f"Student {student.full_name} is already in {classroom.class_name}.")
        else:
            print("Student or classroom not found in the school.")

    def remove_student_from_school(self, student_id):
        target_student = find_student_by_id(self.students, student_id)
        if not target_student:
            print(f"Student with ID {student_id} not found in the school!")
            return
        classrooms_to_remove_from = []
        for classroom in self.classrooms:
            if target_student in classroom.students:
                classrooms_to_remove_from.append(classroom)

        for classroom in classrooms_to_remove_from:
            classroom.remove_student(target_student)
            print(f"Removed {target_student.full_name} from {classroom.class_name}.")

        self.students.remove(target_student)
        print(f"Student {target_student.full_name} (ID: {student_id}) removed from school's main list.")
 
    def show_all_students(self): 
        if not self.students:
            print("No students in the school.")
            return
        
        print(f"\n--- Students in {self.name} ---")
        for student in self.students:
            student.show_info()

    def show_all_teachers(self):
        if not self.teachers:
            print("No teachers in the school.")
            return
        print(f"\n--- Teachers in {self.name} ---")
        for teacher in self.teachers:
            print(f"- Name: {teacher.full_name}, Subject: {teacher.subject}")

    def show_all_classrooms(self):
        if not self.classrooms:
            print("No classrooms in the school.")
            return
        print(f"\n--- Classrooms in {self.name} ---")
        for classroom in self.classrooms:
            print(f"- {classroom.show_class_info()}")

def find_student_by_id(students, student_id):
    for student in students:
        if student.student_id == student_id:
            return student
    return None

def find_teacher_by_name(teachers, teacher_name):
    for teacher in teachers:
        if teacher.full_name == teacher_name:
            return teacher
    return None

def find_classroom_by_name(classrooms, class_name):
    for classroom in classrooms:
        if classroom.class_name == class_name:
            return classroom
    return None

def main():
    school = School("My School")
    while True:
        print("\n=========== School Management Menu ===========")
        print("1. Add student")
        print("2. Add teacher")
        print("3. Add classroom")
        print("4. Assign teacher to classroom")
        print("5. Assign student to classroom")
        print("6. Add score to student")
        print("7. Show student info")
        print("8. Show all students")
        print("9. Show all teachers")
        print("10. Show all classrooms")
        print("11. Remove student from school")
        print("12. Exit")
        print("==============================================")

        choice = input("Enter your choice: ")
        if choice == "1":
            full_name = input("Enter student full name: ")
            age = int(input("Enter student age: "))
            grade = input("Enter student grade: ")
            student_id = input("Enter student ID: ")
            new_student = Student(full_name, age, grade, student_id)
            school.add_student(new_student)

        elif choice == "2":
            full_name = input("Enter teacher full name: ")
            subject = input("Enter teacher subject: ")
            new_teacher = Teacher(full_name, subject)
            school.add_teacher(new_teacher)   

        elif choice == "3":
            class_name = input("Enter classroom name: ")
            new_classroom = Classroom(class_name)
            school.add_classroom(new_classroom)

        elif choice == "4":
            teacher_name = input("Enter teacher full name: ")
            class_name = input("Enter classroom name: ")
            teacher = find_teacher_by_name(school.teachers, teacher_name)
            classroom = find_classroom_by_name(school.classrooms, class_name)

            if teacher is not None and classroom is not None:
                school.assign_teacher_to_classroom(teacher, classroom)
            else:
                print("Teacher or classroom not found.")


        elif choice == "5":
            student_id = input("Enter student ID: ")
            class_name = input("Enter classroom name: ")
            student = find_student_by_id(school.students, student_id)
            classroom = find_classroom_by_name(school.classrooms, class_name)

            if student is not None and classroom is not None:
                school.assign_student_to_classroom(student, classroom)
            else:
                print("Student or classroom not found.")


        elif choice == "6":
            student_id = input("Enter student ID: ")
            student = find_student_by_id(school.students, student_id)

            if student is not None:
                score = int(input("Enter score: "))
                student.add_score(score)

            else:
                print("Student not found.")

        elif choice == "7":
            student_id = input("Enter student ID: ")
            student = find_student_by_id(school.students, student_id)

            if student is not None:
                student.show_info()
                student.show_scores()
                avg = student.average_score()

                if avg is not None: 
                    print(f"Average score: {avg}")
            else:
                print("Student not found.")
                
        elif choice == "8":
            school.show_all_students()

        elif choice == "9":
            school.show_all_teachers()

        elif choice == "10":
            school.show_all_classrooms()

        elif choice == "11":
            student_id = input("Enter student ID to remove: ")
            school.remove_student_from_school(student_id)
            
        elif choice == "12":
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please try again.")
main()