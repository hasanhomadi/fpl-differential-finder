markdown
# FPL Differential Finder

Tool to find undervalued, low-ownership Fantasy Premier League players by pulling live data from the official FPL API and ranking players by points-per-million value. Built as a personal project to learn API integration, web app development, and containerization.

## What it does

- Fetches live player data (prices, ownership %, total points) from the FPL public API
- Filters and ranks players by a "differential" score (low ownership + high points-per-million)
- Displays results in an interactive dashboard with an adjustable ownership threshold slider.

## Tech stack

- **Python** — data fetching and filtering logic
- **Streamlit** — interactive web dashboard
- **Docker** — containerized for consistent, portable deployment

## Running locally

1. Clone the repo and navigate into it
2. Create a virtual environment and activate it:

```bash
python -m venv venv
venv\Scripts\Activate.ps1
```

3. Install dependencies:

pip install -r requirements.txt

4. Run the dashboard:

streamlit run dashboard.py

5. Open `http://localhost:8501` in your browser

## Running with Docker

1. Build the image:

```bash
docker build -t fpl-differential-finder .
```

2. Run the container:

```bash
docker run -p 8501:8501 fpl-differential-finder
```

3. Open `http://localhost:8501` in your browser

## What I learned

This project was built to close a gap in my technical experience around DevOps practices — specifically containerization and (soon) CI/CD automation. Along the way I worked through real issues like handling inconsistent API data types, structuring reusable functions vs. one-off scripts, and choosing a base Docker image with build compatibility and security in mind (opted for `python:3.13-alpine` over `slim` after comparing vulnerability scan results).

## Roadmap

- [ ] Automated testing and CI via GitHub Actions
- [ ] Public deployment
- [ ] Factor in fixture difficulty using the FPL fixtures API