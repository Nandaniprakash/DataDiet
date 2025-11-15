@echo off
REM --- SET API KEY FOR THE SESSION (REPLACE WITH YOUR KEY) ---
set GOOGLE_API_KEY="AIzaSyCFJVFMLiN07bq_N3ajc118DgD70sPBm0k"

REM --- ACTIVATE VIRTUAL ENVIRONMENT ---
call .venv\Scripts\activate.bat

REM --- RUN THE ADK WEB SERVER ON PORT 8001 ---
echo Starting DataDiet Agent on Port 8001...
adk web --port 8001