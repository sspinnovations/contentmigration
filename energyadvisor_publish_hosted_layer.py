import arcgis
from arcgis.gis import GIS
import os
import logging
import time
from arcgis.features import FeatureLayerCollection

starttime=time.time() 

fileLog = str(os.path.abspath(__file__)).replace(".py",".log")
logging.basicConfig(filename=fileLog, filemode='w', format='%(asctime)s :: %(levelname)s :: %(threadName)s :: %(message)s', level=logging.INFO, datefmt='%m/%d/%Y %I:%M:%S %p')

gis = GIS("https://arcgis.com", "username", "password")

#FOLDER PATHS BASED ON PORTAL GROUPS

AMI_Path = r'C:\Temp\AMI'
SSN_SSN_RO_Path = r'C:\Temp\SSN'
AICC_DM_Path = r'C:\Temp\AICCDM'
DM_Path = r'C:\Temp\DM'
IEN_ProjMash_Path =r'C:\Temp\IENPM'

serviceProp = {}
serviceProp['type'] = 'File Geodatabase'
serviceProp['itemType'] = "file"
serviceProp['tags'] = "AMI"
itemId = []

try:
    def AMI():
        for dirpath, subdirs, files in os.walk(AMI_Path) :
            for aFile in files:
                fgdbPath = os.path.join(AMI_Path, aFile)
                fgdbPortalName = os.path.splitext(aFile)[0]
                logging.info("Starting Copy and Publish for " + fgdbPortalName)
                print("Starting Copy and Publish for " + fgdbPortalName)
                
                #TAGS FOR EACH DIRECTORY
                serviceProp = {}
                serviceProp['title'] = fgdbPortalName
                serviceProp['type'] = 'File Geodatabase'
                serviceProp['itemType'] = "file"
                serviceProp['tags'] = "AMI"

                pubProps = {}
                pubProps["hasStaticData"] = 'false'
                pubProps["name"] =fgdbPortalName
                pubProps["maxRecordCount"] = 2000
                pubProps["layerInfo"] = {"capabilities":"Query"}
                

                addFGDB = gis.content.add(item_properties=serviceProp, data = fgdbPath)    

                pubFGDB = addFGDB.publish(publish_parameters = pubProps, file_type = 'filegeodatabase', overwrite=True)

                pubFGDB.share(org=False, groups='AMI')

                print("Finished Copy and Publish for AMI " + fgdbPortalName)
                logging.info("Copy and Publish Complete for AMI " + fgdbPortalName)


    def SSN_SSN_RO():
        for dirpath, subdirs, files in os.walk(SSN_SSN_RO_Path) :
            for aFile in files:
                fgdbPath = os.path.join(SSN_SSN_RO_Path, aFile)
                fgdbPortalName = os.path.splitext(aFile)[0]
                logging.info("Starting Copy and Publish for " + fgdbPortalName)
                print("Starting Copy and Publish for " + fgdbPortalName)
                
                #TAGS FOR EACH DIRECTORY
                serviceProp = {}
                serviceProp['title'] = fgdbPortalName
                serviceProp['type'] = 'File Geodatabase'
                serviceProp['itemType'] = "file"
                serviceProp['tags'] = "SSN"


                pubProps = {}
                pubProps["hasStaticData"] = 'false'
                pubProps["name"] =fgdbPortalName
                pubProps["maxRecordCount"] = 2000
                pubProps["layerInfo"] = {"capabilities":"Query"}

                
                addFGDB = gis.content.add(item_properties=serviceProp, data = fgdbPath)    

                pubFGDB = addFGDB.publish(publish_parameters = pubProps, file_type = 'filegeodatabase', overwrite=True)

                #dual group
                pubFGDB.share(org=False, groups=['SSN','SSN_RO'])

                print("Finished Copy and Publish for SSN " + fgdbPortalName)
                logging.info("Copy and Publish Complete for SSN " + fgdbPortalName)






    def AICC_DM():
        for dirpath, subdirs, files in os.walk(AICC_DM_Path) :
            for aFile in files:
                fgdbPath = os.path.join(AICC_DM_Path, aFile)
                fgdbPortalName = os.path.splitext(aFile)[0]
                logging.info("Starting Copy and Publish for " + fgdbPortalName)
                print("Starting Copy and Publish for " + fgdbPortalName)
                
                #TAGS FOR EACH DIRECTORY
                serviceProp = {}
                serviceProp['title'] = fgdbPortalName
                serviceProp['type'] = 'File Geodatabase'
                serviceProp['itemType'] = "file"
                serviceProp['tags'] = "SSN"


                pubProps = {}
                pubProps["hasStaticData"] = 'false'
                pubProps["name"] =fgdbPortalName
                pubProps["maxRecordCount"] = 2000
                pubProps["layerInfo"] = {"capabilities":"Query"}

                
                addFGDB = gis.content.add(item_properties=serviceProp, data = fgdbPath)    

                pubFGDB = addFGDB.publish(publish_parameters = pubProps, file_type = 'filegeodatabase', overwrite=True)

                #dual group
                pubFGDB.share(org=False, groups=['AICC','DM Group'])

                print("Finished Copy and Publish for SSN " + fgdbPortalName)
                logging.info("Copy and Publish Complete for SSN " + fgdbPortalName)

    def DM():
        for dirpath, subdirs, files in os.walk(DM_Path) :
            for aFile in files:
                fgdbPath = os.path.join(DM_Path, aFile)
                fgdbPortalName = os.path.splitext(aFile)[0]
                logging.info("Starting Copy and Publish for " + fgdbPortalName)
                print("Starting Copy and Publish for " + fgdbPortalName)
                
                #TAGS FOR EACH DIRECTORY
                serviceProp = {}
                serviceProp['title'] = fgdbPortalName
                serviceProp['type'] = 'File Geodatabase'
                serviceProp['itemType'] = "file"
                serviceProp['tags'] = "TEST"


                pubProps = {}
                pubProps["hasStaticData"] = 'false'
                pubProps["name"] =fgdbPortalName
                pubProps["maxRecordCount"] = 2000
                pubProps["layerInfo"] = {"capabilities":"Query"}

                
                addFGDB = gis.content.add(item_properties=serviceProp, data = fgdbPath)    

                pubFGDB = addFGDB.publish(publish_parameters = pubProps, file_type = 'filegeodatabase', overwrite=True)

                #dual group
                pubFGDB.share(org=False, groups=['DM Group'])

                print("Finished Copy and Publish for DM " + fgdbPortalName)
                logging.info("Copy and Publish Complete for SSN " + fgdbPortalName)




    def IENPM():
        for dirpath, subdirs, files in os.walk(IEN_ProjMash_Path) :
            for aFile in files:
                fgdbPath = os.path.join(IEN_ProjMash_Path, aFile)
                fgdbPortalName = os.path.splitext(aFile)[0]
                logging.info("Starting Copy and Publish for " + fgdbPortalName)
                print("Starting Copy and Publish for " + fgdbPortalName)
                
                #TAGS FOR EACH DIRECTORY
                serviceProp = {}
                serviceProp['title'] = fgdbPortalName
                serviceProp['type'] = 'File Geodatabase'
                serviceProp['itemType'] = "file"
                serviceProp['tags'] = "IEN"


                pubProps = {}
                pubProps["hasStaticData"] = 'false'
                pubProps["name"] =fgdbPortalName
                pubProps["maxRecordCount"] = 2000
                pubProps["layerInfo"] = {"capabilities":"Query"}

                
                addFGDB = gis.content.add(item_properties=serviceProp, data = fgdbPath)    

                pubFGDB = addFGDB.publish(publish_parameters = pubProps, file_type = 'filegeodatabase', overwrite=True)

                #dual group
                pubFGDB.share(org=False, groups=['IEN Dev','Project Mashup'])

                print("Starting Copy and Publish for IEN AND PROJECT MASHUP " + fgdbPortalName)
                logging.info("Copy and Publish Complete for SSN " + fgdbPortalName)






    def main():
        logging.info("START")

        AMI()
        SSN_SSN_RO() 
        AICC_DM()
        IENPM()
        DM()

        logging.info("Copy and Publish Complete for all items")
        print("Script has completed publishing the items")

            

except:
    logging.info("There is an error publishing " + fgdbPortalName)
    e = str(sys.exc_info()[1])
    logging.info(e)
    print (e)

if __name__ == '__main__':
    main()
