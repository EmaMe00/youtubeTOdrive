# Requisition
This library used in this script is pytube and pydrive. 
You can download and read documentantion from:
Pydrive: https://pythonhosted.org/PyDrive/
Pytube: https://pytube.io/en/latest/

WARNING: When you would use pydrive you need to change some settings in your google drive account. 
Follow the documentation !

This is settings for your google account: 

Drive API requires OAuth2.0 for authentication. PyDrive makes your life much easier by handling complex authentication steps for you.

1 - Go to APIs Console and make your own project.

2 - Search for ‘Google Drive API’, select the entry, and click ‘Enable’.

3 - Select ‘Credentials’ from the left menu, click ‘Create Credentials’, select ‘OAuth client ID’.

4 - Now, the product name and consent screen need to be set -> click ‘Configure consent screen’ and follow the instructions. Once finished:

      a) Select ‘Application type’ to be Web application.
      
      b) Enter an appropriate name.
      
      c) Input http://localhost:8080 for ‘Authorized JavaScript origins’.
      
      d) Input http://localhost:8080/ for ‘Authorized redirect URIs’.
      
      e) Click ‘Save’.
  
Click ‘Download JSON’ on the right side of Client ID to download client_secret_<really long ID>.json.
The downloaded file has all authentication information of your application. Rename the file to “client_secrets.json” and place it in your working directory.

Create quickstart.py file and copy and paste the following code.

I recommend installing the package: 
pip install httplib2==0.15.0
pip install google-api-python-client==1.6

DO NOT INSTALL PYTUBE3, GIVE PROBLEM, AND IF YOU HAVE UNISTALL NOW.
