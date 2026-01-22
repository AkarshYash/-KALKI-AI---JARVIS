"""
Test script for KALKI AI components
"""

import sys
import os
import time

# Add backend to Python path
sys.path.append(os.path.join(os.path.dirname(__file__), 'backend'))

def test_voice_engine():
    """Test the voice engine"""
    print("Testing Voice Engine...")
    
    try:
        from backend.voice_engine import VoiceEngine
        engine = VoiceEngine()
        
        print("Voice engine initialized successfully.")
        print("Testing speech output...")
        
        # Test speaking
        engine.speak("Hello, this is a test of the KALKI AI voice engine.")
        
        print("Speech output test completed.")
        print("Waiting 3 seconds for speech to complete...")
        time.sleep(3)
        
        print("Voice engine test completed successfully!")
        return True
        
    except Exception as e:
        print(f"Error testing voice engine: {e}")
        return False

def test_cli():
    """Test the CLI"""
    print("Testing CLI...")
    
    try:
        from cli import KalkiCLI
        print("CLI imported successfully.")
        print("CLI test completed successfully!")
        return True
        
    except Exception as e:
        print(f"Error testing CLI: {e}")
        return False

def test_hand_gesture_engine():
    """Test the hand gesture engine"""
    print("Testing Hand Gesture Engine...")
    
    try:
        from backend.hand_gesture_engine import HandGestureEngine
        print("Hand gesture engine imported successfully.")
        
        # Test initialization
        engine = HandGestureEngine()
        print("Hand gesture engine initialized successfully.")
        
        print("Hand gesture engine test completed successfully!")
        return True
        
    except ImportError:
        print("Hand gesture engine not available (missing dependencies).")
        return True  # This is not a failure, just missing optional dependencies
    except Exception as e:
        print(f"Error testing hand gesture engine: {e}")
        return False

def test_configuration():
    """Test configuration loading"""
    print("Testing Configuration...")
    
    try:
        from backend.hand_gesture_engine import load_config
        config = load_config()
        print("Configuration loaded successfully.")
        
        # Check if hand gesture config exists
        if 'hand_gestures' in config:
            print("Hand gesture configuration found.")
            print(f"Camera index: {config['hand_gestures'].get('camera_index', 0)}")
            print(f"Detection confidence: {config['hand_gestures'].get('min_detection_confidence', 0.7)}")
        else:
            print("Hand gesture configuration not found in settings.")
        
        print("Configuration test completed successfully!")
        return True
        
    except Exception as e:
        print(f"Error testing configuration: {e}")
        return False

if __name__ == "__main__":
    print("Running KALKI AI tests...")
    print("=" * 40)
    
    # Test voice engine
    voice_success = test_voice_engine()
    print()
    
    # Test CLI
    cli_success = test_cli()
    print()
    
    # Test hand gesture engine
    hand_success = test_hand_gesture_engine()
    print()
    
    # Test configuration
    config_success = test_configuration()
    print()
    
    # Summary
    print("=" * 40)
    print("Test Summary:")
    print(f"Voice Engine: {'PASS' if voice_success else 'FAIL'}")
    print(f"CLI: {'PASS' if cli_success else 'FAIL'}")
    print(f"Hand Gesture Engine: {'PASS' if hand_success else 'FAIL'}")
    print(f"Configuration: {'PASS' if config_success else 'FAIL'}")
    
    if voice_success and cli_success and hand_success and config_success:
        print("\nAll tests passed! KALKI AI is ready to use.")
    else:
        print("\nSome tests failed. Please check the errors above.")