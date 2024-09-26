# erpnext-api-authentication

This repository provides API functionalities for user authentication and password management in ERPNext.

## Features

- **Generate Session ID**: Allows users to authenticate and generate a session ID.

## Requirements

- [ERPNext](https://erpnext.com) installed and running.
- Frappe framework.

## Usage 
## Login API (Generate Session ID and API Keys)

1. Postman Setup (or Other API Platform)

Method: POST
URL: https://your-erpnext-url.com/api/method/<your_custom_app>.login

2. Body Parameters:
Choose x-www-form-urlencoded or form-data in Postman, and add the following parameters:
User (string) - Username or email.
Password (string) - User password.

3. Headers:
You may not need to add any special headers unless your ERPNext instance requires specific headers like Authorization or Content-Type. In most cases, ERPNext handles these internally.

4. Example Request:
Here’s what the setup will look like in Postman:
Select POST as the method.
URL: https://your-erpnext-url.com/api/method/<your_custom_app>.login.
In the Body tab, select x-www-form-urlencoded and add:
User: username
Password: user_password

5. Click Send.

6. Response:
If the authentication is successful, you'll receive a response containing the session_id, api_key, and api_secret in JSON format.

7. Example Success Response:
                                    json
                                    {
                                        "success_key": 1,
                                        "message": "Authentication success",
                                        "session_id": "example-session-id",
                                        "api_key": "example-api-key",
                                        "api_secret": "example-api-secret",
                                        "username": "example_user",
                                        "email": "user@example.com"
                                    }
8. Example Failure Response:
                                    json
                                    {
                                        "success_key": 0,
                                        "message": "Authentication Error!"
                                    }

## Authorization in Postman

If your ERPNext setup uses a session-based login, you may need to pass the session ID in subsequent requests. You can add the session ID in the headers of your requests, using:
Key: session_id
Value: <session_id_from_login_response>
For APIs requiring authorization using the api_key and api_secret, you can pass these as headers or query parameters:
Header 1: Authorization
Value: Token <api_key>:<api_secret>


