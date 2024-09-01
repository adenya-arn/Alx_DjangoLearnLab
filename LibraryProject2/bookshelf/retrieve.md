
#We retrieve what we want and print it

retrieved = Book.objects.get(id = 1)
print(retrieved)


#Expected output

#1984 George Orwell 1949

