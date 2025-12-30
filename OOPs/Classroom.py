class Student:
    def __init__(self, name, score):
        self.name= name
        self.score= score

    def __str__(self):
        return f"Student: {self.name}, Score: {self.score}"
    
class Classroom:
    def __init__(self, class_name):
        self.class_name= class_name
        self.students= []

    def add_student(self, student_object):
        self.students.append(student_object)

    def get_average(self):
        if not self.students:
            return 0
        
        total_score= 0
        for s in self.students:
            total_score += s.score

        return total_score/len(self.students)
    
    def get_top_student(self):
        if not self.students:
            return 0
        
        top_student= self.students[0]
        for s in self.students:
            if (s.score > top_student.score):
                top_student= s
            else:
                return top_student
    
    def remove_failing_students(self, passing_score):
        self.passing_score= passing_score

        if not self.students:
            return 0
        fail= 0
        pass_students= []
        for s in self.students:
            if (s.score < passing_score):
                print(f"Removing: {s.name}")
                fail +=1
            else:
                pass_students.append(s)

        self.students= pass_students
        print(f"Cleanup finished. {fail} students removed.")
        
# 1. Create Students
s1 = Student("Alice", 90)
s2 = Student("Bob", 40)
s3 = Student("Charlie", 98)
s4 = Student("David", 30)

# 2. Setup Classroom
my_class = Classroom("Python 101")
my_class.add_student(s1)
my_class.add_student(s2)
my_class.add_student(s3)
my_class.add_student(s4)

# 3. Remove anyone with a score below 50
print("Cleaning up the class...")
my_class.remove_failing_students(50)

# 4. Print the remaining students
for s in my_class.students:
    print(s)
