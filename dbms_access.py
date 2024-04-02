import mysql.connector as connector
class DBHelper:
    def __init__(self):
        self.con = connector.connect(   host="localhost",
                                        port="3306",
                                        user="root",
                                        password="root",
                                        database="recipefinder")
        query='create table if not exists Ingredients(Ingre_name varchar(20),Ingre_ID integer primary key, Ingre_type varchar (10))'
        cur=self.con.cursor()
        cur.execute(query)
        print("Created")
    
    #Insert
    def insert_ingre(self,Ingre_name,Ingre_ID,Ingre_type):
        query="insert into Ingredients(Ingre_name,Ingre_ID,Ingre_type) values ('{}' , {} , '{}')".format(Ingre_name,Ingre_ID,Ingre_type)
        print(query)
        cur=self.con.cursor()              #this is accessing the cursor in mysql
        cur.execute(query)                 #executing query using cursor
        self.con.commit()                  #actually makes change to the database
        print("Ingredient saved to database")

    #Fetch All
    def fetch_all(self):
        query="select * from Ingredients"
        cur=self.con.cursor()
        cur.execute(query)
        for row in cur:
            print("Ingredient Name : ", row[0])
            print("Ingredient ID : ", row[1])
            print("Ingredient Type : ", row[2])
            print()
            print()
    
    #Delete 
    def delete_ingre(self,Ingre_ID):
        query="delete from Ingredients where Ingre_ID={}".format(Ingre_ID)
        print(query)
        cur=self.con.cursor()              #this is accessing the cursor in mysql
        cur.execute(query)                 #executing query using cursor
        self.con.commit()                  #actually makes change to the database
        print("Deleted")

#main coding
helper=DBHelper()
#helper.insert_ingre('Flour', 1, 'Dry')
#helper.insert_ingre('Eggs', 3, 'Protein')
#helper.fetch_all()
helper.delete_ingre(1)
helper.fetch_all()