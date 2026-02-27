# turfbook
# 🏟 Turf Booking Application

A Flask-based Turf Booking web application containerized using Docker and integrated with a Jenkins CI pipeline for automated Docker image builds and deployment to Docker Hub.

---

# 📌 Project Overview

This project demonstrates:

- Python (Flask) web application development
- Docker containerization
- Jenkins Continuous Integration (CI)
- Automated Docker image build and push
- Docker Hub registry integration
- End-to-end CI workflow

---

# 🏗 Tech Stack

- Python (Flask)
- Docker
- Jenkins
- GitHub
- Docker Hub

---

# 📂 Project Structure
.
├── app.py
├── requirements.txt
├── Dockerfile
├── Jenkinsfile
├── templates/
├── static/
└── README.md

---

# 🐳 DOCKER SETUP

## 1️⃣ Install Docker

Download and install Docker Desktop:

https://www.docker.com/products/docker-desktop/

Verify installation:

```bash
docker --version

2️⃣ Build Docker Image (Manual Method)
```bash
docker build -t turf-booking .

3️⃣ Run Application Locally
```bash
docker run -d -p 5000:5000 turf-booking


3️⃣ Run Application Locally
```bash
docker run -d -p 5000:5000 turf-booking

🌍 Run Directly From Docker Hub
Prebuilt Docker image:

abdulfaizudeen/turf-booking:latest
Run without cloning the repository:

docker pull abdulfaizudeen/turf-booking:latest
docker run -d -p 5000:5000 abdulfaizudeen/turf-booking

🔁 JENKINS CI PIPELINE SETUP
1️⃣ Run Jenkins Using Docker
docker run -d -p 8080:8080 -p 50000:50000 \
-v /var/run/docker.sock:/var/run/docker.sock \
-v jenkins_home:/var/jenkins_home \
--name jenkins --user root jenkins/jenkins:lts-jdk17
2️⃣ Install Docker Inside Jenkins Container
docker exec -it jenkins bash
apt update
apt install -y docker.io
exit
Verify Docker inside Jenkins:

docker exec -it jenkins docker --version
3️⃣ Unlock Jenkins
Open:

http://localhost:8080
Get initial password:

docker logs jenkins
Install suggested plugins and create admin user.

4️⃣ Add Docker Hub Credentials in Jenkins
Go to:

Manage Jenkins → Credentials → System → Global Credentials → Add Credentials

Configure:

Kind: Username with password

ID: dockerhub-creds

Username: your Docker Hub username

Password: your Docker Hub password

Save credentials.

5️⃣ Create Jenkins Pipeline Job
Click New Item

Name: turf-booking-pipeline

Select: Pipeline

Choose: Pipeline script from SCM

SCM: Git

Repository URL:

https://github.com/subash016-stack/turfbook.git
Branch:

*/main
Save
