# Generated by ScalaTS 0.7.1-SNAPSHOT: https://scala-ts.github.io/scala-ts/

from dataclasses import dataclass
import typing  # noqa: F401
import datetime  # noqa: F401
import time  # noqa: F401


# Declare interface ClassWithTypeArgs

T = typing.TypeVar('T')


@dataclass
class ClassWithTypeArgs(typing.Generic[T]):
    name: str
    value: T
