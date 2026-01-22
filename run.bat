@echo off
title KALKI AI - Autonomous Cyber Developer

echo ========================================
echo KALKI AI - Autonomous Cyber Developer
echo ========================================

echo.
echo Select an option:
echo 1. Run with UI (requires dependencies)
echo 2. Run with CLI (command-line interface)
echo 3. Test voice engine
echo 4. Test hand gesture engine
echo 5. Install dependencies
echo 6. Exit
echo.

choice /c 123456 /m "Enter your choice"

if errorlevel 6 goto :exit
if errorlevel 5 goto :install
if errorlevel 4 goto :test_hand
if errorlevel 3 goto :test_voice
if errorlevel 2 goto :run_cli
if errorlevel 1 goto :run_ui

:run_ui
echo Running KALKI AI with UI...
python run.py
goto :end

:run_cli
echo Running KALKI AI with CLI...
python run.py --cli
goto :end

:test_voice
echo Testing voice engine...
python run.py --test-voice
goto :end

:test_hand
echo Testing hand gesture engine...
echo Please place your hand in front of the camera.
echo Press Ctrl+C to stop.
python run.py --test-hand
goto :end

:install
echo Installing dependencies...
pip install -r requirements.txt
goto :end

:exit
echo Exiting...
goto :end

:end
echo.
echo Press any key to exit...
pause >nul