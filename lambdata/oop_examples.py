class BareMinimumClass:
    pass


class Complex:
    def __init__(self, realpart, imagpart):
        """
        Constructor for Complex numbers.
        Complex numbers are part real, part imaginary.
        Imaginary numbers are roots of negative numbers.
        """
        self.r = realpart
        self.i = imagpart

    def add(self, other_complex):
        self.r += other_complex.r
        self.i += other_complex.i

    def __repr__(self):
        return '({}, {})'.format(self.r, self.i)


class SocialMediaUser:
    def __init__(self, name, location, upvotes=0):
        self.name = str(name)
        self.location = location
        self.upvotes = int(upvotes)

    def recieve_upvote(self):
        self.upvotes += 1

    def is_popular(self):
        return self.upvotes > 100


class Animal:
    """ General class for all animals to use"""
    def __init__(self, name, weight, diet_type):
        self.name = str(name)
        self.weight = float(weight)
        self.diet_type = str(diet_type)

    def run(self):
        return 'Va Va Voom!'

    def golden_dragon(self):
        return 'Skadoosh!'

    def eat(self, food):
        return food + ' is delicious! Yummy in my tummy!'


class Anteater(Animal):
    """ A sub class of anima;, a storage object for the Anteater Class"""

    def __init__(self, name, weight, diet_type='Ants', nose_length):
        super().__init__(name, weight)
        self.diet_type = diet_type
        self.nose_length = nose_length

    def whose_arthur(self):
        return "Yeah, I know that dude Arthur the Aardvark!\n He got his own TV show didn't he?"

    def run(self):
        return 'Skitter Patter!'


class Tiger(Animal):
    """ A sub class of animal, a storage object for the Tiger class."""
    def __init__(self, name, weight, diet_type, num_stripes):
        super().__init__(name, weight, diet_type)
        self.num_stripes = int(num_stripes)

    def say_great(self):
        # Method that only exists for tigers
        return "It's GREEEAAAAT!"

    def run(self):
        # Overriding run to be different for tigers
        return 'Scamper-wooooosh!'


if __name__ == '__main__':
    # Demo code if you run `python oop_examples.py`
    # Example 0
    b = BareMinimumClass()
    # Example 1
    num1 = Complex(3, -5)
    num2 = Complex(-1, 6)
    num1.add(num2)
    print(num1.r, num1.i)
    # Example 2
    user1 = SocialMediaUser('erle', 'Jax')
    user2 = SocialMediaUser('John', 'New York', upvotes=50)
    user3 = SocialMediaUser('John Doe', 'Anytown, USA')
    print(user2.is_popular())  # False
    for _ in range(75):
        user2.receive_upvote()
    print(user2.is_popular())  # True