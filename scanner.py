import asyncio
import aiohttp
import aiofiles
import random
import re
import sys
from pathlib import Path
from urllib.parse import urljoin
from colorama import init, Fore

init(autoreset=True)

def rainbow(text):
    colors = [Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.CYAN, Fore.BLUE, Fore.MAGENTA]
    output = ""
    for i, char in enumerate(text):
        output += colors[i % len(colors)] + char
    return output

BANNER = """
▄▄    ▄▄▄▄▄  ▄▄▄  ▄▄ ▄▄   ▄▄▄▄▄ ▄▄ ▄▄  ▄▄ ▄▄▄▄  ▄▄▄▄▄ ▄▄▄▄  
██    ██▄▄  ██▀██ ██▄█▀   ██▄▄  ██ ███▄██ ██▀██ ██▄▄  ██▄█▄ 
██▄▄▄ ██▄▄▄ ██▀██ ██ ██   ██    ██ ██ ▀██ ████▀ ██▄▄▄ ██ ██ 
"""

def show_banner():
    print(rainbow(BANNER))
    print(rainbow("                  MASS LEAK SCANNER v2.3"))
    print(rainbow("             Credit → https://t.me/DoYouLikePopo\n"))

USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:136.0) Gecko/20100101 Firefox/136.0"
]

