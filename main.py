import sqlite3
import pandas as pd

# Connect to the database
def connect_db():
    return sqlite3.connect('flight.db')


def create_table():
    connect = connect_db()
    cursor = connect.cursor()

    #Create airports table
    cursor.execute("""CREATE TABLE IF NOT EXISTS airports(
    airport_id INTEGER PRIMARY KEY AUTOINCREMENT, 
    name VARCHAR(20), 
    country VARCHAR(20), 
    airport_code VARCHAR(20) UNIQUE );
 """)

    #Create flights table 
    cursor.execute("""CREATE TABLE IF NOT EXISTS flights ( 
    flight_id INTEGER PRIMARY KEY AUTOINCREMENT, 
    origin_airport_id INT, 
    destination_airport_id INT, 
    departure_date DATE, 
    departure_time TIME, 
    arrival_time TIME, 
    status VARCHAR(20), 
    pilot_id INTEGER, 
    FOREIGN KEY (origin_airport_id) REFERENCES airports(airport_id), 
    FOREIGN KEY (destination_airport_id) REFERENCES airports(airport_id), 
    FOREIGN KEY (pilot_id) REFERENCES pilots(pilot_id) ); """)

     #Create pilots table
    cursor.execute("""CREATE TABLE IF NOT EXISTS pilots (
    pilot_id INTEGER PRIMARY KEY AUTOINCREMENT, 
    name VARCHAR(20), 
    flight_hours INTEGER); """)

    connect.commit()
    connect.close()
    print("Tables have been construct")


