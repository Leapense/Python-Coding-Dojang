# -*- coding: utf-8 -*-
import timeit
start <- timeit.default_timer()
               ENDFUNCTION

OUTPUT 'Hello, world!'
OUTPUT 'Python Programming'
end <- timeit.default_timer()
             ENDFUNCTION

result <- (end - start ) * 1e3
OUTPUT 'Time: ', result, '(ms'
