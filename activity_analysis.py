import os
from lxml import etree

import constants

a = 0
for file in os.listdir('profiles'):
    root = etree.parse('profiles/' + file, parser=etree.HTMLParser())
    try:
        hrefs = root.xpath(constants.LAST_ACTIVITY_XPATH)
        if hrefs:
            print(hrefs[0])
            a += 1
    except Exception as e:
        print(e)
print(a)
