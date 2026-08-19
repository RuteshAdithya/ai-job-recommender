# AI Job Recommender

A Streamlit application that analyses a PDF resume, identifies skill gaps, suggests a career roadmap, and finds matching job listings from LinkedIn and Naukri.

## Setup

1. Install the dependencies: `pip install -r requirements.txt`
2. Create a `.env` file with:

   ```env
   GROQ_API_KEY=your_groq_key
   APIFY_API_TOKEN=your_apify_token
   ```

3. Start the application: `streamlit run app.py`

## Notes

- Only text-based PDFs under 5 MB are supported. Scanned resumes need OCR first.
- Resume data is sent to Groq for analysis; use only documents you are permitted to share.
- Job results come from third-party Apify actors. Their availability and result fields can change.

## MCP server

To expose the LinkedIn and Naukri searches to an MCP-compatible client, run:

```bash
python mcp_server.py
```

## Deploy to Streamlit Community Cloud

1. Create an empty GitHub repository (for example, `ai-job-recommender`).
2. In this project folder, run the following commands. Replace `YOUR_USERNAME` with your GitHub username:

   ```bash
   git init
   git add .
   git commit -m "Initial AI Job Recommender release"
   git branch -M main
   git remote add origin https://github.com/YOUR_USERNAME/ai-job-recommender.git
   git push -u origin main
   ```

3. In Streamlit Community Cloud, create a new app from that repository and select `app.py` as the entry file.
4. In the app's **Secrets** settings, add `GROQ_API_KEY` and `APIFY_API_TOKEN`. Never commit your `.env` file.
