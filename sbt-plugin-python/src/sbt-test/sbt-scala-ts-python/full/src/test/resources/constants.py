# Generated by ScalaTS 0.5.14-SNAPSHOT: https://scala-ts.github.io/scala-ts/

from dataclasses import dataclass  # noqa: F401
import typing  # noqa: F401
import datetime  # noqa: F401

from generated import name  # noqa: F401
from generated.name import Name


# Declare singleton Constants
class ConstantsInvariantsFactory:
    @classmethod
    def code(self) -> int:
        return 1

    @classmethod
    def UnknownName(self) -> Name:
        return Name("unknown")

    @classmethod
    def defaultName(self) -> Name:
        return Name("default")

    @classmethod
    def list(self) -> typing.List[int]:
        return [self.code(), 2]

    @classmethod
    def dict(self) -> typing.Dict[str, typing.List[Name]]:
        return {"specific": [self.UnknownName(), self.defaultName(), Name("*")], "invalid": [Name("failed")]}

    @classmethod
    def excluded(self) -> typing.List[str]:
        return ["foo", "bar"]

    @classmethod
    def filtered(self) -> typing.List[str]:
        return self.excluded() + ["filtered"]

    @classmethod
    def names(self) -> typing.List[Name]:
        return [self.UnknownName(), self.defaultName()] + [Name("test")]


@dataclass
class IConstantsInvariants:
    code: int
    UnknownName: Name
    defaultName: Name
    list: typing.List[int]
    dict: typing.Dict[str, typing.List[Name]]
    excluded: typing.List[str]
    filtered: typing.List[str]
    names: typing.List[Name]


ConstantsInvariants = IConstantsInvariants(
    code=ConstantsInvariantsFactory.code(),
    UnknownName=ConstantsInvariantsFactory.UnknownName(),
    defaultName=ConstantsInvariantsFactory.defaultName(),
    list=ConstantsInvariantsFactory.list(),
    dict=ConstantsInvariantsFactory.dict(),
    excluded=ConstantsInvariantsFactory.excluded(),
    filtered=ConstantsInvariantsFactory.filtered(),
    names=ConstantsInvariantsFactory.names(),
)
