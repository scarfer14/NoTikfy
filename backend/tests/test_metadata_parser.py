import sys
import os

# Add the parent directory of backend to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from case.metadata_parser import extract_video_metadata
