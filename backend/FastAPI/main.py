### main ###

from fastapi import FastAPI
from routers import products

# Instance FastAPI
app = FastAPI()

# Routers
app.include_router(products.router)

# Request to the server always must be async
@app.get('/')
async def root():
    return 'Hello FastAPI!'

@app.get('/url')
async def url():
    return { "url_course":"https://mouredev.com/python" }

