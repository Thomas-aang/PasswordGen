import random
from tqdm import tqdm as l
import string as st
import time as t
lenx=int(input("Enter the maximum length of the password you need: "))
length=lenx
all=st.ascii_lowercase + st.ascii_uppercase + st.digits + st.punctuation
tmp=random.sample(all,length)
passcode = "".join(tmp)
t.sleep(2)
print("")
print("Hey! Don't forget to save the file in a secured place....")
t.sleep(3)
print("")
for i in l (range (100),desc="Loading…",ascii=False, ncols=75):
        t.sleep(0.15)
t.sleep(3)
print("")
print("Passcode has been generated-------------------------------------------> ")
t.sleep(2)
print("")
print("Here you go --> ",end="")
print(passcode)
