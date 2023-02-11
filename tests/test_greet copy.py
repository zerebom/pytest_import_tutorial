import pprint
import sys

from greet_wrap import double_hello

pprint.pprint(sys.path)


def test_hello():
    assert double_hello() == "Hello.Hello."
