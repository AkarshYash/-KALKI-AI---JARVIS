"""
Command Line Interface for KALKI AI
"""

import sys
import os
import time

# Add backend to Python path
sys.path.append(os.path.join(os.path.dirname(__file__), 'backend'))

from backend.voice_engine import VoiceEngine

class KalkiCLI:
    """Command Line Interface for KALKI AI"""
    
    def __init__(self):
        """Initialize the CLI"""
        self.voice_engine = VoiceEngine()
        self.hand_engine = None
        self.running = False
        
        # Try to import hand gesture engine
        try:
            from backend.hand_gesture_engine import HandGestureEngine
            self.hand_engine = HandGestureEngine()
            print("Hand gesture engine initialized.")
        except ImportError:
            print("Hand gesture engine not available. Install with: pip install mediapipe opencv-python numpy")
        except Exception as e:
            print(f"Error initializing hand gesture engine: {e}")
    
    def start(self):
        """Start the CLI interface"""
        print("=" * 50)
        print("KALKI AI - Autonomous Cyber Developer")
        print("=" * 50)
        print("Voice assistant initialized.")
        print("Commands:")
        print("  'listen' - Start voice listening mode")
        print("  'hand-control' - Start hand gesture control")
        print("  'speak <text>' - Speak the given text")
        print("  'quit' - Exit the application")
        print("-" * 50)
        
        self.running = True
        while self.running:
            try:
                user_input = input("\n> ").strip()
                self.process_command(user_input)
            except KeyboardInterrupt:
                print("\nExiting...")
                self.running = False
            except EOFError:
                print("\nExiting...")
                self.running = False
    
    def process_command(self, command: str):
        """Process a user command"""
        if not command:
            return
            
        cmd_parts = command.split()
        cmd = cmd_parts[0].lower()
        
        if cmd == "quit" or cmd == "exit":
            # Stop any running engines
            if self.hand_engine:
                self.hand_engine.stop_detection()
            self.running = False
            print("Goodbye!")
            
        elif cmd == "listen":
            print("Starting voice listening mode. Say something!")
            self.voice_engine.listen(self.voice_callback)
            # Listen for 10 seconds for demo purposes
            time.sleep(10)
            self.voice_engine.stop_listening()
            print("Stopped listening.")
            
        elif cmd == "hand-control":
            if not self.hand_engine:
                print("Hand gesture engine not available.")
                return
                
            print("Starting hand gesture control. Use hand gestures in front of camera.")
            print("Available gestures:")
            print("  - Open hand: Switch to next tab")
            print("  - Wave right: Switch to next tab")
            print("  - Wave left: Switch to previous tab")
            print("  - Point up: Maximize window")
            print("  - Point down: Minimize all windows")
            print("  - Victory sign: Take screenshot")
            print("  - Thumbs up: Like/Approve")
            print("  - Prayer gesture (双手合十): Pause/Resume")
            print("  - Double open hands: Fullscreen mode")
            print("Press Ctrl+C to stop.")
            
            try:
                self.hand_engine.start_detection(self.gesture_callback)
                # Keep running until interrupted
                while self.hand_engine.is_detecting:
                    time.sleep(0.1)
            except KeyboardInterrupt:
                print("\nStopping hand gesture control...")
                self.hand_engine.stop_detection()
                print("Hand gesture control stopped.")
            
        elif cmd == "speak":
            text = " ".join(cmd_parts[1:])
            if text:
                self.voice_engine.speak(text)
            else:
                print("Please provide text to speak.")
                
        elif cmd == "help":
            print("Commands:")
            print("  'listen' - Start voice listening mode")
            print("  'hand-control' - Start hand gesture control")
            print("  'speak <text>' - Speak the given text")
            print("  'quit' - Exit the application")
            
        else:
            # Treat as a text query
            response = self.generate_response(command)
            print(f"KALKI AI: {response}")
            self.voice_engine.speak(response)
    
    def voice_callback(self, text: str):
        """Callback for voice recognition"""
        print(f"\nYou said: {text}")
        response = self.generate_response(text)
        print(f"KALKI AI: {response}")
        self.voice_engine.speak(response)
    
    def gesture_callback(self, gesture: str):
        """Callback for hand gesture recognition"""
        print(f"\nDetected gesture: {gesture}")
        
        # Map gestures to actions
        if gesture == "hand_open" or gesture == "wave_right":
            action = "Switching to next tab"
        elif gesture == "wave_left":
            action = "Switching to previous tab"
        elif gesture == "point_up":
            action = "Maximizing window"
        elif gesture == "point_down":
            action = "Minimizing all windows"
        elif gesture == "victory":
            action = "Taking screenshot"
        elif gesture == "thumbs_up":
            action = "Liked! Approved!"
        elif gesture == "prayer":
            action = "Pause/Resume toggle"
        elif gesture == "double_open":
            action = "Entering fullscreen mode"
        else:
            action = "Unknown gesture"
            
        print(f"KALKI AI: {action}")
        # In a full implementation, this would actually control the OS
        self.voice_engine.speak(action)
    
    def generate_response(self, user_input: str) -> str:
        """Generate a response to user input"""
        # This is a placeholder - in a real implementation, this would connect to
        # an AI model or command parser
        
        responses = {
            "hello": "Hello there! How can I assist you today?",
            "hi": "Greetings! What can I do for you?",
            "how are you": "I'm functioning optimally, thank you for asking!",
            "what can you do": "I can help with coding, file management, cybersecurity tasks, and general assistance. Try asking me to create a file or explain a concept!",
            "who are you": "I am KALKI AI, your autonomous cyber developer assistant. I'm here to help with all your development and automation needs.",
            "thank you": "You're welcome! Is there anything else I can help with?",
            "bye": "Goodbye! Feel free to call on me whenever you need assistance."
        }
        
        # Check for exact matches
        input_lower = user_input.lower()
        for key, response in responses.items():
            if key in input_lower:
                return response
                
        # Default response
        return "I understand. How else can I assist you with that?"

def main():
    """Main entry point for CLI version"""
    cli = KalkiCLI()
    cli.start()

if __name__ == "__main__":
    main()