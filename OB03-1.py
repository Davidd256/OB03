#Обновленная версия  программы на Python, которая добавляет функции для сохранения и загрузки информации о зоопарке и его сотрудниках в файл, используя модуль `pickle`. Это позволит сохранить "постоянное состояние" между запусками программы.
import pickle



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


# Подкласс Dogs
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
        print()
    def show_employee(self):
        for employee in self.employees:
            print(f"{employee.name} ")
        print()

    def save_to_file(self, filename):
        with open(filename, 'wb') as file:
            pickle.dump(self, file)
        print(f"Zoo data saved to {filename}.")

    @staticmethod
    def load_from_file(filename):
        with open(filename, 'rb') as file:
            zoo = pickle.load(file)
        print(f"Zoo data loaded from {filename}.")
        return zoo


# Класс для сотрудников зоопарка
class ZooKeeper:
    def __init__(self, name):
        self.name = name

    def feed_animal(self, animal):
        return f"{self.name} кормит и ухаживает за {animal.name}."


class Veterinarian:
    def __init__(self, name):
        self.name = name

    def heal_animal(self, animal):
        return f"{self.name} лечит {animal.name}."


# Пример использования
if __name__ == "__main__":
    # Попробуем загрузить зоопарк из файла
    try:
        zoo = Zoo.load_from_file('zoo_data1.pkl')
    except (FileNotFoundError, EOFError):
# Если файл не найден, создаем новый зоопарк
        zoo = Zoo()

    # Создаем животных
        parrot = Bird("Polly", 2)
        lion = Mammal("Leo", 5)
        snake = Reptile("Sly", 3)
        dog = Dogs("Шарик", 8)

    # Добавляем животных в зоопарк
        zoo.add_animal(parrot)
        zoo.add_animal(lion)
        zoo.add_animal(snake)
        zoo.add_animal(dog)
    # Демонстрация полиморфизма
        animal_sound([parrot, lion, snake, dog])

        # Создаем сотрудников
        keeper = ZooKeeper("John")
        vet = Veterinarian("Dr. Smith")

        # Демонстрация работы сотрудников
        print(keeper.feed_animal(lion))
        print(vet.heal_animal(snake))

        # Добавляем сотрудников в зоопарк
        zoo.add_employee(keeper)
        zoo.add_employee(vet)

# Показываем животных в зоопарке
    print("\nAnimals in the zoo:")
    zoo.show_animals()
    zoo.show_employee()
    # Создаем сотрудников
    keeper = ZooKeeper("John")
    vet = Veterinarian("Dr. Smith")


    # Сохраняем состояние зоопарка в файл
    zoo.save_to_file('zoo_data1.pkl')
#Теперь программа будет сохранять состояние зоопарка и сотрудников между запусками, обеспечивая "постоянное состояние".