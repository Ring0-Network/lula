"""Representation and strict-target guards for the accepted classical family."""
from dataclasses import dataclass
from fractions import Fraction
from math import comb

N = 1 << 128
COUNTER_SPACE = 1 << 32
QUERY_GRID = (24, 30, 38, 40, 41, 44, 50, 64)


def nonnegative_integer(value, name):
    if type(value) is not int or value < 0:
        raise ValueError(f'{name} must be a nonnegative integer')
    return value


def bounded_compositions(length, width, target):
    """Coefficient of x^target in (1+x+...+x^(width-1))^length."""
    return sum((-1)**j * comb(length, j) * comb(target-j*width+length-1, length-1)
               for j in range(min(length, target//width)+1))


@dataclass(frozen=True)
class Parameters:
    a: int
    r: int
    heights: tuple
    ell: tuple
    targets: tuple

    def __post_init__(self):
        for name in ('a', 'r'):
            nonnegative_integer(getattr(self, name), name)
        for name in ('heights', 'ell', 'targets'):
            vector = getattr(self, name)
            if not isinstance(vector, (list, tuple)):
                raise ValueError(f'{name} must be an integer vector')
            for value in vector:
                nonnegative_integer(value, name)
            object.__setattr__(self, name, tuple(vector))
        d = len(self.heights)
        if not 1 <= d <= 256 or len(self.ell) != d or len(self.targets) != d:
            raise ValueError('layer vectors must have equal length in 1..256')
        if not 1 <= self.a <= 31 or not 1 <= self.r <= 94:
            raise ValueError('FORS dimensions exceed the source schema')
        if any(h > 31 for h in self.heights) or self.height > 63:
            raise ValueError('height encoding overflow')
        if self.r * (1 << self.a) > 1 << 32:
            raise ValueError('global FORS index overflow')
        if (self.r+1)*self.a + self.height > 256:
            raise ValueError('digest coordinates exceed 256 bits')
        if 22+16*self.r+9 > 24*64:
            raise ValueError('FORS root compression scratch overflow')
        for i, (ell, target) in enumerate(zip(self.ell, self.targets)):
            width = self.width(i)
            full = 128 // (8 if i == d-1 else 4)
            if not 1 <= ell <= full or not 0 <= target < ell*(width-1):
                raise ValueError('nonempty strict target and full omitted-zero checks required')
            if bounded_compositions(ell, width, target) <= 0:
                raise ValueError('empty acceptance predicate')

    @property
    def height(self):
        return sum(self.heights)

    @property
    def layers(self):
        return len(self.heights)

    def width(self, layer):
        if type(layer) is not int or not 0 <= layer < self.layers:
            raise ValueError('layer index outside the parameter vector')
        return 256 if layer == self.layers-1 else 16

    @property
    def tails(self):
        return tuple(ell*(self.width(i)-1)-s
                     for i, (ell, s) in enumerate(zip(self.ell, self.targets)))

    @property
    def hidden_final_calls(self):
        return self.r + sum(self.tails)

    @property
    def graph_final_calls(self):
        return self.r*(self.a+1)+1+sum(t+1+h for t, h in zip(self.tails, self.heights))

    @property
    def classical_constant(self):
        return self.hidden_final_calls+self.graph_final_calls+self.layers+3

    def acceptance_probability(self, layer):
        """Omitted digits must be zero: the denominator is always 2^128."""
        return Fraction(bounded_compositions(self.ell[layer], self.width(layer),
                                             self.targets[layer]), N)

    @property
    def signature_bytes(self):
        return 20+16*self.r*(self.a+1)+sum(4+16*(ell+h)
                                         for ell, h in zip(self.ell, self.heights))

    @property
    def single_top_cache_bytes(self):
        return 36*(1 << self.heights[-1])-16


BASELINE = Parameters(9, 17, (5, 5, 5, 5, 21), (32, 32, 32, 32, 16),
                      (240, 240, 240, 240, 2040))
