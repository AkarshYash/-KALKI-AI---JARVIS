#!/usr/bin/env python3
"""
KALKI AI - Main Application Launcher
Launch the complete KALKI AI system with all components
"""

import sys
import os
import asyncio
import logging
import subprocess
import signal
from pathlib import Path
from typing import Optional
import multiprocessing as mp

# Add project root to Python path
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

from config.settings import Settings
from ui.app import KalkiUI

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('logs/kalki_ai.log'),
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger(__name__)

class KalkiLauncher:
    """Main launcher for KALKI AI system"""
    
    def __init__(self):
        self.settings = Settings()
        self.backend_process: Optional[subprocess.Popen] = None
        self.ui_process: Optional[mp.Process] = None
        self.running = False
        
    def check_dependencies(self) -> bool:
        """Check if all required dependencies are installed"""
        logger.info("Checking dependencies...")
        
        required_packages = [
            'fastapi', 'uvicorn', 'PyQt5', 'opencv-python', 
            'mediapipe', 'whisper', 'edge-tts', 'sqlalchemy'
        ]
        
        missing_packages = []
        
        for package in required_packages:
            try:
                __import__(package.replace('-', '_'))
            except ImportError:
                missing_packages.append(package)
                
        if missing_packages:
            logger.error(f"Missing packages: {', '.join(missing_packages)}")
            logger.info("Install missing packages with: pip install -r requirements.txt")
            return False
            
        logger.info("All dependencies satisfied")
        return True
        
    def setup_directories(self):
        """Create necessary directories"""
        directories = [
            'logs', 'data', 'cache', 'models', 'config'
        ]
        
        for directory in directories:
            Path(directory).mkdir(parents=True, exist_ok=True)
            
    def start_backend(self) -> bool:
        """Start FastAPI backend server"""
        try:
            logger.info("Starting KALKI AI Backend...")
            
            # Start backend server
            cmd = [
                sys.executable, "-m", "uvicorn",
                "backend.main:app",
                "--host", "127.0.0.1",
                "--port", "8000",
                "--reload" if self.settings.is_debug_mode() else "--no-reload",
                "--log-level", self.settings.get_log_level().lower()
            ]
            
            self.backend_process = subprocess.Popen(
                cmd,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                cwd=project_root
            )
            
            # Wait a moment for server to start
            import time
            time.sleep(3)
            
            # Check if process is still running
            if self.backend_process.poll() is None:
                logger.info("Backend server started successfully")
                return True
            else:
                logger.error("Backend server failed to start")
                return False
                
        except Exception as e:
            logger.error(f"Failed to start backend: {str(e)}")
            return False
            
    def start_ui(self) -> bool:
        """Start PyQt5 UI in separate process"""
        try:
            logger.info("Starting KALKI AI User Interface...")
            
            def run_ui():
                """Run UI in separate process"""
                try:
                    from PyQt5.QtWidgets import QApplication
                    import sys
                    
                    app = QApplication(sys.argv)
                    kalki_ui = KalkiUI()
                    kalki_ui.show()
                    
                    # Connect to backend
                    kalki_ui.connect_to_backend()
                    
                    sys.exit(app.exec_())
                    
                except Exception as e:
                    logger.error(f"UI process error: {str(e)}")
                    
            # Start UI process
            self.ui_process = mp.Process(target=run_ui)
            self.ui_process.start()
            
            logger.info("User Interface started successfully")
            return True
            
        except Exception as e:
            logger.error(f"Failed to start UI: {str(e)}")
            return False
            
    def check_backend_health(self) -> bool:
        """Check if backend is healthy"""
        try:
            import requests
            response = requests.get("http://127.0.0.1:8000/health", timeout=5)
            return response.status_code == 200
        except:
            return False
            
    def wait_for_backend(self, timeout: int = 30) -> bool:
        """Wait for backend to be ready"""
        import time
        
        logger.info("Waiting for backend to be ready...")
        
        for i in range(timeout):
            if self.check_backend_health():
                logger.info("Backend is ready")
                return True
            time.sleep(1)
            
        logger.error("Backend failed to become ready")
        return False
        
    def setup_signal_handlers(self):
        """Setup signal handlers for graceful shutdown"""
        def signal_handler(signum, frame):
            logger.info(f"Received signal {signum}, shutting down...")
            self.shutdown()
            sys.exit(0)
            
        signal.signal(signal.SIGINT, signal_handler)
        signal.signal(signal.SIGTERM, signal_handler)
        
    def start(self) -> bool:
        """Start the complete KALKI AI system"""
        try:
            logger.info("KALKI AI System Starting...")
            logger.info("=" * 50)
            
            # Setup
            self.setup_directories()
            self.setup_signal_handlers()
            
            # Check dependencies
            if not self.check_dependencies():
                return False
                
            # Start backend
            if not self.start_backend():
                return False
                
            # Wait for backend to be ready
            if not self.wait_for_backend():
                return False
                
            # Start UI
            if not self.start_ui():
                return False
                
            self.running = True
            
            logger.info("=" * 50)
            logger.info("KALKI AI System Online!")
            logger.info("Backend: http://127.0.0.1:8000")
            logger.info("Health Check: http://127.0.0.1:8000/health")
            logger.info("=" * 50)
            
            # Keep main process alive
            self.monitor_processes()
            
            return True
            
        except Exception as e:
            logger.error(f"Failed to start KALKI AI: {str(e)}")
            self.shutdown()
            return False
            
    def monitor_processes(self):
        """Monitor backend and UI processes"""
        try:
            while self.running:
                # Check backend process
                if self.backend_process and self.backend_process.poll() is not None:
                    logger.error("Backend process died, restarting...")
                    self.start_backend()
                    
                # Check UI process
                if self.ui_process and not self.ui_process.is_alive():
                    logger.info("UI process ended")
                    break
                    
                import time
                time.sleep(5)
                
        except KeyboardInterrupt:
            logger.info("Received keyboard interrupt")
        finally:
            self.shutdown()
            
    def shutdown(self):
        """Shutdown all processes gracefully"""
        logger.info("Shutting down KALKI AI...")
        
        self.running = False
        
        # Shutdown UI process
        if self.ui_process and self.ui_process.is_alive():
            logger.info("Stopping UI process...")
            self.ui_process.terminate()
            self.ui_process.join(timeout=5)
            if self.ui_process.is_alive():
                self.ui_process.kill()
                
        # Shutdown backend process
        if self.backend_process and self.backend_process.poll() is None:
            logger.info("Stopping backend server...")
            self.backend_process.terminate()
            try:
                self.backend_process.wait(timeout=10)
            except subprocess.TimeoutExpired:
                self.backend_process.kill()
                
        logger.info("KALKI AI shutdown complete")

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
    
    launcher = KalkiLauncher()
    
    try:
        success = launcher.start()
        if not success:
            sys.exit(1)
    except KeyboardInterrupt:
        logger.info("Interrupted by user")
        launcher.shutdown()
        sys.exit(0)
    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}")
        launcher.shutdown()
        sys.exit(1)

if __name__ == "__main__":
    main()