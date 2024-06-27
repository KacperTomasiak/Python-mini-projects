from algosdk import account, mnemonic
import time
import signal
import sys

pattern = ""
count = 0
start_time = time.time()

generated_account = {
  "address": "",
  "private_key": "",
  "secret_phrase": ""
}

def generate_address(address, private_key):
  generated_account["address"] = address
  generated_account["private_key"] = private_key
  generated_account["secret_phrase"] = mnemonic.from_private_key(private_key)

def check_account(address):
  if address.startswith(pattern):
    return True
  else:
    return False

def exit(signum, frame):
  print()
  print(f"Exited after {count} attempts and {round(time.time() - start_time, 2)}s")
  sys.exit()

def print_details():
  print(f"Address: {generated_account['address']}")
  print(f"Private key: {generated_account['private_key']}")
  print(f"Secret phrase: {generated_account['secret_phrase']}")
  print(f"Account found after: {count} attempts and {round(time.time() - start_time, 2)}s")

print("Running...")
signal.signal(signal.SIGINT, exit)

while True:
  private_key, address = account.generate_account()
  count += 1
  if check_account(address) == True:
    generate_address(address, private_key)
    break

print_details()