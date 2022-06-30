#!/usr/bin/python3
"""Ordered set implementations."""

from collections import abc


class _OrderedSetBase(object):

    def __init__(self, iterable=None):
        self._set = collections.OrderedDict()
        if iterable:
            for i in iterable:
                self._set[i] = 1

    def __len__(self):
        return len(self._set)

    def __contains__(self, thing):
        return thing in self._set

    def __iter__(self):
        return iter(self._set)


class _MutableSetBase(_OrderedSetBase):
    def add(self, thing):  # pylint:disable=g-bad-name
        self._set[thing] = 1

    def discard(self, thing):  # pylint:disable=g-bad-name
        if thing in self._set:
            del self._set[thing]

    def clear(self):  # pylint:disable=g-bad-name
        self._set.clear()


class FrozenOrderedSet(_OrderedSetBase, abc.Set, abc.Hashable):
    __hash__ = abc.Set._hash


class MutableOrderedSet(_MutableSetBase, abc.MutableSet):
    pass
