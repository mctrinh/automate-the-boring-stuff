import sys

if len(sys.argv) > 1:
    print(sys.argv)
    print(' '.join(sys.argv[1:]))
else:
    print (sys.argv)