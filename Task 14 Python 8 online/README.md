
### Завдання
* Створити клас Employee.

* __init__ має приймати наступні аргументи: ім’я, ЗП за один робочий день.

* Створити метод work(self, …) який повертає строку “I come to the office.”

* Створити класи Recruiter та Developer, які наслідують клас Employee.

* Перевизначити методи work в класах R та D, щоб вони повертали значення:

    “I come to the office and start to coding.” - для Developer

    “I come to the office and start to hiring.” - для Recruiter

* Перевизначити методи __str__, щоб они повертали строку: “Посада: Ім’я”

* Зробити можливим порівнювати Employee по рівню ЗП.