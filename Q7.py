s:str="   Python is fun!    "
stripped=s.strip(" ")
print(stripped)
l_just=stripped.ljust(16,'*')
print(l_just)
r_just=stripped.rjust(20,'*')
print(r_just)