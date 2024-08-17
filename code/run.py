import subprocess
import os
import shutil
import sys

video_path = sys.argv[1]  # Get the video path from the command-line arguments

runsDir='/home/uday/Desktop/ML_project/code/runs'
outputsDir='/home/uday/Desktop/ML_project/outputs'

if os.path.exists(runsDir):
    shutil.rmtree(runsDir)
if os.path.exists(outputsDir):
    shutil.rmtree(outputsDir)


# Run iteration3.py
subprocess.run(["python", "/home/uday/Desktop/ML_project/code/iteration3.py", video_path])


# Run yolov8.py
subprocess.run(["python", "/home/uday/Desktop/ML_project/code/yolov8.py"])

# Run inference.py
subprocess.run(["python", "/home/uday/Desktop/ML_project/code/inference.py"])


