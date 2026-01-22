#!/usr/bin/env python3
"""
Simple JARVIS AI - Working Version
Basic voice and gesture controls
"""

import asyncio
import logging
import cv2
import numpy as np
import pyautogui
import speech_recognition as sr
import edge_tts
import io
from pydub import AudioSegment
import pygame
from datetime import datetime
import threading
import queue

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class SimpleJARVIS:
    """Simple working JARVIS AI"""
    
    def __init__(self):
        self.is_listening = False
        self.gesture_queue = queue.Queue()
        self.tasks = []
        
        # Initialize pygame for audio
        pygame.mixer.init()
        
        # Initialize speech recognition
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()
        
        # Adjust for ambient noise
        with self.microphone as source:
            print("🔧 Adjusting for ambient noise...")
            self.recognizer.adjust_for_ambient_noise(source, duration=1)
            
    async def speak(self, text: str):
        """Speak text using Edge-TTS"""
        try:
            print(f"🗣️ JARVIS: {text}")
            
            # Use Edge-TTS for speech synthesis
            communicate = edge_tts.Communicate(
                text=text,
                voice="en-US-GuyNeural",  # Male JARVIS-like voice
                rate="-10%",
                pitch="-5Hz"
            )
            
            # Generate audio
            audio_data = b""
            async for chunk in communicate.stream():
                if chunk["type"] == "audio":
                    audio_data += chunk["data"]
                    
            if audio_data:
                # Play audio using pygame
                audio_segment = AudioSegment.from_file(io.BytesIO(audio_data), format="mp3")
                
                # Save temporarily and play
                temp_file = "temp_audio.wav"
                audio_segment.export(temp_file, format="wav")
                
                pygame.mixer.music.load(temp_file)
                pygame.mixer.music.play()
                
                # Wait for playback to finish
                while pygame.mixer.music.get_busy():
                    await asyncio.sleep(0.1)
                    
        except Exception as e:
            print(f"❌ Speech error: {str(e)}")
            
    async def listen_for_wake_word(self):
        """Listen for 'Fantastic' wake word"""
        try:
            with self.microphone as source:
                print("🎤 Listening for 'Fantastic'...")
                audio = self.recognizer.listen(source, timeout=1, phrase_time_limit=3)
                
            try:
                text = self.recognizer.recognize_google(audio).lower()
                if "fantastic" in text:
                    print("✅ Wake word detected!")
                    return True
            except sr.UnknownValueError:
                pass
            except sr.RequestError:
                pass
                
            return False
            
        except sr.WaitTimeoutError:
            return False
        except Exception as e:
            print(f"❌ Wake word error: {str(e)}")
            return False
            
    async def record_command(self):
        """Record voice command"""
        try:
            with self.microphone as source:
                print("🎤 Recording command...")
                audio = self.recognizer.listen(source, timeout=5, phrase_time_limit=10)
                
            text = self.recognizer.recognize_google(audio)
            print(f"📝 Command: {text}")
            return text
            
        except sr.UnknownValueError:
            print("❌ Could not understand audio")
            return None
        except sr.RequestError as e:
            print(f"❌ Speech recognition error: {e}")
            return None
        except Exception as e:
            print(f"❌ Recording error: {str(e)}")
            return None
            
    async def process_command(self, command: str):
        """Process voice command"""
        command_lower = command.lower()
        
        # Task management commands
        if "remember" in command_lower or "yaad rakh" in command_lower:
            task = command_lower.replace("remember", "").replace("yaad rakh", "").strip()
            self.tasks.append({
                "task": task,
                "created": datetime.now(),
                "status": "pending"
            })
            await self.speak(f"Task yaad kar liya: {task}")
            
        elif "today task" in command_lower or "aaj ka kaam" in command_lower:
            if self.tasks:
                task_list = "Aaj ke tasks: "
                for i, task in enumerate(self.tasks, 1):
                    task_list += f"{i}. {task['task']} "
                await self.speak(task_list)
            else:
                await self.speak("Aaj koi task nahi hai")
                
        elif "hello" in command_lower or "hi" in command_lower:
            await self.speak("Namaste Sir! JARVIS ready hai. Kya kaam hai?")
            
        elif "time" in command_lower:
            current_time = datetime.now().strftime("%I:%M %p")
            await self.speak(f"Sir, abhi time hai {current_time}")
            
        elif "screenshot" in command_lower:
            self.take_screenshot()
            await self.speak("Screenshot le liya Sir")
            
        else:
            await self.speak("Samajh nahi aaya Sir. Phir se boliye?")
            
    def take_screenshot(self):
        """Take screenshot"""
        try:
            screenshot = pyautogui.screenshot()
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"screenshot_{timestamp}.png"
            screenshot.save(filename)
            print(f"📸 Screenshot saved: {filename}")
        except Exception as e:
            print(f"❌ Screenshot error: {str(e)}")
            
    def detect_gestures(self):
        """Simple gesture detection"""
        try:
            import mediapipe as mp
            
            mp_hands = mp.solutions.hands
            hands = mp_hands.Hands(
                static_image_mode=False,
                max_num_hands=1,
                min_detection_confidence=0.7
            )
            
            cap = cv2.VideoCapture(0)
            
            while True:
                ret, frame = cap.read()
                if not ret:
                    continue
                    
                # Flip frame
                frame = cv2.flip(frame, 1)
                rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                
                # Process frame
                results = hands.process(rgb_frame)
                
                if results.multi_hand_landmarks:
                    for hand_landmarks in results.multi_hand_landmarks:
                        # Simple gesture detection
                        landmarks = hand_landmarks.landmark
                        
                        # Count extended fingers
                        fingers = []
                        
                        # Thumb
                        if landmarks[4].x > landmarks[3].x:
                            fingers.append(1)
                        else:
                            fingers.append(0)
                            
                        # Other fingers
                        for i in [8, 12, 16, 20]:
                            if landmarks[i].y < landmarks[i-2].y:
                                fingers.append(1)
                            else:
                                fingers.append(0)
                                
                        total_fingers = sum(fingers)
                        
                        # Gesture actions
                        if total_fingers == 5:  # Open palm
                            self.gesture_queue.put("open_palm")
                        elif total_fingers == 0:  # Fist
                            self.gesture_queue.put("fist")
                        elif total_fingers == 1 and fingers[1] == 1:  # Index finger
                            self.gesture_queue.put("point")
                            
                # Show frame
                cv2.imshow('JARVIS Gesture Control', frame)
                
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
                    
            cap.release()
            cv2.destroyAllWindows()
            
        except Exception as e:
            print(f"❌ Gesture detection error: {str(e)}")
            
    async def process_gestures(self):
        """Process detected gestures"""
        while True:
            try:
                if not self.gesture_queue.empty():
                    gesture = self.gesture_queue.get_nowait()
                    
                    if gesture == "open_palm":
                        pyautogui.hotkey('ctrl', 't')  # New tab
                        await self.speak("Naya tab khola")
                    elif gesture == "fist":
                        pyautogui.hotkey('ctrl', 'w')  # Close tab
                        await self.speak("Tab band kar diya")
                    elif gesture == "point":
                        self.take_screenshot()
                        await self.speak("Screenshot le liya")
                        
                await asyncio.sleep(0.1)
                
            except queue.Empty:
                await asyncio.sleep(0.1)
            except Exception as e:
                print(f"❌ Gesture processing error: {str(e)}")
                
    async def run(self):
        """Main JARVIS loop"""
        print("""
        ╔══════════════════════════════════════════════════════════════╗
        ║                    SIMPLE JARVIS AI                          ║
        ║                                                              ║
        ║  🎤 Say "Fantastic" to activate                             ║
        ║  🗣️ Hindi-English mixed responses                           ║
        ║  🤚 Basic gesture controls                                  ║
        ║  📝 Simple task management                                  ║
        ║                                                              ║
        ║              "Sir, JARVIS is Ready!"                        ║
        ╚══════════════════════════════════════════════════════════════╝
        """)
        
        await self.speak("Namaste Sir! JARVIS online hai. Fantastic kehkar activate kariye.")
        
        # Start gesture detection in background
        gesture_thread = threading.Thread(target=self.detect_gestures)
        gesture_thread.daemon = True
        gesture_thread.start()
        
        # Start gesture processing
        asyncio.create_task(self.process_gestures())
        
        # Main voice loop
        while True:
            try:
                # Listen for wake word
                if await self.listen_for_wake_word():
                    await self.speak("Haan Sir, kya kaam hai?")
                    
                    # Record command
                    command = await self.record_command()
                    if command:
                        await self.process_command(command)
                    else:
                        await self.speak("Samajh nahi aaya Sir")
                        
                await asyncio.sleep(0.1)
                
            except KeyboardInterrupt:
                print("\n👋 JARVIS shutting down...")
                break
            except Exception as e:
                print(f"❌ Main loop error: {str(e)}")
                await asyncio.sleep(1)

async def main():
    """Run Simple JARVIS"""
    jarvis = SimpleJARVIS()
    await jarvis.run()

if __name__ == "__main__":
    print("🎭 Starting Simple JARVIS AI...")
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n👋 Goodbye!")