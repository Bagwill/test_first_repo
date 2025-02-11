class ParentClass:
    def __init__(self, name):
        self.name = name

    def display_name(self):
        print(f"Имя: {self.name}")

class ChildClass(ParentClass):
    def __init__(self, name, age):
        super().__init__(name)  # Вызов конструктора родительского класса
        self.age = age

    def display_age(self):
        print(f"Возраст: {self.age}")

# Создание экземпляра дочернего класса
child = ChildClass("Алексей", 25)

# Вызов методов
child.display_name()  # Выведет: Имя: Алексей
child.display_age()   # Выведет: Возраст: 25