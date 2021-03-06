from sanic import Sanic
from sanic.response import text

app = Sanic("My Hello, world app")

# @app.get("/")
# async def hello_world(request):
#     return text("Hello, world.")


@app.websocket("/feed")
async def feed(request, ws):
    while True:
        data = "hello!"
        print("Sending: " + data)
        await ws.send(data)
        data = await ws.recv()
        print("Received: " + data)

if __name__ == "__main__":
  app.run(host="localhost", port=8000)