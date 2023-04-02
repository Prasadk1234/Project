"""# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client
# Set environment variables for your credentials
# Read more at http://twil.io/secure
account_sid = "AC2ec56ee8e21862879d244257b85a0af1"
auth_token = os.environ["TWILIO_AUTH_TOKEN"] = '4e512195f481ce3be7ae4c84ca3ed3ff'
client = Client(account_sid, auth_token)
message = client.messages.create(
  body= Looking for a job in the government sector? Look no further! The government is currently hiring for a wide range of positions across various departments and agencies. Here are some of the benefits of working for the government:
        Job Security: Government jobs offer a high degree of job security, as government employees are typically not subject to layoffs or downsizing.
        Competitive Salaries: Government jobs often offer competitive salaries, as well as opportunities for regular pay raises and promotions.
        Generous Benefits: Government employees typically receive a range of generous benefits, including health insurance, retirement plans, and paid time off.
        Opportunities for Advancement: Government jobs offer a variety of opportunities for career advancement, with many positions offering a clear path for promotion and advancement.
        Public Service: Working for the government offers the opportunity to serve your community and make a positive impact on society.
        If you're interested in a career in the government, there are many positions currently available across a range of departments and agencies. Check out government job boards or websites for more information on available positions and how to apply. Don't miss out on this exciting opportunity to work in public service and make a difference in your community!,

  from_="+14406368196",
  to="+917083404359"
)
print(message.sid)"""

import 
requests.post("https://ntfy.sh/phil_alerts",
    data="Remote access to phils-laptop detected. Act right away.",
    headers={
        "Title": "Unauthorized access detected",
        "Priority": "urgent",
        "Tags": "warning,skull"
    }