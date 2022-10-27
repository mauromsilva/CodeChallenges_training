def check_float(x):
  if isinstance(x,float):
    return True
  else:
    return False
  


vlist = [0.2, 3.0, 4.3, 3.2]

# STANDARD PYTHON
print(all(float(i) for i in vlist))

# CUSTOMIZED FUNCTION USING FOR
print(all(check_float(i) for i in vlist))

# CUSTOMIZED FUNCTION USING MAP FUNCTION
print(all(list(map(check_float,vlist))))

