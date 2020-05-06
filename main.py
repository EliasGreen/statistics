from Quest import Quest
from DefaultGenerator import DefaultGenerator

if __name__ == "__main__":
	testQuests =  [i for i in range(1, 18)]

	for i in range(1, 2):
		            # Задачи - Вариант - Имя документа
		generated = DefaultGenerator(testQuests, i, f"variant_{i}")
