# Copyright (C) 2009-2010 Sergey Koposov
# This file is part of astrolibpy
#
#    astrolibpy is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#   astrolibpy is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with astrolibpy.  If not, see <http://www.gnu.org/licenses/>.


import numpy, re
def from_hex(arr, delim=':'):
	r=re.compile('\s*(\-?)(.+)%s(.+)%s(.+)'%(delim,delim))
	ret=[]
	for a in arr:
		m = r.search(a)

		sign = m[1] == '-'
		sign = -1 if sign else 1
		i1 = int(m[2])
		i2 = int(m[3])
		i3 = float(m[4])
		val = sign * (i1 + i2 / 60. + i3 / 3600.)
		ret.append(val)
	return numpy.array(ret)
		
		