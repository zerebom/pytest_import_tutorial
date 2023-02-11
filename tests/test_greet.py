import pprint
import sys

from greet import hello

pprint.pprint(sys.path)


def test_hello():
    assert hello() == "Hello."

