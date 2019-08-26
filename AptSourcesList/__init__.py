import typing
import parglare
from pathlib import Path
import _io

thisDir = Path(__file__).parent

g = parglare.Grammar.from_file(str(thisDir / "grammar.pglr"))
parser = parglare.Parser(g, ws="")


class Record:
	__slots__ = ("commented", "type", "options", "uri", "distribution", "components")

	def __init__(self, s):
		parsed = parser.parse(s)
		for attrName in parsed._pg_attrs:
			setattr(self, attrName, getattr(parsed, attrName))

		self.commented = bool(self.commented)

		if self.options:
			if self.options.pairs:
				res = [self.options.pairs.firstOption]
				for p in self.options.pairs.restOptions:
					res.append(p.option)
				self.options = res
				self.options = {p.key: p.value for p in self.options}

		if self.components:
			self.components = [c.id for c in self.components]

	def serializeOptions(self):
		if self.options:
			return "[" + ",".join(k + "=" + v for k, v in self.options.items()) + "]"
		return ""

	def serializeComponents(self):
		if self.components:
			return " ".join(self.components)
		return ""

	def __str__(self):
		return " ".join(filter(None, ("#" if self.commented else "", self.type, self.serializeOptions(), self.uri, self.distribution, self.serializeComponents())))

	def __repr__(self):
		return self.__class__.__name__ + "(" + repr(str(self)) + ")"


def parseSourceList(lst: typing.Union[str, Path, _io._TextIOBase] = None):
	if lst is None:
		lst = Path("/etc/apt/sources.list")

	if isinstance(lst, str):
		lines = lst.splitlines()
	elif isinstance(lst, Path):
		lines = lst.open("rt", encoding="utf-8")
	elif isinstance(lst, _io._TextIOBase):
		lines = lst
	else:
		raise ValueError("`lst` has wrong type")

	for l in lines:
		l = l.strip()
		if l:
			try:
				parsed = Record(l)
				yield parsed
			except parglare.exceptions.ParseError as ex:
				if l[0] == "#":
					yield l
				else:
					raise
		else:
			yield ""
