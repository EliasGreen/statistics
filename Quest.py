class Quest():
	def __init__(self, wording: str, decisionProgress: str, answer: str):
		self._wording = wording
		self._decisionProgress = decisionProgress
		self._answer = answer

	@property
	def wording(self) -> str:
		return self._wording

	@property
	def decisionProgress(self) -> str:
		return self._decisionProgress

	@property
	def answer(self) -> str:
		return self._answer
