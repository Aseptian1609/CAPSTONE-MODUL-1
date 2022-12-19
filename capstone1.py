# PROJECT CAPSTONE MODUL 1 
# NAMA ADHITIA SEPTIAN
# PROGRAM DATA NILAI SISWA -AKADEMIK SKOR

listsiswa = [
    {
        'NIS' : '1001',
        'Nama' : 'Asep',
        'Kelas' : 'IPS',
        'Mata Pelajaran' : 'Sosiologi',
        'Nilai' : 90
    },

    {
        'NIS' : '1002',
        'Nama' : 'Dedi',
        'Kelas' : 'IPA',
        'Mata Pelajaran' : 'Biologi',
        'Nilai' : 80
    },
    {
        'NIS' : '1003',
        'Nama' : 'Rita',
        'Kelas' : 'IPA',
        'Mata Pelajaran' : 'Fisika',
        'Nilai' : 70
    },

    {
        'NIS' : '1004',
        'Nama' : 'Beni',
        'Kelas' : 'IPS',
        'Mata Pelajaran' : 'Geografi',
        'Nilai' : 80
    },

    {
        'NIS' : '1005',
        'Nama' : 'Jeni',
        'Kelas' : 'IPA',
        'Mata Pelajaran' : 'Fisika',
        'Nilai' : 95  
    }
]

# MENAMPILKAN NILAI DATA SISWA DAN MENAMPILKAN DATA NILAI SISWA YANG DIPILIH SESUAI NAMA SISWA
def datasiswa():
    while True:
        menutampil = input('''
    =============================================
        DATA NILAI SISWA SEKOLAH SMA N DHIKA 1 
    =============================================
    1. Tampilkan seluruh nilai siswa
    2. Tampilkan nilai siswa yang ingin di pilih
    3. Kembali ke menu utama
    Pilih Menu [1-3] : ''')
        if menutampil=='1': # MENU TAMPILAN APABILA MEMILIH NOMOR 1
            print('''
========================================
DATA NILAI SISWA SEKOLAH SMA N DHIKA 1  
========================================
| NIS | Nama |Kelas|  Pelajaran  |Nilai|      ''')
            for i in range(len(listsiswa)): # FUNGSI MENAMPILKAN LIST DICTIONARY YANG ADA DI LIST SISWA
                print('| {} | {} | {} | {}\t | {}  |'.format(listsiswa[i]['NIS'],listsiswa[i]['Nama'],listsiswa[i]['Kelas'],listsiswa[i]['Mata Pelajaran'],listsiswa[i]['Nilai']))
        elif menutampil=='2': # MENU TAMPILAN APABILA MEMILIH NOMOR 2
            inputtampilsiswa = input('''
Masukan nama siswa yang ingin dilihat : ''').capitalize() # INPUTAN NAMA SISWA YANG INGIN DILIHAT 
            count = 0 # BUAT VARIABLE 
            for i in range(len(listsiswa)): # INDEX YANG BERADA DI DALAM LIST SISWA 
                if inputtampilsiswa in listsiswa[i]['Nama']: # APABILA INPUTAN SESUAI DENGAN NAMA SISWA YANG ADA DI LIST SISWA
                    print('''
 ======================================                   
 DATA NILAI SISWA SEKOLAH SMA N DHIKA 1
 ====================================== 
| NIS | Nama |Kelas|  Pelajaran  |Nilai|      
| {} | {} | {} | {}\t | {}  |'''.format(listsiswa[i]['NIS'],listsiswa[i]['Nama'],listsiswa[i]['Kelas'],listsiswa[i]['Mata Pelajaran'],listsiswa[i]['Nilai'])) #TAMPILAN LIST DICTIONARY YANG DITAMPILKAN SESUAI INPUTAN
                    count += 1
                else:
                    count += 0 # APABILA INDEX YANG DI MASUKAN SAMA DENGAN 0
            if count == 0:
                print("\n\t================= DATA TIDAK DITEMUKAN =================")  
                
                
            # if inputtampilsiswa in range(len(listsiswa[''])):
            #     listsiswa[inputtampilsiswa]['Nama'] == inputtampilsiswa.capitalize()
            #     print(listsiswa[inputtampilsiswa]['Nama'],listsiswa['Nilai'])
            # else:
            #     print("================= DATA TIDAK DITEMUKAN =================")           
        elif menutampil=='3':
            menuawal()
            break
