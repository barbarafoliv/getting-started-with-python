# Student Grade Evaluation and Course Result Calculation

if __name__=='__main__':
    
    # Identify a student by his/her name.
    name = input("Insert the student's name: ")

    subject1 = -1
    subject2 = -1
    subject3 = -1


    # Identify the student's grades on 3 subjects.
    print("Subject's grade must be a value between 0 and 20.")
    while(subject1<0 or subject1>20):
        subject1 = int(input("Insert the grade of the subject 1: "))
    
    while(subject2<0 or subject2>20):
        subject2 = int(input("Insert the grade of the subject 2: "))
    
    while(subject3<0 or subject3>20):
        subject3 = int(input("Insert the grade of the subject 3: "))
    
    allSubjectsGrades = [subject1, subject2, subject3]
    allSubjectsObservations = []


    # Verify observation for each subject.
    for i, grade in enumerate(allSubjectsGrades):
        if(grade<10):
            observation="Not Approved"
        elif(grade<16):
            observation="Approved"
        else:
            observation="Approved with Distinction"
        allSubjectsObservations.append(observation)
    

    # Calculate final average of the Course.
    finalCourseGrade = -1
    if(subject1>10 and subject2>10 and subject3>10):
        finalCourseGrade = (subject1 + subject2 + subject3) / 3
    

    # Show the results. 
    print(f"The student {name} had the following results:")
    
    for i, grade in enumerate(allSubjectsGrades):
        print(f"{grade} - {allSubjectsObservations[i]}")
    
    if(finalCourseGrade<0):
        print(f"The student {name} is not approved at this Course.")
    elif(finalCourseGrade<16):
        print(f"The student {name} is approved at this course with the final average of {finalCourseGrade:2.1f}.")
    else:
        print(f"The student {name} is approved with distinction at this course with the final average of {finalCourseGrade:2.1f}.")
        print("Good job!")