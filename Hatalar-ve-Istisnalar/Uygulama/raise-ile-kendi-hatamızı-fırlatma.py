def tersCevir(s):
    if(type(s) != str):
        raise ValueError("Lütfen sayısal değer girmeyiniz..") #Hatamızı türkçeleştirdik.
    else:
        return s[::-1]
print(tersCevir(12))
"""
//Try Except ile
try:
    print(tersCevir(12))
except ValueError:
    print("Value hatası")
"""
