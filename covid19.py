import requests
import json
import base64
import os
import pandas as pd
# from sendgrid import SendGridAPIClient
# from sendgrid.helpers.mail import (Mail, Attachment, FileContent, FileName, FileType, Disposition, ContentId)







#getting the request from the url
data= requests.get('https://api.covid19india.org/data.json')
#checking the status_code
print(data.status_code)

recovered_list=[]
confiremd_list =[]
date_list=[]
#getting the data as json
if data.status_code == 200:
    covid_json = data.json()
    for d in covid_json['cases_time_series']:
        rec =  d['totalrecovered']
        conf = d['totalconfirmed']
        date = d['date']
        recovered_list.append(rec)
        confiremd_list.append(conf)
        date_list.append(date)

#creation of output file
df = pd.DataFrame({'date':date_list,'confirmed':confiremd_list,'recovered':recovered_list})
df.index+=1
directory = os.path.dirname(os.path.realpath(__file__))
filename = "output.csv"
file_path = os.path.join(directory, filename)
df.to_csv(file_path,index=False)



# #opening the output file and creation of attachment object
# with open(file_path, 'rb') as f:
#      data = f.read()
#      f.close()


   
# encoded = base64.b64encode(data).decode()



# #mail content
# message = Mail(
# from_email='dhayathilak96@gmail.com',
# to_emails='dhayathilakdazee@gmail.com',
# subject='Your File is Ready',
# html_content='<strong>Attached is Your Scraped File</strong>')
# attachment = Attachment()
# attachment.file_content = FileContent(encoded)
# attachment.file_type = FileType('text/csv')
# attachment.file_name = FileName('covid19india.csv')
# attachment.disposition = Disposition('attachment')
# message.attachment = attachment


# #sending the mail
# try:
#     sg = SendGridAPIClient('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')
#     response = sg.send(message)
#     print(response.status_code)
#     print(response.body)
#     print(response.headers)
# except Exception as e:
#     print(e)
