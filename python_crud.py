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
    person = cursor.fetchone()
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

# readpersons = update_person(conn, 2)
# print(readpersons)

#balik muna here para mas magets hehe
updated_person = read_person(conn, 1)
update_person(conn, 1, {'firstname': 'karl', 'lastname': 'aguinaldo', 'age': 12})
print(updated_person)
   