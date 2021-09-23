#!/usr/bin/env python
# coding: utf-8

# In[4]:


#factorial of a number
f = 1
a = int(input("Enter a Number"))
if a<0:
    print("ERROR ! ENTER A VALID NUMBER !")
elif a==0:
    print("Factorial of a is 1")
else:
    for i in range(1,a+1):
        f = f*i
    print("Factorial of the number is",f)


# In[ ]:




