<div align="center">
# MASS LEAK SCANNER v2.3
**Ultra Fast Mass Scanner for Exposed .env, .git, phpinfo & Sensitive Files**
```ascii
▄▄    ▄▄▄▄▄  ▄▄▄  ▄▄ ▄▄   ▄▄▄▄▄ ▄▄ ▄▄  ▄▄ ▄▄▄▄  ▄▄▄▄▄ ▄▄▄▄  
██    ██▄▄  ██▀██ ██▄█▀   ██▄▄  ██ ███▄██ ██▀██ ██▄▄  ██▄█▄ 
██▄▄▄ ██▄▄▄ ██▀██ ██ ██   ██    ██ ██ ▀██ ████▀ ██▄▄▄ ██ ██ 

Features

    ⚡ Ultra Fast — Supports up to 90+ threads
    🎯 Strong Detection — Very low false positives with advanced regex
    💾 Clean Output — Only clean URLs saved line by line
    🌐 Mass Scanning — Works with single target or huge domain lists
    🔥 Live Saving — Results saved instantly (vuln.txt & live_found.txt)
    🎨 Lambo Rainbow Banner — Pure cyber style

Installation
bash

pip install aiohttp aiofiles colorama

Usage
bash

python scanner.py

Then enter:

    Your domains list file (domains_only.txt)
    Number of threads (recommended 45–70)

Output Files
File	Content
vuln.txt	All discovered vulnerable URLs
live_found.txt	Same as above (saved live)
Disclaimer

    This tool is for educational purposes and authorized security testing only.
    Do not use on systems you do not own or have explicit permission to test.

Credit

Made by: QASIM1401
Original Concept & Credit → https://t.me/DoYouLikePopo

⭐ Star this repo if you found it useful!
@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;600;700&display=swap'); body { font-family: 'Space Grotesk', sans-serif; } .rainbow-text { background: linear-gradient(90deg, #ff0000, #ff7f00, #ffff00, #00ff00, #0000ff, #8b00ff); -webkit-background-clip: text; -webkit-text-fill-color: transparent; animation: rainbow 4s linear infinite; } @keyframes rainbow { 0% { background-position: 0% 50%; } 100% { background-position: 200% 50%; } } 
