#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
:mod:`mergesort_analysis` module
:author: FIL - FST - Univ. Lille <http://portail.fil.univ-lille.fr>_
:date: 2024, April. 

Experimental analysis of mergesort algorithm

"""
import random

import matplotlib.pyplot as plt
from ap_decorators import count
from aplst import ApLst
from merge_sort import compare, mergesort, native_to_list


def random_list(size: int) -> ApLst:
    """Return a list of len size containing all natural numbers from 0 to n-1 in random order.

    Précondition : n >= 0
    """
    li = list(range(size))
    random.shuffle(li)
    return native_to_list(li)


def myplot(listX: list[float], listY: list[float],
           title: str = '', xlabel: str = '', ylabel: str = ''):
    """Plot the data in listX and listY."""
    plt.plot(listX, listY)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()


def build_comp_number_list(sort, max_size: int, sample_size: int) -> list[float]:
    """Return the list of average number of comparisons for sorting lists of size up to max_size."""
    comp = count(compare)
    nb_comps = []
    for size in range(1, max_size):
        comp.counter = 0
        for _ in range(sample_size):
            sort(random_list(size), comp=comp)
        nb_comps.append(comp.counter / sample_size)
    return nb_comps


def usage():
    """Print usage."""
    print('Usage: {:s} <max size> <sample size>'.format(sys.argv[0]),
          file=sys.stderr)
    print('\t<max size> = max size of lists to sort', file=sys.stderr)
    print('\t<sample size> = size of samples.', file=sys.stderr)
    exit(1)


if __name__ == '__main__':
    import sys

    if len(sys.argv) != 3:
        print('Bad number of arguments!', file=sys.stderr)
        usage()
    try:
        MAX_SIZE = int(sys.argv[1])
    except ValueError:
        print('Max size must be an integer!', file=sys.stderr)
        usage()
    SIZES = list(range(1, MAX_SIZE))
    try:
        SAMPLE_SIZE = int(sys.argv[2])
    except ValueError:
        print('Sample size must be an integer!', file=sys.stderr)
        usage()
    # all is OK!
    NB_COMPS = build_comp_number_list(mergesort, MAX_SIZE, SAMPLE_SIZE)
    myplot(SIZES, NB_COMPS,
           title=f'Nbre de comparaisons du tri fusion (mesuré sur échantillon de taille {SAMPLE_SIZE})',
           xlabel='taille des listes',
           ylabel='nbre de comparaisons')

