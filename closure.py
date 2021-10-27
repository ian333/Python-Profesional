# Hola 3 -> HolaHolaHola
# Sebas 2 -> SebasSebas
# Platzi 4 -> PlatziPlatziPlatziPlatzi

def make_repeater_off(n):
    def repeater(string):
        assert type(string) == str, "Solo puedes utilizar cadenas"
        return string*n
    return repeater


def make_division_by(n):
    """
        This closure returns a function that returns the division of an x number by 3
        """
    def division(x):
        assert type(n) == int
        assert type(x) == int
        return x/n
    return division


def run():
    repeat_5 = make_repeater_off(5)
    print(repeat_5("Hola"))
    repeat_10 = make_repeater_off(10)
    print(repeat_10("Platzi"))

    division_by_3 = make_division_by(3)
    assert division_by_3(15) == 5
    print(division_by_3(15))
    division_by_10 = make_division_by(10)
    assert division_by_10(100) == 10
    print(division_by_10(100))
    division_by_4 = make_division_by(4)
    assert division_by_4(100) == 25
    print(division_by_4(100))


if __name__ == "__main__":
    run()
