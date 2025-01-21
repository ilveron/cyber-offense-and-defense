import base64
import json

def create_jwt_token(header_str, payload_str):
    # Function to perform base64url encoding
    def base64url_encode(data):
        # Convert to JSON string if input is a string representation
        if isinstance(data, str):
            data = json.loads(data)
        
        # Convert to JSON string
        json_str = json.dumps(data, separators=(',', ':'))
        
        # Encode to base64
        b64_bytes = base64.b64encode(json_str.encode('utf-8'))
        b64_string = b64_bytes.decode('utf-8')
        
        # Make it base64url by replacing characters
        return b64_string.replace('+', '-').replace('/', '_').rstrip('=')

    # Encode header and payload
    encoded_header = base64url_encode(header_str)
    encoded_payload = base64url_encode(payload_str)
    
    # Combine with dots
    token = f"{encoded_header}.{encoded_payload}."
    
    return token

# Example usage
header = '{"alg":"none","typ":"JWT"}'
payload = '{"user":"john","admin":false}'

jwt_token = create_jwt_token(header, payload)
print(jwt_token)