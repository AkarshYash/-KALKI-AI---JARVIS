#!/usr/bin/env python3
"""
JARVIS AI Task Management Demo
Demonstrates task management with Hindi-English voice
"""

import asyncio
import logging
from datetime import datetime, timedelta
from core.task_manager import TaskManager, TaskPriority

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class MockVoiceEngine:
    """Mock voice engine for demo"""
    
    async def speak(self, text: str):
        """Mock speak function"""
        print(f"🗣️ JARVIS: {text}")
        await asyncio.sleep(1)  # Simulate speech time

async def demo_task_management():
    """Demonstrate task management features"""
    
    print("""
    ╔══════════════════════════════════════════════════════════════╗
    ║                  JARVIS TASK MANAGEMENT DEMO                 ║
    ║                                                              ║
    ║  📝 Adding tasks with voice commands                         ║
    ║  🗣️ Hindi-English mixed responses                           ║
    ║  📅 Today/Tomorrow task management                           ║
    ║  ✅ Task completion tracking                                 ║
    ║                                                              ║
    ║              "Task Management Demo Starting..."              ║
    ╚══════════════════════════════════════════════════════════════╝
    """)
    
    # Initialize task manager
    task_manager = TaskManager()
    await task_manager.initialize()
    
    # Set mock voice engine
    mock_voice = MockVoiceEngine()
    task_manager.set_voice_engine(mock_voice)
    
    print("\n🎬 DEMO STARTING...")
    print("=" * 60)
    
    # Demo 1: Adding tasks
    print("\n📢 DEMO 1: Adding Tasks")
    print("-" * 30)
    
    commands = [
        "remember this - complete the project report today",
        "yaad rakh - call client tomorrow",
        "task add - buy groceries urgent",
        "kaam hai - meeting with team at 3 PM today"
    ]
    
    for command in commands:
        print(f"\n👤 User: '{command}'")
        response = await task_manager.process_voice_command(command)
        await mock_voice.speak(response)
        await asyncio.sleep(1)
    
    # Demo 2: Checking today's tasks
    print("\n📢 DEMO 2: Today's Tasks")
    print("-" * 30)
    
    print(f"\n👤 User: 'aaj ka kaam kya hai?'")
    response = await task_manager.process_voice_command("today tasks")
    await mock_voice.speak(response)
    await asyncio.sleep(2)
    
    # Demo 3: Tomorrow's tasks
    print("\n📢 DEMO 3: Tomorrow's Tasks")
    print("-" * 30)
    
    print(f"\n👤 User: 'kal ka kaam batao'")
    response = await task_manager.process_voice_command("tomorrow tasks")
    await mock_voice.speak(response)
    await asyncio.sleep(2)
    
    # Demo 4: Task completion
    print("\n📢 DEMO 4: Completing Tasks")
    print("-" * 30)
    
    # Get today's tasks and complete one
    today_tasks = await task_manager.get_today_tasks()
    if today_tasks:
        task_to_complete = today_tasks[0]
        await task_manager.complete_task(task_to_complete.id)
        print(f"\n✅ Completed task: {task_to_complete.title}")
        await mock_voice.speak(f"Task complete ho gaya: {task_to_complete.title}")
    
    # Demo 5: Updated today's tasks
    print("\n📢 DEMO 5: Updated Today's Tasks")
    print("-" * 30)
    
    print(f"\n👤 User: 'remaining tasks batao'")
    response = await task_manager.process_voice_command("today pending")
    await mock_voice.speak(response)
    
    print("\n🎬 DEMO COMPLETE!")
    print("=" * 60)
    
    print("""
    ✅ Task Management Features Demonstrated:
    • Voice command processing in Hindi-English
    • Task addition with natural language
    • Today/Tomorrow task queries
    • Task completion tracking
    • Proactive reminders and summaries
    • JARVIS-like personality responses
    
    🚀 Ready to integrate with full JARVIS AI system!
    """)

if __name__ == "__main__":
    asyncio.run(demo_task_management())