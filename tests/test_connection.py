import pytest 


def test_import(): 
    import dymopy 
    from dymopy import client 
    dymopy.client.Dymo

def test_connection(): 
    from dymopy.client import Dymo
    dymo = Dymo(host='https://192.168.14.143', port=41951)
    resp = dymo.getprinter()
    