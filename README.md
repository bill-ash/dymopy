# dymopy 

Simple http client for creating labels using the DYMO Connect Web Service. 

Heavily influenced by the [dymojs package](https://github.com/dsandor/dymojs) available for node. 

# Example 

Example using a Dymo Twin Turbo. You may need to modify `make_params()` to 
suit your printer. 

```
from dymopy import Dymo

dymo = Dymo()

status = dymo.get_status()
assert status['status_code'] == 200

printer = dymo.get_printer()
assert printer['status_code'] == 200

# Helpers for with text XML to send to the printer
label_params = make_params(side="Right")
label_xml = make_xml("Hello", "I am Bill!")
    
print_resp = dymo.print(label_xml=label_xml, label_params=label_params)
assert print_resp.status_code == 200
```    

