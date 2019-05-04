# stringler "" ve ya '' tırnak işaretleriyle tanımlanır
print("Tayfun Yakut")

print('507')
# başlangıç ve bitiş tırnakları aynı tip olmalıdır yoksa Syntax hatası verir

# 'Tayfun'un Evi' diye yazarsak yine hata verir. Onun yerine:
print('Tayfun\'un Evi') # \ işareti ile yazarsak sorun olmaz

# değişkene bir strimg atayıp daha sonra matematiksel işlemler yapılabilir

x="Tayfun"
y="Yakut"
z="Python3"
print(x+y+z)

print(z * 4)

# print("Tayfun" + 507) yazarsak hem sayı hemde yazı olduğu için hata alırız

print("Tayfun" + str(507))
# print('8,5' * 5) 8,5 ondalıklı bir sayı olduğu için float ile belirtmek gerekir
print(float(8.5) * 5)

print(x[5])

print(x[-5])

print(x[:6])

print(len(x)) # len komutu değişkenin içinde ki elemanların toplamını gösterir
