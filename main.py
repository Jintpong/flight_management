import sqlite3

# Connect to the database
def connect_db():
    return sqlite3.connect('flight.db')



#This function is use to add flight
def add_flight( origin_airport_id, destination_airport_id, departure_date, departure_time,arrival_time, status, pilot_id):
    connect = connect_db()
    cursor = connect.cursor()


    cursor.execute("INSERT INTO flights (origin_airport_id, destination_airport_id, departure_date, departure_time, arrival_time ,status, pilot_id) VALUES (?, ?, ?, ?, ?, ?, ?)",
                   (origin_airport_id, destination_airport_id, departure_date, departure_time, arrival_time, status, pilot_id))
    connect.commit()
    print("Flight has been added")
    connect.close()

#This function is use to update flight information
def update_flight_information():
    connect = connect_db()
    cursor = connect.cursor()

    
    flight_id = input("Enter the flight ID to update: ").strip()

    update_version = []
    value = []

    
    new_origin_airport_id = input("Enter a new origin airport ID : ").strip()
    new_destination_airport_id = input("Enter a new destination airport ID : ").strip()
    new_departure_date = input("Enter a new departure date (YYYY-MM-DD) ): ").strip()
    new_departure_time = input("Enter a new departure time (HH:MM) : ").strip()
    new_arrival_time = input("Enter a new arrival time (HH:MM) : ").strip()
    new_status = input("Enter a new status : ").strip()
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
    cursor.execute("SELECT flight_id, origin_airport_id, destination_airport_id, departure_date, departure_time, arrival_time, status FROM flights WHERE pilot_id = ? ORDER BY departure_date, departure_time", (pilot_id,))
    schedule = cursor.fetchall()
    for flight in schedule:
        print(f"Flight ID: {flight[0]}, Origin Airport ID: {flight[1]},Destination Aiport ID {flight[2]},  Departure Date: {flight[3]}, Departure Time: {flight[4]}, Arrival Time: {flight[5]}, Status: {flight[6]}")

    connect.close()


def view_update_destination():
    user = input ("Press v to view and u to update: ").lower().strip()
    connect = connect_db()
    cursor = connect.cursor()

    if user == 'v':
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



# This function create a command line interface
def command_line_interface():
    
    while True:
        print("\n--- Flight Management System ---")
        print("1. Show All Destinations")
        print("2. Show All Pilots")
        print("3. Show All Flights")
        print("4. Add a new Flight")
        print("5. Update Flight Information")
        print("6. Assign Pilot to Flight")
        print("7. Pilot Schedule")
        print("8. View/Update Destination Information")
        print("9. View Flights by Criteria")
        print("10. Exit")
        
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            connect = connect_db()
            cursor = connect.cursor()
            cursor.execute("SELECT * FROM airports")
            rows = cursor.fetchall()
            for row in rows:
                print(row)
            connect.close()

        #Display all the pilots 
        elif choice == "2":
            connect = connect_db()
            cursor = connect.cursor()
            cursor.execute("SELECT * FROM pilots")
            rows = cursor.fetchall()
            for row in rows:
                print(row)
            connect.close()

        #Display all the flights 
        elif choice == "3":
            connect = connect_db()
            cursor = connect.cursor()
            cursor.execute("SELECT * FROM flights")
            rows = cursor.fetchall()
            for row in rows:
                print(row)
            connect.close()
        
        elif choice == "4":
            #flight_id = int(input("Enter flight ID: ").strip())
            origin_airport_id = int(input("Enter origin airport ID: ").strip())
            destination_airport_id = int(input("Enter destination airport ID: ").strip())
            departure_date = input("Enter departure date (YYYY-MM-DD): ".strip())
            departure_time = input("Enter departure time (HH:MM): ".strip())
            arrival_time = input("Enter arrival time (HH:MM): ".strip())
            status = input("Enter flight status: ")
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
            print("Thank you")
            break
        
        else:
            print("You have enter an invalid choice")


if __name__ == "__main__":
    command_line_interface()
