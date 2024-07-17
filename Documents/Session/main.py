import random
from string import ascii_uppercase, ascii_lowercase, digits

letters_upper = [letter for letter in ascii_uppercase if letter != 'L' and letter != 'O']
letters_lower = [letter_lower for letter_lower in ascii_lowercase if letter_lower != 'l' and letter_lower != 'o']
digits = [digit for digit in digits if digit != '0' and digit != '1']
together = letters_lower + letters_upper + digits


def generate_password(length: int) -> str:
    res = random.choice(letters_upper) + random.choice(letters_lower) + random.choice(digits)
    # 3 letters out from looping in res
    length = length - 3
    if length < 0:
        raise ValueError("Length is less than 3")
    while length != 0:
        res += random.choice(together)
        length -= 1
    return res


def generate_passwords(count: int, length: int) -> list:
    array = []
    for _ in range(count):
        password = generate_password(length)
        array.append(password)
    return array


n, m = int(input("Count: ")), int(input("Length must be bigger than two: "))
result = generate_passwords(count=n, length=m)

for i in result:
    print(i)
