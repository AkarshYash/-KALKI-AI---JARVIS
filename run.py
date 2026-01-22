#!/usr/bin/env python3
"""
KALKI AI - Main Entry Point
"""

import sys
import os
import argparse

# Add backend to Python path
sys.path.append(os.path.join(os.path.dirname(__file__), 'backend'))

def main():
    """Main entry point for KALKI AI"""
    parser = argparse.ArgumentParser(description="KALKI AI - Autonomous Cyber Developer")
    parser.add_argument("--cli", action="store_true", help="Run in command-line interface mode")
    parser.add_argument("--test-voice", action="store_true", help="Test voice engine")
    parser.add_argument("--test-hand", action="store_true", help="Test hand gesture engine")
    
    args = parser.parse_args()
    
    if args.test_voice:
        from backend.voice_engine import VoiceEngine
        print("Testing voice engine...")
        voice_engine = VoiceEngine()
        voice_engine.speak("Hello, I am KALKI AI. Your autonomous cyber developer assistant.")
        print("Voice test completed. Check your speakers.")
        return
    
    if args.test_hand:
        try:
            from backend.hand_gesture_engine import HandGestureEngine
            print("Testing hand gesture engine...")
            print("Please place your hand in front of the camera.")
            print("Available gestures to test:")
            print("  - Open hand")
            print("  - Wave right (thumb extended)")
            print("  - Wave left (pinky extended)")
            print("  - Point up (index finger)")
            print("  - Point down (fist)")
            print("  - Victory sign (V sign)")
            print("  - Thumbs up")
            print("  - Prayer gesture (双手合十)")
            print("  - Double open hands")
            print("Press Ctrl+C to stop.")
            
            engine = HandGestureEngine()
            
            def gesture_callback(gesture):
                print(f"Detected gesture: {gesture}")
            
            engine.start_detection(gesture_callback)
            
            try:
                import time
                while True:
                    time.sleep(1)
            except KeyboardInterrupt:
                engine.stop_detection()
                print("Hand gesture test completed.")
        except ImportError:
            print("Hand gesture engine not available. Please install dependencies:")
            print("pip install mediapipe opencv-python numpy")
        return
    
    if args.cli:
        # Run CLI version
        print("Initializing KALKI AI in CLI mode...")
        from cli import KalkiCLI
        cli = KalkiCLI()
        cli.start()
    else:
        # Try to run UI version
        try:
            from ui.app import KalkiApp
            from backend.voice_engine import VoiceEngine
            
            print("Initializing KALKI AI...")
            voice_engine = VoiceEngine()
            app = KalkiApp(voice_engine)
            app.run()
        except ImportError as e:
            print(f"UI dependencies not available: {e}")
            print("Run with --cli flag to use command-line interface")
            print("Or install dependencies with: pip install -r requirements.txt")

if __name__ == "__main__":
    main()