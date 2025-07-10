### main ###

from fastapi import FastAPI

# Instance FastAPI
app = FastAPI()

# Request to the server always must be async
@app.get('/')
async def root():
    return 'Hello FastAPI!'

@app.get('/url')
async def url():
    return { "url_course":"https://mouredev.com/python" }

