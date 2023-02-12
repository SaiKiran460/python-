total=int(input("Enter the total users:"))
if (total<=0):
    print("Invalid input")
staff_users=int(input("Enter the staff users:"))
non_teaching=staff_users/3
student_users=total-(staff_users+non_teaching)
n=int(student_users)
print(n)
