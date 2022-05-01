import socket
import termcolor


PORT = 8000
IP = "127.0.0.1" # or "localhost o mismo

ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ls.bind((IP, PORT))
ls.listen()

print("Seq server configured!")
while True:
    print("Waiting for clients .....")

    try:
        (cs, client_ip_port) = ls.accept()

    # -- Server stopped manually
    except KeyboardInterrupt:
        print("Server stopped by the user")

        ls.close()
        exit()

    else:
        print("A client has connected to the server!")
        # -- Read the message from the client
        # -- The received message is in raw bytes
        msg_raw = cs.recv(2048)
        msg = msg_raw.decode().replace("\n", "").strip()
        spl_cmd = msg.split(" ")
        cmd = spl_cmd[0]
        termcolor.cprint(cmd, "yellow")
        print("OK!")
        if cmd != "PING":
            arg = spl_cmd[1]

        print(f"message received: {msg}")
        if cmd == "PING":
            response = "OK!\n"

        elif cmd == "GET":###
            arg = spl_cmd[1]
            l = ["U5", "ADA", "FRAT1", "RNU6_269P", "FXN.txt"]
            if int(arg) < 5:
                print(l[arg])
            else:
                print("THe number you chose isn´t valid")

        else:
            response = "This command is not available in the server.\n" # respuesta que vamos a modif dep de el ejeercicio

        # -- The message has to be encoded into bytes
        cs.send(response.encode())

        # -- Close the data socket
        cs.close()