def populate_table():
    connect = connect_db()
    cursor = connect.cursor()

    #Populate airports table
    cursor.execute("INSERT OR IGNORE INTO airports (name, country, airport_code) VALUES ('Paris', 'France', 'CDG');")
    cursor.execute("INSERT OR IGNORE INTO airports (name, country, airport_code) VALUES ('Bangkok', 'Thailand', 'BKK');")
    cursor.execute("INSERT OR IGNORE INTO airports (name, country, airport_code) VALUES ('London', 'UK', 'LHR');")
    cursor.execute("INSERT OR IGNORE INTO airports (name, country, airport_code) VALUES ('New York City', 'United States', 'JFK');")
    cursor.execute("INSERT OR IGNORE INTO airports (name, country, airport_code) VALUES ('Tokyo', 'Japan', 'HND');")
    cursor.execute("INSERT OR IGNORE INTO airports (name, country, airport_code) VALUES ('Singapore', 'Singapore', 'SIN');")
    cursor.execute("INSERT OR IGNORE INTO airports (name, country, airport_code) VALUES ('Dubai', 'United Arab Emirates', 'DXB');")
    cursor.execute("INSERT OR IGNORE INTO airports (name, country, airport_code) VALUES ('Sao Paulo', 'Brazil', 'GRU');")
    cursor.execute("INSERT OR IGNORE INTO airports (name, country, airport_code) VALUES ('Sydney', 'Australia', 'SYD');")
    cursor.execute("INSERT OR IGNORE INTO airports (name, country, airport_code) VALUES ('Jakarta', 'Indonesia', 'CGK');")


    #Populate flights table
    cursor.execute("""INSERT OR IGNORE INTO flights (flight_id, origin_airport_id, destination_airport_id, departure_date, 
                     departure_time, arrival_time, status, pilot_id) 
                     VALUES (1, 1, 2, '2024-12-01', '10:00', '12:30', 'On Time', 1);""")
    cursor.execute("""INSERT OR IGNORE INTO flights (flight_id, origin_airport_id, destination_airport_id, departure_date, 
                     departure_time, arrival_time, status, pilot_id) 
                     VALUES (2, 2, 3, '2024-12-02', '14:30', '16:45', 'Delayed', 2);""")
    cursor.execute("""INSERT OR IGNORE INTO flights (flight_id, origin_airport_id, destination_airport_id, departure_date, 
                     departure_time, arrival_time, status, pilot_id) 
                     VALUES (3, 3, 4, '2024-12-03', '09:45', '12:00', 'Cancelled', 3);""")
    cursor.execute("""INSERT OR IGNORE INTO flights (flight_id, origin_airport_id, destination_airport_id, departure_date, 
                     departure_time, arrival_time, status, pilot_id) 
                     VALUES (4, 4, 5, '2024-12-04', '16:00', '18:15', 'On Time', 4);""")
    cursor.execute("""INSERT OR IGNORE INTO flights (flight_id, origin_airport_id, destination_airport_id, departure_date, 
                     departure_time, arrival_time, status, pilot_id) 
                     VALUES (5, 5, 6, '2024-12-05', '13:00', '15:20', 'On Time', 5);""")
    cursor.execute("""INSERT OR IGNORE INTO flights (flight_id, origin_airport_id, destination_airport_id, departure_date, 
                     departure_time, arrival_time, status, pilot_id) 
                     VALUES (6, 6, 7, '2024-12-06', '17:30', '20:00', 'Delayed', 6);""")
    cursor.execute("""INSERT OR IGNORE INTO flights (flight_id, origin_airport_id, destination_airport_id, departure_date, 
                     departure_time, arrival_time, status, pilot_id) 
                     VALUES (7, 7, 8, '2024-12-07', '08:45', '11:10', 'Cancelled', 7);""")
    cursor.execute("""INSERT OR IGNORE INTO flights (flight_id, origin_airport_id, destination_airport_id, departure_date, 
                     departure_time, arrival_time, status, pilot_id) 
                     VALUES (8, 8, 9, '2024-12-08', '20:00', '22:30', 'On Time', 8);""")
    cursor.execute("""INSERT OR IGNORE INTO flights (flight_id, origin_airport_id, destination_airport_id, departure_date, 
                     departure_time, arrival_time, status, pilot_id) 
                     VALUES (9, 9, 10, '2024-12-09', '11:00', '13:45', 'On Time', 9);""")
    cursor.execute("""INSERT OR IGNORE INTO flights (flight_id, origin_airport_id, destination_airport_id, departure_date, 
                     departure_time, arrival_time, status, pilot_id) 
                     VALUES (10, 10, 1, '2024-12-10', '16:30', '19:00', 'Delayed', 10);""")



    #Populate pilots table
    # it keeps populating with out stopping
    cursor.execute("INSERT OR IGNORE INTO pilots (name, flight_hours) VALUES ('John Doe', 1500);")
    cursor.execute("INSERT OR IGNORE INTO pilots (name, flight_hours) VALUES ('Jane Smith', 2000);")
    cursor.execute("INSERT OR IGNORE INTO pilots (name, flight_hours) VALUES ('Michael Brown', 1700);")
    cursor.execute("INSERT OR IGNORE INTO pilots (name, flight_hours) VALUES ('Emily White', 10000);")
    cursor.execute("INSERT OR IGNORE INTO pilots (name, flight_hours) VALUES ('Jake Hadley', 20000);")
    cursor.execute("INSERT OR IGNORE INTO pilots (name, flight_hours) VALUES ('Nick Diaz', 3000);")
    cursor.execute("INSERT OR IGNORE INTO pilots (name, flight_hours) VALUES ('Jose Ochoa', 2800);")
    cursor.execute("INSERT OR IGNORE INTO pilots (name, flight_hours) VALUES ('Nick Klein', 9000);")
    cursor.execute("INSERT OR IGNORE INTO pilots (name, flight_hours) VALUES ('Walt Harris', 7800);")
    cursor.execute("INSERT OR IGNORE INTO pilots (name, flight_hours) VALUES ('Artem Vakhitov', 12000);")

    connect.commit()
    connect.close()
    print("Tables have been populated")


#This function is use to add flight
def add_flight( origin_airport_id, destination_airport_id, departure_date, departure_time,arrival_time, status, pilot_id):
    connect = connect_db()
    cursor = connect.cursor()

    cursor.execute(f""" INSERT INTO flights (origin_airport_id, destination_airport_id, departure_date, departure_time, arrival_time, status, pilot_id)
    VALUES ('{origin_airport_id}', '{destination_airport_id}', '{departure_date}', '{departure_time}', '{arrival_time}', '{status}', '{pilot_id}')""")
    connect.commit()
    print("Flight has been added")
    connect.close()


