import importlib
import sys

sys.modules["foo.bar"] = importlib.import_module("spam")

del importlib, sys