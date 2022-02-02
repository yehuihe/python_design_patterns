<h1>Repository for Mastering Python Design Patterns: 
A guide to creating smart, efficient and resuable software
 by Kamon Ayeva and Sakis Kasampalis</h1>

This repo is almost identical to Kamon's own repo:

https://github.com/PacktPublishing/Mastering-Python-Design-Patterns-Second-Edition

But with several error fixed in his code as well as some 
implementation for his suggested improvements. Also I included some of my own practices
with design patterns. Supposed more improvement are yet to be implemented 
will have TODO notes. I followed more PEP 8 style than Kamon did.

In short. An expansion on Kamon's book which I really enjoy reading.

# Important Notes
Kamon's repo is inactive for a few years. Therefore my repo serve as a 
continuation of his work and fixing bugs or compatibility issues I found.
I posted any problems on <b>Issues</b> of his repo and recorded below.

1. chapter13/interpreter.py

    line 141: arg_str = ' '.join(cmd)

    Trigger the ValueError exception.

    Should be arg_str = ' '.join(arg)


2. chapter14

    RxPy 3.2.0 Compatibility Issue

    RxPy 3.2.0 made changes that cancelled Observer class. Therefore in chapter14 code need significant update.
    
    Reflexed in my code in chapter14
