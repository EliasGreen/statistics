import random

import Combinatorics
from IGenerator import IGenerator
from Quest import Quest

class DefaultGenerator(IGenerator):
	def __init__(self, requestQuests: dict):
		super().__init__(requestQuests)

		self._questsFunctionsTable[1] = self.__quest1
		self._questsFunctionsTable[2] = self.__quest2
		self._questsFunctionsTable[3] = self.__quest3
		self._questsFunctionsTable[9] = self.__quest9
		self._questsFunctionsTable[10] = self.__quest10

		counter = 1
		for number, args in self._request:
			try:
				self._questsFunctionsTable[number]

			except KeyError as exp:
				print("Чо за номер, ну шо такое")

			self._quests[counter] = self._questsFunctionsTable[number](**args)
			counter += 1
		
		self.quests[counter] = self._questsFunctionsTable[10](N = 5, K = 2, P = 0.51)

	# Задача 1.
	def __quest1(self, **kwargs) -> Quest:
		# Т1 - альтернатива, где все шарики одного цвета
		if ("whitePick" in kwargs.keys()) and ("blackPick" in kwargs.keys()):
			if kwargs["whitePick"] * kwargs["blackPick"] == 0:
				return __quest1_T2(**kwargs)

		alternatives = [
			self.__quest1_T1,
			self.__quest1_T2
		]

		return random.choice(alternatives)(**kwargs)

	def __quest1_T2(self, **kwargs) -> Quest:
		white = kwargs["white"] if "white" in kwargs else random.randint(5, 15)
		black = kwargs["black"] if "black" in kwargs else random.randint(5, 15)
		n = white + black
		pick = random.randint(2, int(n / 3))

		templatesList = [
			f"В корзине размещено {white} белых шаров и {black} черных шаров. Из них наудачу вынимают {pick} шаров. Найти"
			f" вероятность того, что они одного цвета.",

			f"В шляпе находится {white} красных фантов и {black} желтых фантов. Игрок наудачу вынимает {pick} фантов. Найти"
			f" вероятность того, что они одного цвета.",

			f"В шкафу лежит {white + black} носков, из которых {white} белых, а остальные черные. Петя наудачу берет {pick}"
			f" носков из шкафа. Какова вероятность того, что они одного цвета?"
		]

		template = random.choice(templatesList)
		resultsAll = Combinatorics.combinations(n, pick)
		resultsWhite = Combinatorics.combinations(white, pick)
		resultsBlack = Combinatorics.combinations(black, pick)

		answer = float(f"{(resultsWhite + resultsBlack) / resultsAll : .4f}") # Эта как - единственное, шо я нагуглил

		decisionProgress =  f"Количество исходов в данной задаче равняется количеству способов выбрать {pick} предметов из {n}."
		decisionProgress += f" Представим событие А - выбрано {pick} одинаковых предмета - как сумму двух событий A1 и A2."
		decisionProgress += f" Теперь выберем необходимые предметы из своих кучек и разделим количество способов выбора на все исходы."
		decisionProgress += f" После, просуммируем вероятности несовместных событий А1 и А2:\n"
		decisionProgress += f"P = ({resultsWhite} * {resultsBlack}) / {resultsAll} = {answer}.\n"
		decisionProgress += f"{answer * 100:.2f} % является ответом для данной задачи."

		return Quest(template, decisionProgress, answer)

	def __quest1_T1(self, **kwargs) -> Quest:
		white = kwargs["white"] if "white" in kwargs else random.randint(5, 15)
		whitePick = kwargs["whitePick"] if "whitePick" in kwargs else random.randint(2, int(white / 2.3))
		black = kwargs["black"] if "black" in kwargs else random.randint(5, 15)
		blackPick = kwargs["blackPick"] if "blackPick" in kwargs else random.randint(2, int(black / 2.3))
		n = white + black
		pickNumber = whitePick + blackPick

		templatesList = [
			f"В корзине размещено {white} белых шаров и {black} черных шаров. Из них наудачу вынимают {pickNumber} шаров. Найти"
			f" вероятность того, что будет вынуто ровно {whitePick} белых и {blackPick} черных шаров.",

			f"В шляпе находится {white} красных фантов и {black} желтых фантов. Игрок наудачу вынимает {pickNumber} фантов. Найти"
			f" вероятность того, что будет вынуто ровно {whitePick} красных и {blackPick} желтых фантов.",

			f"В шкафу лежит {white + black} носков, из которых {white} белых, а остальные черные. Петя наудачу берет {pickNumber}"
			f" носков из шкафа. Какова вероятность того, что будет вынуто ровно {whitePick} белых и {blackPick}"
			f" носков?"
		]

		template = random.choice(templatesList)
		resultsAll = Combinatorics.combinations(n, pickNumber)
		resultsWhite = Combinatorics.combinations(white, whitePick)
		resultsBlack = Combinatorics.combinations(black, blackPick)

		answer = float(f"{resultsWhite * resultsBlack / resultsAll : .4f}") # Эта как - единственное, шо я нагуглил

		decisionProgress =  f"Количество исходов в данной задаче равняется количеству способов выбрать {pickNumber} предметов из {n}."
		decisionProgress += f" А это, в свою очередь является количеством сочитаний C из {n} по {pickNumber} = {resultsAll}. Аналогичным образом"
		decisionProgress += f" вычисляем количество способов вытащить заданные предметы из общих куч. В результате получаем следующие вычисления:\n"
		decisionProgress += f"P = {resultsWhite} * {resultsBlack} / {resultsAll} = {answer}.\n"
		decisionProgress += f"{answer * 100:.2f} % является ответом для данной задачи."

		return Quest(template, decisionProgress, answer)
	
	def __quest2(self, **kwargs) -> Quest:
		cardCount = 32 # Питон, где константы
		pickCards = kwargs["pickCount"] if "pickCount" in kwargs else random.randint(cardCount / 4, 3 * cardCount / 4)

		pickRareCards = kwargs["pickRare"] if "pickRare" in kwargs else random.randint(1, 3)
		if (pickRareCards > 3):
			pickRareCards = 3

		cardName = random.choice(["Король", "Дама", "Туз", "Валет"])
		template =  f"В колоде {cardCount} карты. Наугад вынимают {pickCards} карт. Найти вероятность того, что среди них окажется "
		template += f"хотя бы {pickRareCards} карт достоинства \"{cardName}\"."

		decisionProgress =  f"Для верного решения задачи, мы можем выбрать от {pickRareCards} до {4} карт нужного достоинства. "
		decisionProgress += f"Выбор разного количества карт представляет из себя отдельную альтернативу. Сумма альтернаив есть "
		decisionProgress += f"ответ на задачу. Посчитаем их.\n"
	
		answer = 0.0
		for i in range(pickRareCards, 5):
			# import ipdb; ipdb.set_trace()
			alternative = Combinatorics.combinations(4, i) * Combinatorics.combinations(cardCount - 4, pickCards - i) / Combinatorics.combinations(cardCount, pickCards)
			answer += alternative
			decisionProgress += f"Мы можем выбрать {i} карт; шанс получения нужной комбинации: {alternative : .2f}.\n"
		
		answer = float(f"{answer : .4f}")
		decisionProgress += f"Проссумировав данные значения, мы получаем ответ на задачу: {answer} %."

		return Quest(template, decisionProgress, answer)

	def __quest3(self, **kwargs) -> Quest:
		nodesCount = 4
		nodesBreakChance = [random.randint(5, 15)*0.01 for i in range(0, nodesCount)]

		# Я понимаю как хреново читается эта жопка в шансе. Но я хочу попитонить, ня!
		chancesStr = ''.join([f'P({i + 1}) = {ch}; ' for i, ch in enumerate(nodesBreakChance)])
		chancesStr = chancesStr[0 : -2]

		templatesList = [
			f"При изготовлении детали заготовка должна пройти {nodesCount} операции. Предпологая появление брака на отдельных операциях "
			f"независимыми, найти вероятность изготовления стандартной детали, если вероятность появления брака на i-й операции "
			f"P(i) равны {chancesStr}?",

			f"Узел автомашины состоит из {nodesCount} деталей. Вероятности выхода деталей из строя равны {chancesStr}"
			f" и являются независимыми друг от друга. Узел выходит из строя, если сломается хотя бы одна деталь. Какова вероятность того, "
			f"что узел автомашины не выйдет из строя?"
		]
		template = random.choice(templatesList)

		answer = 1.0
		for i in nodesBreakChance:
			answer *= 1 - i

		decisionProgress =  "Для решения данной задачи необходимо просто перемножить вероятности, обратные данным для каждого узла (заготовки).\n"
		decisionProgress += f"P = {''.join([f'(1 - {i})' for i in nodesBreakChance])} = {answer : .2f}.\n"

		answer = float(f"{answer : .4f}")
		decisionProgress += f"Ответ: {answer} %."

		return Quest(template, decisionProgress, answer)

	def __quest9(self, **kwargs) -> Quest:
		casesCount = 3
		cases = dict() # Словарь вида Буква случая -> (Вероятность заболеть, вероятность выжить)

		def getP(max = 1) -> float:
			"""Генерирует и округляет вероятность"""
			p = random.uniform(0, max)
			return float(f"{p : .2f}")

		# Раскрою цикл так, чтобы точно оставались шансы. В цикле иногда багуется, не смог исправить (Лень))0)00
		cases['A'] = (random.randrange(10, 70), getP(0.95))
		cases['B'] = (random.randrange(10, 100 - cases['A'][0]), getP(0.95))
		cases['C'] = (100 - cases['A'][0] - cases['B'][0], getP(0.95))

		for k in cases.keys():
			cases[k] = (cases[k][0] * 0.01, cases[k][1]) # хз моно ли красивее сделать

		templatesList = [
			f"В больницу поступают в среднем {cases['A'][0]} больных с заболеванием А, {cases['B'][0]} с заболеванием В, {cases['C'][0]} с заболеванием "
			f"С. Вероятность полного выздоровления для каждого заболевания соответственно равны {cases['A'][1]}, {cases['B'][1]} и {cases['C'][1]}. "
			f"Больной был выписан здоровым. Найти вероятность того, что он страдал заболеванием А."
		]
		template = random.choice(templatesList)

		PZ = cases['A'][0] * cases['A'][1] + cases['B'][0] * cases['B'][1] + cases['C'][0] * cases['C'][1]
		print(f"{cases['A'][0]} * {cases['A'][1]} + {cases['B'][0]} * {cases['B'][1]} + {cases['C'][0]} * {cases['C'][1]}")
		PAZ = cases['A'][1] * cases['A'][0] / PZ

		PZ = float(f"{PZ : .2f}")
		answer = float(f"{PAZ : .2f}")

		decisionProgress =  f"Обозначим как P(Z) вероятность того, что больной выписан здоровым. P(Z) = {PZ}. Теперь мы можем вычислить  "
		decisionProgress += f"вероятность того, что он болел заболеванием А по формуле Бейеса: P(A / Z) = {answer}. Ответ на задачу: {answer}"

		return Quest(template, decisionProgress, answer)

	# TODO Нужны зависимости в генерации, а то часто бывают ответы уровня 0-0.5 и не более.
	def __quest10(self, **kwargs):
		n = kwargs["N"] if "N" in kwargs else random.randrange(12, 25)
		k = kwargs["K"] if "K" in kwargs else random.randrange(int(n * 0.1), int(n * 0.5))
		p = kwargs["P"] if "P" in kwargs else random.uniform(0.2, 0.6)
		p = float(f"{p : .2f}")

		templatesList = [
			f"За день в магазине было {n} покупателей. Вероятность найти покупку для каждого из них одинакова и равна {p}. Найти вероятность того, что {k} покупателей нашли покупку."
		]
		template = random.choice(templatesList)

		answer = Combinatorics.combinations(n, k) * p**k * (1-p)**(n-k)
		answer = float(f"{answer : .2f}")
		decisionProgress =  f"Воспользуемся распределением Бернулли и получим ответ: {answer}"

		return Quest(template, decisionProgress, answer)