# -*- coding: utf-8 -*-

import timeit

start = timeit.default_timer()

print('Hello, world!')

end = timeit.default_timer()

result = (end - start) * 1e3

print('Time: %.3f (ms)' % (result))

