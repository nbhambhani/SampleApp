from ConfigParser import SafeConfigParser
import os.path 

def get_filepath(relative_filepath):
    my_path = os.path.abspath(os.path.dirname(__file__))
    path = os.path.join(my_path, relative_filepath)
    return path

config_file = get_filepath('../config.ini')

parser = SafeConfigParser()
parser.read(config_file)

def get_consumer_tokens():
    consumer_token = {}
    consumer_token['consumer_key'] = parser.get('Tokens', 'consumer_key')
    consumer_token['consumer_sec'] = parser.get('Tokens', 'consumer_sec')
    return consumer_token

def get_oauth_urls():
	oauth_url = {}
	oauth_url['base_url'] = parser.get('OAuth URLs', 'base_url')
	oauth_url['request_token_url'] = parser.get('OAuth URLs', 'request_token_url')
	oauth_url['access_token_url'] = parser.get('OAuth URLs', 'access_token_url')
	oauth_url['authorize_url'] = parser.get('OAuth URLs', 'authorize_url')
	return oauth_url

def get_api_url():
	return parser.get('API URL', 'base_url')

def get_minorversion(minorversion):
	return '?minorversion='+str(minorversion)
	


