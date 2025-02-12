# CRUD operations

# Create
# Read
# Update
# Delete
import psycopg2


def create_person(conn, firstname, lastname, age):
    cursor = conn.cursor()
    cursor.execute("INSERT INTO person (firstname, lastname, age) VALUES (%s, %s, %s)", (firstname, lastname, age))
    conn.commit()
    cursor.close()

def read_all_persons(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM person")
    persons = cursor.fetchall()
    cursor.close()
    return persons

def read_person(conn, person_id): 
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM person WHERE id = %s", (person_id,))
    person = cursor.fetchone()
    cursor.close()
    return person

def update_person(conn, person_id, person):
    cursor = conn.cursor()
    cursor.execute("UPDATE person SET firstname = %s, lastname = %s, age = %s WHERE id = %s", (person['firstname'], person['lastname'], person['age'], person_id))
    person = cursor.fetchnon()
    cursor.close()
    return person

def delete_person(conn, person_id):
    cursor = conn.cursor()
    cursor.execute("DELETE FROM person WHERE id = %s", (person_id,))
    conn.commit()
    cursor.close()

if __name__ == "__main__":
    conn = psycopg2.connect(
        host="localhost",
        database="postgres",
        user="gelo",
        password="admin"
    )


#from GPT, pinaganda ko lang yung code and trying to understand it even more hehe. di pa masyado gets super dami ng codes hehe dami pa errors
while True:
        print("Select an operation:")
        print("1 - Create person")
        print("2 - Read all persons")
        print("3 - Read person")
        print("4 - Update person")
        print("5 - Delete person")
        print("6 - Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            firstname = input("Enter first name: ")
            lastname = input("Enter last name: ")
            age = input("Enter age: ")
            create_person(conn, firstname, lastname, age)
        elif choice == '2':
            persons = read_all_persons(conn)
            for person in persons:
                print(person)
        elif choice == '3':
            person_id = input("Enter person ID: ")
            person = read_person(conn, person_id)
            print(person)
        elif choice == '4':
            person_id = input("Enter person ID: ")
            firstname = input("Enter new first name: ")
            lastname = input("Enter new last name: ")
            age = input("Enter new age: ")
            update_person(conn, person_id, firstname, lastname, age)
        elif choice == '5':
            person_id = input("Enter person ID: ")
            delete_person(conn, person_id)
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")

        conn.close()

if __name__ == "__main__":
    main()
   