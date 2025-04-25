# flask_app
Flask Web Application

This is a simple multi-page web application developed using the Flask framework. It was deployed and tested inside a VirtualBox-hosted Ubuntu Linux VM.

Framework Used

-Flask (Python Web Framework)

-HTML/CSS with external styling via a custom CSS file


How to Run the Project
Requirements
- Python 3
- VirtualBox + Ubuntu Linux VM
- pip
- Flask

Setup Steps
1. Clone or unzip the project directory inside your Ubuntu VM.
2. In Ubuntu VM terminal:
   ```bash
   sudo apt update && sudo apt upgrade
   ```
   ```bash
   sudo apt install python3-pip
   ```
   ```bash
   sudo apt install python3-flask && sudo apt install python3-django
   ```
4. Configure firewall to allow port 5000 in the terminal:
   ```bash
   sudo ufw allow 5000
   ```
5. In the terminal, go to the project directory and run the app:
   ```bash
   cd <directory-of-flask_app> #cd flask_app
   export FLASK_APP=app.py && flask run --host=0.0.0.0 --port=5000
   ```
   It should show that the website is running.

The web app will be available at:
  ```cpp
  http://<VM-IP>:5000
  ```

You can get your VM IP using:
  ```bash
  ip a
  ```

Issues Encountered and Solutions
1. Permission Error: pip install
Issue: externally-managed-environment error.
Solution: Used "sudo apt install python3-flask && sudo apt install python3-django" in terminal
2. Web app not accessible from host
Issue: App ran, but couldn't access it via browser on the host machine.
Solution: Ensured Flask runs on host='0.0.0.0', allowed port 5000 through ufw, and used a bridged adapter.


Developer

Jave Danielle M. Gamboa

