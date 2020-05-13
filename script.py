with open('welcome.txt') as text_file:
  text_data = text_file.read()
print(text_data)

with open('how_many_lines.txt') as lines_doc:
  for line in lines_doc.readlines():
    print(line)

with open('just_the_first.txt') as first_line_doc:
  first_line = first_line_doc.readline()
  print(first_line)

with open('bad_bands.txt', 'w') as bad_bands_doc:
  bad_bands_doc.write("Hoozer")

with open('cool_dogs.txt', 'a') as cool_dogs_file:
  cool_dogs_file.write("Air Buddy")

with open('fun_file.txt') as close_this_file:

  setup = close_this_file.readline()
  punchline = close_this_file.readline()

print(setup)

with open("logger.csv") as log_csv_file:
  print(log_csv_file.read())

# If newline='' is not specified, newlines embedded inside quoted 
# fields will not be interpreted correctly, and on platforms that use \r\n 
# linendings on write an extra \r will be added. It should always be safe 
# to specify newline='', since the csv module does its own (universal) 
# newline handling.

import csv

with open("cool_csv.csv") as cool_csv_file:
  cool_csv_dict = csv.DictReader(cool_csv_file)
  for row in cool_csv_dict:
    print(row.get("Cool Fact"))

import csv
isbn_list = []
with open("books.csv") as books_csv:
  books_reader = csv.DictReader(books_csv, delimiter="@")
  for books in books_reader:
    isbn_list.append(books.get("ISBN"))
  
#
#Making a csv 

import csv

access_log = [{'time': '08:39:37', 'limit': 844404, 'address': '1.227.124.181'}, {'time': '13:13:35', 'limit': 543871, 'address': '198.51.139.193'}, {'time': '19:40:45', 'limit': 3021, 'address': '172.1.254.208'}, {'time': '18:57:16', 'limit': 67031769, 'address': '172.58.247.219'}, {'time': '21:17:13', 'limit': 9083, 'address': '124.144.20.113'}, {'time': '23:34:17', 'limit': 65913, 'address': '203.236.149.220'}, {'time': '13:58:05', 'limit': 1541474, 'address': '192.52.206.76'}, {'time': '10:52:00', 'limit': 11465607, 'address': '104.47.149.93'}, {'time': '14:56:12', 'limit': 109, 'address': '192.31.185.7'}, {'time': '18:56:35', 'limit': 6207, 'address': '2.228.164.197'}]
fields = ['time', 'address', 'limit']

with open("logger.csv", "w") as logger_csv:
  log_writer = csv.DictWriter(logger_csv, fieldnames=fields)
  log_writer.writeheader()
  for log in access_log:
    log_writer.writerow(log)

import json

with open("message.json") as message_json:
  message = json.load(message_json)
  print(message)
  print(message['text'])

import json

data_payload = [
  {'interesting message': 'What is JSON? A web application\'s little pile of secrets.',
   'follow up': 'But enough talk!'}
]

with open("data.json", "w") as data_json:
  json.dump(data_payload, data_json)

#
# Project
#

import csv 
import json

compromised_users = []
with open("passwords.csv") as password_file:
  password_csv = csv.DictReader(password_file)
  for password_row in password_csv:
    compromised_users.append(password_row['Username'])

fields = ['username']

with open("compromised_users.txt", "w") as compromised_user_file:
  writer = csv.writer(compromised_user_file)
  for compromised_user in compromised_users:
    writer.writerow(compromised_user)

with open("boss_message.json", "w") as boss_message:
  boss_message_dict = {
    "recipient": "The Boss",
    "message": "Mission Success"
  }
  json.dump(boss_message_dict ,boss_message)

slash_null_sig = """
 _  _     ___   __  ____             
/ )( \   / __) /  \(_  _)            
) \/ (  ( (_ \(  O ) )(              
\____/   \___/ \__/ (__)             
 _  _   __    ___  __ _  ____  ____  
/ )( \ / _\  / __)(  / )(  __)(    \ 
) __ (/    \( (__  )  (  ) _)  ) D ( 
\_)(_/\_/\_/ \___)(__\_)(____)(____/ 
        ____  __     __   ____  _  _ 
 ___   / ___)(  )   / _\ / ___)/ )( \
(___)  \___ \/ (_/\/    \\___ \) __ (
       (____/\____/\_/\_/(____/\_)(_/
 __ _  _  _  __    __                
(  ( \/ )( \(  )  (  )               
/    /) \/ (/ (_/\/ (_/\             
\_)__)\____/\____/\____/
"""
  
with open("new_passwords.csv", "w") as new_passwords_obj:
  new_passwords_obj.write(slash_null_sig)
