import pytest 
from dymopy.client import Dymo
from dymopy.client import make_xml, make_params 

def test_url(): 
    dymo = Dymo()
    assert dymo.uri == "https://127.0.0.1:41951/DYMO/DLS/Printing"

def test_status(): 
    dymo = Dymo()
    status = dymo.get_status()
    assert isinstance(status, dict)
    assert status['status_code'] == 200

def test_printer_name(): 
    dymo = Dymo()
    printer = dymo.get_printer()
    assert isinstance(printer, dict)
    assert printer['status_code'] == 200

def test_xml(): 
    label_params = make_params()
    label_xml = make_xml("This is working?")
    

def test_printer_job(): 
    dymo = Dymo()
    label_params = make_params()
    label_xml = make_xml('Hello', 'World!')
    
    print_resp = dymo.print(label_xml=label_xml, label_params=label_params)
    assert print_resp.status_code == 200
    
    