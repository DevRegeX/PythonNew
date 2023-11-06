while True:
# Show the items can be selected in the menu.
    print("Menu:")
    print("1. Add a new student and their score to the list.")
    print("2. Display the list of students and their marks.")
    print("3. Calculate and display the average score of all students.")
    print("4. Display names of students who scored more than a certain threshold..")
    print("5. Exit the program.")
    
# Get The user Choice.
    choice = input("Please Enter your choice (1/2/3/4/5): ")
    
# Option 1: Add a new student and their score to the list.
    if choice == "1":
        name = input("Enter the student's name: ")
        score = int(input("Enter the student's score: "))
        scores.append((name,score))
        print("Student added successfully.")
    
# Option 2: Display the list of students and their marks.
    elif choice == "2":
        if not scores:
            print("No students in the list.")
        else:
            print("List of students and their marks:")
            for student in scores:
                print(f"Name: {student[0]}, Score: {student[1]}")
   
# Option 3: Calculate and display the average score of all students. 
    elif choice == "3":
        if not scores:
            print("No students in the list.")
        else:
            total_score = sum(score for _, score in student_scores)
            average_score = total_score / len(student_scores)
            print(f"Average score of all students: {average_score:.2f}")
 
# Option 4: Display names of students who have scored more than a certain threshold.       
    elif choice == "4":
        threshold = int(input("Enter the threshold score: "))
        print(f"Students who scored more than {threshold}:")
        for student in scores:
            if student[1] > threshold:
                print(student[0]) 
           
# Option 5: Exut the program.    
    elif consent == "5": 
        print("Exiting the program . Thank You")
        break
    
    else:
        # Handle invalid input.
        print("Invalid choice.Please enter a valid option (1/2/3/4/5).")
