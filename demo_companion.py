#!/usr/bin/env python3
"""
KALKI AI Companion Demo
Shows the proactive AI companion in action
"""

import asyncio
import logging
import random
from datetime import datetime

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class MockVoiceEngine:
    """Mock voice engine for demo"""
    
    async def speak(self, text: str):
        """Simulate speaking"""
        print(f"\n🗣️ KALKI: {text}")
        await asyncio.sleep(len(text) * 0.05)  # Simulate speech duration

class MockNLPEngine:
    """Mock NLP engine for demo"""
    pass

async def demo_companion():
    """Demo the companion functionality"""
    
    print("""
    ╔══════════════════════════════════════════════════════════════╗
    ║                    KALKI AI COMPANION DEMO                   ║
    ║              Proactive AI Assistant Experience               ║
    ║                                                              ║
     ║  🎤 Activates with "Fantastic"                            ║
     ║  🤖 Proactively asks how to help                          ║
     ║  💬 Talks regularly and gives suggestions                 ║ 
     ║  🎭 Animated communication like a human                   ║
    ║                                                              ║
    ║                "Your AI Companion is Ready!"                 ║
    ╚══════════════════════════════════════════════════════════════╝
    """)
    
    # Initialize mock engines
    voice_engine = MockVoiceEngine()
    nlp_engine = MockNLPEngine()
    
    # Import and initialize companion
    from core.companion_engine import CompanionEngine
    
    companion_engine = CompanionEngine(voice_engine, nlp_engine)
    await companion_engine.initialize()
    
    companion = companion_engine.get_companion()
    animated_ui = companion_engine.get_animated_ui()
    
    print("\n🎬 DEMO STARTING...")
    print("=" * 60)
    
    # Demo 1: Wake word activation
    print("\n📢 DEMO 1: Wake Word Activation")
    print("User says: 'Fantastic'")
    await asyncio.sleep(1)
    
    animated_ui.set_animation_state('listening')
    print(f"🎭 Animation: {animated_ui.get_current_animation()} (Listening)")
    
    await companion._handle_activation()
    
    # Demo 2: Proactive suggestions
    print("\n📢 DEMO 2: Proactive Suggestions")
    await asyncio.sleep(2)
    
    animated_ui.set_animation_state('thinking')
    print(f"🎭 Animation: {animated_ui.get_current_animation()} (Thinking)")
    await asyncio.sleep(1)
    
    suggestions = [
        "I notice you've been working hard! How about I help organize your desktop files?",
        "Would you like me to create a quick backup of your current project?",
        "I can generate some code templates to speed up your development. Interested?",
        "How about I search for the latest updates in your field of work?",
        "I could help you create a productivity report for today. What do you think?"
    ]
    
    for suggestion in suggestions[:3]:
        animated_ui.set_animation_state('speaking')
        print(f"🎭 Animation: {animated_ui.get_current_animation()} (Speaking)")
        await voice_engine.speak(suggestion)
        await asyncio.sleep(1)
        
        animated_ui.set_animation_state('listening')
        print(f"🎭 Animation: {animated_ui.get_current_animation()} (Waiting for response)")
        await asyncio.sleep(2)
    
    # Demo 3: Regular check-ins
    print("\n📢 DEMO 3: Regular Check-ins")
    
    check_ins = [
        "How's your progress going? I'm here if you need any assistance!",
        "You're doing fantastic work! Keep up the great momentum!",
        "I've been thinking - would you like me to automate any of these repetitive tasks?",
        "Just checking in - is there anything challenging you right now that I could help with?"
    ]
    
    for check_in in check_ins[:2]:
        await asyncio.sleep(3)
        animated_ui.set_animation_state('excited')
        print(f"🎭 Animation: {animated_ui.get_current_animation()} (Excited to help)")
        await voice_engine.speak(check_in)
        
        animated_ui.set_animation_state('listening')
        print(f"🎭 Animation: {animated_ui.get_current_animation()} (Listening)")
        await asyncio.sleep(2)
    
    # Demo 4: Task assistance
    print("\n📢 DEMO 4: Task Assistance")
    print("User says: 'I need to create some documents'")
    
    animated_ui.set_animation_state('working')
    print(f"🎭 Animation: {animated_ui.get_current_animation()} (Working)")
    
    task_responses = [
        "Excellent! I love helping with document creation. What type of documents do you need?",
        "I can create Word documents, Excel spreadsheets, PDFs, or any other format you need!",
        "Would you like me to start with a template, or do you have specific content in mind?",
        "I'm ready to generate professional documents for you. Just tell me the details!"
    ]
    
    for response in task_responses[:2]:
        await voice_engine.speak(response)
        await asyncio.sleep(1)
    
    # Demo 5: Encouragement and motivation
    print("\n📢 DEMO 5: Encouragement & Motivation")
    
    encouragements = [
        "You're absolutely crushing it today! Your productivity is inspiring!",
        "I love seeing you tackle challenges with such determination!",
        "Your problem-solving approach is brilliant - I'm learning from you!",
        "Keep up this amazing energy! You're making incredible progress!"
    ]
    
    for encouragement in encouragements[:2]:
        await asyncio.sleep(2)
        animated_ui.set_animation_state('excited')
        print(f"🎭 Animation: {animated_ui.get_current_animation()} (Enthusiastic)")
        await voice_engine.speak(encouragement)
    
    # Demo 6: Conversation and ideas
    print("\n📢 DEMO 6: Conversation & Ideas")
    
    conversation_starters = [
        "I'm curious about your current project - what's the most exciting part?",
        "I've been thinking of ways to optimize your workflow. Want to brainstorm together?",
        "What's your biggest goal for this week? I'd love to help you achieve it!",
        "Tell me about what you're learning lately - I might have some resources to share!"
    ]
    
    for starter in conversation_starters[:2]:
        await asyncio.sleep(2)
        animated_ui.set_animation_state('thinking')
        print(f"🎭 Animation: {animated_ui.get_current_animation()} (Curious)")
        await voice_engine.speak(starter)
        
        animated_ui.set_animation_state('listening')
        print(f"🎭 Animation: {animated_ui.get_current_animation()} (Engaged listening)")
        await asyncio.sleep(2)
    
    # Demo finale
    print("\n📢 DEMO FINALE: Always Available")
    await asyncio.sleep(2)
    
    animated_ui.set_animation_state('idle')
    print(f"🎭 Animation: {animated_ui.get_current_animation()} (Friendly and ready)")
    
    finale_message = "I'm always here as your AI companion! Just say 'Fantastic' anytime you need me. I'll proactively check in, offer suggestions, help with tasks, and keep you motivated. We're a team!"
    
    await voice_engine.speak(finale_message)
    
    print("\n" + "=" * 60)
    print("🎬 DEMO COMPLETE!")
    print("\nThis is how KALKI AI works as your proactive companion:")
    print("✅ Activates with 'Fantastic'")
    print("✅ Proactively offers help and suggestions")
    print("✅ Regular check-ins and encouragement")
    print("✅ Animated, human-like communication")
    print("✅ Always ready to assist with any task")
    print("✅ Learns your patterns and adapts")
    
    print("\n🚀 Ready to run the full KALKI AI system!")

async def main():
    """Main demo function"""
    try:
        await demo_companion()
    except KeyboardInterrupt:
        print("\n👋 Demo interrupted by user")
    except Exception as e:
        logger.error(f"Demo error: {str(e)}")

if __name__ == "__main__":
    asyncio.run(main())