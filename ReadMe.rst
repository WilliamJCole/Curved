#######################################################
Curved (Grading and Curving for Students and Educators)
#######################################################

By William Cole
*****************

1. Overview
============
Curve is a program that takes lists of grades, gives them weights and then
takes the weighted average to produce a final grade. You will also place a
grading curve if required. This tool can be used by students to calculate
their own grades.

2. Persona
=============

1. **Name**: William Cole
2. **Details**: As a student this tool will help me to see where I stand in any
   course, buy just entering my grades and there weights. I can see which
   classes require more work. I can then see how my GPA will be when I go
   further in SPS
3. **Goals**: To simply see my grade and automatically.

3. Problem Scenario
======================

While Excel can be used to calculate a students grades, I would like a simpler
and more automatic course to get my grades.

1. **Current Alternatives**:Excel and Blackboard both can complete these tasks.
2. **Value Proposition**: This program can also be utilized to calculate
   further grades, and it would be an automatic process.

4. User Stories
==================
As student, James, wants to calculate his GPA so I can get a better view of my
progress in my classes

As a teacher, John, wants to calculate grades for his students and may or may
not want to curve the grade.

5. Acceptance Stories
=====================

Scenario 01:
**Single Student Manually Enters Grades:**
I'm just starting my term, so I dont have many grades to enter so I only need
to create a new Student and add a couple homework assignments, quizes and exams.
I will create a blank text file with a name of my choosing ie "student.txt".

Then I start the Curved program, and follow the written instructions.

.. :
  Enter filename of students' data: student.txt
  Would you like to add another student (y/n)? y
  Name:James Marcos
  Number of assignment grades the student has: 5
  Assignment 2: 85
  Assignment 3: 95
  Assignment 4: 93
  Assignment 5: 94
  Number of quiz grades the student has: 5
  Quiz 1: 90
  Quiz 2: 92
  Quiz 3: 95
  Quiz 4: 93
  Quiz 5: 94
  Number of exam grades the student has: 1
  Exam 1: 90
 
  New student added!
 
  Would you like to add another student (y/n)? n

  Enter filename of output file for students' final grades: Grade.txt
 
  Would you like to curve the student's final grades (y/n)? n
 
  Final grades successfully written to 'Grade.txt'.

Open up 'Grade.txt':

.. :
  James Marcos,91.12,A-

Scenario 02:
**One Student Creates a Grades File Premade and enters it into Curved:**
I created a document with all of the information stored in it to be loaded into
Curved.py

File Named: Student.txt

.. :
  James Marcos|90.0,85.0,95.0,93.0,94.0|90.0,92.0,95.0,93.0,94.0|90.0

Open Curved, and followed prompt:

.. :
  Enter filename of students' data: student.txt

  Would you like to add another student (y/n)? n

  Enter filename of output file for students' final grades: Grade.txt

  Would you like to curve the student's final grades (y/n)? n

  Final grades successfully written to 'Grade.txt'.

File Names: Grade.txt:

.. :
  James Marcos,91.12,A-

Scenario 03:
**A teacher wants to give his students letter grades:**
I created a file with all of my students grades and calculate their letter
grade values.

File Named: Students.txt

