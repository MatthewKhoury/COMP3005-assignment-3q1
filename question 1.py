import psycopg2
from psycopg2 import sql
from datetime import date
"""
Log in for database
"""
DB_NAME = "A3"
DB_USER = "postgres"
DB_PASSWORD = "grmsjm!4Now"
DB_HOST = "localhost"
DB_PORT = "5432"
sidList=[]
def connect():
    "this function takes the global variable log in variables and logs into the data base"
    try:
        conn = psycopg2.connect(
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT
        )
        return conn
    except psycopg2.Error as e:
        print("Connection error")
        print(e)
        return None

def getAllStudents():
    "Retrieves and displays all records from the students table"
    #global sidList
    conn = connect()
    if conn is not None:
        try:
            cur = conn.cursor()
            cur.execute("SELECT * FROM students")
            rows = cur.fetchall()
            print("Student Records:")
            i=0
            for row in rows:
                i+=1
                print(row)
                #sid=row.split(",")
               # sid = row[0]
               # sidList.append(sid)
               # print(sidList)
                
           # print(i)
            
        except psycopg2.Error as e:
            print("Error fetching data from the database.")
            print(e)
        finally:
            conn.close()
            #return sidList
def getAllStudentsID():
    "similar to getting student data this function returns a list of only the student ids"
    global sidList
    conn = connect()
    if conn is not None:
        try:
            cur = conn.cursor()
            cur.execute("SELECT * FROM students")
            rows = cur.fetchall()
            #print("Student Records:")
            i=0
            for row in rows:
                i+=1
                #print(row)
                #sid=row.split(",")
                sid = row[0]
                sidList.append(sid)
                #print(sidList)
                
           # print(i)
            
        except psycopg2.Error as e:
            print("Error fetching data from the database.")
            print(e)
        finally:
            conn.close()
            return sidList         
        
def addStudent(first_name, last_name, email, enrollment_date):
    """Inserts a new student record into the students table"""
    conn = connect()
    if conn is not None:
        try:
            cur = conn.cursor()
            cur.execute(
                "INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s)",
                (first_name, last_name, email, enrollment_date)
            )
            conn.commit()
            print("Student added successfully.")
        except psycopg2.Error as e:
            print("Error adding student to the database.")
            print(e)
        finally:
            conn.close()

def updateStudentEmail(student_id, new_email):
    """"Updates the email address for a student with the specified student_id"""
    conn = connect()
    if conn is not None:
        try:
            cur = conn.cursor()
            cur.execute(
                "UPDATE students SET email = %s WHERE student_id = %s",
                (new_email, student_id)
            )
            conn.commit()
            print("Student email updated successfully.")
        except psycopg2.Error as e:
            print("Error updating student email.")
            print(e)
        finally:
            conn.close()

def deleteStudent(student_id):
    """Deletes the record of the student with the specified student_id"""
    conn = connect()
    if conn is not None:
        try:
            cur = conn.cursor()
            cur.execute(
                "DELETE FROM students WHERE student_id = %s",
                (student_id,)
            )
            conn.commit()
            print("Student deleted successfully.")
        except psycopg2.Error as e:
            print("Error deleting student from the database.")
            print(e)
        finally:
            conn.close()
def clearData():
    '''clears database from all students'''
    getAllStudentsID()
    print(sidList)
    for i in range(0,len(sidList)):
        #print(i)
       # print(sidList[i])
        deleteStudent(sidList[i])
def populateInitialData():
    "populate table with initial data from assignment outline"
    addStudent('John', 'Doe', 'john.doe@example.com', '2023-09-01')
    addStudent('Jane', 'Smith', 'jane.smith@example.com', '2023-09-01')
    addStudent('Jim', 'Beam', 'jim.beam@example.com', '2023-09-02')
    #addStudent('vic', 'v', 'vicv@gmail.com', '2024-03-10')
    
    
    print("studnts populated")
if __name__ == "__main__":
    # Populate initial data
    

    #print(sidList)

    clearData()
    
    #populateInitialData()
    #deleteStudent(92)
    #addStudent('vic', 'v', 'vicv@gmail.com', '2024-03-10')
    #updateStudentEmail(92, 'update@example.com')
    
    getAllStudents()
