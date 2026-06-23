@echo off
cd /d "C:\Users\sawas\.openclaw\workspace\tools\x-poster"
"C:\Program Files\nodejs\node.exe" auto-follow-ai.js
if %ERRORLEVEL% EQU 3 (
    echo ERROR: Authentication failed. Cookie needs update.
    exit /b 3
)
echo auto-follow-ai.js completed with exit code %ERRORLEVEL%
exit /b %ERRORLEVEL%