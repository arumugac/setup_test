import mysql.connector

# """
# Connection to the server
# The username is root, the password is "" and hostnamE is localhost
# """

db = mysql.connector.connect(user="root",
                             host="localhost",
                             password="",
                             database="library"
)
my_cursor = db.cursor()
# query = "SHOW DATABASES"
# my_cursor.execute(query)
#
# for d in my_cursor:
#     print(db)

# Create Table
# query = """
##     CREATE TABLE skyhs_details
#     (
#     name varchar(255),
#     roll int(10),
#     class_Num int(10)
#     )
#     """
# my_cursor.execute(query)


## Insert data into table skyhs_details

# query = """
#     INSERT INTO skyhs_details
#     (name, roll, class_num)
#     VALUES
#     ("BOB",45,4)
#     """
# my_cursor.execute(query)
# db.commit()

# query = """


# def readData(sql):
#     my_cursor = db.cursor()
#     result = my_cursor.execute(sql)
#     result = my_cursor.fetchall()
#     db.close()
#     return result
#
# res = readData("SELECT * FROM skyhs_details")
#
# for row in res:
#     print(f"{row[0]} is in class {row[1]}")

