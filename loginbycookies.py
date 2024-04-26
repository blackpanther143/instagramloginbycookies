import instaloader
import os
from datetime import datetime

username = ""
sessionid = ""
csrftoken = ""
if username == "":
    username = input("username=")
if sessionid == "":
    username = input("sessionid=")
if sessionid == "":
    username = input("sessionid=")
if csrftoken == "":
    username = input("csrftoken=")
L = instaloader.Instaloader()
L.compress_json = False
L.load_session(username, {"sessionid": sessionid, "csrftoken": csrftoken})
L.save_session_to_file("cookies.txt")
if L.context.is_logged_in:
    print(f"Logged as {username}")
else:
    print("An error occurred while logging into the account.")
with open("sessioncookie.txt", "wb") as f:
    L.context.save_session_to_file(f)
with open("sessioncookie.txt", "rb") as f:
    L.context.load_session_from_file(username, f)
user = username
profile = instaloader.Profile.from_username(L.context, username=user)
os.makedirs(user, exist_ok=True)
os.chdir(user)
L.download_profile(user, username)
