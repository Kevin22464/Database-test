import sqlite3  # Import the sqlite3 module to interact with the SQLite database

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
    user_input = '0'  # Set user input to '0'
    while user_input != '3':  # Loop until the user chooses to exit
        print("What do you want to do?\n1. Print all cars by price\n2. Print cars by manufacturer\n3. Exit program")  # Print menu options
        user_input = input()  # Get user input
        if user_input == '1':
            print_cars_by_price()  # Print all cars ordered by price
        elif user_input == '2':
            while True:
                manufacturer = input("Please enter manufacturer name (or 'back' to go back, 'exit' to exit program):\n")  # Prompt user to enter a manufacturer name
                if manufacturer.lower() == 'back':  # Check if user wants to go back
                    break  # Exit the inner loop
                elif manufacturer.lower() == 'exit':  # Check if user wants to exit the program
                    user_input = '3' 
                    break  # Exit the inner loop
                else:
                    print_cars_by_manufacturer(manufacturer)  # Print cars by the specified manufacturer
        elif user_input == '3':
            break  # Exit the outer loop to end the program
        else:
            print("That is not an option.")  # Print an error message for invalid inputs

if __name__ == "__main__":
    main()  # Run the main function when the script is executed


print("hi")
print("hi")
print("hi")
print("hi")
print("hi")
print("hi")
print("hi")