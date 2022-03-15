import socket
import threading

from client import FORMAT

IP = socket.gethostbyname(socket.gethostname())
PORT = 5555
ADDR = (IP, PORT)
SIZE = 1024
key = 'aáàạảãăắằặẳẵâấầậẩẫbcdđeéẹẻẽêếềệểễfghiíìịỉĩjklmnoóòọỏõôốồộổỗơớờợởỡpqrstuúùụủũưứừựửữvwxyýỳỵỷỹAÁÀẠẢÃĂẮẰẶẲẴÂẤẦẬẨẪBCDĐEÉẸẺẼÊẾỀỆỂỄFGHIÍÌỊỈĨJKLMNOÓÒỌỎÕÔỐỒỘỔỖƠỚỜỢỞỠPQRSTUÚÙỤỦŨƯỨỪỰỬỮVWXYÝỲỴỶỸ0123456789`[emailprotected]#$%^&*()'


def decrypt(k, ciphertext):
    result = ''

    for l in ciphertext:
        try:
            i = (key.index(l) - k) % len(key)
            result += key[i]
        except ValueError:
            result += l

    return result


def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")

    data = conn.recv(SIZE)
    str_data = data.decode(FORMAT)
    k = 5
    print(str_data)
    mess_decrypt = decrypt(k, str_data)
    print("Tin nhắn nhận được: " + mess_decrypt)


def main():
    print("[STARTING] Server is starting")
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(ADDR)
    server.listen()
    print(f"[LISTENING] Server is listening on {IP}:{PORT}.")

    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")


if __name__ == '__main__':
    main()
