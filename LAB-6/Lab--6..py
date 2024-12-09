import pickle

class CourseGrades:
    def __init__(self, course_name, stu_IDs, stu_grades):
        self.course_name = course_name
        self.stu_IDs = stu_IDs
        self.stu_grades = stu_grades

    def display(self):
        print(f"Course Name: {self.course_name}")
        print("Student Grades:")
        for stu_id, grade in zip(self.stu_IDs, self.stu_grades):
            print(f"  ID: {stu_id}, Grade: {grade}")
        print()

# Function to create and serialize course grades
def create_and_save_courses():
    with open("grades_info.dat", "ab") as file:  # Open in append-binary mode
        for i in range(4):  # Create 4 CourseGrades objects
            print(f"Creating Course {i + 1}:")
            course_name = input("Enter Course Name: ")
            stu_IDs = []
            stu_grades = []
            for j in range(5):  # Get at least 5 students
                stu_ID = input(f"Enter Student {j + 1} ID: ")
                stu_grade = int(input(f"Enter Student {j + 1} Grade (0-100): "))
                stu_IDs.append(stu_ID)
                stu_grades.append(stu_grade)
            course = CourseGrades(course_name, stu_IDs, stu_grades)
            pickle.dump(course, file)  # Serialize and save the object
            print(f"Course '{course_name}' saved to file.\n")

# Function to read and display course grades from the file
def read_and_display_courses():
    try:
        with open("grades_info.dat", "rb") as file:  # Open in read-binary mode
            print("Reading Courses from File:\n")
            while True:
                try:
                    course = pickle.load(file)  # Deserialize the object
                    course.display()  # Display course details
                except EOFError:  # End of file reached
                    break
    except FileNotFoundError:
        print("No data file found. Please create course records first.")

# Main Program
if __name__ == "__main__":
    while True:
        print("\nMenu:")
        print("1. Create and Save Course Records")
        print("2. Read and Display Course Records")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            create_and_save_courses()
        elif choice == "2":
            read_and_display_courses()
        elif choice == "3":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")
