#Jacobi & Gauss-Seidel
def Jacobi(variabel, var_awal, nilai_persamaan, iterasin):
    for baris in range(len(variabel)):
        d = nilai_persamaan[baris]
        for kolom in range(len(variabel[baris])):
            if baris != kolom:
                d -= variabel[baris][kolom] * var_awal[kolom]
        iterasin[baris] = d / variabel[baris][baris]
    for nilai in range(len(iterasin)):
        var_awal[nilai] = iterasin[nilai]
    return var_awal
def Gauss_Seidel(variabel, var_awal, nilai_persamaan):
    for baris in range(len(variabel)):
        d = nilai_persamaan[baris]
        for kolom in range(len(variabel[baris])):
            if baris != kolom:
                d -= variabel[baris][kolom] * var_awal[kolom]
        var_awal[baris] = d / variabel[baris][baris]
    return var_awal
def cek_syarat_koef_cukup(my_list):
    konvergen = []
    for baris in range(len(my_list)):
        for kolom in range(len(my_list[baris])):
            dom = sorted(my_list[baris])
            if baris == kolom and dom[-1] == my_list[baris][kolom]:
                konvergen.append(1)
            elif baris == kolom and dom[-1] != my_list[baris][kolom]:
                konvergen.append(0)
    return konvergen
def tampil(Tampilan_matriks):
    lebar = 25
    print('| ', end='')
    for i in range(len(Tampilan_matriks)):
        print(f'x{i + 1} = {Tampilan_matriks[i]}', end=', ')
    print('|\n')
    return 0
def inputan():
    nama = input('Contoh : \n |1a + 2b - 3c + 4d = -6 | ----> \'1 2 -3 4 -6\'\n'
                 'Masukkan koefisien persamaan secara berurutan : ')
    j = nama.split()
    output = [int(x) for x in j]
    return output
nakama = 0
while nakama < 1:
    if nakama == 1:
        break
    koef_var = []
    nilai_pers = []
    var_tebak = []
    itera = []
    menu = ['Jacobian', 'Gaus Seidel', 'Ubah persamaan', 'keluar']
    while True:
        brs = input('Masukkan jumlah persamaan (baris) : ')
        klm = input('Masukkan jumlah variabel (hanya jumlah variabel x,a,atau n),\n'
                    'contoh : jika variabel x,y,z maka variabel = 3, jika maksimal variabel x4 maka = 4\n'
                    'Masukkan jumlah variabel : ')
        if brs.isnumeric() and klm.isnumeric():
            break
        print('\nSilakan masukkan kembali, (ket : inputan berupa integer bulat)\n')
    klm = int(klm) + 1
    for baris in range(int(brs)):
        print(f'\ninputan persamaan ke-{baris + 1}\n')
        x = inputan()
        while len(x) != int(klm):
            print('inputan object melebihi baris/kolom, silakan ulangi')
            x = inputan()
        koef_var.append(x)
        nilai_pers.append(x[-1])
        del x[-1]
    for var in range(klm - 1):
        y = input(f'Variabel tebakan ke-x{var + 1} : ')
        while not y.isnumeric():
            y = input(f'Variabel tebakan ke-x{var + 1} : ')
        var_tebak.append(int(y))
        itera.append(int(y))
    print('///'*20)
    if 0 not in cek_syarat_koef_cukup(koef_var):
        print('Persamaan memenuhi syarat cukup dominan diagonal, (Konvergen)')
    elif 0 in cek_syarat_koef_cukup(koef_var):
        print('persamaan tidak memeuhi syarat cukup dominan diagonal, (hasil tidak konvergen)')
    print('///'*15+'\n')
    while nakama < 1:
        for k in range(len(menu)):
            print('|' + str(menu[k]).center(20, ' ') + f'| {k + 1} |')
        pilihan = input('\nMasukkan nomor menu anda : ')
        while not pilihan.isnumeric():
            pilihan = input('Masukkan menu harus sesuai tabel\nMasukkan nomor menu anda : ')
        klm = 1
        iterasi = 0
        if int(pilihan) == 1:
            koef_jacobi = koef_var.copy()
            nilai_jacobi = nilai_pers.copy()
            iterjokobi = itera.copy()
            var_tebak_Jacobi = var_tebak.copy()
            bhnti1 = [sum(var_tebak_Jacobi)]
            while True:
                Hasil_jacobi = Jacobi(koef_jacobi, var_tebak_Jacobi, nilai_jacobi, iterjokobi)
                bhnti1.append(sum(Hasil_jacobi))
                print(Hasil_jacobi)
                if bhnti1[klm] == bhnti1[klm-1]:
                    print(f'\nPerhitungan selesai, jumlah iterasi = {iterasi}')
                    tampil(Hasil_jacobi)
                    break
                klm += 1
                iterasi += 1
        elif int(pilihan) == 2:
            koef_Gseid = koef_var.copy()
            nilai_Gseid = nilai_pers.copy()
            var_tebak_Gseid = var_tebak.copy()
            bhnti2 = [sum(var_tebak_Gseid)]
            while True:
                Hasil_Gseid = Gauss_Seidel(koef_Gseid, var_tebak_Gseid, nilai_Gseid)
                bhnti2.append(sum(Hasil_Gseid))
                print(Hasil_Gseid)
                if bhnti2[klm] == bhnti2[klm-1]:
                    print(f'\nPerhitungan selesai, jumlah iterasi = {iterasi}')
                    tampil(Hasil_Gseid)
                    break
                klm += 1
                iterasi += 1
        elif int(pilihan) == 3:
            print('\nData persamaan akan dihapus\n')
            break
        elif int(pilihan) == 4:
            nakama += 1
            break