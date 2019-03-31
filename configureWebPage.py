import re
import os

SEC_SETTINGS_DIR = 'web/src/delcien/sec_settings.py'

def configure():
	string = ''
	email = ''
	password = ''
	secretKey = ''

	emailRegex = r'[a-z,A-Z,.]+@[a-z,A-Z]+\.[a-z,A-Z,.]+[a-z,A-Z]+$'
	pattern = re.compile(emailRegex)
	while True:
		string = input('Enter an email account for the web page > ')
		if len(string) > 0 and re.match(pattern,string) is not None:
			email = string
			break

	while True:
		string = input('Enter the email password > ')
		if len(string) > 0:
			password = string
			break

	while True:
		string = input('Enter some text for the secret key > ')
		if len(string) > 0:
			secretKey = string
			break

	print(f'email : {email}\npsswd : {password}\nsecret key : {secretKey}')
	string = input('Do you want to use this configuration? [Y]es > ')

	if len(string) > 0 and string.lower()=='y':
		configuration = '''
import os

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
        },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
        },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
        },
]
	
		''' + f"\nEMAIL_HOST_USER = '{email}' \nEMAIL_HOST_PASSWORD = '{password}' \nSECRET_KEY = '{secretKey}'"

		if os.path.exists(SEC_SETTINGS_DIR):
		  os.remove(SEC_SETTINGS_DIR)
		
		with open(SEC_SETTINGS_DIR, 'w') as f:
			f.write(configuration)

def check_configuration():
	if os.path.exists(SEC_SETTINGS_DIR):
		with open(SEC_SETTINGS_DIR, 'r') as f:
			for line in f:
				print(line, end='')
	else:
		print('No configuration file available\n')


def showMenu():
	print('\nServer security options configuration\n(06/12/2018)\n[C]onfigure \nchec[K] status \n[E]xit\n')

def __main__():
	options = dict(C=configure, K=check_configuration, E=exit)
	while True:
		showMenu()
		option = input('> ')
		if option.upper() in list(options.keys()):
			options[option.upper()]()

__main__()
