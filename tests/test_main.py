# ===== IMPORTS AND SETUP =====
# pytest: A testing framework for Python
# TestClient: Allows us to test FastAPI applications without running a real server
# sys & Path: Used to add the python_api directory to the import path

import pytest
from fastapi.testclient import TestClient
import sys
from pathlib import Path
# TODO