from tkinter import * 
from tkinter import ttk
import formsToMySQL

class FormObjects:
    def __init__(self, name, size, passwordMySQL = ""):
        self.form = Tk()
        self.form.title(name)
        self.form.geometry(size)
        self.infoEntry = {}
        self.data = {}
        self.passwordMySQL = passwordMySQL
        
    def close(self):
        self.form.destroy()
        self.form.quit()

    def Actions(self):
        self.form.protocol('WM_DELETE_WINDOW', self.close)
        self.form.mainloop()

    def ButtonCreate(self, objTk, buttonAction, button_name, position):
        self.button = Button(objTk, text=button_name, command=buttonAction, width=30, height=3, bg="#d8c5c5")
        self.button.grid(row=position[0], column=position[1], padx=15, pady=15)

    def TextEntry(self, objTk, textName, position, i, flag = 0):
        #print("Hello", dir(objTk.title))
        self.infoLabel = Label(objTk, text=textName)
        if (flag == 0 and i < 4): self.infoEntry[i] = Entry(objTk, width=30)
        elif (flag == 1): 
            password = StringVar()
            self.infoEntry[i] = Entry(objTk, width=30, textvariable=password, show="*")

        self.infoLabel.grid(row=position[0], column=position[1], padx=15, pady=15)
        if (i < 4): self.infoEntry[i].grid(row=position[0], column=position[1] + 1, padx=15, pady=15)
        else:
            self.listBoxWidget(objTk, position, i)

        

    def listBoxWidget(self, objTk, position, i):
        current_var = StringVar()
        self.combobox = ttk.Combobox(objTk, textvariable=current_var, width=30)
        self.combobox['values'] = ('удаленный', 'смешанный', 'в офисе')
        self.combobox['state'] = 'readonly'
        self.combobox.grid(row=position[0], column=position[1] + 1, padx=15, pady=15, columnspan=1)
        

    def ButtonTextForm(self, objTk):
        self.btnTextForm = Button(objTk, text="Запишите вакансию", width=30, command = self.btnDataSave)
        self.btnTextForm.grid(row=3, column=0, columnspan=2, padx=15, pady=15)
        # self.btnTextForm = Button(objTk, text="Удалите вакансию", width=30, command = self.btnDataDelete)
        # self.btnTextForm.grid(row=3, column=2, columnspan=2, padx=15, pady=15)
        self.btnTextForm = Button(objTk, text="Новая вакансия", width=30, command = self.btnCleanForm)
        self.btnTextForm.grid(row=3, column=2, columnspan=2, padx=15, pady=15)
        self.btnTextForm = Button(objTk, text="Поиск вакансии", width=30, command = self.btnFindVacan)
        self.btnTextForm.grid(row=4, column=0, columnspan=2, padx=15, pady=15)

    def btnFindVacan(self):
        form3 = FormObjects("Поиск вакансии", "600x200", self.passwordMySQL)
        form3.ButtonCreate(form3.form, form3.execFindVacan, "Найти вакансию", (1, 0))
        form3.ButtonCreate(form3.form, form3.close, "Отменить поиск", (1, 1))
        form3.TextEntry(form3.form, "Введите запрос", (0, 0), 0)
        form3.labelText = Label(form3.form, text = '', font = ('Helvetica 10') )
        form3.labelText.grid(row=2, column=0, padx=0, pady=15)
        form3.Actions()
        print(len(form3.infoEntry))
        return

    def execFindVacan(self):
        dataSQL = self.infoEntry[0].get()
        
        if (dataSQL != ""):
            print(dataSQL)
            db = formsToMySQL.FormToMSQLQuery(self.passwordMySQL)
            sql = f"SELECT * FROM database3.vacancies WHERE nameOfvacan='{dataSQL}';"
            lineResult = db.MySQLToFile(sql, "queryResult.csv")
            if lineResult > 0:
                self.labelText.config(text=f'Данные {lineResult} записаны в файл')
            else:
                sql = f"SELECT * FROM database3.vacancies WHERE nameOfvacan LIKE '{dataSQL}%';"
                lineResult = db.MySQLToFile(sql, "queryResult.csv")
                self.labelText.config(text=f'Данные {lineResult} записаны в файл')

        else: 
            self.labelText.config(text="Вы ничего не ввели")

        return

    def btnCleanForm(self):
        for i in range(len(self.infoEntry)): self.infoEntry[i].delete(0,"end")
        self.combobox.set("")
        self.labelText.config(text=" ")
        return

    def btnDataSave(self):
        if (self.infoEntry[0].get() != "" and self.combobox.get() != ""):
            dataSQL = tuple([self.infoEntry[i].get() if i < len(self.infoEntry) else self.combobox.get() for i in range(len(self.infoEntry)+1)])
            print(dataSQL)

            mySqlSent = formsToMySQL.FormToMSQLQuery(self.passwordMySQL)
            mySqlSent.FormMySQLInsert(dataSQL)
            self.labelText.config(text="Вакансия записана")
        else: self.labelText.config(text="Введите корректные данные")

    def btnDataDelete(self):
        dataSQL = self.infoEntry[0].get()
        mySqlSent = formsToMySQL.FormToMSQLQuery(self.passwordMySQL)
        mySqlSent.FormMySQLDelete(dataSQL)

    def button_clicked_1(self):
        self.passwordMySQL = self.infoEntry[0].get()
        db = formsToMySQL.FormToMSQLQuery(self.passwordMySQL)
        lineResult = db.MySQLToFile("SELECT * FROM database3.vacancies;")

      