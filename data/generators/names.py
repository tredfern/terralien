import random

vowels = "aeiouy"
consonants = "bcdfghjklmnpqrstvwxyz"

def create_syllable():
    lengths = [1, 1, 2, 2, 2, 2, 3, 3, 3, 4]
    length = random.choice(lengths)

    if length == 1:
        return random.choice(vowels)
    elif length == 2:
        return random.choice(vowels) + random.choice(consonants)
    elif length == 3:
        return random.choice(consonants) + random.choice(vowels) + random.choice(consonants)
    else:
        return random.choice(consonants) + random.choice(vowels) + random.choice(vowels) + random.choice(consonants)


def create_name():
    syl = random.randint(2, 4)
    name = ""
    for i in range(syl):
        name += create_syllable()

    return name

def print_name():
    print( create_name() )

if __name__ == '__main__':
    print_name()
