def antrian(list_antrian):
    print("Kasir 1:")
    for i in range(0, 5, 1):
        print(list_antrian[i])

    print("")
    print("")
    
    print("Kasir 2:")
    for i in range(5, 10, 1):
        print(list_antrian[i])

    print("")
    print("")

    print("Kasir 3:")
    for i in range(10, 15, 1):
        print(list_antrian[i])

    print("")
    print("")
    print("Kasir cuma 3. Silahkan lihat produk lain dulu supaya antrian ga full")



list_antrian = ["Shalom","Sindu","Hanif","Dedi","Silvi","Ghea","Richard","Tiur",
"Valdo","Risa","Alex","Chris","Edwin","Iko","Noel","Ela","Rachel"]
antrian(list_antrian)
