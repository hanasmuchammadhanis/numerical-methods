#GoldenSection
import matplotlib.pyplot as grafik
k = '(ketik error untuk keluar) ' \
    '\nMasukkan judul/nama file, lengkap dengan titik tipe file\ncontoh, data_listrik.csv ' \
    '(keterangan, letakkan dokumen di file project program anda)\nmasukkan nama file : '
menu = [['Profil', '1'], ['Masukkan/ganti data', '2'], ['Regresi', '3'], ['optimasi', '4'], ['tampil grafik', '5'],
        ['keluar', '6']]
info = [['Metode', 'Cara Mengisi'],
        ['Mengimport File', 'Tuliskan nama file beserta tipenya, contoh --> data_listrik.csv | (Case sensitive) '
                            '| letakkan dulu file yang akan di import berada di file yang sama dengan projrct program'],
        ['Menentukan Tipe Tabel', 'Lihat dari isi data berdasrkan parameter'
                                  'jika dibaca dari kiri ke kanan maka tipe --> baris | '
                                  'jika dibaca dari atas ke bawah maka tipe --> kolom'],
        ['Memilih Vriabel', 'Pilih variabel pada tabel yang tertampil sesaui dengan cara mmebaca tabel']]
Bulan = ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'November',
         'Desember']        
batas = '---' * 20
nakama = 0
def int_input(prompt):
    while True:
        try:
            age = int(input(prompt))
            return age
        except ValueError as e:
            print("silakan masukkan angka yang benar")
def float_input(prompt):
    while True:
        try:
            angka = float(input(prompt))
            return angka
        except ValueError as e:
            print("silakan masukkan angka yang benar")
def mean(var):
    rata_rata = sum(var) / (len(var))
    return rata_rata
def kuadrat_data(var):
    c = []
    for i in range(len(var)):
        c.append(var[i] ** 2)
    return c
def slope(var1, var2):
    kuadrat_var1 = kuadrat_data(var1)
    var12 = []
    for k in range(len(var1)):
        var12.append(var1[k] * var2[k])
    p = len(var1)
    x_sum = sum(var1)
    x12_sum = sum(var12)
    a = ((p * x12_sum) - (x_sum * sum(var2))) / ((p * sum(kuadrat_var1)) - (x_sum ** 2))
    return a
def intercept(var1, var2, slop):
    rata_var1 = mean(var1)
    rata_var2 = mean(var2)
    inter = rata_var2 - (slop * rata_var1)
    return inter
def importcsv_list(pemisah=';'):
    mk = 0
    while mk < 1:
        try:
            data_file = open(input(k), 'r')
        except FileNotFoundError:
            print('\n'+'/'*50+'\nfile tidak ditemukan/error/keluar, silakan ulangi\n'+'\\'*50+'\n')
            kc = input('enter untuk lanjut : ')
            if kc.upper == 'X':
                mk += 1
                exit()
        else:
            break
    data = []
    for larik in data_file:
        data.append(larik.replace('\n', '').split(pemisah))
    data_file.close()
    return data
def tampil_hasil_regresi(f_x, a_1, a_0, std_eror):
    print(f'Nilai slope                 : {round(a_1, 4)}\n'
          f'Nilai intercept             : {round(a_0, 4)}\n'
          f'Persamaan linear regresi    : y =  {round(a_0, 4)} + ({round(a_1, 4)})x\n'
          f'Standar Error Estimasi      : {round(std_eror, 4)}')
    if len(fx) == 12:
        print('Prakiraan Data Perbulan : ')
        for data in range(len(fx)):
            print(f'{Bulan[data]}'.center(15) + f'| {round(fx[data], 4)}')
