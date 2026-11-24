class Student:
    def __init__(self, student_id, name, department):
        self.__student_id = student_id
        self.__name = name
        self.__department = department
        self.__course = "None"

    def set_course(self, course_name):
        self.__course = course_name
        print(f"{self.__name} has been enrolled in {course_name}.")

    def get_student_info(self):
        return (
            f"Student ID: {self.__student_id}\n"
            f"Name: {self.__name}\n"
            f"Department: {self.__department}\n"
            f"Course: {self.__course}"
        )


if __name__ == "__main__":
    student1 = Student("20232020", "Atakan Toksoz", "Computer Engineering")
    student1.set_course("AII003 - Software Implementations")

    print("\nStudent Record")
    print(student1.get_student_info())