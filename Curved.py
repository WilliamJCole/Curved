#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Curved: Grading Help for Students and Educators"""


# Constant variables

MIN_GRADE = 0       # The minimum grade a student can have
MAX_GRADE = 100     # The maximum grade a student can have

WEIGHT_ASSIGNMENTS = 0.2  # Weight of assignments in the final grade for student
WEIGHT_QUIZZES = 0.3      # Weight of quizzes in the final grade of a student
WEIGHT_EXAMS = 0.5        # Weight of exams in the final grade of a student


# Helper/utility functions


def compute_average(numbers):
    """
    Computes and returns the average of the numbers in the given list.
    Returns zero if the list of numbers is empty.

    Args:
        numbers (list(float)) : A list of numbers
    Returns:
        float : The average of the numbers in the list, or zero if the list
            is empty
    Example:
        >>> compute_average([85, 90, 79])
        84.66666666666667
        >>> compute_average([])
        0
    """
    # Initialize the average to zero
    average = 0

    # If the list of numbers is not empty, compute the average
    if numbers:
        average = float(sum(numbers)) / len(numbers)

    # Return the average computed
    return average


def letter_grade(grade):
    """
    Returns the letter grade equivalence of a given grade using the following
    reference:

    Letter Grade      Percentage
    A+                >= 95%
    A                 93% to < 95%
    A-                90% to < 93%
    B+                87% to < 90%
    B                 83% to < 87%
    B-                80% to < 83%
    C+                77% to < 80%
    C                 73% to < 77%
    C-                70% to < 73%
    D+                67% to < 70%
    D                 63% to < 67%
    D-                60% to < 63%
    F                 < 60%

    Args:
        grade (float) : The grade in numerical form
    Returns:
        str : The grade in letter form
    Example:
        >>> letter_grade(94.90)
        'A'
        >>> letter_grade(0)
        'F'
        >>> letter_grade(67)
        'D+'
        >>> letter_grade(120)
        'A+'
        >>> letter_grade(-5)
        'F'
    """
    # List of minimum grades per letter grade
    grades = [95, 93, 90, 87, 83, 80, 77, 73, 70, 67, 63, 60]

    # List of corresponding letter grades
    letters = ['A+', 'A', 'A-', 'B+', 'B', 'B-',
               'C+', 'C', 'C-', 'D+', 'D', 'D-']

    # Iterate over the possible grades and check if grade is
    # at least any of those
    for i, min_grade in enumerate(grades):
        # Once the grade is greater than the one in the list, return its
        # corresponding letter grade
        if grade >= min_grade:
            return letters[i]

    # Return F if the grade wasn't at least any of the minimum grades
    return 'F'


