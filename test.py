# import random
import random

# Getting user input
x=int(input('Ch BW for 5GHz frequency [1] 20MHz [2] 40MHz [3] 80MHz:'))
y=int(input('[1] DFS [2] Non-DFS:'))
# DFS channels
DFS_ch=[52,56,60,64,100,104,108,112,116,120,124,128,132,136,140,144,54,62,102,110,118,126,134,142,58,106,122,138]
Non_DFS_Ch=[36,40,44,48,149,153,157,161,165,38,46,151,159,42,155]
# Select random choice
a=(0,1)
# Checking DFS channel availablity for diff BW
# 20MHz Bandwidth
if y==1:
    print("DFS Channels:",DFS_ch[0:16])
    y=int(input("Enter the channel number:"))
    z=(random.choice(a)) if y in DFS_ch[0:16] else print("Enter the correct channel:") 
    print("Channel is available") if z==0 else print("Channel is not available")
    if y==2:
        print("Non DFS Channels:",Non_DFS_Ch[0:10])
        y=int(input("Enter the channel number:"))
        z=(random.choice(a)) if y in Non_DFS_Ch[0:10] else print("Enter the correct channel:") 
        print("Channel is available") if z==0 else print("Channel is not available")



# 40MHz Bandwidth    
elif y==2:
    print("DFS Channels:",DFS_ch[16:24])
    y=int(input("Enter the channel number:"))
    z=(random.choice(a)) if y in DFS_ch[16:24] else print("Enter the correct channel:")
    print("Channel is available") if z==0 else print("Channel is not available")
    if y==1:
        print("Non DFS Channels:",Non_DFS_Ch[0:10])
        y=int(input("Enter the channel number:"))
        z=(random.choice(a)) if y in Non_DFS_Ch[0:10] else print("Enter the correct channel:") 
        print("Channel is available") if z==0 else print("Channel is not available")


# 80MHz Bandwidth    
elif x==3:
    print("DFS Channels:",DFS_ch[24:30])
    y=int(input("Enter the channel number:"))
    z=(random.choice(a)) if y in DFS_ch[24:30] else print("Enter the correct channel:")
    print("Channel is available") if z==0  else print("Channel is not available")
    if y==1:
        print("Non DFS Channels:",Non_DFS_Ch[0:10])
        y=int(input("Enter the channel number:"))
        z=(random.choice(a)) if y in Non_DFS_Ch[0:10] else print("Enter the correct channel:") 
        print("Channel is available") if z==0 else print("Channel is not available")
