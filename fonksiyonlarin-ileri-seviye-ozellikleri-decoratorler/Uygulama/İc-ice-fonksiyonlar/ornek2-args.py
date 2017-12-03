def fonksiyon(*args):

    def toplama(args):
        toplam =0
        for i in args:
            toplam+=i
        return toplam
    print(toplama(args))

fonksiyon(1,2,3,4,5,6,7)