def input_number(message, min_i=None, max_i=None, num_type=int):
    """
    Repeatedly asks the user to enter a number within the given range until
    the user enters a valid input. Returns the valid input entered by the user.

    Args:
        message (str) : The message to ask the user
        min_i (float) : The minimum number the user can enter (default: None)
        max_i (float) : The maximum number the user can enter (default: None)
        num_type (type) : The type of input to be entered (default: int)
    Returns:
        float : The valid number entered by the user
    Example:
        >>> input_number('Enter an integer from 0 to 100: ',
            min_i=0, max_i=100)
        Enter number from 0 to 100: -1
        Invalid input. Try again.
        Enter number from 0 to 100: 101
        Invalid input. Try again.
        Enter number from 0 to 100: banana
        Invalid input. Try again.
        Enter number from 0 to 100: 59.5
        Invalid input. Try again.
        Enter number from 0 to 100: 59
        59
        >>> input_number('Enter any integer: ')
        Enter any integer: banana
        Invalid input. Try again.
        Enter any integer: 59.5
        Invalid input. Try again.
        Enter any integer: -100
        -100
        >>> input_number('Enter an integer greater or equal to 5: ', min_i=5)
        Enter an integer greater or equal to 5: banana
        Invalid input. Try again.
        Enter an integer greater or equal to 5: 59.5
        Invalid input. Try again.
        Enter an integer greater or equal to 5: 4
        Invalid input. Try again.
        Enter an integer greater or equal to 5: 100
        100
        >>> input_number('Enter an integer less than or equal to 0: ', max_i=0)
        Enter an integer less than or equal to 0: banana
        Invalid input. Try again.
        Enter an integer less than or equal to 0: -59.5
        Invalid input. Try again.
        Enter an integer less than or equal to 0: 1
        Invalid input. Try again.
        Enter an integer less than or equal to 0: 0
        0
        >>> input_number('Enter any number: ', num_type=float)
        Enter any number: banana
        Invalid input. Try again.
        Enter any number: 59.5
        59.5
    """

    # Loop until user enters a valid input
    valid_input = False
    while not valid_input:
        try:
            # Ask user to enter the number
            input_num = num_type(input(message))

            # Validate if the input is within the range
            min_check = True
            max_check = True
            if min_i != None and input_num < min_i:
                min_check = False
            if max_i != None and input_num > max_i:
                max_check = False
            valid_input = min_check and max_check
        except ValueError:
            # Input is invalid if the user did not enter a number or
            # if the user entered a float but only an integer is asked for
            valid_input = False

        # Print error message if the user entered an invalid input
        if not valid_input:
            print("Invalid input. Try again.")

    # Return the valid number entered by the user
    return input_num


def input_numbers(message, length, min_i=None, max_i=None, num_type=int):
    """
    Asks the user to enter multiple numbers. Returns a list containing the
    valid numbers entered by the user. See function input_number for more
    details about the validation of user input.

    Args:
        message (str) : The message to ask the user
        length (int) : The number of numbers to be entered by the user
        min_i (float) : The minimum number the user can enter (default: None)
        max_i (float) : The maximum number the user can enter (default: None)
        num_type (type) : The type of input to be entered (default: int)
    Returns:
        list(float/int) : The list of valid numbers entered by the user
    Example:
        >>> input_numbers('Number', 5, num_type=float)
        Number 1: 0
        Number 2: 100
        Number 3: banana
        Invalid input. Try again.
        Number 3: 67.3
        Number 4: 24.5
        Number 5: 1
        [0.0, 100.0, 67.3, 24.5, 1.0]
    """
    # Loop to fill in the list of numbers
    input_num_list = []
    for i in range(1, length+1):
        # Ask the user for the number and append the valid input to the list
        input_num = input_number(message + " " + str(i) + ": ",
                                 min_i, max_i, num_type=num_type)
        input_num_list.append(input_num)

    # Return the list of numbers entered by the user
    return input_num_list


def input_yn(message):
    """
    Asks the user for a yes/no answer. User must enter either of the following:
    y, Y, n, N. User will be asked again if the user did not enter y/Y/n/N.
    Returns True if the user entered y/Y, False if the user entered n/N.

    Args:
        message (str) : The message to ask the user
    Returns:
        True if the user entered y/Y, False if the user entered n/N
    Example:
        >>> input_yn('Yes or No (y/n)? ')
        Yes or No (y/n)? banana
        Invalid input. Try again.
        Yes or No (y/n)? 55
        Invalid input. Try again.
        Yes or No (y/n)? Y
        True
        >>> input_yn('Yes or No (y/n)? ')
        Yes or No (y/n)? y
        True
        >>> input_yn('Yes or No (y/n)? ')
        Yes or No (y/n)? n
        False
        >>> input_yn('Yes or No (y/n)? ')
        Yes or No (y/n)? N
        False
    """
    # Loop until the user enters a valid input
    valid_input = False
    while not valid_input:
        # Ask the user with y/n question, and convert the user's
        # answer to lower case
        answer = input(message).lower()

        # Validate user's input
        valid_input = answer == 'y' or answer == 'n'

        # Print error message if the user entered an invalid input
        if not valid_input:
            print("Invalid input. Try again.")

    # Return True if the user entered y/Y, False if the user entered n/N
    return answer == 'y'


