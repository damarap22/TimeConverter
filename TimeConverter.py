def timeConverter(seconds):                                 # membuat function bernama timeConverter dengan 1 argument yaitu seconds
    if type(seconds) == int and 0 <= seconds <= 359999:     # membuat kondisi ketika inputan 'seconds' memiliki nilai 0<= x <= 359999 dan bertipe int maka akan dilakukan proses selanjutnya
        jam = seconds//3600                                 # mengkonversi detik menjadi jam, contoh : 7201 detik = 2 + 1/3600, (//) merupakan floor division sehingga hasil pembagian dibulatkan kebawah
        menit = (seconds%3600)//60                          # (%) akan mengembalikan hasil sisa dari pembagian, yaitu pembagian detik dengan jam (3600 detik), lalu akan dibagi dengan menit (60 detik) dan hasilnya dibulatkan kebawah
        detik = seconds%60                                  # mengembalikan hasil sisa pembagian antara detik dengan menit, contoh 61%60 = 1 detik, karena 61 detik = 1 menit 1 detik 
        if jam < 10:
            h = '0'+str(jam)                                # menambahkan str 0 didepan jam ketika nilai jam < 10, jam akan dirubah dari type int menjadi str
        else:
            h = str(jam)                                    
        if menit < 10:
            m = '0'+str(menit)                              # menambahkan str 0 didepan menit ketika nilai menit < 10, menit akan dirubah dari type int menjadi str
        else:
            m = str(menit)
        if detik < 10:
            s = '0'+str(detik)                              # menambahkan str 0 didepan detik ketika nilai detik < 10, detik akan dirubah dari type int menjadi str
        else:
            s = str(detik)
        return f'{h}:{m}:{s}'                               # melakukan formating untuk menghasilkan output dengan format h:m:s
    else:
        return 'Invalid Input!'                             # jika nilai 'seconds' tidak sesuai dengan ketentuan maka function akan menghasilkan keterangan 'Invalid Input!'

print(timeConverter(360000))
print(timeConverter(7153))