paths_data = {
    "env": [
        "/.env", "/.env.bak", "/.env.old", "/.env.save", "/.env~", "/.env.tmp", "/.env.local",
        "/.env.development", "/.env.production", "/.env.staging", "/.env.testing", "/.env.example",
        "/.env.backup", "/.env.dist", "/.env.php", "/.env.json", "/.env.yaml", "/.env.yml",
        "/.env.js", "/.env.tar.gz", "/.env.zip", "/.env.rar", "/.env.7z", "/.env.sql",
        "/.env.old.php", "/.env.php.bak", "/.env.bak.php", "/.env.test", "/.env.dev", "/.env.prod",
        "/.env.backup.php", "/.env.gz", "/.env.dump", "/.env.backup.zip", "/.env.backup.tar.gz",
        "/.env.backup.rar", "/.env.backup.7z", "/.env.test.bak", "/.env.dev.bak", "/.env.prod.bak",
        "/.env.staging.bak", "/.env.local.bak", "/.env.development.bak", "/.env.production.bak",
        "/.env.testing.bak", "/.env.development.local", "/.env.staging.local", "/.env.uat",
        "/.env.live", "/.env.secret", "/.env.credentials", "/.env.keys", "/.env.aws", "/.env.db",
        "/.env.s3", "/.env.mail", "/.env.smtp", "/.env.log", "/.env.debug", "/.env.error",
        "/.env.template", "/.env.local.example", "/.env.local.dist", "/.env.development.local",
        "/.env.test", "/.env.qa", "/.env.preprod", "/.env.SECURE", "/.env.SECRET", "/.env.secret",
        "/.env.enc", "/.env.enc.bak", "/.env.php.bak", "/.env.yaml", "/.env.toml", "/.env.ini",
        "/.envrc", "/.envrc.local", "/.envrc.bak", "/.envvars", "/.envvars.bak", "/.env-vars",
        "/.env-variables", "/.env.override", "/.env-override", "/.env-credentials", "/.env-secrets",
        "/.env_keys", "/.env-archive", "/.env-archive.zip", "/.env-archive.tar.gz", "/.env.production.local",
        "/.env.staging.local", "/.env.testing.local", "/.env_hidden", "/.env-backup.zip",
        "/laravel/.env", "/public/.env", "/api/.env", "/admin/.env", "/backend/.env", "/app/.env",
        "/config/.env", "/storage/.env", "/bootstrap/.env", "/vendor/.env", "/public/env",
        "/public/.env.bak", "/public/.env.old", "/api/.env.bak", "/admin/.env.bak", "/backend/.env.bak",
        "/laravel/.env.bak", "/app/.env.bak", "/wp-content/uploads/.env", "/public/uploads/.env",
        "/.env.local.php", "/.env.local.json", "/.env.local.yml", "/.env_copy", "/.env_backup",
        "/.env-OLD", "/.env-LOCAL", "/.env-PROD", "/.env-STAGE"
    ],
    "git": [
        "/.git/config", "/.git/HEAD", "/.git/index", "/.git/logs/HEAD", "/.git/packed-refs",
        "/.git/logs/refs/heads/master", "/.git/logs/refs/heads/main", "/.git/refs/heads/master",
        "/.git/refs/heads/main", "/.git/description", "/.git/config~", "/.git/HEAD.bak",
        "/.gitmodules", "/.git/FETCH_HEAD", "/.git/logs/refs/heads/develop", "/.git/ORIG_HEAD",
        "/.git/COMMIT_EDITMSG", "/.gitattributes", "/.git-credentials", "/.gitkeep"
    ],
    "phpinfo": [
        "/phpinfo.php", "/info.php", "/phpinfo", "/_profiler/phpinfo.php", "/_profiler/phpinfo",
        "/phpversion.php", "/infophp.php", "/i.php", "/test.php", "/debug.php", "/x.php",
        "/xx.php", "/xxx.php", "/admin.php", "/?phpinfo=1", "/phpinfo.php.bak", "/phpinfo.php.old",
        "/phpinfo.php.save", "/phpinfo.php~", "/phpinfo.php.tmp", "/phpinfo.php.json",
        "/phpinfo.php.yaml", "/phpinfo.php.log", "/info.php.bak", "/test.php.bak", "/debug.php.bak",
        "/debug.php.old", "/phpinfo_backup.php", "/phpinfo_old.php", "/phpinfo_test.php",
        "/phpinfo_dev.php", "/phpinfo_local.php", "/phpinfo_hidden.php", "/phpinfo_dump.php",
        "/public/phpinfo.php", "/public/info.php", "/admin/phpinfo.php", "/laravel/phpinfo.php",
        "/storage/phpinfo.php", "/bootstrap/phpinfo.php", "/vendor/phpinfo.php", "/wp-content/phpinfo.php",
        "/wp-admin/phpinfo.php", "/public/uploads/phpinfo.php", "/health/phpinfo.php", "/monitor/phpinfo.php",
        "/inspect/phpinfo.php", "/tools/phpinfo.php", "/dev/phpinfo.php", "/staging/phpinfo.php",
        "/hidden/phpinfo.php", "/includes/phpinfo.php", "/scripts/phpinfo.php", "/cgi-bin/phpinfo.php",
        "/phpinfo/index.php", "/info/index.php", "/test/index.php", "/debug/index.php",
        "/phpinfo-2026.php", "/phpinfo_testpage.php", "/phpinfo_sample.php", "/phpinfo_export.php",
        "/phpinfo_console.php", "/phpinfo_backup_*.php", "/phpinfo_old_*.php", "/phpinfo_test_*.php"
    ],
    "sensitive": [
        "/wp-config.php", "/wp-config.php.bak", "/wp-config.php.old", "/wp-config.php.save",
        "/wp-config.php~", "/wp-config.bak", "/wp-config.php.swp", "/wp-config.php.zip",
        "/wp-config.php.tar.gz", "/wp-config-sample.php", "/config.php", "/config.php.bak",
        "/config.php.old", "/config.php.save", "/config.php~", "/config.inc.php", "/config.inc.php.bak",
        "/database.php", "/database.php.bak", "/database.php.old", "/db.php", "/db.php.bak",
        "/connect.php", "/connection.php", "/credentials.php", "/passwords.php", "/settings.php",
        "/settings.php.old", "/adminer.php", "/pma.php", "/myadmin.php", "/phpmyadmin/config.inc.php",
        "/composer.json", "/composer.lock", "/package.json", "/package-lock.json", "/yarn.lock",
        "/phpunit.xml", "/phpunit.xml.dist", "/.travis.yml", "/.gitlab-ci.yml", "/docker-compose.yml",
        "/Dockerfile", "/.env.example", "/.htaccess", "/.htpasswd", "/.user.ini", "/.npmrc",
        "/.yarnrc", "/web.config", "/web.config.bak", "/server-status", "/server-info",
        "/laravel.log", "/storage/logs/laravel.log", "/storage/logs/laravel-daily.log",
        "/storage/logs/error.log", "/storage/logs/debug.log", "/bootstrap/cache/services.php",
        "/bootstrap/cache/packages.php", "/logs/laravel.log", "/debug.log", "/error.log",
        "/access.log", "/exception.log", "/application.log", "/storage/logs/laravel-2026.log",
        "/public/storage/laravel.log", "/wp-content/uploads/laravel.log", "/storage/framework/sessions/",
        "/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php", "/.aws/credentials", "/.aws/config",
        "/.ssh/id_rsa", "/.ssh/authorized_keys", "/backup.sql", "/dump.sql", "/database.sql",
        "/db.sql", "/backup.sql.gz", "/dump.sql.gz", "/.DS_Store", "/.gitignore", "/README.md",
        "/php.ini", "/php.ini.bak", "/.well-known/security.txt"
    ]
}

def detect_phpinfo(data):
    if not data or len(data) < 1500: return False
    return bool(re.search(r'(PHP Version|http://www\.php\.net|Configuration.*PHP|phpinfo\(\)|Zend Engine|Server API|Loaded Configuration File|Build Date|Module Name)', data, re.IGNORECASE))

