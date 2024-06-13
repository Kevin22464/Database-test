import sqlite3  # Import the sqlite3 module to interact with the SQLite database

def login_system():
    # Username and password
    username = "admin"
    password = "password"
    
    # Prompt the user to enter username and password
    input_username = input("Enter your username: ")
    input_password = input("Enter your password: ")
    
    # Check if the entered username and password match the hardcoded values
    if input_username == username and input_password == password:
        print("Login successful!")
        return True
    else:
        print("Incorrect username or password.")
        return False
    
def print_cars_by_price():
    # Print all cars from the database ordered by price
    db = sqlite3.connect('Database Test (Cars).db') 
    cursor = db.cursor()  # Create a cursor object to execute SQL queries
    cursor.execute('''
        SELECT c.car_name, m.manufacturer AS manufacturer, co.country AS made_in, c.top_speed, c.approx_price
        FROM Cars c
        JOIN manufacturer m ON c.manufacturer = m.manu_id
        JOIN made_in co ON c.made_in = co.made_id
        ORDER BY c.approx_price;
    ''') 
    results = cursor.fetchall()  # Fetch all results from the executed query
    print_header()  
    print_results(results)  
    db.close()  # Close the database connection

def print_cars_by_manufacturer(manufacturer):
    # Print all cars from a specific manufacturer ordered by price
    db = sqlite3.connect('Database Test (Cars).db')
    cursor = db.cursor()  # Create a cursor object to execute SQL queries
    cursor.execute('''
        SELECT c.car_name, m.manufacturer AS manufacturer, co.country AS made_in, c.top_speed, c.approx_price
        FROM Cars c
        JOIN manufacturer m ON c.manufacturer = m.manu_id
        JOIN made_in co ON c.made_in = co.made_id
        WHERE m.manufacturer = ?
        ORDER BY c.approx_price;
    ''', (manufacturer,))  
    results = cursor.fetchall()  # Fetch all results from the executed query
    print_header()  
    print_results(results) 
    db.close()  # Close the database connection

def print_cars_by_speed_range(min_speed, max_speed):
    db = sqlite3.connect('Database Test (Cars).db')
    cursor = db.cursor()
    cursor.execute('''
        SELECT c.car_name, m.manufacturer AS manufacturer, co.country AS made_in, c.top_speed, c.approx_price
        FROM Cars c
        JOIN manufacturer m ON c.manufacturer = m.manu_id
        JOIN made_in co ON c.made_in = co.made_id
        WHERE c.top_speed BETWEEN ? AND ?
        ORDER BY c.top_speed;
    ''', (min_speed, max_speed))
    results = cursor.fetchall()
    print_header()
    print_results(results)
    db.close()

def print_header():
    # Print the header of the table with fixed widths for each column
    print(" _________________________________________________________________________________________________________________")
    print(f"| {'Car Name':<35} | {'Manufacturer':<20} | {'Made In':<20} | {'Top Speed':<10} | {'Price':>14} |")
    print("|-------------------------------------|----------------------|----------------------|------------|----------------|")

def print_results(results):
    # Print the results of the SQL query in a formatted table
    for car in results: 
        print(f"| {car[0]:<35} | {car[1]:<20} | {car[2]:<20} | {car[3]:<10} | ${car[4]:>13,.2f} |")  # Print each car's details in a formatted row
    print("|_____________________________________|______________________|______________________|____________|________________|")  # Print a closing line for the table

def main():
    # Main function to handle user input and switch between options
    if login_system():
        user_input = '0'
        while user_input != '4':
            print("What do you want to do?\n1. Print all cars by price\n2. Print cars by manufacturer\n3. Print cars by top speed range\n4. Exit program")
            user_input = input()
            if user_input == '1':
                print_cars_by_price()
            elif user_input == '2':
                while True:
                    manufacturer = input("Please enter manufacturer name (or 'back' to go back, 'exit' to exit program):\n")
                    if manufacturer.lower() == 'back':
                        break
                    elif manufacturer.lower() == 'exit':
                        user_input = '4'
                        break
                    else:
                        print_cars_by_manufacturer(manufacturer)
            elif user_input == '3':
                min_speed = input("Enter minimum top speed: ")
                max_speed = input("Enter maximum top speed: ")
                print_cars_by_speed_range(min_speed, max_speed)
            elif user_input == '4':
                break
            else:
                print("That is not an option.")
    else:
        print("ACCESS DENIED")

if __name__ == "__main__":
    main()  # Run the main function when the script is executed
