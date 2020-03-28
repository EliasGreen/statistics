from copy import copy
from Quest import Quest

class IGenerator():
	"""Генерирует задания по заданным требованиям.
	__quests - хранит информацию о заданиях в виде номер задания в документе -> задание.
	__request - сохраненные входные данные. Полезны для дебага во время генерации."""

	def __init__(self, requestQuests: list):
		"""Возвращает список заданий, согласно списку. В списке имеются кортежи вида (номер, аргументы).
		Аргументы являются опциональными - для уточнения задачи или дебага.
		
		То есть, список вида [ (1, {}), (1, {}), (2, {}) ] задает генерацию двух первых заданий и одного
		второго."""

		self._request = copy(requestQuests)
		self._quests = dict()
		self._questsFunctionsTable = dict() # Словарь функций для генерации.

	@property
	def quests(self) -> dict:
		return self._quests
