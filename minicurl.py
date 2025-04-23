import argparse
import urllib.request
import json
import sys
import time

# Function to handle GET request
def handle_get(url, headers):
    req = urllib.request.Request(url, headers=headers, method="GET")
    try:
        with urllib.request.urlopen(req) as response:
            response_body = response.read().decode(errors='replace')
            print(f"Response Code: {response.getcode()}")
            print(f"Response Body: {response_body[:200]}")  # Print only the first 200 chars
            return response
    except Exception as e:
        print(f"Error: {e}")
        return None

# Function to handle POST request
def handle_post(url, headers, data):
    req = urllib.request.Request(url, data=data.encode(), headers=headers, method="POST")
    try:
        with urllib.request.urlopen(req) as response:
            response_body = response.read().decode(errors='replace')
            print(f"Response Code: {response.getcode()}")
            print(f"Response Body: {response_body[:200]}")  # Print only the first 200 chars
            return response
    except Exception as e:
        print(f"Error: {e}")
        return None

# Function to handle headers and formatting
def handle_headers(headers):
    formatted_headers = {}
    for header in headers:
        if ":" in header:
            key, value = header.split(":", 1)
            formatted_headers[key.strip()] = value.strip()
    return formatted_headers

# Main function to parse arguments and send requests
def main():
    parser = argparse.ArgumentParser(description="Minicurl: A simplified curl-like tool for making HTTP requests.")
    parser.add_argument('url', type=str, help='The URL to send the request to')
    parser.add_argument('-X', '--request', choices=['GET', 'POST'], default='GET', help='Specify the request type (default: GET)')
    parser.add_argument('-d', '--data', type=str, help='Data to send in a POST request')
    parser.add_argument('-H', '--header', action='append', help='Custom header to send with the request')
    
    args = parser.parse_args()

    headers = {'User-Agent': 'Minicurl/1.0'}
    
    # Handle additional headers
    if args.header:
        headers.update(handle_headers(args.header))
    
    # Request method logic
    if args.request == "GET":
        handle_get(args.url, headers)
    elif args.request == "POST":
        if not args.data:
            print("Error: POST request requires data (-d <data>)")
            sys.exit(1)
        handle_post(args.url, headers, args.data)

if __name__ == "__main__":
    main()
