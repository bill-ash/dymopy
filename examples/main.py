from dymopy import Dymo
from dymopy.client import make_xml, make_params
from fastapi import FastAPI
import uvicorn 

app = FastAPI()
dymo = Dymo()

@app.post('/')
def print(top:str, bottom:str, copies: str, side:str): 
    label_xml = make_xml(top=top, bottom=bottom)
    label_params = make_params(copies=copies, side=side)
    resp = dymo.print(label_xml=label_xml, label_params=label_params)
    
    if resp.status_code == 200: 
        return True
    else: 
        return False

if __name__ == "__main__": 
    uvicorn.run("main:app", host="127.0.0.1", port=3000, log_level="info")

