
### Завдання 18
* Створити клас Candidate:

    В __init__ передавати:

        first name
        last name
        email
        tech_stack
        main_skill
        main_skill_grade
* Створити @property метод який повертає first name + ‘ ‘ + last name
* Створити @classmethod generate_candidates, який приймає в якості аргументу шлях до файлу.
  Метод generate_candidates має повертати список об’єктів класу Candidate.

  Файл тут
  (https://bitbucket.org/ivnukov/lesson2/raw/4f59074e6fbb552398f87636b5bf089a1618da0a/candidates.csv)
* ** Розширити метод generate_candidates, щоб він міг отримувати в якості аргументу URL на файл та генерувати кандидатів з нього



### Завдання 19
* Покрити тестами класи Employee, Recruiter, Developer, Candidate.
* Зробити тести у окремих файлах у каталозі tests.