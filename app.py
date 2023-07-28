from flask import Flask, jsonify, request, json

app = Flask(__name__)

# Route to get all items


register_success = {
    "status": "SUCCESS",
    "code": 900,
    "message": "Registered Email successfully"
}
loginData = {
    "status": "SUCCESS",
    "code": 900,
    "data": {
        "user_id": 1,
        "name": "loki",
        "email": "lokivikram2022@gmail.com",
        "is_email_verified": True,
        "member_since": "2023-07-17",
        "gender": None,
        "country_code": None,
        "mobile_number": None,
        "is_mobile_verified": False,
        "address": None,
        "pincode": None,
        "country": None,
        "dob": None,
        "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY4OTU5MDk2NiwianRpIjoiNzQzYWFhODgtYTNmYy00NmFhLTk3ZjAtODgzZWUzYWY4MzJhIiwidHlwZSI6ImFjY2VzcyIsInJlc2lkZW50Ijp7InVzZXJfaWQiOjF9LCJuYmYiOjE2ODk1OTA5NjYsImV4cCI6MTY4OTc2Mzc2Nn0.70iZ5PA-lNEdr-0mrMLR3S0E5zF9DEPcbnqR4zTUQ0Q",
        "refresh_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY4OTU5MDk2NiwianRpIjoiY2QzYzQ3NTYtYTFkMi00ODQxLTgzMWYtODZlZDM2MmEzMTkyIiwidHlwZSI6InJlZnJlc2giLCJyZXNpZGVudCI6eyJ1c2VyX2lkIjoxfSwibmJmIjoxNjg5NTkwOTY2LCJleHAiOjE2OTA0NTQ5NjZ9.7PxyJ0SLgJML1fZLxoVJYufoa4itbG9_-3N8lyp0Fgs"
    },
    "message": "Logged in successfully"
}
userdata = {
    'email' : '123',
    'password' : '123',
}
loginError = {
    "status": "ERROR",
    "code": 905,
    "message": "Invaild Email or Password"
}

@app.route('/api/login/', methods=['POST'])
def login():
    responseData = request.get_json()
    with open("accounts.json") as file:
        userAccount = json.load(file)
    if(userAccount != []):
        for data in userAccount:
            if(data['email'] == responseData['email'] and data['password'] == responseData['password']):
                print(data['email'] + ',' + data['password'])
                return loginData
    return loginError

@app.route('/api/categories/', methods=['GET'])
def categories():
    with open("categories.json", "r") as file:
        appData = json.load(file)
        return appData


@app.route('/api/register/', methods = ['POST'])
def register():
    def isExist(data, email):
        for dict in data:
            if dict.get('email') == email:
                return True
        return False
    reqData = request.get_json()
    with open("accounts.json", "r") as file:
        read_data = json.load(file)
    if not isExist(read_data, reqData['email']):
        acc = {
            'email' : reqData['email'],
            'password' : reqData['password']
        }
        with open("accounts.json", "r") as file:
            daa = json.load(file)
        daa.append(acc)    
        with open("accounts.json", "w") as file:
            json.dump(daa, file, indent=2)
        return register_success
    return ({"status": "ERROR",
            "code": 910,
            "message": "Email Exist"})
    
# @app.route('/api/otp', methods=['GET'])
# def otp():
#     client = vonage.Client(key="05c55fc9", secret="JqWUbezjFL8Azp72")
#     sms = vonage.Sms(client)
#     otp = random.randint(1000, 9999)
#     responseData = sms.send_message(
#     {
#         "from": "Vonage APIs",
#         "to": "919342602060",
#         "text": otp,
#     }
#     )

#     if responseData["messages"][0]["status"] == "0":
#         return "OTP sent"
#     else:
#        return(f"Message failed with error: {responseData['messages'][0]['error-text']}")

if __name__ == '__main__':
    app.run(debug=False, host="0.0.0.0")



