from tkinter import * 
import formsObj


def button_clicked():
    passwordMySQL = form1.infoEntry[0].get()
    grid = [(0, 0), (0, 2), (1, 0), (1, 2), (2, 0)]
    fieldNames = ["Наименование вакансии", "Ключевые навыки", "Описание", "Зарплата", "Вид работы"]
    form2 = formsObj.FormObjects("Вводим вакансии", "800x600", passwordMySQL)
    for i in range(len(fieldNames)): form2.TextEntry(form2.form, fieldNames[i], grid[i], i)
    form2.ButtonTextForm(form2.form)
    form2.labelText = Label(form2.form, text = '', font = ('Helvetica 10') )
    form2.labelText.grid(row=5, column=0, padx=0, pady=15, columnspan=2)
    form2.Actions()



form1 = formsObj.FormObjects("Список вакансий", "600x200")
form1.ButtonCreate(form1.form, button_clicked, "Вводим вакансии", (0, 0))
form1.ButtonCreate(form1.form, form1.button_clicked_1, "Записываем в файл", (0, 1))
form1.TextEntry(form1.form, "Пароль в MySQL", (1, 0), 0, 1)
form1.Actions()