# Classes and functions


class Student:
    """
    The Student class represents a Student.
    """

    def __init__(self, name, assignments=None, quizzes=None, exams=None):
        """
        Creates a new Student object with the given name, and lists of their
        grades on assignments, quizzes, and exams.

        Args:
            name (str) : The name of the student
            assignments (list(float)) : The grades of the student on assignments
                (default: None)
            quizzes (list(float)) : The grades of the student on quizzes
                (default: None)
            exams (list(float)) : The grades of the student on exams (default:
                None)
        Example:
            >>> s1 = Student("Ricky Loo",[85,92,88,92,95,94,91,90,93,92],
                    [86,89,89,85,84,91,93],[89,86,85])
            >>> s2 = Student("Emily James",[80,90,84,82,84,89,87,86,87,85],
                    [82,89,86,80,85,80,82],[92,91,92])
        """
        # Set the name of the student
        self.name = name

        # Set the student's assignment grades
        if assignments is None:
            self.assignments = []
        else:
            self.assignments = assignments

        # Set the student's quiz grades
        if quizzes is None:
            self.quizzes = []
        else:
            self.quizzes = quizzes

        # Set the student's exam grades
        if exams is None:
            self.exams = []
        else:
            self.exams = exams

    def assignments_average(self):
        """
        Computes and returns the average of the student's assignment grades.

        Returns:
            float : The average of the student's assignment grades.
        Example:
            >>> s1 = Student("Ricky Loo",[85,92,88,92,95,94,91,90,93,92],
                    [86,89,89,85,84,91,93],[89,86,85])
            >>> s2 = Student("Emily James",[80,90,84,82,84,89,87,86,87,85],
                    [82,89,86,80,85,80,82],[92,91,92])
            >>> s1.assignments_average()
            91.2
            >>> s2.assignments_average()
            85.4
        """
        return compute_average(self.assignments)

    def quizzes_average(self):
        """
        Computes and returns the average of the student's quiz grades.

        Returns:
            float : The average of the student's quiz grades.
        Example:
            >>> s1 = Student("Ricky Loo",[85,92,88,92,95,94,91,90,93,92],
                    [86,89,89,85,84,91,93],[89,86,85])
            >>> s2 = Student("Emily James",[80,90,84,82,84,89,87,86,87,85],
                    [82,89,86,80,85,80,82],[92,91,92])
            >>> s1.quizzes_average()
            88.14285714285714
            >>> s2.quizzes_average()
            83.42857142857143
        """
        return compute_average(self.quizzes)

    def exams_average(self):
        """
        Computes and returns the average of the student's exam grades.

        Returns:
            float : The average of the student's exam grades.
        Example:
            >>> s1 = Student("Ricky Loo",[85,92,88,92,95,94,91,90,93,92],
                    [86,89,89,85,84,91,93],[89,86,85])
            >>> s2 = Student("Emily James",[80,90,84,82,84,89,87,86,87,85],
                    [82,89,86,80,85,80,82],[92,91,92])
            >>> s1.exams_average()
            86.66666666666667
            >>> s2.exams_average()
            91.66666666666667
        """
        return compute_average(self.exams)

    def final_grade(self):
        """
        Computes and returns the final grade of the student. See the constant
        variables WEIGHT_ASSIGNMENTS, WEIGHT_QUIZZES, WEIGHT_EXAMS for the
        weights of assignments, quizzes, and exams respectively.

        Returns:
            float : The computed final grade of the student (without curving)
        Example:
            >>> s1 = Student("Ricky Loo",[85,92,88,92,95,94,91,90,93,92],
                    [86,89,89,85,84,91,93],[89,86,85])
            >>> s2 = Student("Emily James",[80,90,84,82,84,89,87,86,87,85],
                    [82,89,86,80,85,80,82],[92,91,92])
            >>> s1.final_grade()
            88.01619047619047
            >>> s2.final_grade()
            87.94190476190477
        """
        # Compute weighted average of assignments, quizzes, and exams
        avg_assignments = self.assignments_average() * WEIGHT_ASSIGNMENTS
        avg_quizzes = self.quizzes_average() * WEIGHT_QUIZZES
        avg_exams = self.exams_average() * WEIGHT_EXAMS

        # Compute final grade by adding the computed weighted averages
        final_grade = avg_assignments + avg_quizzes + avg_exams

        # Return final grade and its letter grade counterpart
        return final_grade

    def __str__(self):
        """
        Returns the string value of the student in the following
        format:
            name,[a1,a2,a3,...,an,[q1,q2,a3,...,qn],[e1,e2,e3,...,en]
        where:
            name (str) : The name of the student
            a1,a2,a3,..,an (floats) : The grades of the student
                in assignments
            q1,q2,q3,..,qn (floats) : The grades of the student
                in quizzes
            e1,e2,e3,..,en (floats) : The grades of the student
                in exams

        Returns:
            str : The string representation of the student
        Example:
            >>> s1 = Student("Ricky Loo",[85,92,88,92,95,94,91,90,93,92],
                [86,89,89,85,84,91,93],[89,86,85])
            >>> str(s1)
            'Ricky Loo,[85,92,88,92,95,94,91,90,93,92],[86,89,89,85,84,91,93],
                [89,86,85]'
            >>> s2 = Student("Emily James",[80,90,84,82,84,89,87,86,87,85],
                [82,89,86,80,85,80,82],[92,91,92])
            >>> str(s2)
            'Emily James,[80,90,84,82,84,89,87,86,87,85],[82,89,86,80,85,80,82],
                [92,91,92]'
        """
        return ",".join((self.name, str(self.assignments), str(self.quizzes),
                         str(self.exams)))

    def __repr__(self):
        """
        Returns the string representation of the student. See function
        __str__(self).
        """
        return str(self)


