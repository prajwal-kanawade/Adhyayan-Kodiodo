class InvalidMarksException(Exception):
    pass

def get_marks():
    try:
        marks = float(input("Enter your marks in percentage:"))
        if marks < 0 or marks > 100:
            raise InvalidMarksException("Marks must be from 0 to 100.")
        
        print(f"You got {marks} marks!")
    
    except InvalidMarksException as e:
        print(f"InvalidMarksException: {e}")
    except ValueError:
        print("Invalid input! Please enter a numeric value.")

if __name__ == "__main__":
    get_marks()
