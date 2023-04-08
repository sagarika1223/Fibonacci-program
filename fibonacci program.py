#!/usr/bin/env python
# coding: utf-8

# In[7]:


# Program to display the Fibonacci sequence between 1 to 50

num = int(input("enter a number? "))

n1, n2 = 0, 1
count = 0

if num <= 0:
   print("Please enter a positive integer")

elif num == 1:
   print("Fibonacci sequence upto",num,":")
   print(n1)

else:
   print("Fibonacci sequence is:")
   while count < num:
       print(n1)
       nth = n1 + n2
       # update values
       n1 = n2
       n2 = nth
       count += 1


# In[ ]:





# In[ ]:




