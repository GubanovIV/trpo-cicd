def greet() -> None:
    gr = "Hello world\n"
    for i in gr:
        print(i, end="")


def xor(a: int, b: int) -> int:
    return a ^ b


if __name__ == "__main__":
    greet()
