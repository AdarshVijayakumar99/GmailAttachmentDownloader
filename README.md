

# Attachment Downloader
1. Create a google developer account ( https://developers.google.com/gmail/api/quickstart/python )
2. So it will go to Google Cloud and We have to create a project . 
3. After creating the project, we have to enable GMAIL API button ( Select "DESKTOP APP" as OAUTH CLIENT ) and download the credentials 
4. Rename the  credentials file as credentials.json and then paste it into the root directory of the project.
5. Import the EZGmail module using pip install EZGmail 
6. Run the script.
7. Opens the browser for asking to login to Gmail account and allow "QUICKSTART" app to access it
8. A token.json file will be downloaded and paste it into the root directory of the project which the script can use.



# Code Overview


1. First of all i will create a query string with has:attachment in it   
2. ezgmail has a method called search which will help us to search the query string
3. Returns the list of threads containing the gmail messages
4. A GmailThread consists of a GmailMessage where each GmailMessage object has headers/Subject/body etc . 
