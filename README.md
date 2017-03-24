# Basic data import from Excel to QB
#### Sample App in Python that implements Connect to Quickbooks button and imports customer data from Excel to QB company

This sample app is meant to provide working examples of how to integrate your app with the Intuit Small Business ecosystem. Specifically, this sample application demonstrates the following:

- Implementing OAuth to connect an application to a customer's QuickBooks Online company.
- Creating a QB customer with minimal fields that are added from Excel file.

For example, certain concerns are not addressed at all in our samples (e.g. security, privacy, scalability). In our sample apps, we strive to strike a balance between clarity, maintainability, and performance where we can. However, clarity is ultimately the most important quality in a sample app.

Therefore there are certain instances where we might forgo a more complicated implementation (e.g. caching a frequently used value, robust error handling, more generic domain model structure) in favor of code that is easier to read. In that light, we welcome any feedback that makes our samples apps easier to learn from.

## Requirements
1. Python 2.7
2. A developer.intuit.com account
3. An app on developer.intuit.com and the associated app token, consumer key, and consumer secret
4. This sample app uses several libraries which need to be installed including flask, flask_oauth, ConfigParser, openpyxl, requests_oauthlib  

## First Time Instructions
1. Clone the GitHub repo to your computer
2. Install libraries mentioned above
3. Fill in your config.ini file values (consumer key and consumer secret) by copying over from the keys section for your app

## Running the code
1. cd to the project directory
2. Run the command: ```python app.py``` for MacOS/Linux 
3. open a browser and enter ```http://localhost:5000``` 
