import typing
from UniGrammarRuntime.IWrapper import IWrapper, IParseResult


class record(IParseResult):
	__slots__ = ("commented", "rType", "options", "uri", "distribution", "components")

	def __init__(self):
		self.commented = None
		self.rType = None
		self.options = None
		self.uri = None
		self.distribution = None
		self.components = None


class component(IParseResult):
	__slots__ = ("cId",)

	def __init__(self):
		self.cId = None


class optionsR(IParseResult):
	__slots__ = ("pairs",)

	def __init__(self):
		self.pairs = None


class optionsList(IParseResult):
	__slots__ = "firstOption", "restOptions"

	def __init__(self):
		self.firstOption = None
		self.restOptions = None


class additionalOption(IParseResult):
	__slots__ = "separator", "option"

	def __init__(self):
		self.separator = None
		self.option = None


class optionR(IParseResult):
	__slots__ = "key", "value"

	def __init__(self):
		self.key = None
		self.value = None


class recordParser(IWrapper):
	__slots__ = ()

	def process_record(self, parsed) -> record:
		rec = record()
		rec.commented = self.process_commenterR_opt_our(getattr(parsed, "commented", None))
		rec.rType = self.backend.terminalNodeToStr(parsed.rType)
		rec.options = self.process_optionsR_opt_our(getattr(parsed, "options", None))
		rec.uri = self.backend.getSubTreeText(parsed.uri)
		rec.distribution = self.backend.getSubTreeText(parsed.distribution)
		rec.components = self.process_componentsR(parsed.components)
		return rec

	def process_commenterR_opt_our(self, parsed) -> typing.Optional[str]:
		return self.backend.enterOptional(parsed, self.backend.getSubTreeText)

	def process_optionsR_opt_our(self, parsed) -> typing.Optional[optionsR]:
		return self.backend.enterOptional(parsed, self.process_optionsR)

	def process_component(self, parsed) -> component:
		rec = component()
		rec.cId = self.backend.getSubTreeText(parsed.cId)
		return rec

	def process_componentsR_(self, parsed) -> typing.Iterable[component]:
		for f in self.backend.wstr.iterateCollection(parsed):
			yield f

	def process_componentsR(self, parsed) -> typing.Iterable[component]:
		return [self.process_component(f) for f in self.process_componentsR_(parsed)]

	def process_optionsR(self, parsed) -> optionsR:
		rec = optionsR()
		rec.pairs = self.process_optionsList(parsed.pairs)
		return rec

	def process_optionsList(self, parsed) -> optionsList:
		rec = optionsList()
		rec.firstOption = self.process_optionR(parsed.firstOption)
		rec.restOptions = self.process_additionalOptions(parsed.restOptions)
		return rec

	def process_additionalOptions_(self, parsed) -> typing.Iterable[additionalOption]:
		for f in self.backend.wstr.iterateCollection(parsed):
			yield f

	def process_additionalOptions(self, parsed) -> typing.Iterable[additionalOption]:
		return [self.process_additionalOption(f) for f in self.process_additionalOptions_(parsed)]

	def process_additionalOption(self, parsed) -> additionalOption:
		rec = additionalOption()
		rec.separator = self.backend.terminalNodeToStr(parsed.separator)
		rec.option = self.process_optionR(parsed.option)
		return rec

	def process_optionR(self, parsed) -> optionR:
		rec = optionR()
		rec.key = self.backend.terminalNodeToStr(parsed.key)
		rec.value = self.backend.getSubTreeText(parsed.value)
		return rec

	__MAIN_PRODUCTION__ = process_record


__MAIN_PARSER__ = recordParser