#This function is use to update flight information
def update_flight_information():
    connect = connect_db()
    cursor = connect.cursor()

    print("Available Flight ID: ")
    cursor.execute("""SELECT flights.flight_id,origin_airport.name AS origin_name, destination_airport.name AS destination_name
     FROM flights
     JOIN airports AS origin_airport ON flights.origin_airport_id = origin_airport.airport_id
     JOIN airports AS destination_airport ON flights.destination_airport_id = destination_airport.airport_id""")

    flights = cursor.fetchall()
    for i in flights:
        print(f"Flight ID: {i[0]}, Origin: {i[1]}, Destination: {i[2]}")

    while True:
        flight_id = input("Enter the flight ID to update: ").strip()
        if flight_id.isdigit():
            flight_id = int(flight_id)
            break
        else:
            print("Flight ID have to be a number")

    update_version = []
    value = []
    #Show origin ID and let user enter
    print("Available Origin Airport: ")
    cursor.execute("SELECT airport_id, name FROM airports")
    origin_airports = cursor.fetchall()
    for i in origin_airports:
        print(f"ID: {i[0]}, Name: {i[1]}")
    while True:
        new_origin_airport_id = input("Enter a new origin airport ID : ").strip()
        if new_origin_airport_id.isdigit():
            new_origin_airport_id = int(new_origin_airport_id)
            break
        else:
            print("Origin Airport ID must be a number")

    print("Available Destination Airport: ")
    cursor.execute("SELECT airport_id, name FROM airports")
    origin_airports = cursor.fetchall()
    for i in origin_airports:
        print(f"ID: {i[0]}, Name: {i[1]}")
    while True:
        new_destination_airport_id = input("Enter a new destination airport ID : ").strip()
        if new_destination_airport_id.isdigit():
            new_destination_airport_id = int(new_destination_airport_id)
            break
        else:
            print("Destination Airport ID must be a number")


    new_departure_date = input("Enter a new departure date (YYYY-MM-DD) : ").strip()
    new_departure_time = input("Enter a new departure time (HH:MM) : ").strip()
    new_arrival_time = input("Enter a new arrival time (HH:MM) : ").strip()

    #Show the available status
    available_status = ["On Time", "Delayed", "Cancelled"]
    for i in available_status:
        print(f"The available status are: {i} ")
    new_status = input("Enter a new status : ").strip()

    cursor.execute("SELECT pilot_id, name, flight_hours FROM pilots")
    pilot = cursor.fetchall()
    for i in pilot:
        print(f"The available pilots are ID: {i[0]}, Name: {i[1]}, Fligh Experience Hour: {i[2]}")
    new_pilot_id = input("Enter a new pilot ID : ").strip()

    # Check each input and append the corresponding SQL clause and value
    if new_origin_airport_id:
        update_version.append("origin_airport_id = ?")
        value.append(new_origin_airport_id)
    if new_destination_airport_id:
        update_version.append("destination_airport_id = ?")
        value.append(new_destination_airport_id)
    if new_departure_date:
        update_version.append("departure_date = ?")
        value.append(new_departure_date)
    if new_departure_time:
        update_version.append("departure_time = ?")
        value.append(new_departure_time)
    if new_arrival_time:
        update_version.append("arrival_time = ?")
        value.append(new_arrival_time)
    if new_status:
        update_version.append("status = ?")
        value.append(new_status)
    if new_pilot_id:
        update_version.append("pilot_id = ?")
        value.append(new_pilot_id)


    if update_version:
        value.append(flight_id)  
        cursor.execute(f"UPDATE flights SET {', '.join(update_version)} WHERE flight_id = ?", value)
        connect.commit()
        print("The flight has been updated.")
    else:
        print("The flight was not update")

    connect.close()



def assign_pilot():
    connect = connect_db()
    cursor = connect.cursor()

    cursor.execute("SELECT flight_id FROM flights")
    flight = cursor.fetchall()
    for i in flight:
        print(f"The available flight ID are: {i[0]}")

    while True:
        flight_id = input("Enter the flight id you want to assign the pilot: ").strip()
        if flight_id.isdigit():
            flight_id = int(flight_id)
            break
        else:
            print("Flight ID have to be a number")

    cursor.execute("SELECT pilot_id, name, flight_hours FROM pilots")
    pilot = cursor.fetchall()
    for i in pilot:
        print(f"The available pilots are ID: {i[0]}, Name: {i[1]}, Fligh Experience Hour: {i[2]}")
    while True:
        pilot_id = input("Enter the pilot id: ").strip()
        if pilot_id.isdigit():
            pilot_id = int(pilot_id)
            break
        else:
            print("Pilot ID have to be a number")


    #Check if flight id exist
    cursor.execute("SELECT flight_id FROM flights WHERE flight_id = ?", (flight_id,))
    if cursor.fetchone() is None: 
        print(f"The flight id of {flight_id} is invalid")
        connect.close()
        return 

    #Check if pilot  id exist
    cursor.execute("SELECT flight_id FROM flights WHERE pilot_id = ?", (pilot_id,))
    if cursor.fetchone() is None: 
        print(f"The pilot id of {pilot_id} is invalid")
        connect.close()
        return 

    #Update the pilot id for the assign flight 
    cursor.execute("UPDATE flights SET pilot_id = ? WHERE flight_id = ?", (pilot_id, flight_id))
    connect.commit()

    if cursor.rowcount > 0:
        print(f"Pilot id {pilot_id} has been assigned to flight id {flight_id}")
    else:
        print("Fail to assign")



