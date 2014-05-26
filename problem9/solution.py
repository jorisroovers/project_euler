

if __name__ == "__main__":
    total = 1000
    # Very inefficient, but does the job
    def find_abc():
        for a in xrange(1, total+1):
            for b in xrange(1, total+1):
                if a + b > total:
                    continue
                for c in xrange(1, total+1):
                    if a + b + c == total:
                        if (a**2 + b**2) == c**2:
                            return (a, b, c)
    a, b, c = find_abc()
    print "Solution: ", (a*b*c)
    
