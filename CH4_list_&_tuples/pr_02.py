# Write a program to accept the marks of 6 students and display them in a sorted manner.
m1 = int(input("marks of student 1: "))
m2 = int(input("marks of student 2: ")) 
m3 = int(input("marks of student 3: "))
m4 = int(input("marks of student 4: ")) 
m5 = int(input("marks of student 5: ")) 
m6 = int(input("marks of student 6: ")) 

markslist = [m1, m2, m3, m4, m5, m6]

markslist.sort()

print(markslist)                            