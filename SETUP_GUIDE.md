# ETF Investment Simulator - Complete Setup Guide

## 📋 Quick Start

### Windows Users
```powershell
# Run the setup script
.\setup.bat

# Then start the app
venv\Scripts\activate
python run.py
```

### macOS/Linux Users
```bash
# Make the setup script executable
chmod +x setup.sh

# Run the setup script
./setup.sh

# Then start the app
source venv/bin/activate
python run.py
```

---

## 🚀 Manual Setup (If Automated Setup Doesn't Work)

### Step 1: Create Virtual Environment

**Windows:**
```powershell
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### Step 2: Upgrade pip
```bash
python -m pip install --upgrade pip
```

### Step 3: Install Dependencies

**Option A: Using uv with lock file (Recommended - fast & reproducible):**
```bash
# First install uv (if not already installed)
pip install uv

# Then install with locked versions
uv pip install --locked -r uv.lock
```

**Option B: Using uv without lock file:**
```bash
pip install uv
uv pip install -r requirements.txt
```

**Option C: Using pip (Traditional):**
```bash
pip install -r requirements.txt
```

### Step 4: Setup Environment Variables
```bash
# Copy the example file
# Windows:
copy .env.example .env
# macOS/Linux:
cp .env.example .env
```

### Step 5: Run the Application
```bash
python run.py
```

Open your browser and navigate to: `http://127.0.0.1:5000`

---

## 📁 Project Structure

```
ETF/
├── app.py                          # Main Flask application logic
├── run.py                          # Application entry point
├── requirements.txt                # Python dependencies
├── setup.py                        # Package setup configuration
├── setup.bat                       # Windows setup script
├── setup.sh                        # macOS/Linux setup script
│
├── templates/
│   └── index.html                 # Frontend HTML template
│
├── .github/
│   └── workflows/
│       └── python-app.yml         # GitHub Actions CI/CD
│
├── README.md                       # Project documentation
├── CONTRIBUTING.md                # Contribution guidelines
├── LICENSE                        # MIT License
├── .gitignore                     # Git ignore rules
├── .env.example                   # Example environment variables
├── .dockerignore                  # Docker ignore rules
├── MANIFEST.in                    # Package manifest
│
└── venv/                          # Virtual environment (local only)
    ├── Scripts/                   # Windows executables
    ├── bin/                       # macOS/Linux executables
    └── lib/                       # Installed packages
```

---

## 🔧 Configuration

### Environment Variables

Edit `.env` file to customize:

```env
# Flask Configuration
FLASK_ENV=development
FLASK_DEBUG=True
FLASK_APP=app.py

# Server Configuration
HOST=127.0.0.1
PORT=5000
```

**Environment Options:**
- `FLASK_ENV`: `development` or `production`
- `FLASK_DEBUG`: `True` or `False` (enables auto-reload and error page)
- `HOST`: Server host (default: 127.0.0.1)
- `PORT`: Server port (default: 5000)

---

## 📦 Dependency Information

| Package | Version | Purpose |
|---------|---------|---------|
| Flask | 3.0.0 | Web framework |
| NumPy | 1.24.3 | Numerical computing |
| Matplotlib | 3.7.1 | Data visualization |
| python-dotenv | 1.0.0 | Environment variables |

---

## 🐛 Troubleshooting

### Issue: "python: command not found"
**Solution:**
- Install Python from https://www.python.org
- Ensure Python is added to PATH
- Use `python3` instead of `python` on macOS/Linux

### Issue: Virtual environment not activating
**Solution (Windows):**
```powershell
# If you get execution policy error:
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# Then try again:
venv\Scripts\activate
```

### Issue: "ModuleNotFoundError: No module named 'flask'"
**Solution:**
- Ensure virtual environment is activated (you should see `(venv)` in terminal)
- Run: `pip install -r requirements.txt`

### Issue: Port 5000 already in use
**Solution:**
- Change PORT in `.env` file
- Or kill the process using port 5000

### Issue: Chinese characters not displaying
**Solution:**
- Windows: Install Microsoft JhengHei or SimHei font
- macOS: Install SimHei.ttf font
- Linux: `sudo apt-get install fonts-noto-cjk`

---

## 🚀 Running in Production

### Using Gunicorn (Recommended)

```bash
# Install Gunicorn
pip install gunicorn

# Run with Gunicorn
gunicorn -w 4 -b 0.0.0.0:8000 app:app

# -w: Number of worker processes
# -b: Bind address and port
# app:app: application module and variable
```

### Environment Setup
```bash
# Set production environment
# Windows:
set FLASK_ENV=production
set FLASK_DEBUG=False

# macOS/Linux:
export FLASK_ENV=production
export FLASK_DEBUG=False
```

---

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/amazing-feature`
3. Make changes and test
4. Commit: `git commit -m 'Add amazing feature'`
5. Push: `git push origin feature/amazing-feature`
6. Open a Pull Request

See [CONTRIBUTING.md](CONTRIBUTING.md) for more details.

---

## 📚 Additional Resources

- [Flask Documentation](https://flask.palletsprojects.com/)
- [Python Virtual Environments](https://docs.python.org/3/tutorial/venv.html)
- [NumPy Documentation](https://numpy.org/doc/)
- [Matplotlib Documentation](https://matplotlib.org/)

---

## ❓ Common Questions

**Q: Can I use Python 3.7?**
A: No, this project requires Python 3.8 or higher.

**Q: How do I update dependencies?**
A: Run `pip install --upgrade -r requirements.txt`

**Q: Can I deploy this to Heroku/AWS?**
A: Yes! See production setup instructions above.

**Q: How do I generate a new requirements.txt?**
A: Run `pip freeze > requirements.txt`

---

## 📝 License

This project is licensed under the MIT License - see [LICENSE](LICENSE) file for details.

---

## 💡 Tips

- Always activate virtual environment before working
- Keep `.env` file private (never commit to git)
- Use `.env.example` for sharing default configuration
- Update requirements.txt when installing new packages: `pip freeze > requirements.txt`
- Test changes locally before pushing to GitHub

---

**Happy Investing! 📈**
