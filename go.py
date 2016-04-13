from main import main

for x in xrange(1, 73):
    print "Running for latitude", str(x)
    main(x - 1, x, 0, 144, '/home/csc422/topcsvdata/')
