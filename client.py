import websockets
import asyncio

async def mensagem():
 async with websockets.connect("ws://ip da pessoa:8080") as socket:
   while True:
    msn = input("Digite uma mensagem: ")
    if msn == 'sair':
     break
    await socket.send(msn)
    response = await socket.recv()
    print("Resposta de Mr.Robot: ", response)
  
asyncio.get_event_loop().run_until_complete(mensagem())