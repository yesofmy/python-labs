''''''

def validate_name(func):
    """Декоратор для перевірки імені"""
    def wrapper(self, *args, **kwargs):
        name = args[0] if args else self.name
        if not isinstance(name, str) or len(name.strip()) == 0:
            raise ValueError("Name must be a non-empty string.")
        return func(self, *args, **kwargs)
    return wrapper

def validate_age(func):
    """Декоратор для перевірки віку"""
    def wrapper(self, *args, **kwargs):
        age = args[0] if args else self.age
        if not isinstance(age, int) or age <= 0:
            raise ValueError("Age must be a positive integer.")
        return func(self, *args, **kwargs)
    return wrapper

# Клас Person
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @validate_name
    def set_name(self, name):
        self.name = name

    @validate_age
    def set_age(self, age):
        self.age = age

    @validate_name
    def get_name(self):
        return self.name

    @validate_age
    def get_age(self):
        return self.age

# Тестування декораторів
try:
    person = Person("John", 30)
    print(f"Name: {person.get_name()}")
    print(f"Age: {person.get_age()}")

    # Спробуємо встановити некоректне ім'я
    person.set_name("")  # Це викличе помилку
except ValueError as e:
    print(f"Error: {e}")

try:
    # Спробуємо встановити некоректний вік
    person.set_age(-5)  # Це викличе помилку
except ValueError as e:
    print(f"Error: {e}")

# Встановлення правильних значень
person.set_name("Alice")
person.set_age(25)
print(f"Updated Name: {person.get_name()}")
print(f"Updated Age: {person.get_age()}")
