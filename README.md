# 🎵 auto-spotify-s

A **Test Automation Framework** for the Spotify website, built with **Python**, **Selenium**, and **pytest**.

---

## 📋 Table of Contents

- [About](#about)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Running Tests](#running-tests)
- [CI/CD](#cicd)
- [Known Limitations](#known-limitations)

---

## About

`auto-spotify-s` is a browser-based UI test automation project that tests the [Spotify web player](https://open.spotify.com) using Selenium WebDriver. It uses `pytest` as the test runner and follows a structured Page Object Model (POM) pattern.

---

## Project Structure

```
auto-spotify-s/
├── .github/
│   └── workflows/          # GitHub Actions CI pipelines
├── data/                   # Test data files (e.g., credentials, config)
├── docs/                   # Additional documentation
├── libs/                   # Shared libraries / helper utilities
├── tests/                  # Test cases
├── tools/                  # Utility scripts / standalone tools
├── conftest.py             # pytest fixtures and setup/teardown hooks
├── pytest.ini              # pytest configuration
├── requirements.txt        # Python dependencies
└── sonar-project.properties # SonarQube code quality config
```

---

## Prerequisites

- **Python 3.8+**
- **Google Chrome** (or your preferred browser)
- **ChromeDriver** matching your Chrome version — or use `webdriver-manager` (included in dependencies)
- A **Spotify account** (Premium required for playback/API features — see [Known Limitations](#known-limitations))

---

## Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/KKoshy/auto-spotify-s.git
   cd auto-spotify-s
   ```

2. **Create and activate a virtual environment** *(recommended)*

   ```bash
   python -m venv venv
   source venv/bin/activate        # macOS/Linux
   venv\Scripts\activate           # Windows
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

---

## Configuration

Before running tests, set up your Spotify credentials. Check the `data/` folder for any config or `.env` template files and fill in your details:

```
SPOTIFY_USERNAME=your_email@example.com
SPOTIFY_PASSWORD=your_password
```

> ⚠️ Never commit real credentials to the repository. Use environment variables or a `.env` file that's listed in `.gitignore`.

---

## Running Tests

**Run all tests:**

```bash
pytest
```

**Run a specific test file:**

```bash
pytest tests/test_login.py
```

**Run with verbose output:**

```bash
pytest -v
```

**Run with HTML report** *(if pytest-html is installed)*:

```bash
pytest --html=report.html --self-contained-html
```

pytest configuration (markers, paths, etc.) is defined in `pytest.ini`.

---

## CI/CD

This project uses **GitHub Actions** for continuous integration. Workflow files are located in `.github/workflows/`. On each push or pull request, the pipeline:

1. Sets up Python
2. Installs dependencies
3. Runs the test suite

Code quality is tracked via **SonarQube** using the `sonar-project.properties` configuration.

---

## Known Limitations

- **Spotify Web API restrictions**: Certain API endpoints (e.g., playback control, user-specific data) are **not accessible on free-tier accounts**. A **Spotify Premium subscription** is required for these features.
- If you encounter authorization or `403` errors during test runs, verify that your account has an active Premium subscription.

---

## Branch

Default branch: `mainline`
