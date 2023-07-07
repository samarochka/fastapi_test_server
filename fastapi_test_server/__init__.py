from fastapi import FastAPI
from fastapi.responses import PlainTextResponse


app = FastAPI()


@app.get('/')
async def root() -> PlainTextResponse:
    return PlainTextResponse(
        'works!'
    )


def run(port: int = 1488):
    from uvicorn import run

    run(app, host='0.0.0.0', port=port)
