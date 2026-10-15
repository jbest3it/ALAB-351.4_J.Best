# Define a function get_average_grade(grades_tuple) that takes a tuple of numeric grades and returns the average. 
def get_average_grade(grades_tuple):
    if not grades_tuple:
        print("Warning: The grades tuple is empty. Cannot compute average.")
        return None
    return sum(grades_tuple) / len(grades_tuple)

# Include a try/except to handle the case if the tuple is empty (to avoid division by zero), returning None or printing a warning in that case.
try:
    average = get_average_grade((90, 85, 92))
    print(f"The average grade is: {average}")
    
    average_empty = get_average_grade(())
    print(f"The average grade for empty tuple is: {average_empty}")
except Exception as e:
    print(f"An error occurred while calculating the average: {e}")

# Define a dictionary course_grades where keys are course names (e.g., “Math”, “Science”, “History”) and values are tuples of grades.
course_grades = {
    "Math": (90, 85, 92),
    "Science": (88, 79, 95),
    "History": (70, 80, 75),
    # Empty tuple for exception handling
    "Art": ()  
}

# Use a loop to iterate over course_grades. For each course, call get_average_grade(grades_tuple) and print the message: "The average grade for Math is 85.2". 
for course, grades in course_grades.items():
    try:
        average = get_average_grade(grades)
        if average is not None:
            print(f"The average grade for {course} is: {average:.2f}")
        
        # Handle any None values or exceptions gracefully.
        else:
            print(f"The average grade for {course} could not be calculated due to empty grades.")
    except Exception as e:
        print(f"An error occurred while calculating the average for {course}: {e}")



