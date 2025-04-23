# Minicurl: A Simplified `curl`-Like Tool for HTTP Requests

**Minicurl** is a simple Python-based tool designed to mimic the behavior of `curl` for making HTTP requests. It allows users to send `GET` and `POST` requests with custom headers and data. The tool is ideal for testing APIs, debugging, or automating web interactions without relying on the complexity of full-fledged tools.

## Features

- **GET Requests**: Send HTTP GET requests to any URL.
- **POST Requests**: Send HTTP POST requests with custom data.
- **Custom Headers**: Add custom headers to requests.
- **User-Agent**: Easily set a custom User-Agent string for the requests.
- **Simple and Lightweight**: No external dependencies (just Python).

## Installation

To use **Minicurl**, you need Python 3.x installed on your system.

### 1. Clone the repository:

```bash
git clone https://github.com/braybraylon/minicurl.git
cd minicurl
2. Install dependencies:
Minicurl does not require any third-party dependencies beyond the standard Python library. However, ensure you have Python 3.x installed.

bash
Copy
Edit
# If you're using a virtual environment (recommended):
python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
Now you’re ready to run Minicurl.

Usage
Basic Usage:
To use Minicurl, run the minicurl.py script from the command line. You can specify the HTTP method (GET or POST), add custom headers, and send data with POST requests.

bash
Copy
Edit
python minicurl.py <URL> [OPTIONS]
Options:
-X, --request: Specifies the HTTP method (GET, POST).

Default: GET

-d, --data: Data to send with a POST request. This is required for POST requests.

-H, --header: Custom headers to add to the request. You can specify multiple headers.

Example: -H "Content-Type: application/json" -H "Authorization: Bearer token"

--user-agent: (Optional) Specify a custom User-Agent string.

Examples:
1. Send a GET Request:
bash
Copy
Edit
python minicurl.py https://jsonplaceholder.typicode.com/posts
This will send a GET request to https://jsonplaceholder.typicode.com/posts and print the response code and body.

2. Send a POST Request with Data:
bash
Copy
Edit
python minicurl.py https://jsonplaceholder.typicode.com/posts -X POST -d '{"title": "foo", "body": "bar", "userId": 1}'
This sends a POST request with JSON data to the specified URL.

3. Send a POST Request with Custom Headers:
bash
Copy
Edit
python minicurl.py https://jsonplaceholder.typicode.com/posts -X POST -d '{"title": "foo"}' -H "Authorization: Bearer yourtoken"
This sends a POST request with custom headers (such as Authorization).

4. Send a GET Request with a Custom Header:
bash
Copy
Edit
python minicurl.py https://jsonplaceholder.typicode.com/posts -H "Custom-Header: custom_value"
This sends a GET request to the specified URL with a custom header.

Output:
The tool will display the response code and the first part of the response body (up to 200 characters). If an error occurs, it will display the error message.

bash
Copy
Edit
Response Code: 200
Response Body: [{"userId": 1, "id": 1, "title": "delectus aut au...
Requirements
Python 3.x

No external libraries required.

Development
Feel free to contribute to Minicurl. If you want to improve the tool or add new features, follow these steps:

1. Fork the repository.
Go to the Minicurl GitHub Repository and fork the project.

2. Clone your fork.
bash
Copy
Edit
git clone https://github.com/braybraylon/minicurl.git
cd minicurl
3. Make your changes.
Modify the code and add features. For example, you could add support for additional HTTP methods, improve error handling, or add logging capabilities.

4. Run Tests.
If you add new features or make changes, be sure to test the tool thoroughly.

5. Commit and Push Changes.
After making your changes, commit them:

bash
Copy
Edit
git add .
git commit -m "Added feature X"
git push origin main
6. Create a Pull Request.
Go to your repository on GitHub and create a pull request.

License
Minicurl is licensed under the MIT License. See the LICENSE file for more information.
