import frappe
from frappe import auth

# Allow public access via API
@frappe.whitelist(allow_guest=True)
def login(username, password):
    """
    Authenticates user and returns session ID, API key, API secret, username, and email.
    """
    try:
        # Authenticate user
        login_manager = frappe.auth.LoginManager()
        login_manager.authenticate(user=username, password=password)
        login_manager.post_login()
    except frappe.exceptions.AuthenticationError:
        # Handle login failure
        frappe.clear_messages()
        frappe.local.response["message"] = {
            "success_key": 0,
            "message": "Login Authentication Error!"
        }
        return

    # Generate API key/secret
    api_generate = generate_keys(frappe.session.user)
    user = frappe.get_doc('User', frappe.session.user)

    # Send success response with session info
    frappe.response["message"] = {
        "success_key": 1,
        "message": "Login Authentication Successful!",
        "session_id": frappe.session.session_id,
        "api_key": user.api_key,
        "api_secret": api_generate,
        "username": user.username,
        "email": user.email
    }

def generate_keys(user):
    """
    Generates API key and secret for a user if not already present.
    """
    user_details = frappe.get_doc('User', user)
    api_secret = frappe.generate_hash(length=15)

    # Create API key if missing
    if not user_details.api_key:
        api_key = frappe.generate_hash(length=15)
        user_details.api_key = api_key

    user_details.api_secret = api_secret
    user_details.save()

    return api_secret
