students_number=0
Students=[]
running = True
#%%
while running:
    print(f"STUDENT GRADE MANAGEMENT: \n 1. Add Student \n 2. Show Students \n 3. Search Student \n 4. Calculate Average \n 5. Show Statistics \n 6. Exit")
    option = int(input("Choose an option: "))

    #Add Student-->option1
    if option==1:
        subjectWithGrade = {}

        student_name = str(input("Enter your name: "))
        student_age = int(input ("Enter your age : "))
        student_department = str(input("Enter your department: "))
        student_NumOfSubjects = int(input("How many subjects?"))
        students_number+=1

        #enter subjects and grades
        for x in range(1,student_NumOfSubjects+1):
            subject_name= input(f"Enter name of subject {x}: ")

            subject_grade= int(input(f"Enter grade for subject{x}:"))
            while subject_grade<0 or subject_grade>100:
                print("Invalid grade! \n Grade must be between 0 and 100.")
                subject_grade = int(input(f"Enter grade for subject {x}: "))
            subjectWithGrade[subject_name]=subject_grade

        average= sum(subjectWithGrade.values())/student_NumOfSubjects
        if average >= 85:
            Status="Excellent"
        elif average >=75:
            Status="Very Good"
        elif average >=60:
            Status="Good"
        elif average >=50:
            Status="passed"
        else:
            Status="failed"
        #addition
        Students.append({
            "name":student_name,
            "age":student_age,
            "Department":student_department,
            "subjects":subjectWithGrade,
            "average":average,
            "Status":Status})
    
    #Show students-->option 2
    elif option==2:
        print("Students: ")
        print(Students)
    
    #Search Student-->option3
    elif option==3:
        searched_name=str(input("enter the name: "))
        found = False

        for a in Students:
            if searched_name == a["name"]:
                print (f"name: {a['name']} \n age: {a['age']} \n department: {a['Department']}")
                print(f"subject&grades: {a['subjects']} \n average: {a['average']} \n Status: {a['Status']}")
                found = True
                break
        if not found:
            print("Student not found.")

    #avarage-->option4
    elif option == 4:
        flag = False
        student_to_avg = str(input("enter the name:"))
        for sav in Students:
            if student_to_avg == sav["name"]:
                print(f"average: {sav['average']} \n Status: {sav['Status']}")
                flag = True
                break
        if not flag:
            print("Student not found.")

    #Show Statistics-->option 5
    if option==5 and Students:
        listOfAverage =[]
        listOfStatus=[]
        NumberOFExcellent=0
        NumberOFVeryGood=0
        NumberOFGood=0
        NumberOFPassed=0
        NumberOfFailed=0

        #Total Students
        print(f"Total Students: {len(Students)}")
        
        #Highest and Lowest Average
        for c in Students:
            listOfAverage.append(c['average'])
            listOfStatus.append(c['Status'])
        print(f"Highest Average: {max(listOfAverage)}")
        print(f"Lowest Average: {min(listOfAverage)}")

        #Class Average
        print(f"Class Average: {sum(listOfAverage)/len(listOfAverage)}")

        #Number of each Status
        for st in listOfStatus:
            if st=="Excellent":
                NumberOFExcellent+=1
            elif st=="Very Good":
                NumberOFVeryGood+=1
            elif st=="Good":
                NumberOFGood +=1
            elif st=="passed":
                NumberOFPassed+=1
            elif st=="failed":
                NumberOfFailed+=1
        
        print(f"Number of Excellent: {NumberOFExcellent} \nNumber of Very Good: {NumberOFVeryGood}")
        print(f"Number of Good: {NumberOFGood}\nNumber of Passed: {NumberOFPassed} \nNumber of Failed: {NumberOfFailed}")

    elif option==5 and not Students:
        print("NO STUDENTS FOUND")
    
    elif option == 6:
        running = False
        print("Goodbye!")
    

# %%
