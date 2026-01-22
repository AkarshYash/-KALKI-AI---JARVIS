#!/usr/bin/env python3
"""
KALKI AI Comprehensive Gesture Control Demo
Demonstrates all gesture features with voice feedback in Hindi-English
"""

import asyncio
import logging
from datetime import datetime
from core.gesture_engine import GestureEngine
from core.voice_engine import VoiceEngine
from core.task_manager import TaskManager
from models.base_models import GestureType

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class MockVoiceEngine:
    """Mock voice engine for demo"""
    
    async def speak(self, text: str):
        """Mock speak function with Hindi-English output"""
        print(f"🗣️ JARVIS: {text}")
        await asyncio.sleep(1)  # Simulate speech time

async def demo_comprehensive_gestures():
    """Demonstrate comprehensive gesture control system"""
    
    print("""
    ╔══════════════════════════════════════════════════════════════╗
    ║                KALKI AI GESTURE CONTROL DEMO                 ║
    ║                                                              ║
    ║  🤚 Comprehensive Hand Gesture Recognition                   ║
    ║  🗣️ Voice Feedback in Hindi-English Mix                     ║
    ║  📱 Navigation, Window, Media & System Controls              ║
    ║  📸 Screenshot & Recording Features                          ║
    ║  🎵 Volume & Media Control                                   ║
    ║                                                              ║
    ║           "Advanced Gesture System Starting..."              ║
    ╚══════════════════════════════════════════════════════════════╝
    """)
    
    # Initialize components
    gesture_engine = GestureEngine()
    mock_voice = MockVoiceEngine()
    
    # Connect voice engine to gesture engine
    gesture_engine.set_voice_engine(mock_voice)
    
    print("\n🎬 GESTURE CONTROL DEMO")
    print("=" * 60)
    
    # Demo 1: Navigation Gestures
    print("\n📢 DEMO 1: Navigation Controls")
    print("-" * 40)
    
    navigation_gestures = [
        (GestureType.WAVE_RIGHT, "Hand wave right - Next page"),
        (GestureType.WAVE_LEFT, "Hand wave left - Previous page"),
        (GestureType.HAND_DOWN, "Hand down - Minimize all windows"),
        (GestureType.POINT_UP, "One finger up - Restore windows")
    ]
    
    for gesture_type, description in navigation_gestures:
        print(f"\n👤 User performs: {description}")
        
        # Simulate gesture execution
        callback = gesture_engine.gesture_callbacks.get(gesture_type)
        if callback:
            feedback = callback()
            await mock_voice.speak(f"Sir, {feedback}")
        
        await asyncio.sleep(1)
    
    # Demo 2: Two-Hand Gestures
    print("\n📢 DEMO 2: Two-Hand Controls")
    print("-" * 40)
    
    two_hand_gestures = [
        (GestureType.ZOOM_IN, "Both hands open - Zoom in"),
        (GestureType.ZOOM_OUT, "Both hands fist - Zoom out"),
        (GestureType.CLAP, "Clap gesture - Screenshot"),
        (GestureType.PRAYER, "Prayer hands - Start recording")
    ]
    
    for gesture_type, description in two_hand_gestures:
        print(f"\n👤 User performs: {description}")
        
        callback = gesture_engine.gesture_callbacks.get(gesture_type)
        if callback:
            feedback = callback()
            await mock_voice.speak(f"Sir, {feedback}")
        
        await asyncio.sleep(1)
    
    # Demo 3: Media Controls
    print("\n📢 DEMO 3: Media & Volume Controls")
    print("-" * 40)
    
    media_gestures = [
        (GestureType.THUMBS_UP, "Thumbs up - Volume up"),
        (GestureType.THUMBS_DOWN, "Thumbs down - Volume down"),
        (GestureType.PEACE_SIGN, "Peace sign - Play/Pause"),
        (GestureType.PINCH, "Pinch gesture - Mute/Unmute")
    ]
    
    for gesture_type, description in media_gestures:
        print(f"\n👤 User performs: {description}")
        
        callback = gesture_engine.gesture_callbacks.get(gesture_type)
        if callback:
            feedback = callback()
            await mock_voice.speak(f"Sir, {feedback}")
        
        await asyncio.sleep(1)
    
    # Demo 4: System Controls
    print("\n📢 DEMO 4: System & Application Controls")
    print("-" * 40)
    
    system_gestures = [
        (GestureType.FIST, "Fist - Close tab"),
        (GestureType.OPEN_PALM, "Open palm - New tab"),
        (GestureType.FOUR_FINGERS, "Four fingers - Show desktop"),
        (GestureType.L_SHAPE, "L-shape - Task Manager"),
        (GestureType.THREE_FINGERS, "Three fingers - Refresh page")
    ]
    
    for gesture_type, description in system_gestures:
        print(f"\n👤 User performs: {description}")
        
        callback = gesture_engine.gesture_callbacks.get(gesture_type)
        if callback:
            feedback = callback()
            await mock_voice.speak(f"Sir, {feedback}")
        
        await asyncio.sleep(1)
    
    # Demo 5: Advanced Features
    print("\n📢 DEMO 5: Advanced Gesture Features")
    print("-" * 40)
    
    print("\n🎯 Gesture Help System:")
    help_text = gesture_engine.get_gesture_help()
    print(help_text)
    
    await mock_voice.speak("Sir, ye saare gesture controls available hain. Koi bhi use kar sakte hain.")
    
    # Demo 6: Voice Integration
    print("\n📢 DEMO 6: Voice Feedback Integration")
    print("-" * 40)
    
    print("\n🗣️ Voice feedback examples:")
    voice_examples = [
        "Sir, next page par gaye",
        "Sir, saare windows minimize kar diye", 
        "Sir, screenshot save kar diya",
        "Sir, volume badha diya",
        "Sir, zoom in kar diya"
    ]
    
    for example in voice_examples:
        await mock_voice.speak(example)
        await asyncio.sleep(0.5)
    
    print("\n🎬 DEMO COMPLETE!")
    print("=" * 60)
    
    print("""
    ✅ Comprehensive Gesture System Features:
    
    📱 Navigation Controls:
    • Hand Right → Next page/tab
    • Hand Left → Previous page/tab  
    • Hand Down → Minimize all windows
    • One Finger Up → Restore windows
    
    🔍 Zoom & View Controls:
    • Both Hands Open → Zoom In
    • Both Hands Fist → Zoom Out
    
    📸 Capture Features:
    • Clap Gesture → Screenshot
    • Prayer Hands → Screen Recording
    
    🎵 Media Controls:
    • Thumbs Up/Down → Volume Control
    • Peace Sign → Play/Pause
    • Pinch → Mute/Unmute
    
    🛠️ System Controls:
    • Fist → Close Tab
    • Open Palm → New Tab
    • Four Fingers → Show Desktop
    • L-Shape → Task Manager
    • Three Fingers → Refresh Page
    
    🗣️ Voice Features:
    • Hindi-English mixed feedback
    • JARVIS-like male voice
    • Real-time action confirmation
    • Gesture help and guidance
    
    🚀 Ready for full JARVIS AI integration!
    """)

if __name__ == "__main__":
    asyncio.run(demo_comprehensive_gestures())