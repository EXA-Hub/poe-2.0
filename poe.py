import os
import poe
import json

client = poe.Client("TOKEN")

message = "Summarize the GNU GPL v3"
for chunk in client.send_message("capybara", message):
  print(chunk["text_new"], end="", flush=True)
  
# message = "Summarize the GNU GPL v3"
# for chunk in client.send_message("capybara", message):
#   print(chunk["text_new"], end="", flush=True)