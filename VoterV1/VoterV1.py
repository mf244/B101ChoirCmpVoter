#this is from https://www.youtube.com/watch?v=UtNYzv8gLbs

import requests
import os
import random
import string
import json
import time

#Request URL Here
url = 'https://info.hidglobal.com/index.php/leadCapture/save2'#CHANGE ME


#Load JSONs into arrays here
emails = json.loads(open('emails.json').read())

fnames = json.loads(open('fnames.json').read())
lnames = json.loads(open('lnames.json').read())
localnumbers = json.loads(open('localnumbers.json').read())
localzips = json.loads(open('localzips.json').read())




for x in range(0, 100):
    f = open("votingamount.txt", "a")
    #Assign new random shit here
    
    tempemails = random.choice(emails)
    
    tempfnames = random.choice(fnames)
    templnames = random.choice(lnames)
    templocalnumbers = random.choice(localnumbers)
    templocalzips = random.choice(localzips)
   

    

    response = requests.post(url, allow_redirects=False, data={
        #HTTP request data here
        'Email': "men1234@beans.com",
        'FirstName': "findme",
        'LastName': "lastnamme",
        'Company': "wewew",
        'Country': "Azerbaijan",
        'Phone': "4446667777",
        'Role__c_lead': "Partner",
        'LeadSource': "PPC",
        'Lead_Source_Sub_Type__c':"",
        'Lead_Source_Sub_Type_Most_Recent__c': "",
        'Offer_Type__c': "",
        'Detail__c': "2022-idt-nam-09--msgeneric-dig-ads-adw-wp-top-7-cons-right-rfid-tag-IDT-NAM-EN-654",
        'Campaign_Name__c': "",
        'leadSourceMostRecent': "PPC",
        'Lead_Source_Detail__c': "",
        'Lead_Source_Detail_Most_Recent__c': "",
        'Conversion_Page_URL__c': "",
        'CampaignID': "",
        'autofill': "",
        'gclid': "Cj0KCQiAyracBhDoARIsACGFcS4rRciWVVrDyAWP79RrIs6THUTz-FqVPXunNZRXKL45pbBvxO1iu4gaAvo0EALw_wcB",
        'SingleOptIn': "yes",
        'DoubleOptIn': "yes",
        'honeypot': "",
        'lastRecaptchaUserInput': "",
        'lastRecaptchaFail': "",
        'lastReCAPTCHAServerSuccess': "",
        'lastRecaptchaEnabledFormID': "",
        'formid': "2050",
        'lpId': "84044",
        'subId': "380",
        'munchkinId': "289-TSC-352",
        'lpurl': "//info.hidglobal.com/2015-11-NAM-WP-PPC-ChooseTheRightRFIDTag_Request.html?cr={creative}&kw={keyword}",
        'cr': "",
        'kw': "",
        'q': "",
        '_mkt_trk': "id':289-TSC-352&token':_mch-hidglobal.com-1670299168581-14189",
        'formVid': "2050",
        '_mktoReferrer': "https'://info.hidglobal.com/2015-11-NAM-WP-PPC-ChooseTheRightRFIDTag_Request.html?ls=PPC&utm_detail=2022-idt-nam-09--msgeneric-dig-ads-adw-wp-top-7-cons-right-rfid-tag-IDT-NAM-EN-654&gclid=Cj0KCQiAyracBhDoARIsACGFcS4rRciWVVrDyAWP79RrIs6THUTz-FqVPXunNZRXKL45pbBvxO1iu4gaAvo0EALw_wcB",
        'checksumFields': "Email,FirstName,LastName,Company,Country,Phone,Role__c_lead,LeadSource,Lead_Source_Sub_Type__c,Lead_Source_Sub_Type_Most_Recent__c,Offer_Type__c,Detail__c,Campaign_Name__c,leadSourceMostRecent,Lead_Source_Detail__c,Lead_Source_Detail_Most_Recent__c,Conversion_Page_URL__c,CampaignID,autofill,gclid",
        'checksum': "bbf89c147f80fe910c825fdbed3d1e2f041773f435366298b45e0393fbff6a29"
    })
    
    
    writeMe = 'Run number %s of the program returned %s ' % (x, response)
    writeMeFile = '\nRun number %s of the program returned %s ' % (x, response)
    print(writeMe)

    f.write(writeMeFile)
    f.close()
    time.sleep(2)
 


