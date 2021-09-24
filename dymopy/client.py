from requests.utils import quote 
from requests.compat import urljoin
import requests 


#  WS_PROTOCOl = "https://"
#  WS_START_PORT = 41951
#  WS_END_PORT = 41960
#  WS_CHECK_TIMEOUT = 3e3
#  WS_COMMAND_TIMEOUT = 1e4
#  WS_SVC_HOST = "127.0.0.1"
#  WS_SVC_HOST_LEGACY = "localhost"
#  WS_SVC_PATH = "DYMO/DLS/Printing"
#  WS_CMD_STATUS = "StatusConnected"
#  WS_CMD_GET_PRINTERS = "GetPrinters"
#  WS_CMD_OPEN_LABEL = "OpenLabelFile"
#  WS_CMD_PRINT_LABEL = "PrintLabel"
#  WS_CMD_PRINT_LABEL2 = "PrintLabel2"
#  WS_CMD_RENDER_LABEL = "RenderLabel"
#  WS_CMD_LOAD_IMAGE = "LoadImageAsPngBase64"
#  WS_CMD_GET_JOB_STATUS = "GetJobStatus";

class Dymo: 

    def __init__(self, host="https://127.0.0.1", port="41951", printer="DYMO LabelWriter 450"): 
        self.uri = f"{host}:{port}/DYMO/DLS/Printing"
        self.header = {'Content-Type': 'application/x-www-form-urlencoded'}
        self.printer = printer
        self.certificate = False

    def base_url(self, endpoint): 
        return self.uri + endpoint 

    def get_printer(self): 
        url = self.base_url('/GetPrinters')
        resp = requests.get(url, verify=False)
        return resp.content

    def get_status(self): 
        resp = requests.get(self.base_url('/StatusConnected'), verify=False)


    def get_labelpreview(self, printer = None, label_xml=None): 
        url = self.uri + '/RenderLabel'
        printer = self.get_printer(printer)

        body = {
            "printerName=": "",
            "renderParamsXml=": "",
            "labelXml=": label_xml, 
            "labelSetXml=":""
        }
        resp = requests.post()

        return resp.content


    def print(self, printer=None, labelXml='', labelParams=''): 
        # Ensure the status is ready to receive a print
        status = self.get_status()

        if printer is None: 
            printer = self.get_printer()



def make_xml(xml): 
    pass 
