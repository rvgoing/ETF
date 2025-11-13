# 📈 定期定額投資模擬器 (Fixed-Amount Investment Simulator)

A Flask-based web application for simulating fixed-amount investment strategies across multiple ETFs.

## Features

- **Multi-ETF Portfolio Support**: Simulate investments in TSMC (2330), 0050, and 00770
- **Interactive Dashboard**: Real-time calculations and visualizations
- **Flexible Parameters**: Adjust monthly investment amount, investment period, and expected returns
- **Visual Charts**: Matplotlib-based investment growth visualization
- **Traditional Chinese Support**: Full support for Traditional Chinese characters

## Project Structure

```
ETF/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── templates/
│   └── index.html        # Frontend HTML template
├── README.md             # Project documentation
├── .gitignore            # Git ignore rules
├── .env.example          # Example environment variables
└── venv/                 # Virtual environment (created locally)
```

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager) or uv (recommended - modern package manager)

## Installation

### 1. Clone the repository
```bash
git clone <repository-url>
cd ETF
```

### 2. Create a virtual environment

**On Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**On macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

**Using uv with lock file (Recommended - fast & reproducible):**
```bash
pip install uv
uv pip install --locked -r uv.lock
```

**Using uv without lock file:**
```bash
uv pip install -r requirements.txt
```

**Using pip (Traditional):**
```bash
pip install -r requirements.txt
```

### 4. Setup environment variables
```bash
copy .env.example .env
```

Edit `.env` if you need to change default values.

## Running the Application

1. Activate the virtual environment (if not already activated):
   ```bash
   # Windows
   venv\Scripts\activate
   
   # macOS/Linux
   source venv/bin/activate
   ```

2. Run the Flask application:
   ```bash
   python app.py
   ```

3. Open your browser and navigate to:
   ```
   http://127.0.0.1:5000
   ```

## Dependencies

- **Flask** (3.0.0) - Web framework
- **NumPy** (1.24.3) - Numerical computing
- **Matplotlib** (3.7.1) - Data visualization

See `requirements.txt` for complete dependency list.

## Usage

1. Enter your monthly investment amount
2. Set the investment period in years
3. Input expected annual returns for each ETF:
   - TSMC (2330)
   - 0050 (Taiwan ETF)
   - 00770 (High dividend ETF)
4. View the calculated results and visualization chart
5. Adjust parameters to compare different scenarios

## Features Details

### Investment Allocation
- TSMC (2330): 50%
- 0050: 30%
- 00770: 20%

### Calculations
- Monthly compounding interest
- Fixed-amount monthly investment
- Total invested capital tracking
- Profit/loss analysis
- Return on investment (ROI) percentage

## Troubleshooting

### Virtual Environment Not Activating
- Ensure Python 3.8+ is installed
- Try using `python -m venv venv` instead of `python3 -m venv venv`

### Module Not Found Errors
- Confirm virtual environment is activated (should show `(venv)` in terminal)
- Run `pip install -r requirements.txt` again

### Chinese Characters Not Displaying
- Ensure Windows has Microsoft JhengHei or SimHei font installed
- The app provides fallback font support

## Development

### Virtual Environment Setup for Development
```bash
# Create venv
python -m venv venv

# Activate venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # macOS/Linux

# Install dependencies
pip install -r requirements.txt

# Run in debug mode
set FLASK_ENV=development  # Windows
export FLASK_ENV=development  # macOS/Linux
python app.py
```

## Deployment

For production deployment, consider:
- Using a WSGI server (Gunicorn, uWSGI)
- Setting `FLASK_ENV=production`
- Using environment-specific configuration
- Implementing proper error logging

## License

This project is open source and available under the MIT License.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Author

ETF Investment Simulator Project

## Support

For issues and questions, please open an issue on the GitHub repository.
