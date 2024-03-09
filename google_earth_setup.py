import ee

'''
IMPORTANT:
Run this script to allow your computer to access 
the project through your google account
'''

# Trigger the authentication flow.
ee.Authenticate()

# Initialize the library.
ee.Initialize(project='hackathon-416702')