x = int(input("enter a number:"))
def iden(x):
     if  x % 2 == 0:
        print("even")
     else: 
         print("odd")

num_iterations = 50
for _ in range(num_iterations):
   try:
      x = int(input())
      iden(x)
   except ValueError:
      print("invalid input. please print valid number.")

        



