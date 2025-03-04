#   BaseException
#    +-- SystemExit
#    +-- KeyboardInterrupt
#    +-- GeneratorExit
#    +-- Exception
#    +-- StopIteration
#    +-- StopAsyncIteration
#    +-- ArithmeticError
#       | +-- FloatingPointError
#       | +-- OverflowError
#       | +-- ZeroDivisionError
#    +-- AssertionError
#    +-- AttributeError
#    +-- BufferError
#    +-- EOFError
#    +-- ImportError
#    +-- LookupError
#       | +-- IndexError
#       | +-- KeyError
#    +-- MemoryError
#    +-- NameError
#       | +-- UnboundLocalError
#    +-- OSError
#       | +-- BlockingIOError
#       | +-- ChildProcessError
#       | +-- ConnectionError
#       | | +-- BrokenPipeError
#       | | +-- ConnectionAbortedError
#       | | +-- ConnectionRefusedError
#       | | +-- ConnectionResetError
#       | +-- FileExistsError
#       | +-- FileNotFoundError
#       | +-- InterruptedError
#       | +-- IsADirectoryError
#       | +-- NotADirectoryError
#       | +-- PermissionError
#       | +-- ProcessLookupError
#       | +-- TimeoutError
#    +-- ReferenceError
#    +-- RuntimeError
#       | +-- NotImplementedError
#       | +-- RecursionError
#    +-- SyntaxError
#       | +-- IndentationError
#       | +-- TabError
#    +-- SystemError
#    +-- TypeError
#   +-- ValueError
#       | +-- UnicodeError
#       | +-- UnicodeDecodeError
#       | +-- UnicodeEncodeError
#       | +-- UnicodeTranslateError
#   +-- Warning
#   +-- DeprecationWarning
#   +-- PendingDeprecationWarning
#   +-- RuntimeWarning
#   +-- SyntaxWarning
#   +-- UserWarning
#   +-- FutureWarning
#   +-- ImportWarning
#   +-- UnicodeWarning
#   +-- BytesWarning
#   +-- ResourceWarning

class FooException(Exception):
    pass
import numpy as np

try:
    raise FooException("insert description here")
except FooException:
    print("A FooException was raised.")