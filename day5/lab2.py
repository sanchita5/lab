#convert temperatures to and from celsius, fahrenheit.C = (5/9) * (F -32)
temp=int(input("Enter the number "))
c=(5/9) * (temp -32)
f=(9/5)*(temp+32)
print(f"{temp} celsius= {f} fahrenheit")
print(f"{temp} fahrenheit= {c} celsius")