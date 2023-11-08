try:
    grade = int(input("Input your grade: "))
except:
    print("That's not an integer, I bet it!")
    exit(-1)
    

if grade < 0 or grade > 100:
    print("Invalid grade")
    exit(0)

if grade < 60:
    print("不合格")
elif grade >=60 and grade <= 74:
    print("及格")
elif grade >=75 and grade <= 89:
    print("良好")
elif grade >= 90:
    print("优秀")