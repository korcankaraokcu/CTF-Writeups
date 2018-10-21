I'm going to use [PINCE](https://github.com/korcankaraokcu/PINCE) for this challenge
### The proper way
As usual, set a breakpoint at the `main`(or `main.main` in our case)

![](images/pince1.png)  

Apparently, `main.main` calls `main.FLAG_NATIVE_BLOWFISH_ENCRYPTION`, stepping into that

![](images/pince2.png)  

It calls `runtime.stringtoslicebyte` with the parameter `sifrelemeanahtari` to convert that string into a bytearray

![](images/pince3.png)  

Then `NewCipher` is called with that bytearray to create a new cipher

![](images/pince4.png)  

Then `Decrypt` is called with that cipher and bytearray

![](images/pince5.png)  

`Decrypt` is called once again with the cipher and the return value of the last `Decrypt` call

![](images/pince6.png)  

`Decrypt` is called for the last time with the cipher and the return value of the last `Decrypt` call

![](images/pince7.png)  

Stepping out of the last `Decrypt` call reveals our flag  
So the psuedocode would probably look like this:
```
key="sifrelemeanahtari"
bytes=stringtoslicebyte(key)
cipher=NewCipher(bytes)
v1=Decrypt(cipher, bytes)
v2=Decrypt(cipher, v1)
v3=Decrypt(cipher, v2)  # v3 is our flag
```
### The automated way
Using [CTF-Tools](https://github.com/korcankaraokcu/CTF-Tools)

![](images/auto1.png)  

![](images/auto2.png)