def detect_env(data):
    if not data or len(data) < 250: return False
    key_count = len(re.findall(r'^[A-Z][A-Z0-9_]{4,}=', data, re.MULTILINE))
    if key_count >= 8: return True
    return bool(re.search(r'(APP_KEY=|DB_PASSWORD=|AWS_SECRET_ACCESS_KEY=|JWT_SECRET=|SECRET_KEY=|DATABASE_URL=|REDIS_PASSWORD=|MAIL_PASSWORD=|MAIL_HOST=|S3_SECRET=)', data, re.IGNORECASE))

def detect_git(data):
    if not data or len(data) < 100: return False
    patterns = [r'ref:\s*refs/heads/', r'repositoryformatversion\s*=\s*0', r'\[core\]', r'\[remote "origin"\]', r'gitdir:', r'branch\.', r'url =']
    return any(re.search(p, data, re.IGNORECASE) for p in patterns)

def detect_sensitive(data):
    if not data or len(data) < 80: return False
    sensitive_keywords = r'(DB_|PASSWORD|SECRET|KEY|JWT|AWS_|DB_HOST|MAIL_|APP_KEY|mysql|laravel|wp-config|password|credential|token|api_key|private_key|BEGIN RSA PRIVATE KEY|-----BEGIN)'
    return bool(re.search(sensitive_keywords, data, re.IGNORECASE)) or "laravel" in data.lower() or "wp-config" in data.lower() or "DB_PASSWORD" in data

detectors = {
    "env": detect_env,
    "git": detect_git,
    "phpinfo": detect_phpinfo,
    "sensitive": detect_sensitive
}

async def check_url(session, target, category, path, semaphore, seen, lock):
    full_url = urljoin(target, path.lstrip('/'))
    if full_url in seen: return

    headers = {
        "User-Agent": random.choice(USER_AGENTS),
        "Accept": "text/html,application/xhtml+xml,application/xml",
        "Cache-Control": "no-cache",
        "Pragma": "no-cache"
    }

    async with semaphore:
        try:
            async with session.get(full_url, headers=headers, timeout=8, ssl=False) as resp:
                if resp.status != 200:
                    await asyncio.sleep(random.uniform(0.02, 0.09))
                    return
                data = await resp.text()
                if detectors[category](data):
                    async with lock:
                        if full_url not in seen:
                            seen.add(full_url)
                            async with aiofiles.open("vuln.txt", "a") as f:
                                await f.write(full_url + "\n")
                            async with aiofiles.open("live_found.txt", "a") as f:
                                await f.write(full_url + "\n")
                            print(f"\033[32m[VULN] {full_url}\033[0m")
        except:
            pass
        finally:
            await asyncio.sleep(random.uniform(0.02, 0.09))

async def scan_target(target, seen, lock, concurrency):
    print(f"{Fore.CYAN}[+] Scanning → {target}")
    connector = aiohttp.TCPConnector(limit_per_host=12, ttl_dns_cache=300, ssl=False, keepalive_timeout=30)
    
    async with aiohttp.ClientSession(connector=connector) as session:
        semaphore = asyncio.Semaphore(concurrency)
        categories = ["env", "git", "phpinfo", "sensitive"]
        tasks = []
        for cat in categories:
            paths = paths_data[cat][:]
            random.shuffle(paths)
            for path in paths:
                tasks.append(check_url(session, target, cat, path, semaphore, seen, lock))
        await asyncio.gather(*tasks, return_exceptions=True)

async def main():
    show_banner()
    
    file_name = input(f"{Fore.YELLOW}[?] Enter input file name (e.g. domains_only.txt): {Fore.WHITE}").strip() or "domains_only.txt"
    
    try:
        threads_input = input(f"{Fore.YELLOW}[?] Enter threads (recommended 45-70 for max speed): {Fore.WHITE}").strip()
        concurrency = int(threads_input) if threads_input else 50
        concurrency = max(20, min(90, concurrency))
    except:
        concurrency = 50

    print(f"\n{Fore.GREEN}[+] Starting ULTRA-FAST scan with {concurrency} threads")
    print(f"{Fore.GREEN}[+] Credit: https://t.me/DoYouLikePopo\n")

    Path("vuln.txt").touch(exist_ok=True)
    Path("live_found.txt").touch(exist_ok=True)

    seen = set()
    lock = asyncio.Lock()

    try:
        with open(file_name, "r", encoding="utf-8") as f:
            lines = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print(f"{Fore.RED}❌ File '{file_name}' not found!")
        return

    for line in lines:
        if not line.startswith(("http://", "https://")):
            target = "https://" + line.rstrip('/') + "/"
        else:
            target = line if line.endswith('/') else line + '/'
        await scan_target(target, seen, lock, concurrency)

    print(f"\n{Fore.GREEN}[+] Scan completed! Clean URLs saved line by line in vuln.txt and live_found.txt")

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print(f"\n{Fore.RED}[!] Stopped by user. All results saved.")
