
def divisors(num):
    cur = 1
    end = num
    divisors = []
    while cur < end:
        mod = num % cur
        if mod == 0:
            divisors.append(cur)
        print "cur=", cur, "end=", end
        end = num / cur
        cur += 1

    return divisors

def triangle_number(n):
    # This formula is quite well-known -> makes the problem easier!
    return n*(n+1) / 2
   
 
if  __name__ == "__main__":
    
    for i in range(1, 10):
        triangle_num = triangle_number(i)
        print i, triangle_num, divisors(triangle_num)



