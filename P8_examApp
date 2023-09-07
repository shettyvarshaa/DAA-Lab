def calculate_min_time_slots(subjects):
    common_students = {}
    for subject in subjects:
        for student in subject:
            common_students[student] = common_students.get(student, 0) + 1

    return max(common_students.values())

def main():
    # Example usage
    subjects = [
        ["Maths", "Chem", "Bio"],
        ["English", "Hindi"],
        ["Chem", "Bio", "Physics"],
        ["Maths", "Physics"]
    ]

    min_time_slots = calculate_min_time_slots(subjects)
    print("Minimum Time Slots Needed:", min_time_slots)

if __name__ == "__main__":
    main()