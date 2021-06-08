from collections import namedtuple

Transition = namedtuple('Transition', ['s', 'a', 'r', 's_next', 'done'])
