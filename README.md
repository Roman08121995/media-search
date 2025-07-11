<br />
<div align="center">
  <h3 align="center">🔍 Media Search</h3>
</div>

<details>
  <summary>📑 Table of Contents</summary>
  <ol>
    <li><a href="#tech-stack">Tech Stack</a></li>
    <li><a href="#getting-started">Getting Started</a></li>
    <li><a href="#environment-variables">Environment Variables</a></li>
    <li><a href="#run-the-server">Run the Server</a></li>
  </ol>
</details>

## 🧰 Tech Stack

- **Frontend**: HTML, CSS, JavaScript  
- **Backend**: Flask, Python  
- **AI Engine**: Twelve Labs SDK  
  - Marengo 2.6  
  - Pegasus 1.1  

## 🚀 Getting Started

To run the **Media Search** locally, follow these steps:

### Step 1 - Clone the Project

```bash
git clone https://github.com/Roman08121995/media-search.git
cd media-search
```

### Step 2 - Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 3 - Prepare Assets

- Extract `sa_interview_assets.zip` into the `./sample` directory.
- Upload the extracted media files to your Twelve Labs Index.

## 🔐 Environment Variables

Create a `.env` file in the root directory with the following variables:

```env
API_KEY = "<Your API Key>"
INDEX_ID = "<Your Index ID>"
```

## ▶️ Run the Server

Start the Flask development server:

```bash
python app.py
```

The application will be available at:

```
http://127.0.0.1:5000/
```
