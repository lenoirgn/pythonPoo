#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
:mod:`recursive sorts`
:author: `FIL - FST - Univ. Lille.fr <http://portail.fil.univ-lille1.fr>`_
:date: 2016, september. Last revised: 2018, september

Some recursive sorting algorithms:

- quicksort
- mergesort

"""
from typing import Callable, TypeVar
from aplst import ApLst
from tdm07.annexe_tris import *
from tdm07.tris import *



T = TypeVar('T')


def compare(a: T, b: T) -> int:
    """
    return:
       - -1 if a < b
       -  1 if a > b
       -  0 if a = b
    precondition: a and b must be comparable with <
    exemples:

    $$$ compare(0, 1)
    -1
    $$$ compare('a', 'a')
    0
    $$$ compare((2, 1), (1, 2))
    1
    """
    if type(a)==type(b):
        if a<b:
            return -1
        elif a>b:
            return 1
        else:
            return 0
        
        


def length(li: ApLst) -> int:
    """
    return the length of li.

    precondition: none

    examples:

    $$$ length(ApLst())
    0
    $$$ length(ApLst(3, ApLst(1, ApLst(4, ApLst()))))
    3
    """
    temp=li
    comp=0
    while not temp.is_empty():
        comp+=1
        temp=temp.tail()
    return comp

def native_to_list(li: list[T]) -> ApLst:
    """
    return a recursive list containing the same element of li.

    precondition: none

    examples:

    $$$ native_to_list([]).is_empty()
    True
    $$$ rec_lst = native_to_list([3, 1, 4, 1, 5])
    $$$ length(rec_lst)
    5
    $$$ rec_lst.head()
    3
    $$$ l = rec_lst.tail()
    $$$ l.head()
    1
    $$$ l = l.tail()
    $$$ l.head()
    4
    """
    temp=li[::-1]
    res=ApLst()
    for el in temp:
        res=ApLst(el,res)
    return res
    
def list_to_native(li: ApLst) -> list[T]:
    """
    return a native python list containing the same element of li.

    precondition: none

    examples:

    $$$ list_to_native(ApLst())
    []
    $$$ list_to_native(ApLst(3, ApLst(1, ApLst(4, ApLst(1, ApLst(5, ApLst()))))))
    [3, 1, 4, 1, 5]
    """
    res = []
    temp=li
    while not temp.is_empty():
        res.append(temp.head())
        temp=temp.tail()
    return res
    


def is_sorted(l: ApLst, comp: Callable[[T, T], int]=compare) -> bool:
    """
    return True if list l is sorted by ascending order
    and False otherwise.

    precondition: elements of l must be comparable
    exemples:

    $$$ is_sorted(native_to_list([1, 2, 3, 4]))
    True
    $$$ is_sorted(native_to_list([1, 2, 4, 3]))
    False
    """
    temp=l
    tete=temp.head()
    trouve=True
    while not temp.is_empty() and trouve:
        temp=temp.tail()
        if  not temp.is_empty():
            if tete>temp.head():
                trouve=False
            tete=temp.head()
    return trouve
            


def split(l: ApLst) -> tuple[ApLst, ApLst]:
    """
    return a couple (l1,l2) of lists of equal length

    exemples:

    $$$ l = [3, 1, 4, 1, 5, 9, 2]
    $$$ l1, l2 = split(native_to_list(l))
    $$$ abs(length(l1) - length(l2)) <= 1
    True
    $$$ l3 = list_to_native(l1) + list_to_native(l2)
    $$$ len(l3) == len(l)
    True
    $$$ all(k in l for k in l3)
    True
    """
    temp=l
    temp=list_to_native(temp)
    l1,l2= native_to_list(temp[:len(temp)//2]),native_to_list(temp[len(temp)//2:])
    return (l1,l2)


def merge(l1: ApLst, l2: ApLst,
          comp: Callable[[T, T], int]=compare) -> ApLst:
    """
    return a list containing all elements de l1 and l2.
    If l1 and l2 are sorted, so is the returned list.

    precondition: elements of l1 and l2 are comparable
    exemples:

    $$$ list_to_native(merge(native_to_list([1, 3, 4, 9]), native_to_list([1, 2, 5])))
    [1, 1, 2, 3, 4, 5, 9]
    """
    li1= list_to_native(l1)
    li2= list_to_native(l2)
    lif= li1+li2
    tri_select(lif,compare)
    return native_to_list(lif)
  
def mergesort(l: ApLst, comp: Callable[[T, T], int]=compare) -> ApLst:
    """
    return a new list containing elements of l sorted by ascending order.

    precondition: elements of l are comparable
    exemples:

    $$$ list_to_native(mergesort(native_to_list([3, 1, 4, 1, 5, 9, 2])))
    [1, 1, 2, 3, 4, 5, 9]
    $$$ import random
    $$$ n = random.randrange(20)
    $$$ l = native_to_list([random.randrange(20) for k in range(n)])
    $$$ l1 = mergesort(l)
    $$$ length(l1) == length(l)
    True
    $$$ is_sorted(l1)
    True
    """
    temp=list_to_native(l)
    tri_select(temp,compare)
    return native_to_list(temp)
    
    
    


if (__name__ == '__main__'):
    import l1test
    l1test.testmod("merge_sort.py")



