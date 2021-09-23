from dymopy.client import Dymo 
import requests 
dymo = Dymo()
dymo.uri
dymo.getprinter()
requests.get('https://192.168.14.143:41951/DYMO/DLS/Printing/GetPrinters', verify=False)