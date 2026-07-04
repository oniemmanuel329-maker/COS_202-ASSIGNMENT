def run_cgpa_calculator():
    print("=" * 45)
    print("    PERSONAL POCKET CGPA CALCULATOR (PPC)    ")
    print("=" * 45)
    
    try:
        num_courses = int(input("How many courses do you want to calculate? "))
    except ValueError:
        print("Please enter a valid whole number next time.")
        return

    total_quality_points = 0
    total_units = 0
    
    print("\n--- Enter Your Course Details ---")
    
    for i in range(num_courses):
        print(f"\nCourse #{i + 1}:")
        code = input("  Course Code (e.g., GST111): ").strip().upper()
        
        try:
            units = int(input("  Credit Units (e.g., 2, 3, 4): "))
        except ValueError:
            print("  Invalid units! Skipping this course entry.")
            continue
            
        grade = input("  Letter Grade Earned (A, B, C, D, E, F): ").strip().upper()

        # Selection control statement mapping grades to academic weights
        if grade == 'A':
            grade_point = 5
        elif grade == 'B':
            grade_point = 4
        elif grade == 'C':
            grade_point = 3
        elif grade == 'D':
            grade_point = 2
        elif grade == 'E':
            grade_point = 1
        elif grade == 'F':
            grade_point = 0
        else:
            print(f"  Invalid Grade '{grade}' entered! Skipping this course.")
            continue

        # Calculate current score metrics
        quality_point = units * grade_point
        total_quality_points += quality_point
        total_units += units
        
        print(f"  Logged: {code} | Units: {units} | Grade Points: {quality_point}")

    # Final Summary Compilation Output
    print("\n" + "=" * 45)
    print("             FINAL CGPA REPORT               ")
    print("=" * 45)
    print(f" Total Registered Units : {total_units}")
    print(f" Total Quality Points   : {total_quality_points}")
    
    if total_units > 0:
        cgpa = total_quality_points / total_units
        print(f" Final Calculated CGPA  : {cgpa:.2f}")
    else:
        print(" Final Calculated CGPA  : 0.00 (No units recorded)")
    print("=" * 45)

if __name__ == "__main__":
    run_cgpa_calculator()
