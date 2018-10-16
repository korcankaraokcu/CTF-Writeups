The binary is written in C# so I've decompiled it with dnSpy
![](images/dnSpy-x86_1.png)  
That funny looking function calls another funny looking one
![](images/dnSpy-x86_2.png)  
And this goes on and on and on for god knows how many times  
At last, it lands on a function that looks like this  
![](images/dnSpy-x86_3.png)  
Of course, this isn't the real flag. Actually, there are 10098 of them
![](images/cheatengine-x86_64_1.png)  
Continuing with the Cheat Engine from now on  
Put a breakpoint at the line that comes after the `Readline` call to view the string object returned from the `Readline` call  
Returned string object is kept in `eax`, check bottom left window
![](images/cheatengine-x86_64_2.png)  
Skipping to the `ReadKey` call, look who is allocated next to our input :smiley:
![](images/cheatengine-x86_64_3.png)  
We got the flag!  
![](images/TrashCTF_1.png)
