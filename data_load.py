import sqlite3
import csv
 
def create_database(db_name):
    conn = sqlite3.connect(db_name)
    cur = conn.cursor()
 
    #create a vessel table
    cur.execute("""CREATE TABLE vessel (
                    IMO_number integer,
                    vessel_name text,
                    PRIMARY KEY(IMO_number)
                )""") 
                
    #populate vessel table
    cur.execute("""INSERT INTO vessel (IMO_number,vessel_name) VALUES
                    (9632179, 'Mathilde Maersk'),
                    (9247455, 'Australian Spirit'),
                    (9595321, 'MSC Preziosa')
                """)
 
    # save data to a database
    conn.commit()
 
    #create a position table
    cur.execute("""CREATE TABLE position (
                    IMO_number integer,
                    timestamp text,
                    latitude real,
                    longitude real
                )""") 
    #populate position table
    with open ('positions.csv', 'r') as data:
        reader = csv.reader(data)

        query = 'INSERT INTO position(IMO_number,timestamp,latitude,longitude) VALUES (?,?,?,?)'
        for row in reader:
            cur.execute(query, row)
    
        # save data to a database
        conn.commit()
        
if __name__ == '__main__':
    create_database("fleet.db")

