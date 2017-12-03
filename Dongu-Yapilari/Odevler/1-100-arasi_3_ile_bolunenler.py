print("""
*****************************
1 ile 100 arası 3 ile bölünenler
*****************************
""")
for i in range(1,101):
    if(i%3!=0):
        continue
    print(i)
