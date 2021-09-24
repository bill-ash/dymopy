import pytest 
from dymopy import __version__

def test_version():
    assert __version__ == '0.1.0'

def test_import(): 
    import dymopy 
    from dymopy import client 
    dymopy.client.Dymo

def test_connection(): 
    from dymopy.client import Dymo
    dymo = Dymo(host='https://192.168.14.143', port=41951)
    assert dymo.uri == "https://192.168.14.143:41951/DYMO/DLS/Printing"

    