def tabel_listcsv(list_csv, Tipe_Tabel, In_klmx, In_klmy):
    if Tipe_Tabel.upper() == 'BARIS':
        tabel_isi = []
        for baris in list_csv:
            isi = []
            for kolom in baris:
                if kolom.isnumeric():
                    isi.append(float(kolom))
            tabel_isi.append(isi)
        return tabel_isi
    elif Tipe_Tabel.upper() == 'KOLOM':
        tabel_isi_x = []
        tabel_isi_y = []
        for baris in range(len(list_csv)):
            for kolom in range(len(list_csv[baris])):
                if list_csv[baris][kolom].isdecimal():
                    if kolom == In_klmx:
                        tabel_isi_x.append(float(list_csv[baris][kolom]))
                    elif kolom == In_klmy:
                        tabel_isi_y.append(float(list_csv[baris][kolom]))
        return tabel_isi_x, tabel_isi_y
def indeksing(data_indeks, xa, xy):
    c = 0
    for lar in data_indeks:
        if xa in lar:
            brsx, klmx = c, lar.index(xa)
        if xy in lar:
            brsy, klmy = c, lar.index(xy)
        c += 1
    return brsx, brsy, klmx, klmy
def tampil_tabel(tabel):
    rs = []
    print('\n')
    for brs in tabel:
        rs.append(max(brs, key=len))
    r = max(rs, key=len)
    for baris in range(len(tabel)):
        for kolom in range(len(tabel[baris])):
            print('| ' + f'{tabel[baris][kolom]}'.center(len(r) + 2), end='')
            if kolom == len(tabel[baris]) - 1:
                print(' |')
            if baris == 0 and kolom == len(tabel[baris]) - 1:
                print('|' + '-' * ((len(r) + 4) * (len(tabel[baris]))) + '|')
def standard_error(yi, a0_a1x):
    std_erro = []
    for i in range(len(yi)):
        std_erro.append((yi[i] - a0_a1x[i]) ** 2)
    hasil_standar_error_estimasi = ((sum(std_erro)) / (len(yi) - 2)) ** 0.5
    return hasil_standar_error_estimasi
def regresi_linear(tabel_x, tabel_y):
    a1 = slope(tabel_x.copy(), tabel_y.copy())
    a0 = intercept(tabel_x.copy(), tabel_y.copy(), a1)
    y = str(f'{a0}+{a1}*x')
    fx = []
    grafik.plot(tabel_x, tabel_y, 'o')
    grafik.ylabel(f'y = {round(a0, 3)} + {round(a1, 3)}x')
    for x in tabel_x:
        fx.append(eval(y))
    grafik.plot(tabel_x, fx)
    std_error = standard_error(tabel_y, fx)
    print(f'Nilai slope                 : {round(a1, 4)}\n'
          f'Nilai intercept             : {round(a0, 4)}\n'
          f'Persamaan linear regresi    : y =  {round(a0, 4)} + ({round(a1, 4)})x\n'
          f'Standar Error Estimasi      : {round(std_error, 4)}\n')
    return fx, a1, a0, y, std_error
def golden_section(fx, x_l, x_u, fx1, fx2, toler, maxit, metodes):
    xl = x_l
    xu = x_u
    d = ((5 ** (1 / 2) - 1) / 2) * (xu - xl)
    x1 = xu - d
    x2 = xl + d
    k = 1
    r = 15
    while True:
        d = ((5 ** (1 / 2) - 1) / 2) * (xu - xl)
        x2 = xl + d
        x1 = xu - d
        hasil_fx1 = eval(fx1)
        hasil_fx2 = eval(fx2)
        print(f'iterasi ke = {k}'.ljust(r) + '|' + f'xl = {round(xl, 4)}'.center(r) + '|' +
              f'xu = {round(xu, 4)}'.center(r) + '|' + f'd = {round(d, 4)}'.center(r) + '|' +
              f'x1 = {round(x1, 4)}'.center(r) + '|' + f'x2 = {round(x2, 4)}'.center(r) + '| ' +
              f'f(x1) = {round(hasil_fx1, 4)}'.center(r) + ' | '+f'f(x2) = {round(hasil_fx2, 4)}'.center(r) + ' |')
        if d <= toler or k >= maxit:
            print('\n'+'=='*50)
            print(f'nilai golden section, x1 = {x1}, x2 = {x2} | {metodes}')
            break
        if metodes.upper() == 'MINIMUM':
            if hasil_fx1 < hasil_fx2:
                xu = x2
            elif hasil_fx1 > hasil_fx2:
                xl = x1
        elif metodes.upper() == 'MAKSIMUM':
            if hasil_fx1 < hasil_fx2:
                xl = x1
            elif hasil_fx1 > hasil_fx2:
                xu = x2
        k += 1
