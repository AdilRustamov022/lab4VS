def bolunmeyen_ededler_ve_hasil(massiv):
    bolunmeyen_ededler = []
    hasil = 1
    for eded in massiv:
        if eded % 5 != 0:
            bolunmeyen_ededler.append(eded)
            hasil *= eded
    
    # Fayla yazmaq
    with open("bolunmeyen_ededler.txt", "w") as f:
        for eded in bolunmeyen_ededler:
            f.write(str(eded) + "\n")
    
    return bolunmeyen_ededler, hasil

# Massiv
massiv = [12, 15, 20, 25, 30, 35, 40, 45, 50]

bolunmeyenler, hasil = bolunmeyen_ededler_ve_hasil(massiv)
print("Bölünməyən ədədlər:", bolunmeyenler)
print("Bölünməyən ədədlərin hasil:", hasil)