.. :
  John Doe|85.0,92.0,88.0,92.0,95.0,94.0,91.0,90.0,93.0,92.0|86.0,89.0,89.0,85.0,84.0,91.0,93.0|
  89.0,86.0,85.0,87.0
  Emily Rose|80.0,90.0,84.0,82.0,84.0,89.0,87.0,86.0,87.0,85.0|82.0,89.0,86.0,80.0,85.0,80.0,82.0|
  92.0,91.0,92.0,80.0
  Erica Moss|84.0,81.0,78.0,77.0,75.0,84.0,84.0,82.0,75.0,85.0|75.0,75.0,75.0,84.0,77.0,85.0,78.0|
  83.0,81.0,76.0,84.0
  Michelle Jonas|84.0,83.0,82.0,84.0,74.0,83.0,83.0,78.0,71.0,79.0|76.0,79.0,75.0,73.0,82.0,78.0,81.0|
  83.0,71.0,78.0,74.0
  Kevin Omega|96.0,91.0,81.0,87.0,83.0,88.0,94.0,89.0,96.0,82.0|100.0,81.0,98.0,99.0,91.0,81.0,98.0|
  96.0,97.0,99.0,100.0
  Tiffany Lee|95.0,90.0,100.0,100.0,90.0,94.0,92.0,94.0,100.0,95.0|92.0,94.0,99.0,90.0,94.0,98.0,90.0|
  93.0,92.0,95.0,96.0
  Ricky Chua|78.0,66.0,65.0,75.0,67.0,68.0,67.0,72.0,75.0,79.0|68.0,75.0,67.0,75.0,68.0,70.0,80.0|
  75.0,71.0,68.0,65.0
  Annalise Sy|93.0,94.0,93.0,93.0,97.0,94.0,95.0,94.0,95.0,94.0|95.0,93.0,96.0,95.0,95.0,97.0,97.0|
  95.0,95.0,94.0,94.0
  Andrew Thomas|65.0,61.0,63.0,69.0,67.0,65.0,60.0,70.0,70.0,60.0|68.0,60.0,65.0,70.0,64.0,65.0,60.0|
  67.0,62.0,66.0,63.0
  Bob Davidler|50.0,59.0,51.0,51.0,58.0,59.0,57.0,68.0,59.0,68.0|55.0,50.0,52.0,61.0,55.0,66.0,67.0|
  60.0,54.0,55.0,60.0

Open Curved and followed the prompt:

.. :
  Enter filename of students' data: students.txt

  Would you like to add another student (y/n)? n

  Enter filename of output file for students' final grades: grades.txt

  Would you like to curve the student's final grades (y/n)? n

  Final grades successfully written to 'grades.txt'.

File Named: grades.txt

.. :
  John Doe,88.06,B+
  Emily Rose,86.48,B
  Erica Moss,80.13,B-
  Michelle Jonas,77.58,C+
  Kevin Omega,94.51,A
  Tiffany Lee,94.16,A
  Ricky Chua,70.67,C-
  Annalise Sy,94.72,A
  Andrew Thomas,64.62,D
  Bob Davidler,57.62,F

Scenario 04:
**A teacher wants to give his students letter grades with a curve:**
A teacher wants to give a letter grade for all the work his students have
completed, and then curve the grades.

File Name Students.txt

Open Curved and followed the prompt:

.. :
  Enter filename of students' data: students.txt

  Would you like to add another student (y/n)? n

  Enter filename of output file for students' final grades: grades.txt

  Would you like to curve the student's final grades (y/n)? y

  Final grades successfully written to 'grades.txt'.

File Named Grades.txt:

.. :
  John Doe,93.34,A
  Emily Rose,91.76,A-
  Erica Moss,85.41,B
  Michelle Jonas,82.87,B-
  Kevin Omega,99.79,A+
  Tiffany Lee,99.44,A+
  Ricky Chua,75.95,C
  Annalise Sy,100.00,A+
  Andrew Thomas,69.90,D+
  Bob Davidler,62.91,D-

**************
INSTRUCTIONS
**************

1. Installation
================

The Curved Program is all incompasing. No extra modules are required for execution.

2. Executing Curved.py
=======================
**Formatting input file:**

When you are planning on importing a list of students, or just one Student by using the following format:
::
    John Doe|85.0,92.0,88.0,92.0,95.0,94.0,91.0,90.0,93.0,92.0|86.0,89.0,89.0,85.0,84.0,91.0,93.0|89.0,86.0,85.0

The "|" seperators denote the transitions in grading weight.
::
    Student|Homework|Quizes|Tests

**Default Weight System:**

Assignments = 20%
Quizes      = 30%
Exams       = 50%

.. :
    It's simple to change the default weights as they are on the top of the Curved.py Program.
