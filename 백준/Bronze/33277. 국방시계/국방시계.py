n, m = map(int, input().split())

m = 24*60*m//n
hh = m//60
mm = m%60
print(f'{hh if hh>=10 else "0"+str(hh)}:{mm if mm>=10 else "0"+str(mm)}')