def read_students_file(filename):
    """
    Opens and reads the file with the given filename and returns a list of
    students based on the read data. This may raise an IOError if there were
    any problems reading the file (e.g. FileNotFoundError).

    Args:
        filename (str) : The name of the file containing the data to be read.
            Each line in the file represents a Student object and must be
            in the following format:
                name|a1,a2,a3,...,an|q1,q2,q3,...,qn|e1,e2,e3,...,en
            where:
                name (str) : The name of the student
                a1,a2,a3,..,an (floats) : The grades of the student
                    in assignments
                q1,q2,q3,..,qn (floats) : The grades of the student
                    in quizzes
                e1,e2,e3,..,en (floats) : The grades of the student
                    in exams
    Returns:
        list(Student) : The list of the student objects created
    Example:
        data.txt:
        Ricky Loo|85,92,88,92,95,94,91,90,93,92|86,89,89,85,84,91,93|89,86,85
        Emily James|80,90,84,82,84,89,87,86,87,85|82,89,86,80,85,80,82|92,91,92
        Jojo Fernandez|||

        >>> read_students_file('data.txt')
        [Ricky Loo,[85.0, 92.0, 88.0, 92.0, 95.0, 94.0, 91.0, 90.0, 93.0, 92.0],
            [86.0, 89.0, 89.0, 85.0, 84.0, 91.0, 93.0],[89.0, 86.0, 85.0],
            Emily James,[80.0, 90.0, 84.0, 82.0, 84.0, 89.0, 87.0, 86.0, 87.0,
            85.0],[82.0, 89.0, 86.0, 80.0, 85.0, 80.0, 82.0],[92.0, 91.0, 92.0],
            Jojo Fernandez,[],[],[]]

        data.txt:
        <empty>

        >>> read_students_file('data.txt')
        []
    """
    # Initialize list of students to an empty list
    students = []

    # Open file
    with open(filename) as file:
        # Iterate over the lines in the file
        for line in file:
            # Remove leading and trailing white spaces form the line
            line = line.strip()

            # Check if line is not empty
            if line:
                # Split the line by the "|" separator
                student_attribtues = line.split("|")

                # Retrieve the student's name
                name = student_attribtues[0]

                # Retrieve the student's list of assignment grades by splitting
                # with ","
                assignments = [float(x) for x in
                               student_attribtues[1].split(",") if x]

                # Retrieve the student's list of quiz grades by splitting
                # with ","
                quizzes = [float(x) for x in
                           student_attribtues[2].split(",") if x]

                # Retrieve the student's list of exam grades by splitting
                # with ","
                exams = [float(x) for x in
                         student_attribtues[3].split(",") if x]

                # Create a new student object and append it to the list
                # of students
                students.append(Student(name, assignments, quizzes, exams))

    # Return list of students
    return students


