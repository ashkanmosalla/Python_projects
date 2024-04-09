from abc import ABC, abstractmethod
import string
import random


words = ['ashkan', 'arash', 'pesareChirinoo', 'ramin', 'matool', 'mashool', 'apply']


class PasswordGenerator(ABC):
    @abstractmethod
    def generate(self):
        pass


class PinGenerator(PasswordGenerator):
    def __init__(self, length):
        self.length = length

    def generate(self):
        return ''.join([random.choice(string.digits) for _ in range(self.length)])
    

class RandomPasswordGenerator(PasswordGenerator):
    def __init__(self, length, include_numbers, include_symbols):
        self.length = length
        self.character = string.ascii_letters
        if include_numbers:
            self.character += string.digits
        if include_symbols:
            self.character += string.punctuation

    def generate(self):
        return ''.join([random.choice(self.character) for _ in range(self.length)])    


class MemorablePasswordGenerator(PasswordGenerator):
    def __init__(self, num_of_words= 4, separator= '-', capitalize= True, vocab= None):
        if vocab is None:
            self.vocab = nltk.corpus.words.words()
        self.num_of_words = num_of_words
        self.capitalize = capitalize
        self.separator = separator

    def generate(self):
        password_words = [random.choice(self.vocab) for _ in range(self.num_of_words)]
        if self.capitalize:
            password_words = [words.upper() if random.choice([True, False]) else words.lower() for words in password_words]
        
        return self.separator.join(password_words)


if __name__ == '__main__':
    p_obj = RandomPasswordGenerator(length= 10, include_numbers= True, include_symbols= True)
    print(p_obj.generate())