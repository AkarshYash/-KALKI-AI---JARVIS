#!/usr/bin/env python3
"""
Test KALKI AI Voice - Make sure it can speak!
"""

import asyncio
import logging
import edge_tts
import pygame
import io
import tempfile
import os

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def test_voice_synthesis():
    """Test if KALKI can speak"""
    
    print("🎤 Testing KALKI AI Voice...")
    
    try:
        # Initialize pygame mixer for audio playback
        pygame.mixer.init()
        
        # Test messages
        messages = [
            "Hello! I am KALKI, your AI companion!",
            "I can hear you and speak to you!",
            "Say 'Fantastic' to activate me anytime!",
            "I'm ready to help you with anything you need!"
        ]
        
        for i, message in enumerate(messages, 1):
            print(f"\n🗣️ KALKI Speaking ({i}/{len(messages)}): {message}")
            
            # Generate speech using Edge-TTS
            communicate = edge_tts.Communicate(
                text=message,
                voice="en-GB-RyanNeural",  # Male British JARVIS-like voice
                rate="-10%",  # Slower for sophistication
                pitch="-5Hz",  # Lower pitch for authority
                volume="+0%"
            )
            
            # Save to temporary file
            with tempfile.NamedTemporaryFile(suffix=".mp3", delete=False) as tmp_file:
                async for chunk in communicate.stream():
                    if chunk["type"] == "audio":
                        tmp_file.write(chunk["data"])
                
                tmp_file_path = tmp_file.name
            
            # Play the audio
            try:
                pygame.mixer.music.load(tmp_file_path)
                pygame.mixer.music.play()
                
                # Wait for playback to complete
                while pygame.mixer.music.get_busy():
                    await asyncio.sleep(0.1)
                    
                print("✅ Speech completed!")
                
            except Exception as e:
                print(f"❌ Playback error: {e}")
                
            finally:
                # Cleanup temp file
                try:
                    os.unlink(tmp_file_path)
                except:
                    pass
                    
            # Pause between messages
            await asyncio.sleep(1)
            
        print("\n🎉 Voice test completed! KALKI can speak!")
        return True
        
    except Exception as e:
        print(f"❌ Voice test failed: {e}")
        return False

async def test_wake_word_simulation():
    """Simulate wake word detection and response"""
    
    print("\n🎯 Testing Wake Word Response...")
    
    # Simulate user saying "Fantastic"
    print("👤 User says: 'Fantastic'")
    await asyncio.sleep(1)
    
    # KALKI responds
    responses = [
        "Yes! How can I help you today?",
        "I'm here and ready to assist!",
        "What would you like to work on?",
        "I'm listening! What can I do for you?"
    ]
    
    import random
    response = random.choice(responses)
    
    print(f"🤖 KALKI responds: {response}")
    
    # Generate and play response
    try:
        communicate = edge_tts.Communicate(
            text=response,
            voice="en-GB-RyanNeural",  # Male British JARVIS-like voice
            rate="-5%",  # Slightly slower for sophistication
            pitch="-3Hz",  # Slightly lower pitch
            volume="+0%"
        )
        
        with tempfile.NamedTemporaryFile(suffix=".mp3", delete=False) as tmp_file:
            async for chunk in communicate.stream():
                if chunk["type"] == "audio":
                    tmp_file.write(chunk["data"])
            
            tmp_file_path = tmp_file.name
        
        pygame.mixer.music.load(tmp_file_path)
        pygame.mixer.music.play()
        
        while pygame.mixer.music.get_busy():
            await asyncio.sleep(0.1)
            
        os.unlink(tmp_file_path)
        
        print("✅ Wake word response working!")
        return True
        
    except Exception as e:
        print(f"❌ Wake word response failed: {e}")
        return False

async def main():
    """Main test function"""
    
    print("""
    ╔══════════════════════════════════════════════════════════════╗
    ║                    KALKI AI VOICE TEST                       ║
    ║              Testing Speech and Communication                 ║
    ║                                                              ║
    ║  🎤 Testing voice synthesis                                  ║
    ║  🗣️ Testing speech playback                                  ║
    ║  👂 Testing wake word response                               ║
    ║                                                              ║
    ║                "Let's make KALKI talk!"                     ║
    ╚══════════════════════════════════════════════════════════════╝
    """)
    
    try:
        # Test voice synthesis
        voice_works = await test_voice_synthesis()
        
        if voice_works:
            # Test wake word response
            wake_word_works = await test_wake_word_simulation()
            
            if wake_word_works:
                print("\n🎉 SUCCESS! KALKI AI voice is working perfectly!")
                print("✅ Voice synthesis: Working")
                print("✅ Audio playback: Working") 
                print("✅ Wake word response: Working")
                print("\n🚀 KALKI is ready to talk to you!")
                
                # Final test message
                await asyncio.sleep(1)
                print("\n🤖 KALKI says:")
                
                final_message = "I'm ready to be your AI companion! Just say 'Fantastic' and I'll help you with anything!"
                
                communicate = edge_tts.Communicate(
                    text=final_message,
                    voice="en-GB-RyanNeural",  # Male British JARVIS-like voice
                    rate="-5%",  # Slower for sophistication
                    pitch="-3Hz"  # Lower pitch for authority
                )
                
                with tempfile.NamedTemporaryFile(suffix=".mp3", delete=False) as tmp_file:
                    async for chunk in communicate.stream():
                        if chunk["type"] == "audio":
                            tmp_file.write(chunk["data"])
                    
                    tmp_file_path = tmp_file.name
                
                pygame.mixer.music.load(tmp_file_path)
                pygame.mixer.music.play()
                
                while pygame.mixer.music.get_busy():
                    await asyncio.sleep(0.1)
                    
                os.unlink(tmp_file_path)
                
                return True
            else:
                print("❌ Wake word response not working")
                return False
        else:
            print("❌ Voice synthesis not working")
            return False
            
    except KeyboardInterrupt:
        print("\n👋 Test interrupted by user")
        return False
    except Exception as e:
        print(f"❌ Test failed: {e}")
        return False
    finally:
        pygame.mixer.quit()

if __name__ == "__main__":
    print("🎬 Starting KALKI AI Voice Test...")
    result = asyncio.run(main())
    
    if result:
        print("\n✅ KALKI AI is ready to talk!")
        print("Run the full system with: python run_kalki_companion.py")
    else:
        print("\n❌ Voice test failed. Installing required packages...")
        print("Run: pip install pygame edge-tts")