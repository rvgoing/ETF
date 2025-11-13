# 🤖 Git Setup - Ready to Push to GitHub

## 1. Initialize Git (if not already done)

```powershell
cd e:\Project\ETF

# Initialize repository
git init

# Configure Git (one-time setup)
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

---

## 2. Add All Files

```powershell
# Stage all files (respects .gitignore)
git add .

# Verify what will be committed
git status
```

**What gets committed:**
- ✓ All source files (.py, .html, .md)
- ✓ `requirements.txt` + `uv.lock` (locked versions)
- ✓ `pyproject.toml`, setup scripts
- ✓ Documentation and LICENSE
- ✓ GitHub workflows

**What is ignored (gitignored):**
- ✗ `venv/` - Virtual environment (not committed)
- ✗ `__pycache__/` - Python cache files
- ✗ `.env` - Environment variables (sensitive)
- ✗ `*.pyc` - Compiled Python files

---

## 3. Create Initial Commit

```powershell
git commit -m "Initial commit: ETF Investment Simulator with uv package management"
```

Or with more detail:
```powershell
git commit -m "Initial commit: ETF Investment Simulator

- Flask-based investment calculator
- uv package manager with reproducible builds
- All 20 dependencies locked in uv.lock
- Complete documentation and setup scripts
- GitHub Actions CI/CD pipeline included"
```

---

## 4. Create GitHub Repository

1. Go to https://github.com/new
2. Create repository name: `ETF` (or similar)
3. Do **NOT** initialize with README/LICENSE (we have them!)
4. Click "Create repository"

---

## 5. Connect Local Repo to GitHub

```powershell
# Add remote (replace YOUR_USERNAME and YOUR_REPO)
git remote add origin https://github.com/YOUR_USERNAME/ETF.git

# Rename branch to main (if needed)
git branch -M main

# Push code to GitHub
git push -u origin main
```

---

## 6. Verify on GitHub

After pushing:
1. Refresh GitHub repository page
2. Verify you see:
   - ✓ All your Python files
   - ✓ README.md displayed at bottom
   - ✓ `uv.lock` file (shows reproducible builds!)
   - ✓ Documentation files

---

## 7. For Team Members (Cloning)

Once on GitHub, team members can clone:

```powershell
git clone https://github.com/YOUR_USERNAME/ETF.git
cd ETF
.\setup.bat                  # Uses uv.lock for identical environment!
python run.py                # Start the app
```

---

## 📝 Commit Message Convention

### For Updates:

**Adding dependencies:**
```powershell
git commit -m "Add pandas for data analysis

- Install: pandas==2.0.0
- Update uv.lock with all sub-dependencies
- Update requirements.txt"
```

**Bug fixes:**
```powershell
git commit -m "Fix Chinese character encoding in charts

- Set matplotlib backend to Agg
- Configure font preferences
- Resolves issue #5"
```

**Documentation:**
```powershell
git commit -m "Update README with deployment guide"
```

---

## 🔄 Git Workflow (Going Forward)

### 1. Make Changes
```powershell
# Edit files
code app.py
# OR
# Edit requirements.txt to add new package
```

### 2. Install If Needed
```powershell
uv pip install new-package
uv pip compile requirements.txt --output-file uv.lock
```

### 3. Test Locally
```powershell
python run.py
# Test in browser: http://127.0.0.1:5000
# Press Ctrl+C to stop
```

### 4. Commit Changes
```powershell
# Check what changed
git status

# Stage changes
git add .

# Commit with message
git commit -m "Descriptive message about changes"
```

### 5. Push to GitHub
```powershell
git push origin main
```

### 6. Pull Latest (Team)
```powershell
git pull origin main
uv pip install -r uv.lock    # Update dependencies if needed
```

---

## 🛡️ Important: Don't Commit

**NEVER commit these files:**

```powershell
# ✗ DON'T commit
venv/                 # Virtual environment (site-specific)
.env                  # Sensitive data (API keys, passwords)
*.pyc                 # Compiled files (regenerated)
__pycache__/          # Cache (auto-generated)
.DS_Store             # macOS files
Thumbs.db             # Windows files
*.swp                 # Editor temp files
```

**These are already in `.gitignore`** ✓

---

## 🚀 Minimal Quick Setup for New Devs

After cloning from GitHub:

```powershell
cd ETF
.\setup.bat              # That's it! Uses uv.lock
python run.py
# App runs at http://127.0.0.1:5000
```

No need to:
- ✗ Manually create venv
- ✗ Research package versions
- ✗ Install packages individually
- ✗ Worry about compatibility

Everything is in `uv.lock`! ✓

---

## 📊 Useful Git Commands

```powershell
# See commit history
git log --oneline

# See what changed in a file
git diff app.py

# Undo last commit (before push)
git reset --soft HEAD~1

# See current status
git status

# Create a branch for features
git checkout -b feature/new-feature

# Switch branches
git checkout main

# Merge feature into main
git merge feature/new-feature
```

---

## ✅ Checklist Before First Push

- [ ] `git status` shows correct files
- [ ] No `.env` or `venv/` in commit
- [ ] `uv.lock` is included
- [ ] `requirements.txt` is included
- [ ] All documentation in place
- [ ] LICENSE file added
- [ ] `.gitignore` configured
- [ ] Initial commit created locally
- [ ] GitHub repo created
- [ ] Remote added (`git remote add origin ...`)
- [ ] Pushed to GitHub (`git push -u origin main`)

---

## 🎉 You're Ready!

```powershell
# Summary:
git init
git add .
git commit -m "Initial commit: ETF Investment Simulator with uv"
git remote add origin https://github.com/YOUR_USERNAME/ETF.git
git branch -M main
git push -u origin main
```

Now your project is on GitHub with:
- ✅ Reproducible builds (uv.lock)
- ✅ Complete documentation
- ✅ CI/CD pipeline
- ✅ Ready for team collaboration

**Share the GitHub link with your team!** 🚀
