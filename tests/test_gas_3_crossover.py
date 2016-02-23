# coding=utf-8
# pylint: disable=missing-docstring,redefined-outer-name

"""
Genetic Algorithm Series - #2 Mutation tests
"""

from src.gas_3_crossover import crossover


def test_returns_correct_result():
    assert crossover('111000', '000110', 3), ['111110', '000000']


def test_last_gen_cross():
    assert crossover('110', '001', 2) == ['111', '000']


def test_full_cross():
    assert crossover('11111', '00000', 0) == ['00000', '11111']
