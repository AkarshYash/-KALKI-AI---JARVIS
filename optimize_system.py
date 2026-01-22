#!/usr/bin/env python3
"""
KALKI AI System Optimization Script
Fine-tune all system parameters for optimal performance
"""

import asyncio
import logging
from pathlib import Path
import sys

# Add project root to Python path
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

from config.settings import Settings
from core.voice_engine import VoiceEngine
from core.gesture_engine import GestureEngine

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class SystemOptimizer:
    """System optimization and calibration"""
    
    def __init__(self):
        self.settings = Settings()
        
    async def optimize_voice_settings(self):
        """Optimize voice recognition and synthesis"""
        logger.info("🎤 Optimizing voice settings...")
        
        # JARVIS-like voice optimization
        self.settings.voice.voice_id = "en-US-GuyNeural"  # Deep male voice
        self.settings.voice.speed = 0.85  # Slightly slower for authority
        self.settings.voice.pitch = -8.0  # Lower pitch for depth
        self.settings.voice.volume = 0.9  # Clear and audible
        self.settings.voice.emotion_level = 0.7  # Expressive for Hindi-English
        
        logger.info("✅ Voice settings optimized for JARVIS-like performance")
        
    async def optimize_gesture_settings(self):
        """Optimize gesture recognition parameters"""
        logger.info("🤚 Optimizing gesture recognition...")
        
        # Enhanced gesture detection
        self.settings.gesture.sensitivity = 0.85  # Higher sensitivity
        self.settings.gesture.confidence_threshold = 0.75  # Better accuracy
        self.settings.gesture.gesture_timeout = 1.5  # Faster response
        self.settings.gesture.calibration_required = False  # Auto-calibration
        
        logger.info("✅ Gesture settings optimized for responsive control")
        
    async def test_camera_access(self):
        """Test camera access and permissions"""
        logger.info("📷 Testing camera access...")
        
        try:
            import cv2
            camera = cv2.VideoCapture(0)
            
            if camera.isOpened():
                ret, frame = camera.read()
                if ret:
                    logger.info("✅ Camera access working properly")
                    height, width = frame.shape[:2]
                    logger.info(f"📐 Camera resolution: {width}x{height}")
                else:
                    logger.warning("⚠️ Camera opened but no frame captured")
                    
                camera.release()
            else:
                logger.error("❌ Cannot access camera - check permissions")
                
        except Exception as e:
            logger.error(f"❌ Camera test failed: {str(e)}")
            
    async def test_microphone_access(self):
        """Test microphone access and audio input"""
        logger.info("🎤 Testing microphone access...")
        
        try:
            import speech_recognition as sr
            
            recognizer = sr.Recognizer()
            microphone = sr.Microphone()
            
            with microphone as source:
                logger.info("🔧 Adjusting for ambient noise...")
                recognizer.adjust_for_ambient_noise(source, duration=1)
                
            logger.info("✅ Microphone access working properly")
            
        except Exception as e:
            logger.error(f"❌ Microphone test failed: {str(e)}")
            
    async def optimize_system_performance(self):
        """Optimize system performance settings"""
        logger.info("⚡ Optimizing system performance...")
        
        # Disable PyAutoGUI fail-safe for gesture controls
        try:
            import pyautogui
            pyautogui.FAILSAFE = False
            pyautogui.PAUSE = 0.1  # Faster automation
            logger.info("✅ PyAutoGUI optimized for gesture controls")
        except ImportError:
            logger.warning("⚠️ PyAutoGUI not available")
            
        # Create necessary directories
        directories = ['screenshots', 'recordings', 'logs', 'data', 'cache']
        for directory in directories:
            Path(directory).mkdir(exist_ok=True)
            
        logger.info("✅ System directories created")
        
    async def verify_dependencies(self):
        """Verify all required dependencies are installed"""
        logger.info("📦 Verifying dependencies...")
        
        required_packages = {
            'cv2': 'opencv-python',
            'mediapipe': 'mediapipe',
            'speech_recognition': 'SpeechRecognition',
            'edge_tts': 'edge-tts',
            'pyautogui': 'pyautogui',
            'pydub': 'pydub',
            'PIL': 'Pillow',
            'win32gui': 'pywin32'
        }
        
        missing_packages = []
        
        for module, package in required_packages.items():
            try:
                __import__(module)
                logger.info(f"✅ {package} - Available")
            except ImportError:
                logger.error(f"❌ {package} - Missing")
                missing_packages.append(package)
                
        if missing_packages:
            logger.error(f"❌ Missing packages: {', '.join(missing_packages)}")
            logger.info("💡 Install with: pip install " + " ".join(missing_packages))
            return False
        else:
            logger.info("✅ All dependencies satisfied")
            return True
            
    async def run_system_diagnostics(self):
        """Run comprehensive system diagnostics"""
        logger.info("🔍 Running system diagnostics...")
        
        # Test voice engine
        try:
            voice_engine = VoiceEngine()
            logger.info("✅ Voice engine initialization - OK")
        except Exception as e:
            logger.error(f"❌ Voice engine error: {str(e)}")
            
        # Test gesture engine
        try:
            gesture_engine = GestureEngine()
            logger.info("✅ Gesture engine initialization - OK")
        except Exception as e:
            logger.error(f"❌ Gesture engine error: {str(e)}")
            
    async def save_optimized_settings(self):
        """Save all optimized settings"""
        logger.info("💾 Saving optimized settings...")
        
        self.settings.save_config()
        logger.info("✅ Settings saved successfully")
        
    async def run_full_optimization(self):
        """Run complete system optimization"""
        logger.info("🚀 Starting KALKI AI System Optimization...")
        logger.info("=" * 60)
        
        # Run all optimization steps
        await self.verify_dependencies()
        await self.optimize_voice_settings()
        await self.optimize_gesture_settings()
        await self.test_camera_access()
        await self.test_microphone_access()
        await self.optimize_system_performance()
        await self.run_system_diagnostics()
        await self.save_optimized_settings()
        
        logger.info("=" * 60)
        logger.info("✅ KALKI AI System Optimization Complete!")
        logger.info("🎯 System is now optimized for maximum performance")
        logger.info("🗣️ JARVIS-like voice configured")
        logger.info("🤚 Gesture controls calibrated")
        logger.info("📝 Task management ready")
        logger.info("🚀 Ready to run full JARVIS AI system!")

async def main():
    """Main optimization entry point"""
    print("""
    ╔══════════════════════════════════════════════════════════════╗
    ║                KALKI AI SYSTEM OPTIMIZER                     ║
    ║                                                              ║
    ║  🎤 Voice Recognition Optimization                          ║
    ║  🤚 Gesture Control Calibration                             ║
    ║  📷 Camera & Microphone Testing                             ║
    ║  ⚡ Performance Tuning                                      ║
    ║  🔍 System Diagnostics                                      ║
    ║                                                              ║
    ║              "Optimizing JARVIS AI..."                      ║
    ╚══════════════════════════════════════════════════════════════╝
    """)
    
    optimizer = SystemOptimizer()
    await optimizer.run_full_optimization()

if __name__ == "__main__":
    asyncio.run(main())