def write_students_file(filename, students):
    """
    Writes the list of students data to the file with the given filename.
    This may raise an IOError if there were any problems reading the file
    (e.g. FileNotFoundError). See function read_students_file for more
    details on the format of the contents of the file.

    Args:
        filename (str) : The name of the file where to write the data
        students (list(Student) : The list of student objects whose data is to
            be written to the file
    Example:
        >>> s1 = Student("Ricky Loo",[85,92,88,92,95,94,91,90,93,92],
            [86,89,89,85,84,91,93],[89,86,85])
        >>> s2 = Student("Emily James",[80,90,84,82,84,89,87,86,87,85],
            [82,89,86,80,85,80,82],[92,91,92])
        >> s3 = Student("Jojo Fernandez")
        >>> students = [s1, s2, s3]
        >>> write_students_file('data.txt', students)

        data.txt:
        Ricky Loo|85,92,88,92,95,94,91,90,93,92|86,89,89,85,84,91,93|89,86,85
        Emily James|80,90,84,82,84,89,87,86,87,85|82,89,86,80,85,80,82|92,91,92
        Jojo Fernandez|||

        >>> write_students_file('data.txt', [])

        data.txt:
        <empty>
    """
    # Open file for writing
    with open(filename, 'w') as file:
        # Iterate over the list of students
        for student in students:
            # Write the name of the student
            file.write(student.name)

            # Write the assignment grades of the student
            file.write("|" + ",".join([str(x) for x in student.assignments]))

            # Write the quiz grades of the student
            file.write("|" + ",".join([str(x) for x in student.quizzes]))

            # Write the exam grades of the student
            file.write("|" + ",".join([str(x) for x in student.exams]))

            # Write a new line
            file.write("\n")


