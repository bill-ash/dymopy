from requests.utils import quote 
from requests.compat import urljoin
import requests 

class Dymo: 

    def __init__(self, host="https://127.0.0.1", port="41951", printer="DYMO LabelWriter 450"): 
        self.uri = f"{host}:{port}/DYMO/DLS/Printing"
        self.printer = printer

    def getprinter(self): 
        url = self.uri + '/GetPrinters'
        resp = requests.get(url, verify=False)
        return resp 
