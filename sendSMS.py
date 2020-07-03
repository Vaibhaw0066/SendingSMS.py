# # /usr/bin/env python
# # Download the twilio-python library from twilio.com/docs/libraries/python
# from twilio.rest import Client
#
# # Find these values at https://twilio.com/user/account
# account_sid = "ACb067bfc2d6227a4377f359d8b64dbcbe"
# auth_token = "b463e376694b232ac5c117fe6a70a152"
#
# client = Client(account_sid, auth_token)
#
# client.api.account.messages.create(
#     to="+919304330174",
#     from_="+1 251 244 1259",
#     body=" Approved Gadhi, bandar! ")
# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'ACb067bfc2d6227a4377f359d8b64dbcbe'
auth_token = 'b463e376694b232ac5c117fe6a70a152'
client = Client(account_sid, auth_token)

call = client.calls.create(
                        url='C:\\Vaibhaw\\Development\\Python\\Python Scripting\\SMS\\On-My-Way.mp3',
                        to='+919304330174',
                        from_='+12512441259'
                    )

print(call.sid)