#View pilot schedule
def pilot_schedule():
    connect = connect_db()
    cursor = connect.cursor()

    cursor.execute("SELECT pilot_id, name, flight_hours FROM pilots")
    pilot = cursor.fetchall()

    for i in pilot:
        print(f"The available pilots are ID: {i[0]}, Name: {i[1]}, Fligh Experience Hour: {i[2]}")    
    pilot_id = input("Enter the pilot id to check the schedule: ").strip()

    cursor.execute("SELECT flight_id, origin_airport_id, destination_airport_id, departure_date, departure_time, arrival_time, status FROM flights WHERE pilot_id = ? ORDER BY departure_date, departure_time", (pilot_id,))
    schedule = cursor.fetchall()
    for flight in schedule:
        print(f"Flight ID: {flight[0]}, Origin Airport ID: {flight[1]},Destination Aiport ID {flight[2]},  Departure Date: {flight[3]}, Departure Time: {flight[4]}, Arrival Time: {flight[5]}, Status: {flight[6]}")

    connect.close()


def view_update_destination():
    user = input("Press v to view and u to update: ").lower().strip()
    connect = connect_db()
    cursor = connect.cursor()

    if user == 'v':
        print("Available Destination Airport: ")
        cursor.execute("SELECT airport_id, name FROM airports")
        origin_airports = cursor.fetchall()
        for i in origin_airports:
            print(f"ID: {i[0]}, Name: {i[1]}")        
        destination_airport_id = input("Enter the destination airport id: ")
        cursor.execute("SELECT * FROM airports WHERE airport_id = ?", (destination_airport_id,))
        destination_info = cursor.fetchone()

        if destination_info:
            print(f"Airport ID: {destination_info[0]}")
            print(f"Destination Name: {destination_info[1]}")
            print(f"Country: {destination_info[2]}")
            print(f"Destination Airport Code: {destination_info[3]}")
        else:
            print("No destination airport ID was found")

    elif user == 'u':
        print("Available Destination Airport: ")
        cursor.execute("SELECT airport_id, name FROM airports")
        origin_airports = cursor.fetchall()
        for i in origin_airports:
            print(f"ID: {i[0]}, Name: {i[1]}")        
        destination_airport_id = input("Enter the Destination airport ID to update: ").lower().strip()
        cursor.execute("SELECT * FROM airports WHERE airport_id = ?", (destination_airport_id,))
        destination = cursor.fetchone()

        new_name = input("Enter the new city name: ").strip()
        new_country = input("Enter the new country: ").strip()
        new_code = input("Enter the new code: ").strip()

        update = []
        value = []

        if new_name:
            update.append("name = ?")
            value.append(new_name)
        if new_country:
            update.append("country = ?")
            value.append(new_country)
        if new_code:
            update.append("airport_code = ?")
            value.append(new_code)


        if update:
            value.append(destination_airport_id) 
            cursor.execute(f"UPDATE airports SET {', '.join(update)} WHERE airport_id = ?", value)
            connect.commit()
            print("The destination has been updated")
        else:
            print("No changes occured")

        connect.close()

def flight_by_criteria():
    connect = connect_db()
    cursor = connect.cursor()
    flight_information = ['flight_id', 'origin_airport_id','destination_airport_id', 'departure_date', 'departure_time','arrival_time', 'status', 'pilot_id']
    print("The available criteria includes: 'flight_id','origin_airport_id' ,'destination_airport_id', 'departure_date', 'departure_time','arrival_time', 'status', 'pilot_id")

    criteria = input("Enter the criteria: ").strip()

    if criteria not in flight_information:
        print("The criteria is invalid") 
        connect.close()
        return

    value = input(f"Enter the value for {criteria}: ").strip()
    query = (f"SELECT * FROM flights where {criteria} = ?")
    cursor.execute(query,(value,))
    flights = cursor.fetchall()
    connect.close()

    if flights:
        for flight in flights:
            print(flight)
    else:
        print("No criteria was found")

