''''
4. Application Health Checker:

Please write a script that can check the uptime of an application and
determine if it is functioning correctly or not. The script must accurately
assess the application's status by checking HTTP status codes. It should be
able to detect if the application is 'up', meaning it is functioning correctly, or
'down', indicating that it is unavailable or not responding.
'''

''' Script owner -> Deepa Shelar [deepashelar7@gmail.com] '''


import requests
import logging
import time

# Set up logging
logging.basicConfig(filename='app_health.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Application URL to check
APPLICATION_URL = 'https://tour2tech.com/'

# Time interval between checks (in seconds)
CHECK_INTERVAL = 60

def check_application_health(url):
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            logging.info(f'Application is UP. Status code: {response.status_code}')
            return 'UP'
        else:
            logging.warning(f'Application is DOWN. Status code: {response.status_code}')
            return 'DOWN'
    except requests.exceptions.RequestException as e:
        logging.error(f'Application is DOWN. Error: {e}')
        return 'DOWN'

def main():
    logging.info('Application Health Checker Script Started')

    while True:
        status = check_application_health(APPLICATION_URL)
        logging.info(f'Application status: {status}')

        # Wait for the specified interval before checking again
        time.sleep(CHECK_INTERVAL)

if __name__ == '__main__':
    main()
