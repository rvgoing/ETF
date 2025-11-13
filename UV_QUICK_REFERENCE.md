# ⚡ UV Quick Reference Card

## Installation

```powershell
# First time setup (Windows)
.\setup.bat

# Or manually:
pip install uv
uv pip install -r uv.lock
```

---

## Daily Commands

| Task | Command |
|------|---------|
| **Install from lock** | `uv pip install -r uv.lock` |
| **List packages** | `uv pip list` |
| **Add new package** | `uv pip install package-name` |
| **Update all** | `uv pip install --upgrade` |
| **Update lock file** | `uv pip compile requirements.txt --output-file uv.lock` |
| **Show dependency tree** | `uv pip tree` |
| **Remove package** | `uv pip uninstall package-name` |

---

## Workflow: Adding a New Package

```powershell
# 1. Install
uv pip install new-package

# 2. Edit requirements.txt - add: new-package==version

# 3. Regenerate lock
uv pip compile requirements.txt --output-file uv.lock

# 4. Test
python run.py

# 5. Commit
git add requirements.txt uv.lock
git commit -m "Add new-package"
```

---

## Current Locked Packages (20 total)

```
Flask==3.0.0
NumPy==1.24.3
Matplotlib==3.7.1
Python-dotenv==1.0.0
+ 16 sub-dependencies (all locked)
```

---

## Tips

- ✅ Always commit `uv.lock` to Git
- ✅ Always regenerate lock after `requirements.txt` changes
- ✅ Use `uv pip install -r uv.lock` for reproducible installs
- ✅ `uv` is 10-100x faster than pip
- ❌ Don't edit `uv.lock` manually

---

## Troubleshooting

| Issue | Solution |
|-------|----------|
| `uv: command not found` | Run `pip install uv` |
| Lock file stale | Run `uv pip compile requirements.txt --output-file uv.lock` |
| Package version mismatch | Delete venv, run `setup.bat` again |
| New package not found | Check if added to `requirements.txt` and lock regenerated |

---

See `UV_LOCK_EXPLAINED.md` for detailed explanation.
