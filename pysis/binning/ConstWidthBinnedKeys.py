# -*- coding: utf-8 -*-
#
#   ConstWidthBinnedKeys.py
#   Copyright 2011 William Trevor Olson <trevor@heytrevor.com>
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.
#


from math import ceil
from AbstractBinnedKeys import AbstractBinnedKeys

class ConstWidthBinnedKeys(AbstractBinnedKeys):
    """
    A Binned Keys construct where bins are of a constant width.
    """

    def __init__(self, min_value, max_value, num_bins=None, max_bin_size=None):
        """
        Create set of bins of the range `min_value` to `max_value` given either
        the number of bins `num_bins` or a maximum bin size `max_bin_size` with
        which to split the range.
        """
        self.min_value = float(min_value)
        self.max_value = float(max_value)

        if max_bin_size is not None:
            num_bins = ceil((self.max_value - self.min_value) / max_bin_size)

        self.num_bins = int(num_bins)

        self.bin_size = (self.max_value - self.min_value) / self.num_bins
        self.bins = [[] for _ in xrange(self.num_bins)]


    def get_bin_index(self, value):
        """
        Used to get the index of the bin to place a particular value.
        """
        if value == self.max_value:
            return self.num_bins - 1

        return int((value - self.min_value) / self.bin_size)


    def get_bounds(self, bin_num):
        """
        Get the bonds of a bin, given its index `bin_num`. A `Bounds` namedtuple
        is returned with properties min and max respectively.
        """
        min_bound = (self.bin_size * bin_num) + self.min_value
        max_bound = min_bound + self.bin_size

        return BinnedKeys.Bounds(min_bound, max_bound)
