""" from amostras_madlibs import hp, code, zombie, hungergames
import random

if __name__ == "__main__":
    m = random.choice([hp, code, zombie, hungergames])
    m.madlib() """

from amostras_madlibs import code
import random

if __name__ == "__main__":
    m = random.choice([code])
    m.madlib()