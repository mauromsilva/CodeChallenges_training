# Enter your code here. Read input from STDIN. Print output to STDOUT
import datetime 
mes, dia, ano = map(int, input().split())
fdate = datetime.date(ano, mes, dia)
print(fdate.strftime('%A').upper())
