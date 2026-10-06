"""
Pytest configuration and fixtures for DPR_PythonPlaywright
"""
import sys
from pathlib import Path

# Add project root to path
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))