def inputan_gs(fx, a, b, c, d, j):
    cek = ['X', 'Y', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
           'U', 'V', 'W', 'Z']
    var = ''
    for k in fx:
        for i in cek:
            if k.upper() == i:
                var = k
    f_x = fx.replace(var, 'x')
    f_x1 = f_x.replace('x', 'x1')
    f_x2 = f_x.replace('x', 'x2')
    golden_section(f_x, float(a), float(b), f_x1, f_x2, float(c), int(d), j)
while nakama == 0:
    print('\n')
    jenis = ''
    tipe = ''
    n = []
    x1 = ''
    y1 = ''
    n = importcsv_list()
    while True:
        cek_x1 = False
        cek_y1 = False
        prmt1 = 0
        parmt = 0
        tampil_tabel(n)
        tampil_tabel(menu)
        pilihan = input('\nMasukkan pilihan menu (integer) : ')
        while pilihan not in ['1', '2', '3', '4', '5', '6']:
            pilihan = input('\nInput menu gagal,\nMasukkan pilihan menu (integer) : ')
        if int(pilihan) == 1:
            for i in range(len(info)):
                print(f'{info[i][0]}'.ljust(25) + f'| {info[i][1]}')
        elif int(pilihan) == 2:
            break
        elif int(pilihan) == 3:
            while prmt1 == 0:
                print(batas)
                tipe = input('tipe cara pembacaan nilai parameter (x,y) tabel'
                             '\ncara membaca dari kiri ke kanan --> baris'
                             '\ncara membaca dari atas ke bawah --> kolom\nmasukkan tipe tabel : ')
                if tipe.upper() == 'BARIS' or tipe.upper() == 'KOLOM':
                    prmt1 += 1
                else:
                    print('\n========Inputan tidak sesuai, silakan ulangi==========\n')
            while parmt == 0:
                print(batas)
                x1 = input('masukkan nama parameter (sesuai tabel yang ditampilkan, note : case sensistive)\n'
                           'nama data yang akan dihitung sebagai x : ')
                y1 = input('masukkan nama parameter (sesuai tabel yang ditampilkan, note : case sensistive)\n'
                           'nama data yang akan dihitung sebagai y : ')
                for isi in n:
                    if x1 in isi:
                        cek_x1 = True
                    if y1 in isi:
                        cek_y1 = True
                if cek_x1 == True and cek_y1 == True:
                    parmt += 1
                else:
                    print('\n========Inputan tidak sesuai, silakan ulangi==========\n')
            if tipe.upper() == 'BARIS':
                print(batas)
                barisx, barisy, kolomx, kolomy = indeksing(n, x1, y1)
                isi_tabel = tabel_listcsv(n.copy(), tipe, kolomx, kolomy)
                fx, a1, a0, y, std_error = regresi_linear(isi_tabel[barisx], isi_tabel[barisy])
            elif tipe.upper() == 'KOLOM':
                print(batas)
                barisx, barisy, kolomx, kolomy = indeksing(n, x1, y1)
                isi_tabelx, isi_tabely = tabel_listcsv(n.copy(), tipe, kolomx, kolomy)
                fx, a1, a0, y, std_error = regresi_linear(isi_tabelx, isi_tabely)
        elif int(pilihan) == 4:
            xxl = float_input('masukkan tebakan xl : ')
            xxu = float_input('masukkan tebakan xu : ')
            tolx = float_input('masukkan nilai toleransi  : ')
            maxiter = int_input('masukkan jumlah iterasi : ')
            maks_min = input('masukkan jenis (maksimum / minimum) : ')
            print(f'nilai slope : {a1}')
            inputan_gs(y, xxl, xxu, tolx, maxiter, maks_min)
        elif int(pilihan) == 5:
            grafik.show()
        elif int(pilihan) == 6:
            nakama += 1
            break