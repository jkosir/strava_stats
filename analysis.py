import os
from lxml import etree

import constants

activities = []
premium = 0
for file in os.listdir('profiles'):
    root = etree.parse('profiles/' + file, parser=etree.HTMLParser())
    try:
        #a = root.xpath(constants.LAST_4_WEEKS_ACTIVITIES_XPATH)[0].text
        #activities.append(a)
        title = etree.tostring(root.xpath('//div[@class = "athlete-title"]')[0])
        if b'Premium Member' in title:
            premium+=1
    except:
        continue
#print(len([x for x in activities if int(x) > 10]))
print(premium)