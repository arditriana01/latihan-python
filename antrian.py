class Queue:
    def __init__(self):
        self.items = []
    
    # mengecek apakah nilai queue kosong
    def isEmpty(self):
        return self.items == []

    # menambah data baru ke dalam queue
    def enQueue(self, item):
        self.items.insert(0, item)

    # mengeluarkan data yang pertama masuk
    def deQueue(self):
        return self.items.pop()

    # mengecek jumlah data yang ada di dalam queue
    def size(self):
        return len(self.items)

    # mengambil data yang ada di dalam queue
    def data(self):
        return self.items

    def mainMenu(self): 
        ulang = "y"       
        while(ulang == "y"):
            print("1. Cek Empty")
            print("2. Ambil Data")
            print("3. Tambah Data")
            print("4. Jumlah Data")   
            print("5. Hapus Data")     

            pilih = int(input("Masukan pilihan anda : "))
            if(pilih == 1):
                if(self.isEmpty()):
                    print("Data kosong\n")
                else:
                    print("Terdapat data\n")

            elif(pilih == 2):            
                print(self.data(), "\n")

            elif(pilih == 3):
                enqueue = str(input("Masukan data baru : "))
                self.enQueue(enqueue)
                print("")

            elif(pilih == 4):
                print("Data berjumlah", self.size(), "\n")

            elif(pilih == 5):
                if(self.size() <= 0 ):
                    print("Tidak ada data yang dikeluarkan\n")
                else:
                    print("Data yang dikeluarkan adalah ", self.deQueue(), "\n")

            else:
                print("Tidak ada pilihan\n")


# membuat objek baru
q = Queue()

# mengambil fungsi mainMenu
q.mainMenu()