#menambahkan data
def inputtambah():
    while True:
        menutambah = int(input('''
    ====================================
        FORM INPUT TAMBAH DATA SISWA 
                SMA N DHIKA 1
    ====================================
    1. Tambah Data Nilai Siswa
    2. Kembali ke menu utama
    Masukkan menu yang ingin di jalankan [1 atau 2] : '''
    ))
        if (menutambah==1):
            inputnama = input('Masukkan Nama Siswa : ').capitalize()
            for key in listsiswa:
                if key['Nama'] == inputnama:
                    print('''
                ===========================
                    DATA SISWA SUDAH ADA
                ===========================''')
                    break
                else:
                    inputnis = input('Masukkan NIS : ')
                    inputkelas = input('Masukkan Kelas : ')
                    inputmatapelajaran = input('Masukkan Mata Pelajaran : ')
                    inputnilai = input('Masukkan nilai : ')
                    a = input('Apakah data yang anda masukan telah benar (Y/T) :')
                    if (a == 'Y' or a == 'y'):
                        listsiswa.append({
                            'NIS' : int(inputnis),
                            'Nama' : inputnama,
                            'Kelas' : inputkelas,
                            'Mata Pelajaran' : inputmatapelajaran,
                            'Nilai' : int(inputnilai)
                        })
                        print('''
                        ================================
                            DATA BERHASIL DI SIMPAN
                        ================================''')
                        break
                    elif (a == 'T' or a == 't'):
                        break
        elif menutambah == 2:
            menuawal()
            break
# mengupdate siswa
def updatesiswa():
    while True:
        menuupdate = int(input('''
        ===============================
            UPDATE DATA NILAI SISWA
                SMA N DHIKA 1
        ===============================
        1. Update Data Nilai Siswa
        2. Kembali ke menu utama
        Masukkan menu yang ingin di jalankan [1 atau 2] : '''
        ))
        if (menuupdate==1):
            Namaupdate = input('Masukkan Nama siswa yang ingin di Update : ').capitalize()
            # datasiswa = False
            x = []
            for i in listsiswa:
                x.append(i['Nama'])
                # if i['Nama'] == Namaupdate.capitalize() :
            if Namaupdate in x:
                while True:
                    gantinilai = input('Masukkan Nilai yang baru : ')
                    if gantinilai.isdigit():
                        yakinupdate = input('Apakah data yang anda masukan telah benar (Y/T) :')
                    # while True:
                        if (yakinupdate == 'Y' or yakinupdate=='y'):
                            for key in listsiswa:
                                if key['Nama'] == Namaupdate.capitalize():
                                    key.update({'Nilai': gantinilai})
                                    print('''
                                    =============================
                                        DATA TELAH TERUPDATE 
                                    =============================''')
                        elif (yakinupdate == 'T' or yakinupdate=='t'):
                            menuawal()
                            break
                        break
                    else:
                        print('Masukkan nilai berupa angka')
            else :
                print ('''
                =============================
                    SISWA TIDAK DI TEMUKAN 
                =============================''')
        else:
            menuawal()
            break
#menghapus data siswa
def hapussiswa():
    while True:
        print('''
=============================
    FORM HAPUS DATA SISWA
        SMA N DHIKA 1 
=============================''')
        inputhapussiswa = input('''
1. Hapus Data Siswa sesuai nama siswa 
2. Kembali ke menu utama 
Silahkan pilih menu [1 atau 2] : ''')
        if inputhapussiswa=='1':
            siswahapus = input('Masukan Nama Siswa yang ingin dihapus : ').capitalize()
            count = 0
            for hs in range(len(listsiswa)):
                if siswahapus == listsiswa[hs]['Nama']:
                    yakinhapus = input('Apakah anda yakin ingin menghapus data siswa [Y/T] : ')
                    count += 1
                    if (yakinhapus == 'Y' or yakinhapus =='y'):
                        listsiswa.pop(hs)
                        print('''
                        =================================
                            DATA SISWA TELAH TERHAPUS 
                        =================================''')
                        break
                    elif(yakinhapus=='t' or yakinhapus=='T'):
                        hapussiswa()
                        break
                    else:
                        print('''
                        ==========================
                        MASUKAN PILIHAN YANG BENAR 
                        ==========================''')
                else:
                    count +=0
            if count == 0:
                print('''1
                ========================== 
                DATA SISWA TIDAK DITEMUKAN 
                ==========================''')
        elif inputhapussiswa == '2':
            menuawal()
            break
        else:
            print('''
            ===================================
                MASUKAN PILIHAN YANG BENAR 
            ===================================''')
#menu awal
def menuawal(): 
    while True:
        print('''
        ===========================================================
                        DATA NILAI SISWA SEKOLAH
                            SMA NEGERI DHIKA 1
        ===========================================================
            Data Siswa :
            1. Tampilkan Data Nilai Siswa
            2. Input Data Nilai Siswa
            3. Update Data Nilai Siswa
            4. Hapus Data Siswa
            5. Exit
            ''')
        pilih = int(input('\tMasukkan pilihan anda (1-5) : '))
        if pilih == 1:
            datasiswa()
            break
        elif pilih == 2:
            inputtambah()
            break
        elif pilih == 3:
            updatesiswa()
            break
        elif pilih == 4:
            hapussiswa()
            break
        elif pilih == 5:
            print('''
            ============================
                    TERIMA KASIH
            ===========================''')
            break
        else:
            print('''
            =======================================
                PILIHAN YANG ANDA MASUKAN SALAH 
            =======================================''')
menuawal()