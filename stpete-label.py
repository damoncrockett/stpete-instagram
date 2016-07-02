import base64
import httplib2

from googleapiclient import discovery
from oauth2client.service_account import ServiceAccountCredentials

cred_file = '/Users/damoncrockett/Desktop/stpete/stpete-cred.json'

DISC_URL='https://{api}.googleapis.com/$discovery/rest?version={apiVersion}'
creds = ServiceAccountCredentials.from_json_keyfile_name(cred_file)
service = discovery.build('vision', 'v1', credentials=creds, discoveryServiceUrl=DISC_URL)

import glob
import os
import pandas as pd

DIR = "/Users/damoncrockett/Desktop/stpete/sample/"

tmp = []
for file in glob.glob(os.path.join(DIR,"*.jpg")):
    tmp.append(file)
    
df = pd.DataFrame(tmp,columns=["local_path"])
n = len(df)

labels = []

for i in range(n):
    with open(df.local_path.loc[i], 'rb') as image:
        image_content = base64.b64encode(image.read())
        service_request = service.images().annotate(body={
            'requests': [{
                'image': {
                    'content': image_content.decode('UTF-8')
                },
                'features': [{
                    'type': 'LABEL_DETECTION',
                    'maxResults': 1000
                }]
            }]
        })
        
        response = service_request.execute()
        
        if response['responses'][0]:
            label = response['responses'][0]['labelAnnotations'][0]['description']
            labels.append(label)
        else:
            labels.append('unknown')
            
    print i
        
df['label'] = labels
df.to_csv("./labels.csv",index=False)