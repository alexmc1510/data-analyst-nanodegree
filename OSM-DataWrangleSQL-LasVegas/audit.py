import xml.etree.cElementTree as ET
from collections import defaultdict
import re
import pprint

# Audit Street Type ######################################################
street_type_re = re.compile(r'\b\S+\.?$', re.IGNORECASE)

expected = ["Street", "Avenue", "Boulevard", "Drive", "Court", "Place", "Square", "Lane", "Road", 
            "Trail", "Parkway", "Commons", "Cove", "Alley", "Park", "Way", "Walk" "Circle", "Highway", 
            "Plaza", "Path", "Center", "Mission"]

mapping = { "Ave": "Avenue",
            "Ave.": "Avenue",
            "avenue": "Avenue",
            "ave": "Avenue",
            "Blvd": "Boulevard",
            "Blvd.": "Boulevard",
            "Blvd,": "Boulevard",
            "Boulavard": "Boulevard",
            "Boulvard": "Boulevard",
            "Ct": "Court",
            "Dr": "Drive",
            "Dr.": "Drive",
            "E": "East",
            "Hwy": "Highway",
            "Ln": "Lane",
            "Ln.": "Lane",
            "Pl": "Place",
            "Plz": "Plaza",
            "Rd": "Road",
            "Rd.": "Road",
            "St": "Street",
            "St.": "Street",
            "st": "Street",
            "street": "Street",
            "square": "Square",
            "parkway": "Parkway"
            }


def audit_street_type(street_types, street_name):
    m = street_type_re.search(street_name)
    if m:
        street_type = m.group()
        if street_type not in expected:
            street_types[street_type].add(street_name)

            
def street_name(elem):
    return (elem.attrib['k'] == "addr:street")


def audit(osmfile):
    osm_file = open(osmfile, "r")
    street_types = collections.defaultdict(set)
    for event, elem in ET.iterparse(osm_file, events=("start",)):

        if elem.tag == "node" or elem.tag == "way":
            for tag in elem.iter("tag"):
                if street_name(tag):
                    audit_street_type(street_types, tag.attrib['v'])
    osm_file.close()
    return street_types


def update_name(name, mapping, regex):
    m = regex.search(name)
    if m:
        st_type = m.group()
        if st_type in mapping:
            name = re.sub(regex, mapping[st_type], name)
    return name

# Audit Postal Code ######################################################
def audit_postal_code(error_codes, postal_codes, this_postal_code):
    # Append incorrect zip codes to list
    if this_postal_code.isdigit() == False:
        error_codes.append(this_postal_code)
    elif len(this_postal_code) != 5:
        error_codes.append(this_postal_code)
    else:
        postal_codes.update([this_postal_code])

def is_postal_code(elem):
    # Identify element tag as postal code
    return (elem.attrib['k'] == "addr:postcode")

def audit_post(osmfile):
    # Parse osm file for incorrect postal codes
    osm_file = open(osmfile, "r")
    error_codes = []
    postal_codes = set([])
    for event, elem in ET.iterparse(osm_file, events=("start",)):
        if elem.tag == "node" or elem.tag == "way":
            for tag in elem.iter("tag"):
                if is_postal_code(tag):
                    audit_postal_code(error_codes, postal_codes, tag.attrib["v"]) 
    return error_codes, postal_codes

bad_list, good_list = audit_post(OSM_PATH)

# Identify zip codes in our data outside of Las Vegas city
lasvegas_zips = [ '89044','89054','89101','89102','89103','89104','89105','89106','89107','89108','89109','89110','89111',
                 '89112','89113','89114','89115','89116','89117','89118','89119','89120','89121','89122','89123','89124',
                 '89125','89126','89127','89128','89129','89130','89131','89132','89133','89134','89135','89136','89137',
                 '89138','89139','89140','89141','89142','89143','89144','89145','89146','89147','89148','89149','89150',
                 '89151','89152','89153','89154','89155','89156','89157','89159','89160','89161','89162','89163','89164',
                 '89165','89166','89169','89170','89173','89177','89178','89179','89180','89183','89185','89191','89193',
                 '89195','89199']

# Count zip codes that occur outside Las Vegas city
count = 0
for el in good_list:
    if el not in lasvegas_zips:
        count += 1
        
bad_list