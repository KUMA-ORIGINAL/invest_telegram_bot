from aiohttp import web

routes = web.RouteTableDef()


@routes.post('/api')
async def cryptomus_webhook(request):
    data = await request.json()
    print(data)
