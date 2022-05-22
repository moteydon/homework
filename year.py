# year=input("input a month")
# if year=="1":
#     print("janaury")
# elif year=="2":
#     print("feb")
# elif year=="3":
#     print("march")
# elif year=="4":
#     print("april")
# elif year=="5":
#     print("may")
# elif year=="6":
#     print("june")
# elif year=="7":
#     print("july")
# elif year=="8":
#     print("august")
# elif year=="9":
#     print("sept")
# elif year=="10":
#     print("october")
# elif year=="11":
#     print("november")
# elif year=="12":
#     print("december")
# else: 
#     print("error")
import pdb
bike1="yamaha"
bike1_price =250000
bike2="honda"
bike2_price =50000
pdb.set_trace()
name=input("enter your name:")
choose=int(input("press 1 for yamaha and 2 for honda:"))
print(f"hello{name}")
if choose==1:
    print(f"{bike1}will cost you{bike1_price}")
elif choose==2:
     print(f"{bike2}will cost you{bike2_price}")
else:
    print("press only 1or 2:")