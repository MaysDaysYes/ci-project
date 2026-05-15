import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from main import greet


def test_greet():
    assert greet() == "Hello from peresdacha!"
