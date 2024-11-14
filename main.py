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

# Need to fix this function since it is not updating the updated flight
def update_flight_information(flight_id=None, new_flight_id=None, destination_id=None, departure_date=None, 
                              departure_time=None, status=None, pilot_id=None):
    connect = connect_db()
    cursor = connect.cursor()
    update_version = []
    value = []

    new_flight_id = input("Enter a new flight id: ").strip()
    new_destination_id = input("Enter a new destination id: ").strip()
    new_departure_date = input("Enter a departure date: ").strip()
    new_departure_time = input("Enter a new departure time: ").strip()
    new_status = input("Enter a status: ").strip()
    new_pilot_id = input("Enter a new pilot id : ").strip()

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

def assign_pilot():
    flight_id = input("Enter the flight id you want to assign the pilot: ").strip()
    pilot_id = input("Enter the pilot id: ").strip()
    connect = connect_db()
    cursor = connect.cursor()


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
    pilot_id = input("Enter the pilot id to check the schedule: ").strip()
    connect = connect_db()
    cursor = connect.cursor()
    cursor.execute("SELECT flight_id, destination_id, departure_date, departure_time, status FROM flights WHERE pilot_id = ? ORDER BY departure_date, departure_time", (pilot_id,))
    schedule = cursor.fetchall()
    for flight in schedule:
        print(f"Flight ID: {flight[0]}, Destination ID: {flight[1]}, Departure Date: {flight[2]}, Departure Time: {flight[3]}, Status: {flight[4]}")

    connect.close()


def view_update_destination():
    user = input ("Press v to view and u to update: ").lower().strip()
    connect = connect_db()
    cursor = connect.cursor()

    if user == 'v':
        destination_id = input("Enter the destination id: ")
        cursor.execute("SELECT * FROM destinations WHERE destination_id = ?", destination_id,)
        destination_info = cursor.fetchone()

        print(f"Destination Information ID: {destination_id}")
        print(f"Destination Name: {destination_info[1]}")
        print(f"Country: {destination_info[2]}")
        print(f"Destination Airport Code: {destination_info[3]}")

    elif user == 'u':
        destination_id = input("Enter the Destination ID to update: ").strip()
        cursor.execute("SELECT * FROM destinations WHERE destination_id = ?", (destination_id,))
        destination = cursor.fetchone()

        new_name = input("Enter the new name: ")
        new_country = input("Enter the new country: ")
        new_code = input("Enter the new code: ")

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
            value.append(destination_id) 
            cursor.execute(f"UPDATE destinations SET {', '.join(update)} WHERE destination_id = ?", value)
            connect.commit()
        else:
            print("No changes occured")

        connect.close()

# This function create a command line interface
def command_line_interface():
    
    while True:
        print("\n--- Flight Management System ---")
        print("1. Add a new Flight")
        print("2. Update Flight Information")
        print("3. Assign Pilot to Flight")
        print("4. Show All Destinations")
        print("5. Show All Pilots")
        print("6. Show All Flights")
        print("7. Pilot Schedule")
        print("8. View/Update Destination Information")
        print("10. Exit")
        
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

        elif choice == "3":
            assign_pilot()

        
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
            pilot_schedule()

        elif choice == "8":
            view_update_destination()
        
        elif choice == "9":
            print("Goodbye!")
            break
        
        else:
            print("You have enter an invalid choice")


if __name__ == "__main__":
    command_line_interface()
