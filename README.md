<br />
<div align="center">
  <h3 align="center">Media Search</h3>
</div>

<details>
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#about">About</a></li>
    <li><a href="#features">Features</a></li>
    <li><a href="#tech-stack">Tech Stack</a></li>
    <li><a href="#instructions-on-running-project-locally">Instructions on Running Project Locally</a></li>
    <li><a href="#use-cases">Use Cases</a></li>
    <li><a href="#feedback">Feedback</a></li>
  </ol>
</details>


## About

The **Media Search** is designed to automatically analyze video footage from security videos. By detecting and highlighting key events such as accident, unauthorized access, or suspicious activities, it helps security personnel or security operators to quickly identify critical moments in video footage. 

This tool saves time and improves efficiency in video monitoring, making it a must have for both personal and professional security needs. Generate automated documentation of security incidents for records or reports for the detected events.

## Features

🎯 **Event Detection with Search**: Automatically detect key events such as accident, intrusion, and unusual behavior by search prompt.

🔍 **Anomaly Highlighting**: The tool analyzes the footage and highlights abnormal activities.

🧠 **AI Driven Insights Report**: Accurate and efficient security analysis report.

## Tech Stack

- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Flask, Python
- **AI Engine**: Integration with Twelve Labs SDK (Marengo 2.6 and Pegasus 1.1)
- **Deployment**: Render

## Instructions on Running Project Locally

To run the **Media Search** locally, follow these steps -

### Step 1 - Clone the Project

```bash
git clone https://github.com/Roman08121995/Twelve-Labs-Security-Analysis.git
```

Install Dependencies

```
 cd Twelve-Labs-Security-Aanlysis
 
 pip install -r requirements.txt
```

Prepare the .emv file as per the instrcution. The .env file is provided below

```
API_KEY = "<Your API Key>"
INDEX_ID = "<Your Index ID>"
```

To Run the Server Locally

```
python app.py
```

The application is live at -

```
http://127.0.0.1:5000/
```

## Usecases

📽️ **Security Operators** : Automate video analysis to detect events such as unauthorized access, break-ins, or other security breaches.

📊 **Security Analytics** : Leverage historical footage of CCTV videos to detect the events and generate the report to improve incident response times.

🔒 **Private Security** : Analyze private security camera footage for events like trespassing or package theft.

📋 **Automated Documentation and Report Generation** :
Generate automated documentation of security incidents for records or reports.

⚖️ **Legal Evidence Review**
For law enforcement, security footage analysis can assist in reviewing evidence from incidents or crimes. The tool can highlight important segments of video footage that might be relevant for the usecase.

🚗 **Traffic Security and Management**
Monitor traffic footage to detect violations, accidents, or abnormal traffic conditions. This is particularly useful for cities or transportation agencies that need to track traffic patterns, accidents, and enforcement of traffic laws.

## Feedback

If you have any feedback, please reach out to us at **roman.business0812@gmail.com**
