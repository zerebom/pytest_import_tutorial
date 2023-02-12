from my_package.greet import hello


def test_hello():
    import sys
    from pprint import pprint
    pprint(sys.path)
    assert hello() == "Hello."
