from curses.ascii import SI
import socket
import os

IP = socket.gethostbyname(socket.gethostname())
PORT = 5555
ADDR = (IP, PORT)
FORMAT = "utf-8"
SIZE = 1024
# key = 'aáàạảãăắằặẳẵâấầậẩẫbcdđeéẹẻẽêếềệểễfghiíìịỉĩjklmnoóòọỏõôốồộổỗơớờợởỡpqrstuúùụủũưứừựửữvwxyýỳỵỷỹAÁÀẠẢÃĂẮẰẶẲẴÂẤẦẬẨẪBCDĐEÉẸẺẼÊẾỀỆỂỄFGHIÍÌỊỈĨJKLMNOÓÒỌỎÕÔỐỒỘỔỖƠỚỜỢỞỠPQRSTUÚÙỤỦŨƯỨỪỰỬỮVWXYÝỲỴỶỸ0123456789`[emailprotected]#$%^&*()'

key = 'abcdefghiklmnopqrstuvwxyz'


def encrypt(k, plaintext):
    result = ''

    for l in plaintext:
        try:
            i = (key.index(l) + k) % len(key)
            result += key[i]
        except ValueError:
            result += l
    return result


def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDR)
    message = input("Nhập vào tin nhắn: ")
    # k = int(input("Nhập vào k: "))
    k = 5

    mess_encry = encrypt(k, message)

    client.sendall(bytes(mess_encry, FORMAT))


if __name__ == "__main__":
    main()
