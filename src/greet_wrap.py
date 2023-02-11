from greet import hello


def double_hello():
    return hello() * 2


if __name__ == "__main__":
    print(double_hello())
