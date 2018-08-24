'''
print twice routines
'''

def print_twice(bruce):
    print(bruce)
    print(bruce)

def do_twice(f, val):
    f(val)
    f(val)

def print_spam(s):
    print(s)

do_twice(print_spam, "+i")

print('+', end=' ')
print('-')