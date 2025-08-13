import requests

def send_otp_sms(phone, otp):
    url = "https://www.fast2sms.com/dev/bulkV2"
    headers = {
        'authorization': 'J739ogYVjvE6wHPCkT41xWaOF50nDlyAfZziXrbptGqh8KcNeL2aElA0tHxBrIscZRnuzLv6khJ7bfNF',  # 🔁 Replace with your actual key
        'Content-Type': "application/x-www-form-urlencoded"
    }
    data = {
        'variables_values': otp,
        'route': 'otp',
        'numbers': phone
    }

    response = requests.post(url, headers=headers, data=data)
    return response.json()