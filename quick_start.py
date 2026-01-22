#!/usr/bin/env python3
"""
KALKI AI - Quick Start Version
Simplified version to get KALKI running immediately
"""

import sys
import asyncio
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def check_essential_imports():
    """Check if essential packages are available"""
    missing = []
    
    try:
        import fastapi
        logger.info("✅ FastAPI available")
    except ImportError:
        missing.append("fastapi")
        
    try:
        import uvicorn
        logger.info("✅ Uvicorn available")
    except ImportError:
        missing.append("uvicorn")
        
    try:
        import PyQt5
        logger.info("✅ PyQt5 available")
    except ImportError:
        missing.append("PyQt5")
        
    try:
        import cv2
        logger.info("✅ OpenCV available")
    except ImportError:
        missing.append("opencv-python")
        
    try:
        import mediapipe as mp
        logger.info("✅ MediaPipe available")
    except ImportError as e:
        logger.warning(f"MediaPipe import issue: {e}")
        # MediaPipe is optional for gesture recognition
        logger.info("⚠️ MediaPipe not available - gesture recognition disabled")
        
    try:
        import edge_tts
        logger.info("✅ Edge-TTS available")
    except ImportError:
        missing.append("edge-tts")
        
    try:
        import win32gui
        logger.info("✅ Win32GUI available")
    except ImportError:
        missing.append("pywin32")
        
    return missing

async def start_kalki_backend():
    """Start KALKI AI backend server"""
    try:
        from backend.main import app
        import uvicorn
        
        logger.info("🚀 Starting KALKI AI Backend Server...")
        
        # Start server
        config = uvicorn.Config(
            app=app,
            host="127.0.0.1",
            port=8000,
            log_level="info"
        )
        server = uvicorn.Server(config)
        await server.serve()
        
    except Exception as e:
        logger.error(f"❌ Backend startup failed: {str(e)}")
        return False

def start_kalki_ui():
    """Start KALKI AI user interface"""
    try:
        from PyQt5.QtWidgets import QApplication
        from ui.app import KalkiUI
        
        logger.info("🖥️ Starting KALKI AI User Interface...")
        
        app = QApplication(sys.argv)
        window = KalkiUI()
        window.show()
        
        # Connect to backend
        window.connect_to_backend()
        
        return app.exec_()
        
    except Exception as e:
        logger.error(f"❌ UI startup failed: {str(e)}")
        return False

def main():
    """Main entry point"""
    print("""
    ╔══════════════════════════════════════════════════════════════╗
    ║                        KALKI AI                              ║
    ║              JARVIS-Inspired AI Assistant                    ║
    ║                                                              ║
    ║  🎤 Voice Control    🤖 AI Intelligence   🔒 Cybersecurity   ║
    ║  👋 Gesture Control  💻 Code Generation   🌐 Web Integration ║
    ║                                                              ║
    ║                    "System Ready, Sir"                      ║
    ╚══════════════════════════════════════════════════════════════╝
    """)
    
    logger.info("🔍 Checking system dependencies...")
    
    # Check dependencies
    missing = check_essential_imports()
    
    if missing:
        logger.error(f"❌ Missing dependencies: {', '.join(missing)}")
        logger.info("Install missing packages with:")
        logger.info(f"pip install {' '.join(missing)}")
        return 1
        
    logger.info("✅ All essential dependencies available!")
    
    # Ask user what to start
    print("\nChoose startup mode:")
    print("1. Full System (Backend + UI)")
    print("2. Backend Only")
    print("3. UI Only")
    
    try:
        choice = input("Enter choice (1-3): ").strip()
        
        if choice == "1":
            logger.info("🚀 Starting Full KALKI AI System...")
            
            # Start backend in background
            import multiprocessing as mp
            import time
            
            def run_backend():
                asyncio.run(start_kalki_backend())
                
            backend_process = mp.Process(target=run_backend)
            backend_process.start()
            
            # Wait for backend to start
            time.sleep(3)
            
            # Start UI
            result = start_kalki_ui()
            
            # Cleanup
            backend_process.terminate()
            backend_process.join()
            
            return result
            
        elif choice == "2":
            logger.info("🚀 Starting KALKI AI Backend Only...")
            asyncio.run(start_kalki_backend())
            return 0
            
        elif choice == "3":
            logger.info("🖥️ Starting KALKI AI UI Only...")
            return start_kalki_ui()
            
        else:
            logger.error("Invalid choice")
            return 1
            
    except KeyboardInterrupt:
        logger.info("Interrupted by user")
        return 0
    except Exception as e:
        logger.error(f"Startup error: {str(e)}")
        return 1

if __name__ == "__main__":
    sys.exit(main())