#!/usr/bin/env python3
"""
KALKI AI - Complete JARVIS System
Full integration with gesture controls, task management, and Hindi-English voice
"""

import asyncio
import sys
from pathlib import Path

# Add project root to Python path
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

from jarvis_main import JarvisAI

async def main():
    """Run complete JARVIS AI system"""
    
    print("""
    ╔══════════════════════════════════════════════════════════════╗
    ║                    KALKI AI - JARVIS                         ║
    ║              Complete AI Assistant System                    ║
    ║                                                              ║
    ║  🎤 Voice: "Fantastic" to activate                          ║
    ║  🤚 Gestures: All hand controls ready                       ║
    ║  📝 Tasks: Voice task management                            ║
    ║  🗣️ Language: Hindi-English mixed                           ║
    ║  🎭 Voice: JARVIS-like male voice                           ║
    ║                                                              ║
    ║  📱 Navigation Gestures:                                     ║
    ║    • Hand Right → Next page                                 ║
    ║    • Hand Left → Previous page                              ║
    ║    • Hand Down → Minimize all                               ║
    ║    • One Finger Up → Restore                                ║
    ║                                                              ║
    ║  🔍 Zoom Controls:                                           ║
    ║    • Both Hands Open → Zoom In                              ║
    ║    • Both Hands Fist → Zoom Out                             ║
    ║                                                              ║
    ║  📸 Capture:                                                 ║
    ║    • Clap → Screenshot                                      ║
    ║    • Prayer Hands → Screen Recording                        ║
    ║                                                              ║
    ║  🎵 Media:                                                   ║
    ║    • Thumbs Up/Down → Volume                                ║
    ║    • Peace Sign → Play/Pause                                ║
    ║    • Pinch → Mute                                           ║
    ║                                                              ║
    ║  📝 Task Commands:                                           ║
    ║    • "Remember this task"                                   ║
    ║    • "Today tasks kya hain"                                 ║
    ║    • "Tomorrow ka kaam"                                     ║
    ║                                                              ║
    ║              "Sir, JARVIS is Ready!"                        ║
    ╚══════════════════════════════════════════════════════════════╝
    """)
    
    # Initialize and start JARVIS
    jarvis = JarvisAI()
    
    try:
        # Initialize all systems
        print("🚀 Initializing JARVIS AI systems...")
        success = await jarvis.initialize()
        
        if not success:
            print("❌ Failed to initialize JARVIS AI")
            return
            
        print("✅ All systems initialized successfully!")
        print("\n🎬 Starting JARVIS AI...")
        print("=" * 60)
        print("🎤 Say 'Fantastic' to activate voice commands")
        print("🤚 Use hand gestures for system control")
        print("📝 Voice task management available")
        print("🗣️ All responses in Hindi-English mix")
        print("=" * 60)
        
        # Start the complete system
        await jarvis.start()
        
    except KeyboardInterrupt:
        print("\n👋 JARVIS AI stopped by user")
        await jarvis.stop()
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        await jarvis.stop()

if __name__ == "__main__":
    print("🎭 KALKI AI - JARVIS System")
    print("🗣️ Hindi-English Voice Assistant")
    print("🤚 Comprehensive Gesture Controls")
    print("📝 Advanced Task Management")
    print()
    
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n👋 Goodbye!")
    except Exception as e:
        print(f"❌ System Error: {str(e)}")
        sys.exit(1)