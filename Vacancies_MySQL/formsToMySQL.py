import mysql.connector
from numpy import append
import pandas as pd

class FormToMSQLQuery:
    def __init__(self, passwordMySQL):
        self.mydb = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password=passwordMySQL,
            database="database3"
        )
        self.mycursor = self.mydb.cursor()

    def FormMySQLInsert(self, dataSQL):
        sql = "INSERT INTO database3.vacancies (nameOfvacan, keyFeatures, description, salary, typeOfOffice) VALUES (%s, %s, %s, %s, %s)"
        self.val = dataSQL
        self.mycursor.execute(sql, self.val)

        self.mydb.commit()

    def MySQLToFile(self, query, filename="vacansies.csv"):
        sql = query
        self.mycursor.execute(sql)
        myAllData = self.mycursor.fetchall()
        print(len(myAllData))
        columnNames = {"id": [], "nameOfVacan" : [], "keyFeatures": [], "description": [], "salary" : [], "typeOfOffice" : []}
        counter = 0
        for i in columnNames.keys(): 
            for x in myAllData: columnNames[i].append(x[counter])
            counter += 1
        df = pd.DataFrame(columnNames)
        df_csv = df.to_csv(filename, sep=";", encoding='utf-8-sig')
        return len(myAllData)

    def FormMySQLDelete(self, dataSQL):
        sql = f"DELETE FROM database3.phone_book WHERE id = {int(dataSQL)};"
        self.mycursor.execute(sql)
        self.mydb.commit()
