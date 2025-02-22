import collections
import bisect

Student = collections.namedtuple("Student", ("name", "grade_point_average"))

# explicitly implementing comparisons for our Student class.
def comp_gpa(student):
    return (-student.grade_point_average, student.name)

# time complexity: O(log n)
def search_student(students, target, comp_gpa):
    i = bisect.bisect_left([comp_gpa(s) for s in students], comp_gpa(target))
    return 0 <= i < len(students) and students[i] == target