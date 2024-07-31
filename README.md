
# DuckDuckGo Email Combiner

This repository contains the source code for a simple web application that combines multiple email addresses using the DuckDuckGo Email Protection service. The application is hosted on PythonAnywhere and can be accessed [here](https://gingerbreadmat.pythonanywhere.com/).

## Usage

To use the application, follow these steps:

1.  Go to the web address [https://gingerbreadmat.pythonanywhere.com/](https://gingerbreadmat.pythonanywhere.com/).
2.  Enter the email addresses you want to combine in the provided input fields.
3.  Click the "Combine" button to generate the combined email addresses.
4.  Copy the combined email address for use.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contact

For any questions or suggestions, please open an issue on the repository or contact the maintainer.

----------

Visit the application at [https://gingerbreadmat.pythonanywhere.com/](https://gingerbreadmat.pythonanywhere.com/) to start combining your email addresses securely and easily.

# Local Development 

### Prerequisites

-   Python 3.x
-   Flask

### Installation

1.  Clone the repository:

bash

Copy code

`git clone https://github.com/gingerbreadmat/DuckDuckGo-Email-Combiner.git
cd DuckDuckGo-Email-Combiner` 

2.  Create and activate a virtual environment:

bash

Copy code

``python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate` `` 

3.  Install the required packages:

bash

Copy code

`pip install -r requirements.txt` 

### Running the Application Locally

1.  Set the Flask app environment variable:

bash

Copy code

`export FLASK_APP=app.py` 

2.  Run the Flask development server:

bash

Copy code

`flask run` 

3.  Open your web browser and go to `http://127.0.0.1:5000/` to view the application.

### Usage

To use the application, follow these steps:

1.  Go to the web address [https://gingerbreadmat.pythonanywhere.com/](https://gingerbreadmat.pythonanywhere.com/).
2.  Enter the email addresses you want to combine in the provided input fields.
3.  Click the "Combine" button to generate the combined email addresses.
4.  Copy the combined email address for use.

### Deployment

The application is deployed on PythonAnywhere. To deploy your own instance, follow these steps:

1.  Create an account on [PythonAnywhere](https://www.pythonanywhere.com/).
2.  Upload the repository files to your PythonAnywhere account.
3.  Set up a web app on PythonAnywhere using the Flask framework.
4.  Configure the WSGI file to point to your Flask app.
5.  Reload the web app to apply the changes.

For detailed instructions on deploying Flask applications on PythonAnywhere, refer to the official documentation.
