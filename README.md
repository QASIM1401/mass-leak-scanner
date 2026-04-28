<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>Mass Leak Scanner v2.3</title>
  <script src="https://cdn.tailwindcss.com"></script>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.6.0/css/all.min.css"/>
  <style>
    @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;600;700&display=swap');
    
    body {
      font-family: 'Space Grotesk', sans-serif;
    }
    
    .rainbow-text {
      background: linear-gradient(90deg, #ff0000, #ff7f00, #ffff00, #00ff00, #0000ff, #8b00ff);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      animation: rainbow 3s linear infinite;
    }
    
    @keyframes rainbow {
      0% { background-position: 0% 50%; }
      50% { background-position: 100% 50%; }
      100% { background-position: 0% 50%; }
    }
    
    .neon-card {
      transition: all 0.4s ease;
    }
    
    .neon-card:hover {
      transform: translateY(-10px);
      box-shadow: 0 0 30px rgba(0, 255, 150, 0.6);
    }
    
    .terminal {
      background: #0a0a0a;
      border: 2px solid #00ff9d;
      font-family: monospace;
    }
    
    .scan-line {
      animation: scan 4s linear infinite;
    }
  </style>
</head>
<body class="bg-zinc-950 text-white overflow-x-hidden">
  <!-- Navbar -->
  <nav class="border-b border-zinc-800 bg-black/80 backdrop-blur-lg fixed w-full z-50">
    <div class="max-w-7xl mx-auto px-6 py-4 flex justify-between items-center">
      <div class="flex items-center gap-3">
        <i class="fa-solid fa-bolt text-emerald-400 text-2xl"></i>
        <span class="text-2xl font-bold rainbow-text">MASS LEAK</span>
      </div>
      <a href="https://github.com/YOURUSERNAME/mass-leak-scanner" target="_blank"
         class="flex items-center gap-2 bg-zinc-900 hover:bg-zinc-800 px-5 py-2 rounded-full border border-zinc-700 transition">
        <i class="fa-brands fa-github"></i>
        <span>Star on GitHub</span>
      </a>
    </div>
  </nav>

  <!-- Hero -->
  <section class="min-h-screen flex items-center justify-center pt-20 relative">
    <div class="absolute inset-0 bg-[radial-gradient(at_center,#00ff9d10_0%,transparent_70%)]"></div>
    
    <div class="max-w-5xl mx-auto text-center px-6 relative z-10">
      <pre class="text-emerald-400 text-[14px] md:text-[18px] leading-tight mb-8 font-mono opacity-90">
▄▄    ▄▄▄▄▄  ▄▄▄  ▄▄ ▄▄   ▄▄▄▄▄ ▄▄ ▄▄  ▄▄ ▄▄▄▄  ▄▄▄▄▄ ▄▄▄▄  
██    ██▄▄  ██▀██ ██▄█▀   ██▄▄  ██ ███▄██ ██▀██ ██▄▄  ██▄█▄ 
██▄▄▄ ██▄▄▄ ██▀██ ██ ██   ██    ██ ██ ▀██ ████▀ ██▄▄▄ ██ ██ 
      </pre>
      
      <h1 class="text-6xl md:text-7xl font-bold rainbow-text mb-4 tracking-tighter">
        MASS LEAK SCANNER
      </h1>
      <p class="text-2xl text-emerald-300 mb-6">v2.3 — Ultra Fast • High Accuracy</p>
      
      <p class="max-w-2xl mx-auto text-zinc-400 text-lg mb-10">
        The fastest mass scanner for finding exposed <span class="text-white font-semibold">.env</span>, 
        <span class="text-white font-semibold">.git</span>, <span class="text-white font-semibold">phpinfo()</span>, 
        and other sensitive files.
      </p>

      <div class="flex flex-wrap justify-center gap-4">
        <button onclick="window.scrollTo({top: document.getElementById('install').offsetTop, behavior: 'smooth'})"
                class="bg-emerald-500 hover:bg-emerald-600 text-black font-bold px-10 py-4 rounded-2xl flex items-center gap-3 text-lg transition">
          <i class="fa-solid fa-rocket"></i>
          GET STARTED
        </button>
        <a href="scanner.py" download
           class="border border-zinc-700 hover:border-emerald-400 px-8 py-4 rounded-2xl flex items-center gap-3 transition">
          <i class="fa-solid fa-download"></i>
          Download Scanner
        </a>
      </div>

      <div class="mt-16 text-xs text-zinc-500 flex items-center justify-center gap-8">
        <div>⚡ UP TO 90 THREADS</div>
        <div>🔥 LOW FALSE POSITIVES</div>
        <div>📁 LIVE SAVING</div>
      </div>
    </div>

    <div class="absolute bottom-10 left-1/2 animate-bounce">
      <i class="fa-solid fa-chevron-down text-3xl text-emerald-500"></i>
    </div>
  </section>

  <!-- Features -->
  <section class="py-24 bg-black">
    <div class="max-w-6xl mx-auto px-6">
      <h2 class="text-4xl font-bold text-center mb-16 rainbow-text">POWERFUL FEATURES</h2>
      
      <div class="grid md:grid-cols-3 gap-8">
        <div class="neon-card bg-zinc-900 border border-zinc-800 p-8 rounded-3xl">
          <div class="text-5xl mb-6">⚡</div>
          <h3 class="text-2xl font-semibold mb-3">Ultra Fast Scanning</h3>
          <p class="text-zinc-400">Supports up to 90+ concurrent threads with smart connection management and minimal delays.</p>
        </div>
        
        <div class="neon-card bg-zinc-900 border border-zinc-800 p-8 rounded-3xl">
          <div class="text-5xl mb-6">🎯</div>
          <h3 class="text-2xl font-semibold mb-3">Strong Detection</h3>
          <p class="text-zinc-400">Advanced regex + content length analysis for very low false positive rate.</p>
        </div>
        
        <div class="neon-card bg-zinc-900 border border-zinc-800 p-8 rounded-3xl">
          <div class="text-5xl mb-6">💾</div>
          <h3 class="text-2xl font-semibold mb-3">Clean Live Output</h3>
          <p class="text-zinc-400">Only clean URLs saved line by line in vuln.txt and live_found.txt</p>
        </div>
      </div>
    </div>
  </section>

  <!-- Installation -->
  <section id="install" class="py-24 bg-zinc-950">
    <div class="max-w-4xl mx-auto px-6">
      <h2 class="text-4xl font-bold text-center mb-4">Installation</h2>
      <p class="text-center text-zinc-400 mb-12">Just 2 commands and you're ready to hunt.</p>
      
      <div class="terminal p-8 rounded-3xl text-emerald-400 font-mono text-lg leading-relaxed shadow-2xl">
        <div class="flex items-center gap-2 mb-6 text-zinc-500">
          <div class="w-3 h-3 rounded-full bg-red-500"></div>
          <div class="w-3 h-3 rounded-full bg-yellow-500"></div>
          <div class="w-3 h-3 rounded-full bg-green-500"></div>
          <span class="ml-4 text-white">terminal — mass-leak-scanner</span>
        </div>
        
        <div class="scan-line">
          $ pip install aiohttp aiofiles colorama<br/><br/>
          $ python scanner.py
        </div>
      </div>
      
      <div class="text-center mt-10 text-zinc-500">
        After running, enter your domain list file and desired thread count.
      </div>
    </div>
  </section>

  <!-- Footer -->
  <footer class="bg-black border-t border-zinc-800 py-12">
    <div class="max-w-6xl mx-auto px-6 text-center">
      <p class="text-zinc-500 mb-4">
        Made for educational and authorized security testing only.<br>
        Use responsibly.
      </p>
      <p class="text-emerald-400">
        Credit → <a href="https://t.me/DoYouLikePopo" target="_blank" class="hover:underline">@DoYouLikePopo</a>
      </p>
      <p class="text-xs text-zinc-600 mt-8">
        © 2026 Mass Leak Scanner • All Rights Reserved
      </p>
    </div>
  </footer>

  <script>
    // Simple tailwind script
    tailwind.config = {
      content: [],
      theme: {
        extend: {}
      }
    }
  </script>
</body>
</html>
