# x^n+y^n=z^n
n=1 # intialising the n value as 1
while ((n <= 2) or (n >= 12)):
    n= int(input("Please Enter n such that  2 < n < 12 -->\t")) # placing the n value in between 2 and 12
k=1 # intialising the k value as 1
while k <= 10: # iterating the loop while k is less than 10
    k= int(input("Please Enter k such that k > 10 -->\t")) # placing the k value less than 10
past_miss=None # intialising the past miss is equal to None
for x in range(10, k+1): # the x value is in the range of 10 to k+1
    for y in range(x,k+1): # the y value is in the range of x value  to  k+1
        ans=pow(x,n)+pow(y,n) # the value of x^n+y^n stored in the ans
        z=pow(ans,1/n)
        z1=pow(ans,1/n)
        z_pow=pow(int(z),n)
        z1_pow=pow(int(z1+1),n)
        if z_pow < ans and ans <  z1_pow: # if ans is in between z_pow and z1_pow
            miss=min((ans-z_pow),(z_pow-ans))
            r_miss=miss/ans
            print(f"x is {x} y is {y} z is {z}  and relative miss is {r_miss}") # then print the value of x ,y , and relative missof 3 possible iterations)//jaya phanimdra nersu
