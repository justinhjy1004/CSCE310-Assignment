import time
import math

def rus_multiplication(x,y):

    solution = 0

    if x == 1:
        return y

    while(x != 1):
        if not(x & 1):
            x = x >> 1
            y = y << 1
        else:
            solution = solution + y
            x = x >> 1
            y = y << 1

    solution = solution + y

    return solution

def karatsuba(x, y):
    if x < 10 and y < 10:
        return x * y

    n = max(len(str(x)), len(str(y)))
    m = int(math.ceil(float(n) / 2))

    # divide x into two half
    xh = int(math.floor(x / 10 ** m))
    xl = int(x % (10 ** m))

    # divide y into two half
    yh = int(math.floor(y / 10 ** m))
    yl = int(y % (10 ** m))

    # Karatsuba's algorithm.
    s1 = karatsuba(xh, yh)
    s2 = karatsuba(yl, xl)
    s3 = karatsuba(xh + xl, yh + yl)
    s4 = s3 - s2 - s1

    return int(s1 * (10 ** (m*2)) + s4 * (10 ** m) + s2)


if __name__ == "__main__":

    x = 3564425341984098130593642452352352545245823522435245245245259796945634563465374545346534545646787674564635746857967867534576878564535768756745634657687564756345768756745634657676534536896867989677686786786786798678867924245252452346858758678672445235254252352453520948012235245235235235235948098039481048013958409683052345264354624354623452644335246534564986034582934563545456343463463463465363452381305982093581039641847813759879481739582793871394857982749813572698479827538246982572
    y = 462625326049852093840924860928509180398094523523524523245235425347464574654745745968896976967896787698797696796796867867864572343254234325354287567546376878567456746875674567685475633523524523524523523524355235325820498029235462445235624354523412452246235465645224634251345364213541454635723524139593827489137598247359248379184759183759468273068972309587628374594872958724289457293875293857928579832457928374298137524834795427
    start_time = time.time()
    print(x*y)
    print("Python:")
    print("--- %s seconds ---" % (time.time() - start_time))

    start_time = time.time()
    print(rus_multiplication(x,y))
    print("Russian:")
    print("--- %s seconds ---" % (time.time() - start_time))

    print(x*y == rus_multiplication(x,y))

    start_time = time.time()
    print(karatsuba(x,y))
    print("Karatsuba: ")
    print("--- %s seconds ---" % (time.time() - start_time))