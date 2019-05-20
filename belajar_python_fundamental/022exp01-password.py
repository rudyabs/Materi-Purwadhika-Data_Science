password = '12345'
input_user = ""
melebihi = False
input_ke = 0
batas_max = 2

while input_user != password and not melebihi: 
    if input_ke <= batas_max:
        input_user = input('Ketik password: ')
        if input_user != password and input_ke < batas_max:
            input_ke += 1
            print("Input ke-", input_ke, "Maaf password salah!")
        elif input_user != password and input_ke == batas_max:
            input_ke += 1
            print("Password salah! Kesempatan anda habis!")
            break
        elif input_ke == 3:
            print('Batas maksimal memasukan password sudah mencapai 3 kali')
            break
        else:
            print("Login sukses!")

