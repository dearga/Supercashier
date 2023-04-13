
import pandas as pd

class transaction():    
    def __init__(self):
        self.keranjang=dict()  
    def add_item(self,barang,price,qty):
        """Fungsi untuk menambahkan item belanjaan
           #
           Masukkan data berupa
           barang: nama barang (str)
           price : harga (int)
           qty   : jumlah (int)
           contoh belanja1.add_item("telur",13000,1)"""
        try: 
            if type(barang)==str and type(price)==int and type(qty)==int:
                self.keranjang.update({barang.lower():[price,qty]})
                self.show_order()
                print (f" \nDitambahkan {barang} sejumlah {qty} dengan harga satuan Rp {price}")
        except TypeError:
            print ("Input salah, format: barang (string), harga (int), qty (int)")
    def update_item_name(self,nama_barang,nama_baru):
        """Fungsi untuk merubah nama barang
           #
           Masukkan data berupa
           nama_barang : nama barang lama yang sudah dimasukkan sebelumnya (str)
           nama_baru   : nama barang baru yang menggantikan nama lama (int)
           contoh belanja1.update_item_name("telur","telur_bebek")"""
        try:
            if type(nama_barang)==str and type(nama_baru)==str:
                temp=self.keranjang[nama_barang.lower()]
                self.keranjang.pop(nama_barang.lower())
                self.keranjang.update({nama_baru.lower():temp})
                self.show_order()
                print (f" \nNama barang {nama_barang} diupdate menjadi {nama_baru}")
        except:
            print ("Input salah, format : nama item lama (string), nama item baru (string)")
    def update_item_price(self,nama_barang,price_baru):
        """Fungsi untuk merubah harga barang
           #
           Masukkan data berupa
           nama_barang : nama barang yang sudah dimasukkan sebelumnya (str)
           price_baru  : harga barang baru yang menggantikan harga lama (int)
           contoh belanja1.update_item_price("telur_bebek",20000,1)"""
        try:
            if type(nama_barang)==str and type(price_baru)==int:
                temp_price= self.keranjang[nama_barang.lower()][0]
                self.keranjang[nama_barang.lower()][0]=price_baru
                self.show_order()
                print(f' \nHarga {nama_barang} diperbaharui dari Rp {temp_price} menjadi Rp {price_baru}')
            
        except:
            print("Input salah, format : nama item (string), harga baru (int)")
    def update_item_qty(self,nama_barang,qty_baru):
        """Fungsi untuk merubah jumlah barang
           #
           Masukkan data berupa
           nama_barang : nama barang yang sudah dimasukkan sebelumnya (str)
           qty_baru    : jumlah barang baru yang menggantikan jumlah lama (int)
           contoh belanja1.update_item_qty("telur bebek",2)"""
        try:
            if type(nama_barang)==str and type(qty_baru)==int:
                temp_qty=self.keranjang[nama_barang.lower()][1]
                self.keranjang[nama_barang.lower()][1]=qty_baru
                self.show_order()
                print(f' \nJumlah {nama_barang} diperbaharui dari {temp_qty} menjadi {qty_baru}')
            
        except:
            print("Input salah, format : nama item (string), quantity baru (int)")
    def delete_item(self,nama_barang):
        """Fungsi untuk menghapus barang
           #
           Masukkan data berupa
           nama_barang : nama barang yang sudah dimasukkan sebelumnya dan akan  (str)
           Pada confirmation input isikan Y untuk menghapus item yang dipilih atau N untuk membatalkan fungsi
           contoh belanja1.delete_item("telur_bebek")"""
        try:
            del_confirm=input("Hapus Item? Y/N?:").lower()
            if del_confirm=="n":
                print("Batal hapus item")
            elif del_confirm=="y" and type(nama_barang)==str :
                self.keranjang.pop(nama_barang.lower())
                self.show_order()
                print (f" \nBarang {nama_barang} berhasil dihapus")
            
        except:
            print("Input salah, format: nama item (string)")
    def reset_transaction(self):
        """Fungsi untuk mereset / hapus seluruh data belanjaan
           #
           Tidak perlu memasukkan data
           Pada confirmation input isikan Y untuk menghapus seluruh input atau N untuk membatalkan fungsi
           contoh belanja1.reset_transaction()"""
        reset_confirm=input("Hapus seluruh item? Y/N?: ").lower()
        if reset_confirm=="n":
            print("Batal hapus item")
        else:
            self.keranjang.clear()
            print("Barang berhasil dihapus")
    def check_order(self):
        """Fungsi untuk cek error pada daftar belanjaan
           #
           Tidak perlu memasukkan data
           contoh belanja1.check_order()"""
        n=0        
        for i in self.keranjang.keys():
            if type (i) != str:
                print(f"Nama barang {i} salah")
            elif type(self.keranjang[i][0])!=int:
                print(f"Harga barang {i} salah")
            elif type(self.keranjang[i][1])!=int:
                print(f"Jumlah barang {i} salah")
            else:
                n+=1
        if n == len(self.keranjang):
            self.show_order()
            print (" \nDaftar belanjaan sudah benar.")
        else:
            pass
    def show_order(self):
        """Fungsi untuk menampilkan tabel daftar belanjaan
           #
           Tidak perlu memasukkan data
           contoh belanja1.show_order()"""
        item=self.keranjang.keys()
        harga=list()
        jumlah=list()
        sub_total=list()
        data_belanja=dict()
        for i in item:
            harga.append(self.keranjang[i][0])
            jumlah.append(self.keranjang[i][1])
            sub_total.append(self.keranjang[i][0] * self.keranjang[i][1])
        data_belanja.update(barang=item,price=harga,qty=jumlah,total=sub_total)
        print(pd.DataFrame(data=data_belanja))
                
    def total_price(self):
        """Fungsi untuk cek total harga belanjaan
           #
           Tidak perlu memasukkan data
           contoh belanja1.total_price()"""
        sub_price = list()
        for i in self.keranjang.keys():
            sub_price += [self.keranjang[i][0]*self.keranjang[i][1]]
        total_price = sum(sub_price)
        if total_price > 500_000:
            diskon= int(total_price *0.1)
        elif total_price >300_000:
            diskon=int(total_price*0.08)
        elif total_price >200_000:
            diskon=int(total_price*0.05)
        else:
            diskon=0
        final=total_price - diskon
        self.show_order()
        print(f" \nTotal harga adalah Rp{total_price}, diskon sebesar Rp{diskon} dan total harga akhir sebesar Rp{final}")
