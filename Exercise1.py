#Masukkan definisi
def bonus(GPA):
    Bonus = 500000
    insentif = GPA*Bonus
    return insentif

listGPA = [3, 2.7, 2.5,  4]

#Masukkan pengulangan
for GPA in listGPA:
    if GPA > 3:
        print("Anda mendapatkan insentif: Rp",bonus(GPA))
    else:
        print("Mohon Maaf Anda Tidak Mendapatkan Bonus")