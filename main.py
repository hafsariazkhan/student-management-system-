from database import connect_db

# ---------------- GRADE FUNCTION ----------------
def calculate_grade(marks):
    if marks >= 85:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 50:
        return "C"
    else:
        return "F"

# ---------------- ADD STUDENT ----------------
def add_student():
    name = input("Enter student name: ")
    roll = input("Enter roll number: ")
    marks = int(input("Enter marks: "))
    grade = calculate_grade(marks)

    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO students (name, roll_no, marks, grade) VALUES (?, ?, ?, ?)",
        (name, roll, marks, grade)
    )
    conn.commit()
    conn.close()

    print("✅ Student added successfully!")

# ---------------- VIEW STUDENTS ----------------
def view_students():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    records = cursor.fetchall()
    conn.close()

    print("\nID | Name | Roll No | Marks | Grade")
    print("-" * 40)
    for row in records:
        print(row)

# ---------------- UPDATE STUDENT ----------------
def update_student():
    student_id = input("Enter student ID to update: ")
    new_marks = int(input("Enter new marks: "))
    new_grade = calculate_grade(new_marks)

    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE students SET marks = ?, grade = ? WHERE id = ?",
        (new_marks, new_grade, student_id)
    )
    conn.commit()
    conn.close()

    print("✅ Student record updated successfully!")

# ---------------- DELETE STUDENT ----------------
def delete_student():
    student_id = input("Enter student ID to delete: ")

    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute(
        "DELETE FROM students WHERE id = ?",
        (student_id,)
    )
    conn.commit()
    conn.close()

    print("🗑️ Student deleted successfully!")

# ---------------- MENU ----------------
def menu():
    while True:
        print("\n🎓 Student Management System")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            view_students()
            update_student()
        elif choice == "4":
            view_students()
            delete_student()
        elif choice == "5":
            print("👋 Exiting...")
            break
        else:
            print("❌ Invalid choice")

# ---------------- RUN PROGRAM ----------------
menu()