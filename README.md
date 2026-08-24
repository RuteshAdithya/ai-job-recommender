# AI Job Recommender 🤖💼

An intelligent resume analysis and job recommendation application powered by **OpenAI ChatGPT**, **Streamlit**, and **Apify**.

## Features

✨ **AI-Powered Resume Analysis**
- Extract and analyze resume text
- Generate smart resume summary using ChatGPT
- Identify skill gaps and missing certifications
- Create personalized career roadmap

🔍 **Job Recommendations**
- Auto-generate relevant job search keywords
- Fetch jobs from LinkedIn
- Fetch jobs from Naukri (India-focused)
- Display recommendations with company and location info

🎨 **Beautiful UI**
- Modern dark theme design
- Responsive layout
- Real-time processing status
- Easy-to-use file upload

## Tech Stack

- **Frontend:** Streamlit
- **AI Model:** OpenAI ChatGPT (gpt-3.5-turbo)
- **Job Scraping:** Apify
- **PDF Processing:** PyMuPDF
- **Deployment:** Docker, Streamlit Cloud, Heroku

## Installation

### Local Setup

1. **Clone the repository:**
```bash
git clone https://github.com/RuteshAdithya/ai-job-recommender.git
cd ai-job-recommender
```

2. **Create virtual environment:**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies:**
```bash
pip install -r requirements.txt
```

4. **Set up environment variables:**
```bash
cp .env.example .env
```

5. **Add your API keys to `.env`:**
```dotenv
OPENAI_API_KEY=your_openai_api_key_here
APIFY_API_TOKEN=your_apify_token_here
```

6. **Run the app:**
```bash
streamlit run app.py
```

Visit `http://localhost:8501` in your browser.

## Deployment

### Quick Deploy to Streamlit Cloud

1. Push code to GitHub
2. Go to [streamlit.io/cloud](https://streamlit.io/cloud)
3. Connect your repository
4. Add secrets in app settings:
   - `OPENAI_API_KEY`
   - `APIFY_API_TOKEN`
5. Deploy! 🚀

For detailed deployment instructions to other platforms (Heroku, Google Cloud, AWS), see [DEPLOYMENT.md](DEPLOYMENT.md).

## Getting API Keys

### OpenAI API Key
1. Visit [platform.openai.com](https://platform.openai.com)
2. Sign up or log in
3. Go to API keys section
4. Create new secret key
5. Copy and save securely

**Pricing:** ~$0.001-0.01 per request (depends on model and usage)

### Apify Token
1. Visit [apify.com](https://apify.com)
2. Sign up or log in
3. Go to Settings → Integrations
4. Copy your API token
5. Free tier includes job scraping

## Usage

1. **Upload Resume:** Click to upload a PDF resume (max 5 MB)
2. **Wait for Analysis:** App extracts text and analyzes with ChatGPT
3. **Review Insights:**
   - Resume summary
   - Skill gaps
   - Career roadmap
4. **Get Job Recommendations:** Click "Get Job Recommendations" button
5. **Browse Jobs:** View LinkedIn and Naukri job listings
6. **Apply:** Click "View job" links to apply on job platforms

## Project Structure

```
ai-job-recommender/
├── app.py                 # Main Streamlit application
├── src/
│   ├── __init__.py
│   ├── helper.py         # PDF extraction & ChatGPT integration
│   └── job_api.py        # LinkedIn & Naukri job fetching
├── .streamlit/
│   └── config.toml       # Streamlit configuration
├── requirements.txt      # Python dependencies
├── Dockerfile           # Docker container configuration
├── Procfile            # Heroku deployment config
├── setup.sh            # Setup script for Heroku
└── DEPLOYMENT.md       # Deployment guide
```

## Error Handling

The app includes robust error handling for:
- Invalid or corrupted PDF files
- Missing or invalid API keys
- Empty or malformed resume text
- API rate limiting
- Network errors during job scraping

## Performance Tips

- **Faster responses:** Use `gpt-3.5-turbo` (default) instead of `gpt-4`
- **Lower costs:** Reduce `max_tokens` for shorter responses
- **Better accuracy:** Use `gpt-4` for complex analysis (slower, more expensive)
- **Caching:** Results are cached in session state

## Limitations

- PDF must be text-based (not scanned images)
- Maximum resume size: 5 MB
- Maximum resume text: 30,000 characters
- Job scraping depends on Apify actor availability
- API rate limits apply based on your plan

## Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

MIT License - feel free to use for personal and commercial projects.

## Support

- 📧 Email: contact@example.com
- 🐛 Report bugs: [GitHub Issues](https://github.com/RuteshAdithya/ai-job-recommender/issues)
- 💬 Discussions: [GitHub Discussions](https://github.com/RuteshAdithya/ai-job-recommender/discussions)

## Roadmap

- [ ] Add support for multiple resume formats (DOCX, etc.)
- [ ] Support for multiple languages
- [ ] Resume scoring/ranking
- [ ] Job market analytics
- [ ] Email notifications for matching jobs
- [ ] User accounts and saved preferences
- [ ] Resume optimization suggestions

## Changelog

### v1.1.0 (Current)
- ✅ Switched from Groq to OpenAI ChatGPT
- ✅ Added Docker support
- ✅ Added comprehensive deployment guide
- ✅ Improved error messages

### v1.0.0
- Initial release with Groq integration

---

Made with ❤️ by [RuteshAdithya](https://github.com/RuteshAdithya)
