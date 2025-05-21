from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def mensagem():
    return {'mensagem': 'Olá mundo'}