def create_new_destination():
    connect = connect_db()
    cursor = connect.cursor()

    print("Create a new destination")
    while True: 
        city_name = input("Enter the city name of the new destination: ").strip()
        if city_name.isalpha():
            break
        print("City name needs to be an alphabetic character")
    while True:
        country = input("Enter the country name of the new destination: ").strip()
        if country.isalpha():
            break
        print("City name needs to be an alphabetic character")

    while True:
        airport_code = input("Enter the airport code for the new destination: ").strip().upper()
        if airport_code.isalpha():
            break
        print("City name needs to be an alphabetic character")

    #Check if the city name, country and airport code are enter
    if not city_name or not country or not airport_code:
        print("All the new destination information needs to be filled out")
        return

    cursor.execute("SELECT * from airports WHERE airport_code = ?", (airport_code,))
    if cursor.fetchone():
        print(f"'{airport_code}' already exist")
        return


    cursor.execute("INSERT INTO airports (name, country, airport_code) VALUES (?,?,?)", (city_name, country, airport_code))
    connect.commit()
    print(f"{city_name}, {country}, {airport_code} have been created")


    connect.close()

def delete_information():
    connect = connect_db()
    cursor = connect.cursor()
    user_input = input("Press d to delete formation about the destination\n Press f to delete information about the flights\n Press p to delete information about the pilots\n Enter: ").strip().lower()

    if user_input == "d":
        cursor.execute("SELECT airport_id, name FROM airports")
        origin_airports = cursor.fetchall()
        for i in origin_airports:
            print(f"ID: {i[0]}, Name: {i[1]}")  
        destination_id = input("Enter the destination ID to delete: ")
        cursor.execute("SELECT * FROM airports WHERE airport_id = ?", (destination_id,))
        destination = cursor.fetchone()
        if not destination:
            print(f"No destination with ID '{destination_id}'")
        else:
            cursor.execute("DELETE FROM airports WHERE airport_id = ?", (destination_id,))
            connect.commit()
            print(f"'{destination_id} has been deleted'")

    if user_input == "f":
        cursor.execute("""SELECT flights.flight_id, origin_airport.name AS origin_name , destination_airport.name AS destination_name FROM flights
        JOIN airports AS origin_airport ON flights.origin_airport_id = origin_airport.airport_id
        JOIN airports AS destination_airport ON flights.destination_airport_id = destination_airport.airport_id """)
        flight = cursor.fetchall()
        for i in flight:
            print(f"ID: {i[0]}, Origin: {i[1]}, Destination: {i[2]}")  
        flight_id = input("Enter the flight ID to delete: ")
        cursor.execute("SELECT * FROM flights WHERE flight_id = ?", (flight_id,))
        flight = cursor.fetchone()
        if not flight:
            print(f"No flight with ID '{flight_id}'")
        else:
            cursor.execute("DELETE FROM flights WHERE flight_id = ?", (flight_id,))
            connect.commit()
            print(f"Flight ID: '{flight_id} has been deleted'")

    if user_input == "p":
        cursor.execute("SELECT pilot_id, name , flight_hours FROM pilots")
        pilot = cursor.fetchall()
        for i in pilot:
            print(f"ID: {i[0]}, Name: {i[1]}, Flight Hour: {i[2]}")  
        pilot_id = input("Enter the pilot ID to delete: ")
        cursor.execute("SELECT * FROM pilots WHERE pilot_id = ?", (pilot_id,))
        pilot = cursor.fetchone()
        if not pilot:
            print(f"No pilot with ID '{pilot_id}'")
        else:
            cursor.execute("DELETE FROM pilots WHERE pilot_id = ?", (pilot_id,))
            connect.commit()
            print(f"Pilot ID: '{pilot_id}' has been deleted'")