def add_student(students):
    """
    Asks the user for the details of a student, then creates a Student object
    with those details and adds it to the list of students. See the constant
    variables MIN_GRADE and MAX_GRADE for the minimum and maximum grades the
    user can enter for the student's grades.

    Args:
        students (list(Student)) : The list of students where the new student
            to be created will be added
    Example:
        >>> students = []
        >>> add_student(students)
        Name: Ricky Loo
        Number of assignment grades the student has: 5
        Assignment 1: 95
        Assignment 2: 80
        Assignment 3: 87.5
        Assignment 4: 88
        Assignment 5: 91.5
        Number of quiz grades the student has: 4
        Quiz 1: 69.8
        Quiz 2: 70
        Quiz 3: 75
        Quiz 4: 80.5
        Number of exam grades the student has: 3
        Exam 1: 80.5
        Exam 2: 90
        Exam 3: 85
        >>> students
        [Ricky Loo, [95.0, 80.0, 87.5, 88.0, 91.5], [69.8, 70.0, 75.0, 80.5],
            [80.5, 90.0, 85.0]]
        >>> add_student(students)
        Name: Emily James
        Number of assignment grades the student has: 5
        Assignment 1: 85
        Assignment 2: 90
        Assignment 3: 77.5
        Assignment 4: 98.2
        Assignment 5: 67
        Number of quiz grades the student has: 4
        Quiz 1: 63
        Quiz 2: 90
        Quiz 3: 85
        Quiz 4: 82.5
        Number of exam grades the student has: 3
        Exam 1: 99.5
        Exam 2: 100
        Exam 3: 75
        >>> students
        [Ricky Loo,[95.0, 80.0, 87.5, 88.0, 91.5], [69.8, 70.0, 75.0, 80.5],
            [80.5, 90.0, 85.0], Emily James,[85.0, 90.0, 77.5, 98.2, 67.0],
            [63.0, 90.0, 85.0, 82.5], [99.5, 100.0, 75.0]]
    """
    # Ask user for the name of the student
    name = input("Name: ")

    # Ask user for the number of assignment grades the student has, then ask
    # the user for the student's assignment grades
    num_assignments = input_number(
        "Number of assignment grades the student has: ", min_i=0)
    assignments = input_numbers("Assignment", num_assignments,
                                min_i=MIN_GRADE, max_i=MAX_GRADE,
                                num_type=float)

    # Ask user for the number of quiz grades the student has, then ask
    # the user for the student's quiz grades
    num_quizzes = input_number(
        "Number of quiz grades the student has: ", min_i=0)
    quizzes = input_numbers("Quiz", num_quizzes,
                            min_i=MIN_GRADE, max_i=MAX_GRADE,
                            num_type=float)

    # Ask user for the number of exam grades the student has, then ask
    # the user for the student's exam grades
    num_exams = input_number(
        "Number of exam grades the student has: ", min_i=0)
    exams = input_numbers("Exam", num_exams,
                          min_i=MIN_GRADE, max_i=MAX_GRADE,
                          num_type=float)

    # Create a new student object and add it to the list
    students.append(Student(name, assignments, quizzes, exams))


def write_final_grades(filename, students, curve=False):
    """
    Computes and writes the final grades of the students in the list to the
    file with the given filename. This may raise an IOError if there were any
    problems reading the file (e.g. FileNotFoundError). Each line in the
    output file would represent the final grade of a student and would be in
    the format:
        name,numeric_final_grade,letter_final_grade
    where:
        name (str) : The name of the student
        numeric_final_grade (float) : The final grade of the student (rounded to
            two decimal places)
        letter_final_grade (str) : The final grade of the student in letter form
    see the function comput_final_grade in the Student class for more details
    on how the final grade will be computed.

    Args:
        filename (str) : The name if the file where the final grades of the
            students would be written
        students (list(Student)) : The students  whose final grades will be
            computed and written on the file
        curve (bool) : Indicator if the final grade of the students
            will be curved. If True, all students' final grades will be
            curved depending on the highest final grade out of all
            the students (default: False)
    Example:
        >>> s1 = Student("Ricky Loo",[85,92,88,92,95,94,91,90,93,92],
            [86,89,89,85,84,91,93],[89,86,85])
        >>> s2 = Student("Emily James",[80,90,84,82,84,89,87,86,87,85],
            [82,89,86,80,85,80,82],[92,91,92])
        >> s3 = Student("Jojo Fernandez")
        >>> students = [s1, s2, s3]
        >>> write_final_grades('grades.txt', students)

        grades.txt:
        Ricky Loo,88.02,B+
        Emily James,87.94,B+
        Jojo Fernandez,0.00,F

        >>> write_final_grades('grades.txt', students, curve=True)

        grades.txt:
        Ricky Loo,100.00,A+
        Emily James,99.93,A+
        Jojo Fernandez,11.98,F
    """
    # Open the file for writing
    with open(filename, 'w') as file:
        # Iterate over the students in the list, then compute and store
        # their final grades in a list
        final_grades = []
        for student in students:
            final_grades.append(student.final_grade())

        # Check if students grades must be curved
        if curve:
            # Get the highest final grade
            highest = max(final_grades)

            # Compute the points to be added on all the final grades
            to_add = MAX_GRADE - highest

            # Add additional points to the final grades
            for i in range(len(final_grades)):
                final_grades[i] += to_add

        # Iterate over students in the list
        for i, student in enumerate(students):
            # Write the student's name to the file
            file.write(student.name)

            # Write the final grade of the student
            file.write(",{:.2f}".format(final_grades[i]))

            # Write the final letter grade of the student
            file.write("," + letter_grade(final_grades[i]))

            # Write a new line to the file
            file.write("\n")


