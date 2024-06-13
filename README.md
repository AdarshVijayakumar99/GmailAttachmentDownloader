

# Attachment Downloader
  -- > Create a google developer account ( https://developers.google.com/gmail/api/quickstart/python )
  -- > So it will go to Google Cloud and We have to create a project . 
  -- > After creating the project, we have to enable GMAIL API button ( Select "DESKTOP APP" as OAUTH CLIENT ) and download the credentials 
  -- > Rename the  credentials file as credentials.json and then paste it into the root directory of the project.
  -- > Import the EZGmail module using pip install EZGmail 
  -- > Run the script.
  -- > Opens the browser for asking to login to Gmail account and allow "QUICKSTART" app to access it
  -- > A token.json file will be downloaded and paste it into the root directory of the project which the script can use.



# Code Overview


 -- > First of all i will create a query string with has:attachment in it   
 -- > ezgmail has a method called search which will help us to search the query string
 -- > Returns the list of threads containing the gmail messages
 -- > A GmailThread consists of a GmailMessage where each GmailMessage object has headers/Subject/body etc . 
