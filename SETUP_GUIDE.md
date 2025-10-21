# PHIA Setup Guide

## Quick Start

### Option 1: Automated Setup (Recommended)
```bash
cd "/mnt/c/Users/User/OneDrive/Desktop/client projects/personal-health-insights-agent-main"
source phia_env/bin/activate
python setup_environment.py
python launch_phia.py
```

### Option 2: Manual Setup
```bash
# 1. Navigate to project
cd "/mnt/c/Users/User/OneDrive/Desktop/client projects/personal-health-insights-agent-main"

# 2. Activate virtual environment
source phia_env/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Register Jupyter kernel
python -m ipykernel install --user --name=phia_env --display-name="PHIA Environment"

# 5. Start Jupyter
jupyter notebook phia_demo_configured.ipynb
```

## Dependencies Installed

The project includes these key packages:
- `pandas==2.3.3` - Data manipulation
- `google-generativeai==0.8.5` - Google Gemini AI integration  
- `ipywidgets==8.1.7` - Interactive notebook widgets
- `numpy` - Numerical computing
- `matplotlib` - Plotting
- `scipy` - Scientific computing
- `seaborn` - Statistical visualization

## Important Notes

1. **Kernel Selection**: When running the notebook, make sure to select "PHIA Environment" from the Kernel menu
2. **API Key**: The Gemini API key is pre-configured in the startup scripts
3. **Synthetic Data**: The project includes synthetic health data for users 465, 333, 171, and 41

## Troubleshooting

### Import Errors
If you get `ModuleNotFoundError`, ensure:
1. Virtual environment is activated: `source phia_env/bin/activate`
2. Correct kernel is selected in Jupyter
3. Dependencies are installed: `pip install -r requirements.txt`

### Kernel Issues
If the kernel isn't available:
```bash
python -m ipykernel install --user --name=phia_env --display-name="PHIA Environment"
```

### Test Installation
```bash
python test_imports.py
```

## Files Overview

- `phia_demo_configured.ipynb` - Main demo notebook (pre-configured)
- `phia_demo.ipynb` - Original demo notebook
- `setup_environment.py` - Automated setup script
- `launch_phia.py` - Quick launcher
- `test_imports.py` - Import verification
- `start_phia.sh` - Bash startup script
