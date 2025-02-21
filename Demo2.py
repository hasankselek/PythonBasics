values = [1, 2, "hasan", 4, 5]
# Listeler birden fazla data tipi bulundurmasına izin verir

print(values[0]) #1
print(values[1]) #2
print(values[2]) #'hasan'
print(values[3]) #4
print(values[1:3]) #2 'hasan'

values.insert(3,"Kücükselek") #istenen indexe istenen veriyi ekler
print(values)

values.append("End") #Listenin sonuna ekler
print(values)

