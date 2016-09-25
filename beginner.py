from statistics import mean as mean

adminDict = {'Python': 'Pass123', 'user2': 'pass2'}

studentDict = {"Josh": [78, 65, 79, 93],
               'Steve': [90, 12, 79, 60],
               'John': [78, 45, 99, 85]}


def enterGrades():
    studentName = input('Student: ')
    gradeToEnter = input('Grade: ')

    if studentName in studentDict:
        studentDict[studentName].append(float(gradeToEnter))
        print "Adding Grade...."
    else:
        print 'Student does not exist'

    print studentDict


def addStudent():
    studentToAdd = input('Student: ')

    if studentToAdd in studentDict:
        print('Student Already Exists')
    else:
        studentDict[studentToAdd] = []

    print(studentDict)


def removeStudent():
    studentToRemove = input('Student: ')

    if studentToRemove in studentDict:
        print("Removing Student....")
        del studentDict[studentToRemove]
    else:
        print('Student does not exist')

    print(studentDict)


def averageStudentGrade():
    studentToAverage = input('Student: ')

    if studentToAverage in studentDict:
        gradeList = studentDict[studentToAverage]
        avgGrade = mean(gradeList)
        # Removes need for statistics dependency
        # avgGrade = sum(gradeList)/ len(gradeList)
        print(studentToAverage, 'has average grade of', avgGrade)
    else:
        print('Student does not exist')


def main():
    print("""
    Welcome to Grade Central

    [1] - Enter Grades
    [2] - Add Students
    [3] - Remove Students
    [4] - Student Average Grade
    [5] - Exit
    """)

    entry = input("What would you like to do? (Enter a number) ")

    if entry == '1':
        enterGrades()
    elif entry == '2':
        addStudent()
    elif entry == '3':
        removeStudent()
    elif entry == '4':
        averageStudentGrade()
    elif entry == '5':
        exit()
    else:
        print('No Valid choice was given')


login = input('Username: ')
password = input('Password: ')

if login in adminDict:
    if adminDict[login] == password:
        print('Welcome,', login)
        while True:
            main()
    else:
        print('invalid password')
else:
    print('invalid username')