def main():
    """
    The main function. The flow would be:
    1) User enters the name of the file where the students' data is stored
        (see function read_students_file(filename) for more details on how
        data from a file would be read)
    2) User add new student/s and their grades to the program
        and to the actual data file (see function input_yn(message) for more
        details on how to ask the user if he/she wants to add a student,
        see function add_new(students) for more details on how a user can
        add a new student, and see function write_students_file(filename,
        students) for more details on how the students data will be written to
        a file)
    3) User enters the name of the output file where to write the final grades
        of the students
    4) User chooses whether or not to curve before computing the final grade
    5) Program computes the final grades of the students and writes the output
        to the output file (see function write_final_grade(filename, students)
        for more details on how the final grades of the students will be written
        to a file)

    Example:
        >>>
        Enter filename of students' data: students.txt

        Would you like to add another student (y/n)? y

        Name: Ricky Loo
        Number of assignment grades the student has: 5
        Assignment 1: 95
        Assignment 2: 80
        Assignment 3: 87.5
        Assignment 4: 88
        Assignment 5: 91.5
        Number of quiz grades the student has: 4
        Quiz 1: 69.8
        Quiz 2: 70
        Quiz 3: 75
        Quiz 4: 80.5
        Number of exam grades the student has: 3
        Exam 1: 80.5
        Exam 2: 90
        Exam 3: 85

        New student added!

        Would you like to add another student (y/n)? y

        Name: Emily James
        Number of assignment grades the student has: 5
        Assignment 1: 85
        Assignment 2: 90
        Assignment 3: 77.5
        Assignment 4: 98.2
        Assignment 5: 67
        Number of quiz grades the student has: 4
        Quiz 1: 63
        Quiz 2: 90
        Quiz 3: 85
        Quiz 4: 82.5
        Number of exam grades the student has: 3
        Exam 1: 99.5
        Exam 2: 100
        Exam 3: 75

        New student added!

        Would you like to add another student (y/n)? y

        Name: Jojo Fernandez
        Number of assignment grades the student has: 0
        Number of quiz grades the student has: 0
        Number of exam grades the student has: 0

        New student added!

        Would you like to add another student (y/n)? n

        Enter filename of output file for students' final grades: grades.txt

        Would you like to curve the student's final grades (y/n)? y

        Final grades successfully written to 'grades.txt'.
    """
    # Ask user for the input filename
    in_filename = input("Enter filename of students' data: ")

    # Load the students data
    students = read_students_file(in_filename)

    # Loop to add students if the user wanted to
    add_new = True
    while add_new:
        # Ask user if he/she wants to add a student
        add_new = input_yn("\nWould you like to add another student (y/n)? ")

        # Print an empty line
        print()

        if add_new:
            # Add new student to list of students
            add_student(students)

            # Print success message
            print("\nNew student added!")

    # Overwrite the input file to add any new students created
    write_students_file(in_filename, students)

    # Ask user for the output filename
    out_filename = input("Enter filename of output file for students' "
                         + "final grades: ")

    # Ask if user wants to curve the grades
    curve = input_yn("\nWould you like to curve the student's final "
                     +"grades (y/n)? ")

    # Compute and write the results to output file
    write_final_grades(out_filename, students, curve)

    # Print success message
    print("\nFinal grades successfully written to '" +
          str(out_filename) + "'.")


if __name__ == '__main__':
    main()
