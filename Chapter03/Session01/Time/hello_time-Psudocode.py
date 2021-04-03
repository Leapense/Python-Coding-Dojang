# -*- coding: utf-8 -*-
import timeit
start <- timeit.default_timer()
               ENDFUNCTION

OUTPUT 'Hello, world!'
end <- timeit.default_timer()
             ENDFUNCTION

result <- (end - start) * 1e3
OUTPUT 'Time: %.3f (ms)' % (result)
