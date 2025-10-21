#!/usr/bin/env python3
"""Test script to verify all required imports work correctly."""

import os
import sys
import importlib
import glob
from IPython.display import HTML, display
import pandas as pd
import google.generativeai as genai
import ipywidgets

print("✓ All imports successful!")
print(f"Python version: {sys.version}")
print(f"Pandas version: {pd.__version__}")
print(f"Google GenerativeAI version: {genai.__version__}")
print(f"IPywidgets version: {ipywidgets.__version__}")
