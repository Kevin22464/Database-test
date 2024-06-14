import sqlite3  # Import the sqlite3 module to interact with the SQLite database

# ANSI colours
RESET_COLOR = "\033[0m"
RED = "\033[31m"
GREEN = "\033[32m"
BLUE = "\033[34m"
CYAN = "\033[36m"
PINK = "\033[95m"

def login_system():
    # Username and password
    username = "admin"
    password = "password"
    
    # Ask the user to enter username and password
    print(BLUE + "Hint: The username and password are hidden in this word: dapgdabmsxiscnwvholnrlkd" + RESET_COLOR)
    input_username = input("Enter username: ")
    input_password = input("Enter password: ")
    
    # Check if the entered username and password is correct
    if input_username == username and input_password == password:
        print(GREEN + "Login successful!" + RESET_COLOR)
        return True  # Return True if login is successful
    else:
        print(RED + "Incorrect username or password." + RESET_COLOR)
        return False  # Return False if login fails

def print_cars_by_price():
    # Connect to the database
    db = sqlite3.connect('Database Test (Cars).db')
    cursor = db.cursor()  # Create a cursor to execute SQL queries
    
    # Execute a SQL query to select car details ordered by price
    cursor.execute('''
        SELECT c.car_name, m.manufacturer AS manufacturer, co.country AS made_in, c.top_speed, c.approx_price
        FROM Cars c
        JOIN manufacturer m ON c.manufacturer = m.manu_id
        JOIN made_in co ON c.made_in = co.made_id
        ORDER BY c.approx_price;
    ''')
    results = cursor.fetchall()  # Fetch all results from the executed query
    print_header()  # Print the table header
    print_results(results)  # Print the query results
    db.close()  # Close the database connection

def print_cars_by_manufacturer(manufacturer):
    # Convert manufacturer to lowercase
    manufacturer = manufacturer.lower()
    
    # Connect to the database
    db = sqlite3.connect('Database Test (Cars).db')
    cursor = db.cursor()  # Create a cursor to execute SQL queries
    
    # Execute a SQL query to select car details for a specific manufacturer ordered by price
    cursor.execute('''
        SELECT c.car_name, m.manufacturer AS manufacturer, co.country AS made_in, c.top_speed, c.approx_price
        FROM Cars c
        JOIN manufacturer m ON c.manufacturer = m.manu_id
        JOIN made_in co ON c.made_in = co.made_id
        WHERE LOWER(m.manufacturer) = ?
        ORDER BY c.approx_price;
    ''', (manufacturer,))
    results = cursor.fetchall()  # Fetch all results from the executed query
    print_header()  # Print the table header
    print_results(results)  # Print the query results
    db.close()  # Close the database connection

def print_cars_by_speed_range(min_speed, max_speed):
    # Convert speed inputs to integers
    min_speed = int(min_speed)
    max_speed = int(max_speed)
    
    # Connect to the database
    db = sqlite3.connect('Database Test (Cars).db')
    cursor = db.cursor()  # Create a cursor to execute SQL queries
    
    # Execute a SQL query to select car details within a specific speed range ordered by top speed
    cursor.execute('''
        SELECT c.car_name, m.manufacturer AS manufacturer, co.country AS made_in, c.top_speed, c.approx_price
        FROM Cars c
        JOIN manufacturer m ON c.manufacturer = m.manu_id
        JOIN made_in co ON c.made_in = co.made_id
        WHERE c.top_speed BETWEEN ? AND ?
        ORDER BY c.top_speed;
    ''', (min_speed, max_speed))
    results = cursor.fetchall()  # Fetch all results from the executed query
    print_header()  # Print the table header
    print_results(results)  # Print the query results
    db.close()  # Close the database connection

def print_header():
    # Print the header of the table with fixed widths for each column
    print(CYAN + " ______________________________________________________________________________________________________________" + RESET_COLOR)
    print(CYAN + f"| {'Car Name':<35} | {'Manufacturer':<20} | {'Made In':<20} | {'Top Speed':<10} | {'Price':>11} |" + RESET_COLOR)
    print(CYAN + "|-------------------------------------|----------------------|----------------------|------------|-------------|" + RESET_COLOR)

def print_results(results):
    # Print the results of the SQL query in a formatted table
    for car in results:
        # Print each car's details
        print(CYAN + f"| {car[0]:<35} | {car[1]:<20} | {car[2]:<20} | {car[3]:<10} | ${car[4]:>10,.0f} |" + RESET_COLOR)
    # Print a closing line for the table
    print(CYAN + "|_____________________________________|______________________|______________________|____________|_____________|" + RESET_COLOR)

def main():
    # Main function to handle user input and switch between options
    if login_system():  # Check if the login is successful
        user_input = '0'
        while user_input != '4':
            print(PINK + "What do you want to do?\n1. Print all cars by price\n2. Print cars by manufacturer\n3. Print cars by top speed range\n4. Exit program" + RESET_COLOR)
            user_input = input()
            if user_input == '1':
                print_cars_by_price()  # Print all cars by price
            elif user_input == '2':
                while True:
                    manufacturer = input("Please enter manufacturer name (or 'back' to go back, 'exit' to exit program):\n")
                    if manufacturer.lower() == 'back':
                        break  # Go back to the main menu
                    elif manufacturer.lower() == 'exit':
                        user_input = '4'
                        break  # Exit the program
                    else:
                        print_cars_by_manufacturer(manufacturer)  # Print cars by the specified manufacturer
            elif user_input == '3':
                min_speed = input(GREEN + "Enter minimum top speed: " + RESET_COLOR)
                max_speed = input(RED + "Enter maximum top speed: " + RESET_COLOR)
                print_cars_by_speed_range(min_speed, max_speed)  # Print cars by top speed range
            elif user_input == '4':
                print(GREEN + "Have a nice day!" + RESET_COLOR)
                break  # Exit the program
            else:
                print(RED + "That is not an option." + RESET_COLOR)
    else:
        print(RED + "ACCESS DENIED" + RESET_COLOR)

if __name__ == "__main__":
    main()  # Run the main function when the script is executed
