def gcd(x, y):
    while x % y:
        x, y = y, x % y
    return y

s = input()
t = input()

s_len = len(s)
t_len = len(t)

gcd_st = gcd(s_len, t_len)
lcm_st = s_len * t_len // gcd_st

new_s = s * (lcm_st // s_len)
new_t = t * (lcm_st // t_len)

if new_s == new_t:
    print(1)
else:
    print(0)