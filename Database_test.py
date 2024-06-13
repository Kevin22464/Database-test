import sqlite3  # Import the sqlite3 module to interact with the SQLite database

def login_system():
    # Username and password
    username = "admin"
    password = "password"
    
    # Ask the user to enter username and password
    print("Hint : The username and password is hidden in this word : dapgdabmsxiscnwvholnrlkd")
    input_username = input("Enter username: ")
    input_password = input("Enter password: ")
    
    # Check if the entered username and password is correct
    if input_username == username and input_password == password:
        print("Login successful!")
        return True  # Return True if login is successful
    else:
        print("Incorrect username or password.")
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
    # Connect to the database
    db = sqlite3.connect('Database Test (Cars).db')
    cursor = db.cursor()  # Create a cursor to execute SQL queries
    
    # Execute a SQL query to select car details for a specific manufacturer ordered by price
    cursor.execute('''
        SELECT c.car_name, m.manufacturer AS manufacturer, co.country AS made_in, c.top_speed, c.approx_price
        FROM Cars c
        JOIN manufacturer m ON c.manufacturer = m.manu_id
        JOIN made_in co ON c.made_in = co.made_id
        WHERE m.manufacturer = ?
        ORDER BY c.approx_price;
    ''', (manufacturer,))  
    results = cursor.fetchall()  # Fetch all results from the executed query
    print_header()  # Print the table header
    print_results(results)  # Print the query results
    db.close()  # Close the database connection

def print_cars_by_speed_range(min_speed, max_speed):
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
    print(" ______________________________________________________________________________________________________________")
    print(f"| {'Car Name':<35} | {'Manufacturer':<20} | {'Made In':<20} | {'Top Speed':<10} | {'Price':>11} |")
    print("|-------------------------------------|----------------------|----------------------|------------|-------------|")

def print_results(results):
    # Print the results of the SQL query in a formatted table
    for car in results: 
        # Print each car's details
        print(f"| {car[0]:<35} | {car[1]:<20} | {car[2]:<20} | {car[3]:<10} | ${car[4]:>10,.0f} |")  
    # Print a closing line for the table
    print("|_____________________________________|______________________|______________________|____________|_____________|")  

def main():
    # Main function to handle user input and switch between options
    if login_system():  # Check if the login is successful
        user_input = '0'
        while user_input != '4':
            print("What do you want to do?\n1. Print all cars by price\n2. Print cars by manufacturer\n3. Print cars by top speed range\n4. Exit program")
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
                min_speed = input("Enter minimum top speed: ")
                max_speed = input("Enter maximum top speed: ")
                print_cars_by_speed_range(min_speed, max_speed)  # Print cars by top speed range
            elif user_input == '4':
                print("Have a nice day!")
                break  # Exit the program
            else:
                print("That is not an option.")
    else:
        print("ACCESS DENIED")  # Deny access if login fails

if __name__ == "__main__":
    main()  # Run the main function when the script is executed
