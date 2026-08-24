#!/usr/bin/env python3
import requests

def run():
    print("\n[+] Starting Admin Path Finder...")
    target = input("Enter target URL (e.g. https://example.com): ")
    wordlist = [
    "admin", "login", "dashboard", "administrator", "panel", "wp-admin", "backup", "yonetim",
    "admin1", "admin2", "admin3", "admin4", "admin5", "admin6", "admin7", "admin8", "admin9",
    "administrator1", "administrator2", "administrator3", "administrator4", "administrator5",
    "adm", "admins", "administrators", "administration", "superadmin", "root", "sysadmin",
    "webadmin", "siteadmin", "mainadmin", "adminpanel", "admincp", "cp", "cpanel", "controlpanel",
    "paneladmin", "dashboardadmin", "admin-dashboard", "backend", "manage", "management",
    "webmaster", "master", "host", "server", "secure", "private", "hidden", "secret",
    "config", "configuration", "settings", "setup", "install", "installer", "update",
    "upgrade", "maintenance", "tmp", "temp", "test", "testing", "demo", "sample",
    "backup1", "backup2", "backup3", "backups", "db", "database", "mysql", "phpmyadmin",
    "phpmyadmin1", "phpmyadmin2", "phpmyadmin3", "myadmin", "mysqladmin", "webmail",
    "mail", "email", "ftp", "ftpadmin", "files", "filemanager", "upload", "uploads",
    "images", "img", "css", "js", "javascript", "assets", "static", "media", "download",
    "downloads", "logs", "log", "error", "errors", "debug", "dev", "development",
    "staging", "stage", "prod", "production", "live", "qa", "quality", "beta", "alpha",
    "release", "releases", "archive", "archives", "old", "new", "migrate", "migration",
    "api", "apiv1", "apiv2", "v1", "v2", "v3", "v4", "ws", "webservice", "rest",
    "soap", "xmlrpc", "rpc", "gateway", "proxy", "cache", "caching", "session",
    "sessions", "cookie", "cookies", "auth", "authentication", "authorization",
    "register", "registration", "signup", "signin", "user", "users", "userpanel",
    "member", "members", "profile", "profiles", "account", "accounts", "password",
    "passwords", "reset", "recovery", "forgot", "forget", "logout", "signout",
    "verify", "verification", "confirm", "confirmation", "activate", "activation",
    "deactivate", "deactivation", "block", "blocked", "ban", "banned", "suspend",
    "suspended", "pending", "approve", "approved", "reject", "rejected", "review",
    "moderate", "moderator", "mod", "editor", "contributor", "author", "publisher",
    "distributor", "partner", "vendor", "supplier", "customer", "clients", "client",
    "support", "help", "faq", "guide", "docs", "documentation", "manual", "tutorial",
    "blog", "news", "events", "calendar", "booking", "reservation", "shop", "store",
    "cart", "checkout", "payment", "payments", "invoice", "invoices", "order", "orders",
    "product", "products", "category", "categories", "catalog", "inventory", "stock",
    "warehouse", "ship", "shipping", "delivery", "track", "tracking", "return", "returns",
    "refund", "refunds", "coupon", "coupons", "discount", "discounts", "promo", "promotion",
    "voucher", "vouchers", "gift", "gifts", "certificate", "certificates", "affiliate",
    "affiliates", "refer", "referral", "loyalty", "reward", "rewards", "point", "points"
]
    print("[*] Scanning started... (This may take a moment)")

    for path in wordlist:
        url = f"{target.rstrip('/')}/{path}"
        try:
            response = requests.get(url, timeout=5)
            if response.status_code != 404:
                print(f"[+] FOUND! -> {url} (Status: {response.status_code})")
        except requests.exceptions.ConnectionError:
            print(f"[-] Connection error: {url}")
        except requests.exceptions.Timeout:
            print(f"[-] Timeout: {url}")
        except Exception as e:
            print(f"[!] Unexpected error: {url} - {e}")

    print("\n[+] Scan completed!")
    input("Press Enter to return to the main menu...")
