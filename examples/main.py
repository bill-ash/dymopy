from dymopy import Dymo
from dymopy.client import make_xml, make_params
from fastapi import FastAPI
import uvicorn 

app = FastAPI()
dymo = Dymo()

@app.post('/')
def print(labelXml, printParams): 
    label_xml = make_xml()
    label_params = make_params()
    # dymo.print()
    return {
        'Label': label_xml, 
        'Params': label_params
    }

if __name__ == "__main__": 
    uvicorn.run("main:app", host="127.0.0.1", port=5000, log_level="info")

