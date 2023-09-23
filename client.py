import websockets
import asyncio
from cryptography.fernet import Fernet

# Chave de criptografia (a mesma chave usada no servidor)
key = b'your-secret-key-here'
cipher_suite = Fernet(key)

async def mensagem():
    async with websockets.connect("ws://ip-da-pessoa:8080") as socket:
        while True:
            msn = input("Digite uma mensagem: ")
            if msn == 'sair':
                break

            # Criptografa a mensagem antes de enviar
            encrypted_message = cipher_suite.encrypt(msn.encode())
            await socket.send(encrypted_message)

            response = await socket.recv()
            
            # Descriptografa a resposta recebida do servidor
            decrypted_response = cipher_suite.decrypt(response).decode()
            print("Resposta de Mr.Robot (descriptografada):", decrypted_response)

asyncio.get_event_loop().run_until_complete(mensagem())
