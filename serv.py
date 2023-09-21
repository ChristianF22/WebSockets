import websockets
import asyncio

#Função chamada quando um cliente se conectar

async def response(websocket, path):
    msn = await websocket.recv()
    print(f"Mensagem recebida: {msn}")
    await websocket.send("Mensagem recebida, xero")

start_server = websockets.serve(response, '0.0.0.0', 8080)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()