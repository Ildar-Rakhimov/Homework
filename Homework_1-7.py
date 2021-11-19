class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {avg_grade(self.grades)}'\
              f'\nКурсы в процессе изучения: {self.courses_in_progress}\nЗавершенные курсы: {self.finished_courses}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Ошибка: можно сравнивать студента только со студентом')
            return
        return avg_grade(self.grades) < avg_grade(other.grades)


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}'
        return res


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []
        self.grades = {}

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {avg_grade(self.grades)}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Ошибка: можно сравнивать лектора только с лектором')
            return
        return avg_grade(self.grades) < avg_grade(other.grades)


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}'
        return res


def avg_grade(grades):
    """Вычисление средней оценки"""
    grade_list = []
    count = 0

    for element in grades.values():
        grade_list += element
        count += len(element)

    return round(sum(grade_list) / count, 2)


def avg_grade_hw(students_list, course):
    """
    Подсчет средней оценки за домашние задания по всем студентам в рамках конкретного курса
    """
    grade_list = []
    count = 0

    for student in students_list:
        for key, value in student.grades.items():
            if course == key:
                grade_list += value
                count += len(value)
    return round(sum(grade_list) / count, 2)


def avg_grade_lecture(lecturer_list, course):
    """
    Подсчет средней оценки за лекции всех лекторов в рамках курса
    """
    grade_list = []
    count = 0

    for lecturer in lecturer_list:
        for key, value in lecturer.grades.items():
            if course == key:
                grade_list += value
                count += len(value)
    return round(sum(grade_list) / count, 2)


# Студент № 1
sasha = Student('Александр', 'Иванов', 'мужской')
sasha.courses_in_progress += ['Python', 'Django', 'C++']
sasha.finished_courses += ['Java']
sasha.grades = {'Python': [3, 5, 5, 4, 4], 'Django': [4, 4, 3, 5, 3], 'C++': [5, 5, 4, 5, 4]}

# Студент № 2
tanya = Student('Татьяна', 'Петрова', 'женский')
tanya.courses_in_progress += ['Python', 'GitHub', 'C#']
tanya.finished_courses += ['C', 'Kotlin']
tanya.grades = {'Python': [5, 4, 4, 5, 5], 'GitHub': [3, 5, 5, 4, 5], 'C#': [4, 4, 3, 5, 5]}

# Преподаватель № 1
dima = Mentor('Дмитрий', 'Пяткин')
dima.courses_attached += ['Python', 'Django', 'C++', 'Java', 'GitHub', 'C#', 'C', 'Kotlin']

# Преподаватель № 2
olya = Mentor('Ольга', 'Мыскина')
dima.courses_attached += ['Python', 'Django', 'C++', 'Java', 'GitHub', 'C#', 'C', 'Kotlin']

# Лектор № 1
anya = Lecturer('Анна', 'Рожкова')
anya.courses_attached += ['Python', 'Django', 'C++', 'Java', 'GitHub', 'C#', 'C', 'Kotlin']
anya.grades = {'Python': [4, 5, 4, 5, 4], 'Django': [4, 4, 5, 5, 4], 'C++': [5, 5, 4, 5, 4]}

# Лектор № 2
roma = Lecturer('Роман', 'Никитин')
roma.courses_attached += ['Python', 'Django', 'C++', 'Java', 'GitHub', 'C#', 'C', 'Kotlin']
roma.grades = {'Python': [5, 5, 5, 4, 4], 'Django': [4, 4, 5, 5, 5], 'C++': [4, 5, 4, 5, 5]}

# Эксперт № 1
anton = Reviewer('Антон', 'Атласов')
anton.courses_attached += ['Python', 'Django', 'C++', 'Java', 'GitHub', 'C#', 'C', 'Kotlin']

# Эксперт № 2
mary = Reviewer('Мария', 'Соколова')
mary.courses_attached += ['Python', 'Django', 'C++', 'Java', 'GitHub', 'C#', 'C', 'Kotlin']

# print(sasha)
# print(tanya)
# print(dima)
# print(olya)
# print(anya)
# print(roma)
# print(anton)
# print(mary)

# Студент № 1 оценивает Лектора № 2
sasha.rate_lecture(roma, 'Python', 1000)
print(roma)

# Эксперт № 2 оценивает Студента № 1
mary.rate_hw(sasha, 'Python', 1000)
print(sasha)

# Список студентов
students = [sasha, tanya]

# Список лекторов
lecturers = [anya, roma]

specified_course = 'Django'

print(avg_grade_hw(students, specified_course))
print(avg_grade_lecture(lecturers, specified_course))