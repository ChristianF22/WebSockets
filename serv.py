import websockets
import asyncio
from cryptography.fernet import Fernet

# Chave para criptografar e descriptografar a mensagem
key = Fernet.generate_key()
cipher_suite = Fernet(key)

# Função para criptografar uma mensagem
def encrypt_message(message):
    encrypted_message = cipher_suite.encrypt(message.encode())
    return encrypted_message

# Função para descriptografar uma mensagem
def decrypt_message(encrypted_message):
    decrypted_message = cipher_suite.decrypt(encrypted_message).decode()
    return decrypted_message

# Função chamada quando um cliente se conectar
async def response(websocket, path):
    msn = await websocket.recv()
    decrypted_message = decrypt_message(msn)
    print(f"Mensagem recebida (descriptografada): {decrypted_message}")
    
    response_message = "Mensagem recebida, xero"
    encrypted_response = encrypt_message(response_message)
    await websocket.send(encrypted_response)

start_server = websockets.serve(response, '0.0.0.0', 8080)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
