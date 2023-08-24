
### Завдання
* Додати до класу Employee методи save_email(self) та validate(self) та атрибут email

* Створити виняток EmailAlreadyExistsException

* Метод save_email має викликатись в кінці методу __init__ та записувати email в файл emails.csv

* Метод validate має перевіряти чи існує імейл в файлі. Якщо імейл вже існує, то викликати помилку EmailAlreadyExistsException


* ** У разі виникнення винятку EmailAlreadyExistsException записати в файл logs.txt повідомлення у вигляді: %дата% %час% | %traceback%