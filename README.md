# Code Explain API

An AI-powered backend service that analyzes code and returns structured insights such as explanation, complexity, concepts, and improvements.

Built using **FastAPI + OpenAI API**, this project transforms raw code into meaningful developer-friendly analysis.

---

## Live Demo

https://code-explain-api.onrender.com

---

##  Features

*  Explain code in simple terms
*  Analyze time & space complexity
*  Extract key concepts used
*  Suggest improvements
*  Structured JSON output
*  FastAPI backend with clean design
*  Deployed and publicly accessible

---

## Tech Stack

* **Backend:** FastAPI
* **AI Integration:** OpenAI API
* **Validation:** Pydantic
* **Environment Management:** python-dotenv
* **Deployment:** Render

---

## Project Structure

```id="o3y9qb"
code-explain-api/
│
├── main.py              # API routes and logic
├── requirements.txt
├── start.sh
├── .env                # (not committed)
└── .gitignore
```

---

## API Endpoints

### Health Check

```id="7mcb4r"
GET /
```

---

### Explain Code

```id="4ogd9g"
POST /explain
```

---

### Request Body

```json id="jplg1c"
{
  "code": "for(int i=0;i<n;i++){sum+=i;}"
}
```

---

### Response

```json id="s3k2ov"
{
  "status": "success",
  "analysis": {
    "summary": "Iterates from 0 to n-1 and accumulates the sum.",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "concepts": ["loop", "iteration"],
    "improvements": "Consider using a formula for faster computation."
  }
}
```

---

## ⚙️ Setup Locally

### 1. Clone repository

```id="wq5g6y"
git clone <your-repo-url>
cd code-explain-api
```

---

### 2. Create virtual environment

```id="cptx2u"
python -m venv venv
venv\Scripts\activate   # Windows
```

---

### 3. Install dependencies

```id="db3b1u"
pip install -r requirements.txt
```

---

### 4. Add environment variable

Create `.env`:

```id="x4t8l9"
OPENAI_API_KEY=your_api_key_here
```

---

### 5. Run server

```id="fl8w7q"
uvicorn main:app
```

---

### 6. Open Swagger UI

```id="9b7r3p"
http://127.0.0.1:8000/docs
```

---

## Deployment (Render)

* Push code to GitHub
* Create Web Service on Render
* Set environment variable:

```id="envrender"
OPENAI_API_KEY = your_api_key
```

* Build command:

```id="buildcmd"
pip install -r requirements.txt
```

* Start command:

```id="startcmd"
bash start.sh
```

---

## Key Learnings

* Integrating external APIs into backend systems
* Handling unstructured AI responses
* Prompt engineering for structured output
* Building production-ready APIs
* Debugging environment and deployment issues

---

## Future Improvements

* Language detection
* Code complexity visualization
* Batch code analysis
* Authentication (API keys for users)
* Rate limiting (integrate previous project)

---

## 🏁 Conclusion

This project demonstrates the ability to build intelligent backend services by combining API design with AI-powered analysis.

---

⭐ If you like this project, consider giving it a star!
