from arcgis.gis import GIS
gis = GIS("https://arcgis.com", "username”, "password")

items =  ['ae01a7e0145945a6b2ecd0fbef46821a',
 '602cc246c09b4432a21e4373a627eb8e',
 'a60d0f38244d423fb9047badd7748d39',
 '86c03824866e4a73b58e74a4feb6b0bb',
 '545db7a2be764e4eb778caac7517a78e',
 '126531fb33f84c6f8eeb0a02d8af5be6',
 'f3e7960862cf4028b00fbb3cb3366d39',
 '30ce8b50df0847c1a4ffa7baee15d43a',
 'f18731db5d1749e8a6718fc6ee45b8cc',
 '86ef94da64534d77ac68b79b38cdfb32',
 'fac116b4db824a408a6a68d93103cb7f',
 '64fdadfa1d5542ad9122372a7e0fa917',
 '5edf8211780e4f4093f52fcefefa7f73',
 '945b5a8e5a4f4fb69b8994558b000653']
]

#List items to download
for item in items:
    GISitem = gis.content.get(item)
    print (GISitem.title)
    service_title = GISitem.title
    version = ""
    fgdb_title = (service_title)
    result = GISitem.export(fgdb_title, "File Geodatabase")
    result.download(r'C:\Temp\GoLive\FGDB')
    result.delete()
    

print("Script has completed downloading the items")
