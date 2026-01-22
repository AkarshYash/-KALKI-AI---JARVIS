#!/usr/bin/env python3
"""
KALKI AI - JARVIS-Style AI Assistant
Enhanced with Task Management and Hindi-English Voice
Inspired by: https://github.com/rajkishorbgp/JARVIS-AI-Assistant.git
"""

import asyncio
import logging
import sys
import os
from pathlib import Path
from datetime import datetime
import signal

# Add project root to Python path
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

from core.voice_engine import VoiceEngine
from core.companion_engine import CompanionEngine
from core.task_manager import TaskManager
from core.nlp_engine import NLPEngine
from config.settings import Settings

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('logs/jarvis_ai.log'),
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger(__name__)

class JarvisAI:
    """Main JARVIS AI Assistant with Task Management"""
    
    def __init__(self):
        self.settings = Settings()
        self.voice_engine = VoiceEngine()
        self.nlp_engine = NLPEngine()
        self.task_manager = TaskManager()
        self.companion_engine = CompanionEngine(self.voice_engine, self.nlp_engine)
        
        self.running = False
        
    async def initialize(self):
        """Initialize all components"""
        try:
            logger.info("🚀 Initializing JARVIS AI Assistant...")
            
            # Create necessary directories
            self._create_directories()
            
            # Initialize components
            voice_success = await self.voice_engine.initialize()
            nlp_success = await self.nlp_engine.initialize()
            task_success = await self.task_manager.initialize()
            companion_success = await self.companion_engine.initialize()
            
            # Initialize gesture engine
            from core.gesture_engine import GestureEngine
            self.gesture_engine = GestureEngine()
            gesture_success = await self.gesture_engine.initialize()
            
            if all([voice_success, nlp_success, task_success, companion_success, gesture_success]):
                # Connect components
                self.voice_engine.set_task_manager(self.task_manager)
                self.task_manager.set_voice_engine(self.voice_engine)
                self.gesture_engine.set_voice_engine(self.voice_engine)
                
                # Register voice command callback
                self.voice_engine.register_callback("voice_command", self._handle_voice_command)
                
                # Announce gesture system ready
                await self.gesture_engine.announce_gesture_ready()
                
                logger.info("✅ JARVIS AI Assistant with Gesture Controls initialized successfully!")
                return True
            else:
                logger.error("❌ Failed to initialize some components")
                return False
                
        except Exception as e:
            logger.error(f"❌ Initialization error: {str(e)}")
            return False
            
    def _create_directories(self):
        """Create necessary directories"""
        directories = ['logs', 'data', 'cache', 'models']
        for directory in directories:
            Path(directory).mkdir(parents=True, exist_ok=True)
            
    async def _handle_voice_command(self, command: str):
        """Handle voice commands including gesture help"""
        try:
            logger.info(f"🎤 Processing command: {command}")
            
            # Check for gesture help commands
            if any(phrase in command.lower() for phrase in ['gesture help', 'gesture commands', 'hand controls', 'gesture kya hai']):
                if hasattr(self, 'gesture_engine'):
                    help_text = self.gesture_engine.get_gesture_help()
                    await self.voice_engine.speak("Sir, ye gesture controls available hain:")
                    # Summarize key gestures in voice
                    summary = "Hand right wave next page ke liye, hand left wave previous page ke liye, hand down minimize ke liye, clap screenshot ke liye, prayer hands recording ke liye use kar sakte hain."
                    await self.voice_engine.speak(summary)
                return
            
            # Check for task management commands
            task_response = await self.task_manager.process_voice_command(command)
            
            if task_response != "Task management ke liye 'remember this', 'today tasks', 'tomorrow tasks' ya 'complete task' keh sakte hain.":
                # Task command processed
                await self.voice_engine.speak(task_response)
            else:
                # Process through companion engine
                companion = self.companion_engine.get_companion()
                response = await companion._process_user_input(command)
                await self.voice_engine.speak(response)
                
        except Exception as e:
            logger.error(f"Voice command handling error: {str(e)}")
            await self.voice_engine.speak("Sir, command process karne mein problem hui.")
            
    async def start(self):
        """Start JARVIS AI Assistant with all features"""
        try:
            self.running = True
            
            logger.info("🎬 JARVIS AI Assistant Starting...")
            logger.info("=" * 60)
            
            # Welcome message with gesture info
            welcome_msg = "Namaste Sir! JARVIS online hai. Voice ke liye 'Fantastic' kahiye, gesture controls bhi ready hain."
            await self.voice_engine.speak(welcome_msg)
            
            # Start gesture monitoring
            if hasattr(self, 'gesture_engine'):
                asyncio.create_task(self.gesture_engine.start_monitoring())
                logger.info("🤚 Gesture recognition started")
            
            # Start companion mode
            await self.companion_engine.start_companion_mode()
            
        except Exception as e:
            logger.error(f"Start error: {str(e)}")
            
    async def stop(self):
        """Stop JARVIS AI Assistant"""
        try:
            logger.info("🔄 JARVIS AI Assistant shutting down...")
            
            self.running = False
            
            # Cleanup components
            await self.voice_engine.cleanup()
            
            if hasattr(self, 'gesture_engine'):
                await self.gesture_engine.cleanup()
            
            logger.info("✅ JARVIS AI Assistant shutdown complete")
            
        except Exception as e:
            logger.error(f"Shutdown error: {str(e)}")
            
    def setup_signal_handlers(self):
        """Setup signal handlers for graceful shutdown"""
        def signal_handler(signum, frame):
            logger.info(f"Received signal {signum}, shutting down...")
            asyncio.create_task(self.stop())
            
        signal.signal(signal.SIGINT, signal_handler)
        signal.signal(signal.SIGTERM, signal_handler)

async def main():
    """Main entry point"""
    print("""
    ╔══════════════════════════════════════════════════════════════╗
    ║                        JARVIS AI                             ║
    ║              Advanced AI Assistant with Tasks                ║
    ║                                                              ║
    ║  🎤 Voice: "Fantastic" to activate                          ║
    ║  🗣️ Language: Hindi-English Mixed                           ║
    ║  📝 Tasks: "Remember this", "Today tasks"                   ║
    ║  🤖 Proactive: Regular check-ins & suggestions              ║
    ║  🎭 Personality: JARVIS-like male voice                     ║
    ║                                                              ║
    ║              "Sir, JARVIS is Ready!"                        ║
    ╚══════════════════════════════════════════════════════════════╝
    """)
    
    jarvis = JarvisAI()
    
    try:
        # Setup signal handlers
        jarvis.setup_signal_handlers()
        
        # Initialize
        success = await jarvis.initialize()
        if not success:
            logger.error("Failed to initialize JARVIS AI")
            sys.exit(1)
            
        # Start
        await jarvis.start()
        
    except KeyboardInterrupt:
        logger.info("Interrupted by user")
        await jarvis.stop()
    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}")
        await jarvis.stop()
        sys.exit(1)

if __name__ == "__main__":
    # Run JARVIS AI
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n👋 JARVIS AI Assistant stopped by user")
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        sys.exit(1)