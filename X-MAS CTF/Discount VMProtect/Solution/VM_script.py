src="""18 72 A2 A4 9D 89 1F A2  8D 9B 94 0D 6D 9B 95 EC
EC 12 9B 94 23 16 9B 6C  13 0E 6D 0D 96 8D 0E 90
13 97 8A BB CF 64 7E D3  1A 40 23 EC DF 00""".split()
src=[int("0x"+x,16) for x in src]

s=[0]*1280
test_str="AAAABBBBCCCCDDDD"
for x in range(len(test_str)):
    s[x]=ord(test_str[x])

byte_6025A0=[0]*256

counter=0
rbp_8=0
dword_602580=0

s[rbp_8+256]=byte_6025A0[128] ; rbp_8+=1
byte_6025A0[0] = 1
for x in range(len(src)):
    byte_6025A0[10+x]=src[x]
while True:
    s[rbp_8 + 256] = s[rbp_8 + 255] ; rbp_8+=1
    s[rbp_8 + 256] = s[rbp_8 + 255] ; rbp_8+=1
    byte_6025A0[128] = s[rbp_8 + 255] ; rbp_8-=1
    s[rbp_8 + 255] = s[s[rbp_8 + 255]]
    rbp_8-=1
    if s[rbp_8+1 + 255]==0:
        break
    s[rbp_8 + 256]=1 ; rbp_8+=1
    s[rbp_8 + 254]=(s[rbp_8 + 255]+s[rbp_8 + 254]) & 0xFF ; rbp_8-=1
    s[rbp_8 + 256] = s[rbp_8 + 255] ; rbp_8+=1
    s[rbp_8 + 256] = s[rbp_8 + 255] ; rbp_8+=1
    s[rbp_8 + 254]=(s[rbp_8 + 254]-s[rbp_8 + 255]) & 0xFF ; rbp_8-=1
    rbp_8-=1
    if s[rbp_8+1 + 255]==0:
        continue
    else:
        break
s[rbp_8 + 256]=35 ; rbp_8+=1
s[rbp_8 + 254]=(s[rbp_8 + 254]-s[rbp_8 + 255]) & 0xFF ; rbp_8-=1
rbp_8-=1
if s[rbp_8+1 + 255]!=0:
    s[rbp_8 + 256]=0 ; rbp_8+=1
    byte_6025A0[0] = s[rbp_8 + 255] ; rbp_8-=1
s[rbp_8 + 256]=0 ; rbp_8+=1
byte_6025A0[128] = s[rbp_8 + 255] ; rbp_8-=1
print(s)

counter=0
rbp_8=0

s[rbp_8+256]=byte_6025A0[128] ; rbp_8+=1
while True:
    s[rbp_8 + 256] = s[rbp_8 + 255] ; rbp_8+=1
    s[rbp_8 + 256] = s[rbp_8 + 255] ; rbp_8+=1
    byte_6025A0[128] = s[rbp_8 + 255] ; rbp_8-=1
    s[rbp_8 + 255] = s[s[rbp_8 + 255]]
    s[rbp_8 + 256] = s[rbp_8 + 255] ; rbp_8+=1
    rbp_8-=1
    if s[rbp_8+1 + 255]==0:
        break
    s[rbp_8 + 255]=((s[rbp_8 + 255] << 7) | (s[rbp_8 + 255] >> 1)) & 0xFF
    s[rbp_8 + 256]=99 ; rbp_8+=1
    s[rbp_8 + 254]=(s[rbp_8 + 255]^s[rbp_8 + 254]) & 0xFF ; rbp_8-=1
    s[rbp_8 + 256]=152 ; rbp_8+=1
    s[rbp_8 + 254]=(s[rbp_8 + 255]+s[rbp_8 + 254]) & 0xFF ; rbp_8-=1
    s[rbp_8 + 255]=~s[rbp_8 + 255] & 0xFF
    dword_602580+=1
    s[rbp_8+256]=byte_6025A0[128] ; rbp_8+=1
    s[rbp_8 + 256]=10 ; rbp_8+=1
    s[rbp_8 + 254]=(s[rbp_8 + 255]+s[rbp_8 + 254]) & 0xFF ; rbp_8-=1
    s[rbp_8 + 255]=byte_6025A0[s[rbp_8 + 255]]
    s[rbp_8 + 254]=(s[rbp_8 + 254]-s[rbp_8 + 255]) & 0xFF ; rbp_8-=1
    rbp_8-=1
    if s[rbp_8+1 + 255]!=0:
        s[rbp_8 + 256]=0 ; rbp_8+=1
        byte_6025A0[0] = s[rbp_8 + 255] ; rbp_8-=1
    s[rbp_8 + 256]=1 ; rbp_8+=1
    s[rbp_8 + 254]=(s[rbp_8 + 255]+s[rbp_8 + 254]) & 0xFF ; rbp_8-=1
    s[rbp_8 + 256] = s[rbp_8 + 255] ; rbp_8+=1
    s[rbp_8 + 256] = s[rbp_8 + 255] ; rbp_8+=1
    s[rbp_8 + 254]=(s[rbp_8 + 255]^s[rbp_8 + 254]) & 0xFF ; rbp_8-=1
    rbp_8-=1
    if s[rbp_8+1 + 255]==0:
        continue
    else:
        break

print(s)
