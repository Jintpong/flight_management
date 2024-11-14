import sqlite3

# Connect to the database
def connect_db():
    return sqlite3.connect('flight.db')



#This function is use to add flight
def add_flight(flight_id, destination_id, departure_date, departure_time, status, pilot_id):
    connect = connect_db()
    cursor = connect.cursor()
    cursor.execute("INSERT INTO flights (flight_id, destination_id, departure_date, departure_time, status, pilot_id) VALUES (?, ?, ?, ?, ?, ?)",
                   (flight_id, destination_id, departure_date, departure_time, status, pilot_id))
    connect.commit()
    connect.close()

def update_flight_information(flight_id=None, new_flight_id=None, destination_id=None, departure_date=None, 
                              departure_time=None, status=None, pilot_id=None):
    connect = connect_db()
    cursor = connect.cursor()
    update_version = []
    value = []

    new_flight_id = input("Enter a new flight id: ")
    new_destination_id = input("Enter a new destination id: ")
    new_departure_date = input("Enter a departure date: ")
    new_departure_time = input("Enter a new departure time: ")
    new_status = input("Enter a status: ")
    new_pilot_id = input("Enter a new pilot id : ")

    if new_flight_id:
        update_version.append("flight_id = ?")
        value.append(new_flight_id)
    if new_destination_id:
        update_version.append("destination_id = ?")
        value.append(destination_id)
    if new_departure_date:
        update_version.append("departure_date = ?")
        value.append(departure_date)
    if new_departure_time:
        update_version.append("departure_time = ?")
        value.append(departure_time)
    if new_status:
        update_version.append("status = ?")
        value.append(status)
    if new_pilot_id:
        update_version.append("pilot_id = ?")
        value.append(pilot_id)

    if update_version:
        value.append(flight_id)
        cursor.execute(f"UPDATE flights SET {', '.join(update_version)} WHERE flight_id = ?", value)
        connect.commit()
        print("The flight has been update")
    else:
        print("The flight has not been update")

    connect.close()




# Function to search for flights by destination
def search_flights_by_destination(destination_name):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''SELECT flights.flight_id, destinations.name, flights.departure_date, flights.departure_time, flights.status, pilots.name
                      FROM flights
                      JOIN destinations ON flights.destination_id = destinations.destination_id
                      JOIN pilots ON flights.pilot_id = pilots.pilot_id
                      WHERE destinations.name = ?''', (destination_name,))
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    conn.close()

# This function create a command line interface
def command_line_interface():
    
    while True:
        print("\n--- Flight Management System ---")
        print("1. Add a new Flight")
        print("2. Update Flight Information")
        print("4. Show All Destinations")
        print("5. Show All Pilots")
        print("6. Show All Flights")
        print("7. Search Flights by Destination")
        print("8. Exit")
        
        choice = input("Enter your choice: ")
        
        
        if choice == "1":
            flight_id = int(input("Enter flight ID: "))
            destination_id = int(input("Enter destination ID: "))
            departure_date = input("Enter departure date (YYYY-MM-DD): ")
            departure_time = input("Enter departure time (HH:MM): ")
            status = input("Enter flight status: ")
            pilot_id = int(input("Enter pilot ID: "))
            add_flight(flight_id, destination_id, departure_date, departure_time, status, pilot_id)
            print("Flight added successfully!")
        
        elif choice == "2":
            update_flight_information()

        
        #Display all the destinations
        elif choice == "4":
            connect = connect_db()
            cursor = connect.cursor()
            cursor.execute("SELECT * FROM destinations")
            rows = cursor.fetchall()
            for row in rows:
                print(row)
            connect.close()
        
        #Display all the pilots 
        elif choice == "5":
            connect = connect_db()
            cursor = connect.cursor()
            cursor.execute("SELECT * FROM pilots")
            rows = cursor.fetchall()
            for row in rows:
                print(row)
            connect.close()
        
        #Display all the flights 
        elif choice == "6":
            connect = connect_db()
            cursor = connect.cursor()
            cursor.execute("SELECT * FROM flights")
            rows = cursor.fetchall()
            for row in rows:
                print(row)
            connect.close()
            
        
        elif choice == "7":
            destination_name = input("Enter destination name: ")
            search_flights_by_destination(destination_name)
        
        elif choice == "8":
            print("Goodbye!")
            break
        
        else:
            print("You have enter an invalid choice")


if __name__ == "__main__":
    command_line_interface()