# This function create a command line interface
def command_line_interface():
    
    while True:
        print("\n--- Flight Management System ---")
        print("To create a table press c")
        print("To populate a table press p")
        print("1. Show All Destinations")
        print("2. Show All Pilots")
        print("3. Show All Flights")
        print("4. Add a new Flight")
        print("5. Update Flight Information")
        print("6. Assign Pilot to Flight")
        print("7. Pilot Schedule")
        print("8. View/Update Destination Information")
        print("9. View Flights by Criteria")
        print("10. Create New Destination")
        print("11. Delete Information")
        print("12. Exit")
        
        choice = input("Enter your choice: ").lower().strip()

        if choice == "c":
            create_table()

        elif choice == "p":
            populate_table()

        elif choice == "1":
            connect = connect_db()
            cursor = connect.cursor()
            cursor.execute("SELECT * FROM airports")

            airports = cursor.fetchall()

            if airports:
                columns = ["Airport ID", "City Name", "Country", "Airport Code"]
            df = pd.DataFrame(airports, columns = columns)
            print(df)
            

            connect.close()

        #Display all the pilots 
        elif choice == "2":
            connect = connect_db()
            cursor = connect.cursor()
            cursor.execute("SELECT * FROM pilots")
            pilot = cursor.fetchall()

            if pilot:
                columns = ["Pilot ID", "Name", "Flight Hours"]

            df = pd.DataFrame(pilot, columns = columns)
            print(df)


            connect.close()

        #Display all the flights 
        elif choice == "3":
            connect = connect_db()
            cursor = connect.cursor()
            cursor.execute("""SELECT 
            flights.flight_id, 
            flights.origin_airport_id, 
            origin_airport.name AS origin_name,
            flights.destination_airport_id, 
            destination_airport.name AS destination_name,
            flights.departure_date, 
            flights.departure_time, 
            flights.arrival_time, 
            flights.status, 
            flights.pilot_id, 
            pilots.name AS pilot_name, 
            pilots.flight_hours AS pilot_flight_time 

            FROM flights 
            JOIN airports AS origin_airport ON flights.origin_airport_id = origin_airport.airport_id 
            JOIN airports AS destination_airport ON flights.destination_airport_id = destination_airport.airport_id 
            JOIN pilots ON flights.pilot_id = pilots.pilot_id""")

            
            flight = cursor.fetchall()
            columns = [
                "Flight ID", "Origin Airport ID", "Origin Name", 
                "Destination Airport ID", "Destination Name", 
                "Departure Date", "Departure Time", "Arrival Time", 
                "Status", "Pilot ID", "Pilot Name", "Pilot Flight Time"
            ]
            if flight:
                df = pd.DataFrame(flight, columns = columns)
            print(df)
            connect.close()
        
        elif choice == "4":
            connect = connect_db()
            cursor = connect.cursor()
            #flight_id = int(input("Enter flight ID: ").strip())
            #Show the available origin airport
            print("Available Origin Airport: ")
            cursor.execute("SELECT airport_id, name FROM airports")
            origin_airports = cursor.fetchall()
            for i in origin_airports:
                print(f"ID: {i[0]}, Name: {i[1]}")
            origin_airport_id = int(input("Enter origin airport ID: ").strip())

            #Show the available destination airport
            print("Available Destination Airport: ")
            cursor.execute("SELECT airport_id, name FROM airports")
            origin_airports = cursor.fetchall()
            for i in origin_airports:
                print(f"ID: {i[0]}, Name: {i[1]}")
            destination_airport_id = int(input("Enter destination airport ID: ").strip())


            departure_date = input("Enter departure date (YYYY-MM-DD): ".strip())
            departure_time = input("Enter departure time (HH:MM): ".strip())
            arrival_time = input("Enter arrival time (HH:MM): ".strip())

            #Show the available status
            available_status = ["On Time", "Delayed", "Cancelled"]
            for i in available_status:
                print(f"The available status are: {i} ")

            status = input("Enter flight status: ")

            #Show the available pilot
            cursor.execute("SELECT pilot_id, name, flight_hours FROM pilots")
            pilot = cursor.fetchall()
            for i in pilot:
                print(f"The available pilots are ID: {i[0]}, Name: {i[1]}, Fligh Experience Hour: {i[2]}")
            pilot_id = int(input("Enter pilot ID: ").strip())
            add_flight(origin_airport_id, destination_airport_id, departure_date, departure_time, arrival_time, status, pilot_id)
            
        
        elif choice == "5":
            update_flight_information()

        elif choice == "6":
            assign_pilot()
            
        elif choice == "7":
            pilot_schedule()

        elif choice == "8":
            view_update_destination()

        elif choice == "9":
            flight_by_criteria()

        elif choice == "10":
            create_new_destination()

        elif choice == "11":
            delete_information()
        
        elif choice == "12":
            print("Thank you")
            break
        
        else:
            print("You have enter an invalid choice")


if __name__ == "__main__":
    command_line_interface()
