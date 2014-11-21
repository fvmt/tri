from lxml import etree

import requests

from settings import TRIANGLE_URL, XSD_PATH, IS_TRIANGLE_XPATH, TRI_TYPE_XPATH



def check_triangle(payload):

    params = {'legs': payload}
    url = TRIANGLE_URL
    r = requests.get(url, params=params)
    return r.content


def valid_xml(text):

    try:
        with open(XSD_PATH, 'rb') as xsd_path:
            schema_root = etree.XML(xsd_path.read())
        schema = etree.XMLSchema(schema_root)
        parser = etree.XMLParser(schema=schema)
        root = etree.fromstring(text, parser)
        return True
    except etree.XMLSyntaxError:
        return False


def parse_response(text):

    root = etree.XML(text)
    is_triangle = root.xpath(IS_TRIANGLE_XPATH)[0].text
    tri_type = root.xpath(TRI_TYPE_XPATH)[0].text
    return is_triangle, tri_type


if __name__ == "__main__":
    validate_xml(check_triangle('1,2,a'))
    print parse_response(check_triangle(1,1,1))
    

