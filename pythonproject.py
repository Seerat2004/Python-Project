#Input no. of ways in a cake should be cut.
N=int(input("Number of ways in a cake should be cut in: "))
for i in range (N):
    #Input the angle in which the cake should be cut.
    A=int(input("Angle in which the cake should be cut in: "))
    if A > 360:
        print('n n n')
    else:
        s=[]
        #CASE1-Give "True" value if cake can be cut into N equal pieces.
        s.append("True" if 360 % N == 0 else "False")
        #CASE2-Give "True" if cake can be cut into N pieces of any size.
        s.append("True")
        #CASE3-Give "True" if cake can be cut into N pieces such that no two of them are equal.
        s.append("False" if (N*(N+1))//2 <= 360 else "True")
        print(s)
    break    

                
