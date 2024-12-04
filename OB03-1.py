
# Базовый класс Animal
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        raise NotImplementedError("Subclasses must implement this method")

    def eat(self):
        return f"Животное {self.name} ест."


# Подкласс Bird
class Bird(Animal):
    def make_sound(self):
        return f"Птица {self.name} чирикает."


# Подкласс Mammal
class Mammal(Animal):
    def make_sound(self):
        return f"Млекопитающее {self.name} рычит."

# Подкласс Mammal
class Dogs(Mammal):
    def make_sound(self):
        return f"Млекопитающее собака {self.name} лает, воет."

# Подкласс Reptile
class Reptile(Animal):
    def make_sound(self):
        return f"Рептилия {self.name} шипит."


# Функция для демонстрации полиморфизма
def animal_sound(animals):
    for animal in animals:
        print(animal.make_sound())


# Класс Zoo для композиции
class Zoo:
    def __init__(self):
        self.animals = []
        self.employees = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def add_employee(self, employee):
        self.employees.append(employee)

    def show_animals(self):
        for animal in self.animals:
            print(f"{animal.name}, Age: {animal.age}")


# Класс для сотрудников зоопарка
class ZooKeeper:
    def __init__(self, name):
        self.name = name

    def feed_animal(self, animal):
        return f"{self.name} Кормит и ухаживает за {animal.name}."


class Veterinarian:
    def __init__(self, name):
        self.name = name

    def heal_animal(self, animal):
        return f"{self.name} лечит {animal.name}."


# Пример использования
if __name__ == "__main__":
    # Создаем животных
    parrot = Bird("Polly", 2)
    lion = Mammal("Leo", 5)
    snake = Reptile("Sly", 3)
    dog = Dogs("Шарик", 8)

    # Демонстрация полиморфизма
    animal_sound([parrot, lion, snake, dog])

    # Создаем зоопарк
    zoo = Zoo()
    zoo.add_animal(parrot)
    zoo.add_animal(lion)
    zoo.add_animal(snake)
    zoo.add_animal(dog)

    # Показываем животных в зоопарке
    print("\nAnimals in the zoo:")
    zoo.show_animals()

    # Создаем сотрудников
    keeper = ZooKeeper("John")
    vet = Veterinarian("Dr. Smith")

    # Демонстрация работы сотрудников
    print(keeper.feed_animal(lion))
    print(vet.heal_animal(snake))
# ```
#
# ### Объяснение:
#
# 1. **Базовый класс Animal**: Содержит общие атрибуты и методы. Метод `make_sound()` является абстрактным и должен быть переопределен в подклассах.
#
# 2. **Подклассы**: `Bird`, `Mammal` и `Reptile` наследуют от `Animal` и переопределяют метод `make_sound()`.
#
# 3
#

# . **Полиморфизм**: Функция `animal_sound(animals)` принимает список животных и вызывает их метод `make_sound()`.
#
# 4. **Композиция**: Класс `Zoo` содержит список животных и сотрудников с методами для добавления их в зоопарк.
#
#5. **Сотрудники**: Классы `ZooKeeper` и `Veterinarian` имеют специфические методы для взаимодействия с животными.