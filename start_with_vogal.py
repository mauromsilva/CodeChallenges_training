# PRINT ONLY NAME STARTING WITH VOGAL
import re 

vlist = ['amanda', 'mor', 'mozinho', 'feiosa', 'lindinha', 'linda', 'fidida']

# USING FOR 
names_vow = [ name for name in vlist if name[0] in 'aeiouAEIOU']
print(names_vow)

# USING REGULAR EXPRESSION
names_vow = [ name for name in vlist if re.match('^[aeiouAEIOU]\w+',name)]
print(names_vow)