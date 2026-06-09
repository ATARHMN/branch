while True:
   a,b,c=map(int,input("ENTER THREE NO:").split())
   if a>b and a>c:
      print("max:",a)
   elif b>c and b>a:
      print("max:",b)
   else:
      print("max:",c)
   z=input("Do You Want To Continue?:")
   if z!="yes":
      break
    
      

