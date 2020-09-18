# Email Client
An online tool to send an email to single or multiple email IDs along with other emails features like cc, bcc etc. There is also an option to import email ID list from CSV file.
  

# UX / UI

A basic UI to input parameters like email IDs, subject, message body etc and send an email. A library named "tag_editor" (also called chips structure) is used for email inputs so that every email ID will be separated by entering comma or enter. This will improve the user experience.
A file import button is used to import CSV file and all list of email IDs mentioned in the file will be auto filled to input "To".

See the snapshot for UI:
![N|Solid](https://raw.githubusercontent.com/nkpatil/email_client/master/compose_mail_ui.png)

## Improvements on project
Since this is a basic app to send an email to recipients. There is a lot of scope in the application to make it ready for the production. Below are few:
    - User authentication needs to be added and allow only logged in users to access the features
    - ELK stack to be used for logs management and visualization
    - Use scalable and reliable database like postgresql etc.
    - Can be deployed on cloud services such as AWS, google cloud.
    - For email configuration, AWS SES etc can be used.

## UI Improvements
There is a scope for improvements in UI to make a better user experience. Below are few of them:
    - Validations on email IDs while entering. Before making it as chips, it should validate if that is the proper email ID format or not.
    - Validaton on maximum number of email IDs allowed to send an email. This has to be done on "to, cc and bcc".
    - Filter the special characters and html tags and repalce them to a string format so that it won't affect the interface while showing the data on html page.
    - Can show success/failure respose (from backed) in better visualization than into alert box.
    - Validations on email IDs inside CSV while importing them to input


## Framework and tools:
  - Backend: Django, python, sqlite
  - Frontend: HTML, javascript, jquery, mdb(materialize-bootstrap), css


## Database

- Mail: A table named "mail" will store the logs along with created timestamp. Fields are: receivers, cc, bcc, subject, message and timestamp.


## Local Installation and Setup
(Install python-pip and setup a virtual environment)
  - git clone https://github.com/nkpatil/email_client.git
  - cd email_client
  - pip install -r requirements
  - python manage.py makemigrations
  - python manage.py migrate
  - python manage.py runserver

  - To create new superuser: python manage.py createsuperuser

URL: http://localhost:8000/
Note: Above steps are to run the project in local environment setup.

### Command to send email statistics
python manage.py send_email_report <receivers> <date>
Above command will take 2 parameters: comma separated email id list to send the report and date for which the statistics need to be shared. Default date is for current day in case not provided.
ie: python manage.py send_email_report abc@gmail.com,xyz@yahoo.com 2020-09-01

The command can be scheduled to run with interval using cronjob.
See the snapshot which is the mail stats received:
![N|Solid](https://raw.githubusercontent.com/nkpatil/email_client/master/email_stats.png)



## Configuration
Below are few configurations has to be done to run the project:
    - Django SECRET_KEY: Generate a random secret key and paste in settings.py in variable SECRET_KEY. https://djecrety.ir/ can be used to generate the new secret key.
    - EMAIL configs:
    EMAIL_HOST='smtp.office365.com' is used, this can be modified as per the send email service. Can be used AWS SES here.
    EMAIL_HOST_USER and EMAIL_HOST_PASSWORD: fill email id and password to test the app.
Note: all above configurations are to test the project in local system only. To deploy this on production, some secure configuration service (like AWS Secrets Manager
) has to be used to securely storing the secret keys and credentials.
