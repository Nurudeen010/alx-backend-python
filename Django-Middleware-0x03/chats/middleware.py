import datetime
from datetime import datetime
from django.http import HttpResponseForbidden, JsonResponse
import time

class RequestLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Get the current user (if any)
        user = request.user if request.user.is_authenticated else "Anonymous"
        
        # Log the request details to a file
        with open("requests.log", "a") as log_file:
            log_file.write(f"{datetime.now()} - User: {user} - Path: {request.path}\n")
        
        # Continue processing the request
        response = self.get_response(request)
        return response

class RestrictAccessByTimeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Get the current server time (24-hour format)
        current_hour = datetime.now().hour
        
        # Define restricted hours (outside 6 PM to 9 PM)
        if request.path.startswith("/chats/") and (current_hour < 18 or current_hour >= 21):
            return HttpResponseForbidden("Access to the chat is restricted outside 6 PM to 9 PM.")

        # Allow the request to proceed during allowed hours
        response = self.get_response(request)
        return response

class OffensiveLanguageMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # Dictionary to track message counts and timestamps for each IP
        self.ip_message_log = {}

    def __call__(self, request):
        # Only track POST requests sent to the chat endpoint
        if request.method == "POST" and request.path.startswith("/chats/"):
            # Get the IP address of the user
            ip_address = self.get_client_ip(request)
            
            # Get current time in seconds
            current_time = time.time()
            
            # Initialize or update the IP entry
            if ip_address not in self.ip_message_log:
                self.ip_message_log[ip_address] = []

            # Clean up old timestamps (older than 1 minute)
            self.ip_message_log[ip_address] = [
                timestamp for timestamp in self.ip_message_log[ip_address] 
                if current_time - timestamp <= 60
            ]

            # Check if the user exceeded the message limit (5 messages per minute)
            if len(self.ip_message_log[ip_address]) >= 5:
                return JsonResponse(
                    {"error": "Message limit exceeded. Try again in a minute."}, 
                    status=429
                )

            # Log the current request timestamp
            self.ip_message_log[ip_address].append(current_time)

        # Allow the request to proceed
        response = self.get_response(request)
        return response

    def get_client_ip(self, request):
        """Retrieve the client's IP address from the request headers."""
        x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
        if x_forwarded_for:
            ip = x_forwarded_for.split(",")[0]
        else:
            ip = request.META.get("REMOTE_ADDR")
        return ip

class RolepermissionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Check if the user is authenticated
        if request.user.is_authenticated:
            # Get the user's role from the request (assuming a `role` field exists)
            user_role = getattr(request.user, 'role', None)
            
            # Define restricted paths and roles
            restricted_paths = ["/admin/", "/host/"]
            restricted_roles = ["admin", "host"]

            # Check if the request is for a restricted path
            if request.path in restricted_paths and user_role not in restricted_roles:
                return HttpResponseForbidden("You do not have the required permissions to access this page.")

        # Allow the request to proceed
        response = self.get_response(request)
        return response
