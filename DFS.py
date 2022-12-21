import random
a=(0,1)
x=int(input('Ch BW [1] 20MHz [2] 40MHz [3] 80MHz:'))
DFS_ch=[52,56,60,64,100,104,108,112,116,120,124,128,132,136,140,144,54,62,102,110,118,126,134,142,58,106,122,138]
if x==1:
    print("DFS Channels:",DFS_ch[0:16])
    y=int(input("Enter the channel number:"))
    z=(random.choice(a)) if y in DFS_ch[0:16] else print("Enter the correct channel:")
    print("Channel is available") if z==0 else print("Channel is not available")
'''elif x==2:
    print("DFS Channels:",DFS_ch[16:24])
    y=int(input("Enter the channel number:"))
    if y in DFS_ch[16:24]:
        z=(random.choice(a))
        print("Channel is available") if z==0 else print("Channel is not available")
elif x==3:
    print("DFS Channels:",DFS_ch[24:30])
    y=int(input("Enter the channel number:"))
    if y in DFS_ch[24:30]:
        z=(random.choice(a))
        print("Channel is available") if z==0  else print("Channel is not available")'''