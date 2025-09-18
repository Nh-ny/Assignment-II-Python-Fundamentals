# classroom.py
# Name: Nayeon Kim
# Student ID: u3309753
# Date: 17-09-2025

# Room state
room = {
    "projector_on": False,
    "capacity": 30,
    "topic": ""
}

# Attendance set
attendance = set()

# Temperature readings
temperatures = []

# --- Functions (skeletons) ---

def toggle_projector():
    # Toggle projector status
    pass

def set_topic():
    # Set the class topic
    pass

def add_student():
    # Add a student to attendance
    pass

def remove_student():
    # Remove a student from attendance
    pass

def add_temperature():
    # Add a temperature reading and check for warnings
    pass

def get_stats():
    # Return min, max, avg as a tuple
    pass

def show_report():
    # Print classroom status and stats
    pass

# --- Main loop ---

def main():
    while True:
        # Display menu options
        choice = input("Enter your choice: ")

        if choice == "1":
            toggle_projector()

        elif choice == "2":
            set_topic()

        elif choice == "3":
            add_student()

        elif choice == "4":
            remove_student()

        elif choice == "5":
            add_temperature()

        elif choice == "6":
            show_report()

        elif choice == "7":
            print("Exiting program.")
            break

        else:
            print("Invalid option. Please try again.")

# Run the program
if __name__ == "__main__":
    main()
