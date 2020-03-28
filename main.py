from Quest import Quest
from DefaultGenerator import DefaultGenerator

if __name__ == "__main__":
	testQuests = [(1, {}) for i in range(0, 20)]

	generated = DefaultGenerator(testQuests)

	# Как тут консольный вывод красивый делался, забыл уже.
	for i in generated.quests.values():
		print("----------------------------------")
		print()
		print("Задание:")
		print(i.wording)
		print()
		print("Ход решения:")
		print(i.decisionProgress)
		print()
		print("Ответ:", end=' ')
		print(i.answer)
		print()