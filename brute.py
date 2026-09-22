import pexpect
import time
from dotenv import load_dotenv
import os


# Load secret password from .env
load_dotenv()
SUDO_PASSWD = os.getenv("SUDO_PASSWD")

with open('passwords.txt', "r") as file:
    passwords = file.readlines()

counter = 1
for password in passwords:
    password = password.strip()

    print(counter)
    print(f"Trying:.... {password}")

    child = pexpect.spawn('sudo firmwarepasswd -delete')

    # Wait for the sudo password prompt and enter the password
    child.expect('Password:')
    child.sendline(SUDO_PASSWD)

    # Enter the current firmware password
    child.expect('Enter password:')
    child.sendline(password)

    # Wait for the password to finish and capture the output
    child.expect(pexpect.EOF)
    output = child.before.decode()
    print(f"\n{output}\n")

    child.close()
    time.sleep(0.1)
    counter += 1
