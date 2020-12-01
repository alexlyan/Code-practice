# step import libraries
import pandas as pd
import smtplib
import datetime
from email.message import EmailMessage

# Step 1. Loading json file and prepare for sending
# 1.1. Load Json file
df = pd.read_json('/Users/lyanalexandr/OneDrive/Projects/Programming/Python/practice/scrapping/hackernews/hacker.jsonl', lines=True)
# 1.2. Drop duplicates
df.drop_duplicates('Article Header', inplace=True)
# 1.3. Create name for file
date_file = (datetime.datetime.today() - datetime.timedelta(1)).strftime('%Y-%m-%d 0:0:0')

df = df[df['Datetime'] > date_file].sort_values(by='Points', ascending=False)
# 1.4. CSV or HTML?
# df.to_csv(f'{date_file}.csv')

# Step 2. Send mail in html format

EMAIL_ADDRESS = 'alexlyan1612@gmail.com'
EMAIL_PASSWORD = 'cbknfmxgdafgilct'

# Recipients List
recipients = ['alexlyan1612@gmail.com',
              # 'sanjar.mamatov.197@gmail.com', 'Begimai.amantaeva@gmail.com'
              ]
msg = EmailMessage()
msg['From'] = EMAIL_ADDRESS
msg['To'] = ', '.join(recipients)
msg['Subject'] = f'TOP HACKER NEWS for {date_file}'
# msg['body'] = 'Hacker News'

html = """\
<html>
  <head></head>
  <body>
    {0}
  </body>
</html>
""".format(df.head(10).to_html())

msg.add_alternative(html, subtype='html')


with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
# with smtplib.SMTP_SSL('localhost', 456) as smtp:

    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)



