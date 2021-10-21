import requests 
import xml.etree.ElementTree as ET

class Dymo: 

    def __init__(self, host="https://127.0.0.1", port="41951", printer="DYMO LabelWriter 450 Twin Turbo"): 
        self.uri = f"{host}:{port}/DYMO/DLS/Printing"
        self.header = {'Content-Type': 'application/x-www-form-urlencoded'}
        self.printer = printer
        self.certificate = False


    def base_url(self, endpoint): 
        return self.uri + endpoint 


    def get_status(self): 
        resp = requests.get(self.base_url('/StatusConnected'), verify=False)
        return {'status_code': resp.status_code, 'content': resp.content}


    def get_printer(self): 
        url = self.base_url('/GetPrinters')
        resp = requests.get(url, verify=False)
        try: 
            root = ET.fromstring(resp.get('content'))
            content = [{c.tag:c.text} for c in root.iter() if c.text is not None]
        except: 
            content = resp.content

        return {'status_code': resp.status_code, 'content': content}


    def encode_printer(self):
        return {'printerName': requests.utils.quote(self.printer)}
    
    def encode_label(self, label):
        return {'labelXml': requests.utils.quote(label)}
    
    def encode_params(self, print_params):
        return {'printParamsXml': requests.utils.quote(print_params)}


    def get_labelpreview(self, printer = None, label_xml=None): 
        """Not implemented."""
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


    def print(self, label_xml='', label_params=''): 
        
        status = self.get_status()
        
        if status: 
            body = {
                **self.encode_printer(), 
                **self.encode_label(label_xml), 
                **self.encode_params(label_params),
                'labelSetXml': ''
            }
        else: 
            raise('Printer not found')
        
        # Fix this
        body = [k + '=' + v for k, v in body.items()]
        complete_body = "&".join(body)

        resp = requests.post(
            self.base_url('/PrintLabel'), headers=self.header, 
            data=complete_body, verify=False
            )
        
        return resp


def make_xml(top='Hello', bottom='World'): 
    """
    Test xml that prints a shipping label with top and bottom text seperated by a line. 
    """
    resp = """<?xml version="1.0" encoding="utf-8"?>
            <DieCutLabel Version="8.0" Units="twips">
                <PaperOrientation>Landscape</PaperOrientation>
                <Id>NameBadge</Id>
                <PaperName>30256 Shipping</PaperName>
                <DrawCommands>
                    <Path>
                        <FillMode>EvenOdd</FillMode>
                        <RoundRectangle X="0" Y="0" Width="3331" Height="5760" Rx="180" Ry="180" />
                        <RoundRectangle X="2880" Y="2520" Width="1180" Height="720" Rx="120" Ry="120" />
                    </Path>
                </DrawCommands>
                <ObjectInfo>
                    <TextObject>
                        <Name>Top Text</Name>
                        <ForeColor Alpha="255" Red="0" Green="0" Blue="0" />
                        <BackColor Alpha="0" Red="255" Green="255" Blue="255" />
                        <LinkedObjectName></LinkedObjectName>
                        <Rotation>Rotation0</Rotation>
                        <IsMirrored>False</IsMirrored>
                        <IsVariable>False</IsVariable>
                        <HorizontalAlignment>Center</HorizontalAlignment>
                        <VerticalAlignment>Middle</VerticalAlignment>
                        <TextFitMode>AlwaysFit</TextFitMode>
                        <UseFullFontHeight>True</UseFullFontHeight>
                        <Verticalized>False</Verticalized>
                        <StyledText>
                            <Element>
                                <String>{}</String>
                                <Attributes>
                                    <Font Family="Arial" Size="48" Bold="True" Italic="False" Underline="False" Strikeout="False" />
                                    <ForeColor Alpha="255" Red="0" Green="0" Blue="0" />
                                </Attributes>
                            </Element>
                        </StyledText>
                    </TextObject>
                    <Bounds X="336" Y="497.256622314453" Width="5338" Height="822.743347167969" />
                </ObjectInfo>
                <ObjectInfo>
                    <ShapeObject>
                        <Name>Shape</Name>
                        <ForeColor Alpha="255" Red="0" Green="0" Blue="0" />
                        <BackColor Alpha="0" Red="255" Green="255" Blue="255" />
                        <LinkedObjectName></LinkedObjectName>
                        <Rotation>Rotation0</Rotation>
                        <IsMirrored>False</IsMirrored>
                        <IsVariable>False</IsVariable>
                        <ShapeType>HorizontalLine</ShapeType>
                        <LineWidth>45</LineWidth>
                        <LineAlignment>Center</LineAlignment>
                        <FillColor Alpha="0" Red="255" Green="255" Blue="255" />
                    </ShapeObject>
                    <Bounds X="336" Y="1425" Width="5338" Height="45" />
                </ObjectInfo>
                <ObjectInfo>
                    <TextObject>
                        <Name>Top Text</Name>
                        <ForeColor Alpha="255" Red="0" Green="0" Blue="0" />
                        <BackColor Alpha="0" Red="255" Green="255" Blue="255" />
                        <LinkedObjectName></LinkedObjectName>
                        <Rotation>Rotation0</Rotation>
                        <IsMirrored>False</IsMirrored>
                        <IsVariable>False</IsVariable>
                        <HorizontalAlignment>Center</HorizontalAlignment>
                        <VerticalAlignment>Middle</VerticalAlignment>
                        <TextFitMode>AlwaysFit</TextFitMode>
                        <UseFullFontHeight>True</UseFullFontHeight>
                        <Verticalized>False</Verticalized>
                        <StyledText>
                            <Element>
                                <String>{}</String>
                                <Attributes>
                                    <Font Family="Arial" Size="65" Bold="True" Italic="False" Underline="False" Strikeout="False" />
                                    <ForeColor Alpha="255" Red="0" Green="0" Blue="0" />
                                </Attributes>
                            </Element>
                        </StyledText>
                    </TextObject>
                    <Bounds X="0" Y="1518" Width="7755" Height="3731" />
                </ObjectInfo>
            </DieCutLabel>""".format(top, bottom)

    return resp.strip().replace('\n', '')
            
def make_params(side="Left"): 
    """
    Arguments: 
        side:str 
        Choose the left or right side of the roll if using Dymo Twin Turbo.
    """
    return '<LabelWriterPrintParams><TwinTurboRoll>{}</TwinTurboRoll></LabelWriterPrintParams>'.format(side)
 
