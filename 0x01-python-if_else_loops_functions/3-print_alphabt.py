#!/usr/bin/python3

# ASCII in lowercase with a single print statement, excluding letters 'q' and 'e'
print((''.join(chr(i) for i in range(97, 123) if chr(i) not in {'q', 'e'}))
      .format(),
      end='')
