# Simple News Scraper (Flask + BeautifulSoup)

This project is a simple web scraping practice inspired by Dea Afrizal.  
The app fetches the **main news headline** from:
- Kompas
- Detik
- Tribunnews

## How to run

1. Clone or download this repo  
2. Install dependencies:
   ```bash
   pip install flask requests beautifulsoup4
   ```
# Run the server:

```bash
Copy code
python app.py
```
Open your browser at http://127.0.0.1:5000/

# Notes
It only grabs the main headline, so if the site structure changes it may break.
For learning purposes only, not for commercial use.
