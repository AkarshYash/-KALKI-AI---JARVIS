#!/usr/bin/env python3
"""
KALKI AI - Complete Companion System
Run the full KALKI AI with proactive companion features
"""

import sys
import asyncio
import logging
import multiprocessing as mp
from datetime import datetime

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def run_backend():
    """Run KALKI AI backend"""
    try:
        import uvicorn
        from backend.main import app
        
        uvicorn.run(
            app,
            host="127.0.0.1",
            port=8000,
            log_level="info"
        )
    except Exception as e:
        logger.error(f"Backend error: {str(e)}")

def run_ui():
    """Run KALKI AI UI"""
    try:
        from PyQt5.QtWidgets import QApplication
        from ui.app import KalkiUI
        
        app = QApplication(sys.argv)
        window = KalkiUI()
        window.show()
        
        # Connect to backend
        window.connect_to_backend()
        
        return app.exec_()
    except Exception as e:
        logger.error(f"UI error: {str(e)}")
        return 1

def main():
    """Main entry point"""
    print("""
    ╔══════════════════════════════════════════════════════════════╗
    ║                        KALKI AI                              ║
    ║              Your Proactive AI Companion                     ║
    ║                                                              ║
    ║  🎤 Say "Fantastic" to activate                             ║
    ║  🤖 Proactive suggestions and help                          ║
    ║  👋 Gesture control (wave for tabs)                         ║
    ║  💻 Code generation and automation                          ║
    ║  🎭 Human-like animated communication                       ║
    ║                                                              ║
    ║            "Your AI Companion is Starting..."               ║
    ╚══════════════════════════════════════════════════════════════╝
    """)
    
    try:
        logger.info("🚀 Starting KALKI AI Companion System...")
        
        # Start backend process
        backend_process = mp.Process(target=run_backend)
        backend_process.start()
        
        # Wait for backend to start
        import time
        time.sleep(5)
        
        logger.info("🖥️ Starting KALKI AI User Interface...")
        
        # Start UI
        result = run_ui()
        
        # Cleanup
        backend_process.terminate()
        backend_process.join()
        
        return result
        
    except KeyboardInterrupt:
        logger.info("👋 KALKI AI shutdown by user")
        return 0
    except Exception as e:
        logger.error(f"System error: {str(e)}")
        return 1

if __name__ == "__main__":
    print("🎬 KALKI AI - Your Proactive Companion is Ready!")
    print("✨ Features:")
    print("  • Say 'Fantastic' to activate")
    print("  • Proactive conversations and suggestions")
    print("  • Gesture controls (wave right/left for tabs)")
    print("  • File creation and system automation")
    print("  • Code generation and execution")
    print("  • Human-like animated responses")
    print("  • Regular check-ins and encouragement")
    print("\n🚀 Starting system...")
    
    sys.exit(main())