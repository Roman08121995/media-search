<br />
<div align="center">
  <h3 align="center">Media Search</h3>
</div>

<details>
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#tech-stack">Tech Stack</a></li>
    <li><a href="#instructions-on-running-project-locally">Instructions on Running Project Locally</a></li>
  </ol>
</details>

## Tech Stack

- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Flask, Python
- **AI Engine**: Integration with Twelve Labs SDK (Marengo 2.6 and Pegasus 1.1)

## Instructions on Running Project Locally

To run the **Media Search** locally, follow these steps -

### Step 1 - Clone the Project

Install Dependencies

``` 
 pip install -r requirements.txt
```

Prepare the .env file as per the instrcution. The .env file is provided below

```
API_KEY = "<Your API Key>"
INDEX_ID = "<Your Index ID>"
```
Extract sa_interview_assets.zip in .../sample path and Upload these media files in your IndexID

To Run the Server Locally

```
python app.py
```

The application is live at -

```
http://127.0.0.1:5000/
```
