"""
for i in range(35):
    x=user_input[i]
    a=((x << 7) | (x >> 1)) & 0xFF
    a=a^99
    a=(a+152) & 0xFF
    a=~a
    if a!=src[i]:
        byte_6025A0[0]=0
        break
"""

src="""18 72 A2 A4 9D 89 1F A2  8D 9B 94 0D 6D 9B 95 EC
EC 12 9B 94 23 16 9B 6C  13 0E 6D 0D 96 8D 0E 90
13 97 8A BB CF 64 7E D3  1A 40 23 EC DF 00""".split()
src=[int("0x"+x,16) for x in src]

flag=""

for x in src:
    x=~x & 0xFF
    x=(x-152) & 0xFF
    x^=99
    for y in range(256):
        if ((y << 7) | (y >> 1)) & 0xFF == x:
            flag+=chr(y)

print(flag)
