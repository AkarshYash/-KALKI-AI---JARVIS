# KALKI AI - Autonomous Cyber Developer & Multilingual Digital Companion

KALKI AI is a next-generation AI operating system assistant, inspired by J.A.R.V.I.S from Iron Man — designed for developers, cybersecurity experts, and creators. It can listen, talk, think, code, automate, search, and adapt, performing any system or online task with a human-like voice and personality.

## Quick Start

1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
   
2. Run the application:
   ```
   # Run with UI (requires PyQt5)
   python run.py
   
   # Run with CLI (no UI dependencies)
   python run.py --cli
   
   # Test voice engine
   python run.py --test-voice
   
   # Test hand gesture engine
   python run.py --test-hand
   ```

## Phase 1 - Core Voice + Chat Assistant with Enhanced Hand Gesture Control

This is the implementation of Phase 1 which includes:
- Voice command detection
- Speech recognition (multilingual)
- Voice output (JARVIS-like tone)
- Text + Voice chat interface
- Enhanced hand gesture recognition for UI control
- Personality & humor

## Features

- Voice input/output
- Text chat interface
- Enhanced hand gesture control for window management
- Additional gestures: Victory sign, Thumbs up, Prayer position, Double open hands
- Basic command processing
- Extensible architecture
- CLI mode for systems without UI support

## Tech Stack

- Python 3.x
- PyQt5 for UI (optional)
- Edge-TTS for voice synthesis
- SpeechRecognition for voice input
- MediaPipe/OpenCV for hand gesture recognition

## Project Structure

```
KalkiAI/
│
├── backend/
│   ├── voice_engine.py          # Voice recognition and synthesis
│   ├── hand_gesture_engine.py   # Hand gesture recognition
│   └── ...
├── ui/
│   ├── app.py                   # PyQt5 UI (optional)
│   └── ...
├── config/
│   └── settings.json            # Configuration file
├── docs/
│   ├── phase1_implementation.md  # Implementation details
│   ├── phase1_summary.md         # Quick summary
│   └── project_blueprint.md      # Complete project vision
├── cli.py                  # Command-line interface
├── run.py                  # Main entry point
├── requirements.txt        # Dependencies
└── README.md               # This file
```

## Enhanced Hand Gesture Control

KALKI AI now supports enhanced hand gesture control for window management:

- **Open hand**: Switch to next tab
- **Wave right**: Switch to next tab
- **Wave left**: Switch to previous tab
- **Point up**: Maximize window
- **Point down**: Minimize all windows
- **Victory sign**: Take screenshot
- **Thumbs up**: Like/Approve
- **Prayer position** (双手合十): Pause/Resume
- **Double open hands**: Fullscreen mode

To use hand gesture control:
1. Run the application with UI: `python run.py`
2. Click "Start Hand Control" button
3. Use hand gestures in front of your camera

Or with CLI:
1. Run: `python run.py --cli`
2. Type "hand-control" command

## Documentation

For detailed information about the implementation, see:
- [Phase 1 Implementation Details](docs/phase1_implementation.md)
- [Phase 1 Summary](docs/phase1_summary.md)
- [Complete Project Blueprint](docs/project_blueprint.md)

## Installation

1. Clone the repository
2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```
   
3. Run the application:
   ```
   # Run with UI (requires PyQt5)
   python run.py
   
   # Run with CLI (no UI dependencies)
   python run.py --cli
   
   # Test voice engine
   python run.py --test-voice
   
   # Test hand gesture engine
   python run.py --test-hand
   ```

On Windows, you can also double-click `run.bat` to use the menu-driven interface.

🎭 KALKI AI - JARVIS SYSTEM OVERVIEW
🚀 What This Tool Does:
This is a complete JARVIS-inspired AI assistant with advanced capabilities:

🎤 VOICE FEATURES:
Wake Word: Say "Fantastic" to activate JARVIS
Language: Hindi-English mixed responses (like you requested)
Voice: Male JARVIS-like voice (not female)
Commands: Natural voice commands for everything
🤚 GESTURE CONTROLS (From Your Video):
Hand Right Wave → Next page/tab
Hand Left Wave → Previous page/tab
Hand Down → Minimize all windows
One Finger Up → Restore from minimize
Both Hands Open → Zoom in
Both Hands Fist → Zoom out
Clap Gesture → Take screenshot
Prayer Hands → Start/Stop screen recording
🎵 ADDITIONAL CONTROLS:
Thumbs Up/Down → Volume control
Peace Sign → Play/Pause media
Pinch → Mute/Unmute
Fist → Close tab
Open Palm → New tab
Four Fingers → Show desktop
📝 TASK MANAGEMENT:
"Remember this task" → Add tasks with voice
"Today tasks kya hain" → Get today's tasks
"Tomorrow ka kaam" → Get tomorrow's tasks
Voice reminders → Daily task summaries
🤖 AI COMPANION:
Proactive conversations → Asks how to help
Regular check-ins → Motivational messages
Smart suggestions → Context-aware help
Human-like personality → Like JARVIS from movies
🛠️ SYSTEM AUTOMATION:
File operations → Create documents, spreadsheets
System control → Window management, app launching
Web automation → Browser control, searches
Code generation → Programming assistance
