def filter_student_info(first_name, last_name, student_id):
    # Create a dictionary to store the student information
    student_info = {
        "First Name": first_name,
        "Last Name": last_name,
        "ID": student_id
    }
    
    # Filter out values that are "000"
    filtered_info = {key: value for key, value in student_info.items() if value != "000"}
    
    return filtered_info

# Example usage:
first_name = "John"
last_name = "Doe"
student_id = "000123"
filtered_student_info = filter_student_info(first_name, last_name, student_id)
print(filtered_student_info)
