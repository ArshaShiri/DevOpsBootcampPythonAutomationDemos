import requests
import smtplib
import os
import paramiko
import linode_api4
import time
import schedule

# These environment variables should be set
EMAIL_ADDRESS = os.environ.get('EMAIL_ADDRESS')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD')
LINODE_TOKEN = os.environ.get('LINODE_TOKEN')


def restart_server_and_container():
    # restart linode server
    print('Rebooting the server...')
    client = linode_api4.LinodeClient(LINODE_TOKEN)

    # Linode ID: 46883764
    nginx_server = client.load(linode_api4.Instance, 46883764)
    nginx_server.reboot()

    # Restart the application
    while True:
        nginx_server = client.load(linode_api4.Instance, 46883764)
        if nginx_server.status == 'running':
            time.sleep(5)
            restart_container()
            break


# Set sending using email from gmail
def send_notification(email_msg):
    print('Sending an email...')
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        # Communication encryption
        smtp.starttls()
        smtp.ehlo()
        
        # Make sure that gmail is also configured for connection from this application
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        message = f"Subject: SITE DOWN\n{email_msg}"
        smtp.sendmail(EMAIL_ADDRESS, EMAIL_ADDRESS, message)


def restart_container():
    print('Restarting the application...')
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname='172.105.80.40', username='root', key_filename='/Users/arsha/.ssh/id_rsa')
    stdin, stdout, stderr = ssh.exec_command('docker start 6e7a334211ba')
    print(stdout.readlines())
    ssh.close()


def monitor_application():
    try:
        response = requests.get('http://172-105-80-40.ip.linodeusercontent.com:8080/')
        if response.status_code == 200:
            print('Application is running successfully!')
        else:
            print('Application Down. Fix it!')
            msg = f'Application returned {response.status_code}'
            send_notification(msg)
            restart_container()
    except Exception as ex:
        print(f'Connection error happened: {ex}')
        msg = 'Application not accessible at all'
        send_notification(msg)
        restart_server_and_container()


schedule.every(5).minutes.do(monitor_application)

while True:
    schedule.run_pending()