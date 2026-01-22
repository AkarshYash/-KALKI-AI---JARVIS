"""
Setup script for KALKI AI
"""

import os
import sys
import subprocess
import platform

def check_python_version():
    """Check if Python 3.7+ is installed"""
    version = sys.version_info
    if version.major < 3 or (version.major == 3 and version.minor < 7):
        print("KALKI AI requires Python 3.7 or higher.")
        print(f"You are using Python {version.major}.{version.minor}.{version.micro}")
        return False
    return True

def install_requirements():
    """Install required packages"""
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error installing requirements: {e}")
        return False

def check_dependencies():
    """Check if required dependencies are installed"""
    dependencies = [
        ("speech_recognition", "SpeechRecognition"),
        ("edge_tts", "edge-tts"),
        ("cv2", "opencv-python"),
        ("mediapipe", "mediapipe")
    ]
    
    missing = []
    for module, package in dependencies:
        try:
            __import__(module)
        except ImportError:
            missing.append(package)
    
    return missing

def main():
    """Main setup function"""
    print("KALKI AI Setup")
    print("=" * 30)
    
    # Check Python version
    if not check_python_version():
        return
    
    # Check if running on Windows
    is_windows = platform.system() == "Windows"
    
    # Check existing dependencies
    missing = check_dependencies()
    
    if not missing:
        print("All dependencies are already installed!")
        print("\nYou can now run KALKI AI:")
        if is_windows:
            print("- Double-click run.bat")
        print("- Run with UI: python run.py")
        print("- Run with CLI: python run.py --cli")
        print("- Test voice: python run.py --test-voice")
        print("- Test hand gestures: python run.py --test-hand")
        return
    
    print(f"Missing dependencies: {', '.join(missing)}")
    
    # Ask user if they want to install dependencies
    response = input("\nDo you want to install missing dependencies? (y/n): ").strip().lower()
    
    if response in ['y', 'yes']:
        print("Installing dependencies...")
        if install_requirements():
            print("Dependencies installed successfully!")
            print("\nYou can now run KALKI AI:")
            if is_windows:
                print("- Double-click run.bat")
            print("- Run with UI: python run.py")
            print("- Run with CLI: python run.py --cli")
            print("- Test voice: python run.py --test-voice")
            print("- Test hand gestures: python run.py --test-hand")
        else:
            print("Failed to install dependencies. Please try manually:")
            print("pip install -r requirements.txt")
    else:
        print("You can manually install dependencies later with:")
        print("pip install -r requirements.txt")

if __name__ == "__main__":
    main()