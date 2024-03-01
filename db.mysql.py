import mysql.connector

database = mysql.connector.connect(
    host ="localhost",
    user = "root",
    password = "arowosola1449",
)

mycursor = database.cursor()

mycursor.execute('CREATE DATABASE DogSheltersXP')
