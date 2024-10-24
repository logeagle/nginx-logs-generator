#!/usr/bin/env python3

import os
import time
import random
from datetime import datetime, timedelta
import ipaddress
import argparse

class NginxLogGenerator:
    def __init__(self, access_log="/var/log/nginx/access.log", error_log="/var/log/nginx/error.log"):
        self.access_log = access_log
        self.error_log = error_log
        
        # Create log directories if they don't exist
        os.makedirs(os.path.dirname(self.access_log), exist_ok=True)
        os.makedirs(os.path.dirname(self.error_log), exist_ok=True)
        
        # Initialize data for generating realistic logs
        self.user_agents = [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Safari/605.1.15",
            "Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1",
            "Mozilla/5.0 (Linux; Android 11; SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.120 Mobile Safari/537.36"
        ]
        
        self.endpoints = [
            "/", "/about", "/contact", "/api/v1/users", "/api/v1/products",
            "/login", "/logout", "/register", "/profile", "/settings",
            "/images/logo.png", "/css/main.css", "/js/app.js", "/favicon.ico",
            "/products", "/cart", "/checkout", "/blog", "/search"
        ]
        
        self.http_methods = ["GET", "POST", "PUT", "DELETE"]
        self.status_codes = [
            200, 200, 200, 200, 200,  # More weight to 200
            201, 204, 301, 302,
            400, 401, 403, 404, 429,
            500, 502, 503
        ]
        
        self.error_levels = ["error", "warn", "crit", "alert"]
        self.error_messages = [
            "Connection refused",
            "File not found",
            "Permission denied",
            "Invalid request",
            "Database connection failed",
            "Memory limit exceeded",
            "CPU usage too high",
            "Disk space low",
            "Invalid configuration",
            "SSL certificate error"
        ]

    def generate_ip(self):
        """Generate a random IP address."""
        return str(ipaddress.IPv4Address(random.randint(0, 2**32 - 1)))

    def generate_access_log(self):
        """Generate a single access log entry."""
        ip = self.generate_ip()
        timestamp = datetime.now().strftime("%d/%b/%Y:%H:%M:%S +0000")
        method = random.choice(self.http_methods)
        endpoint = random.choice(self.endpoints)
        protocol = "HTTP/1.1"
        status = random.choice(self.status_codes)
        bytes_sent = random.randint(200, 15000)
        referer = "-"
        user_agent = random.choice(self.user_agents)
        
        return f'{ip} - - [{timestamp}] "{method} {endpoint} {protocol}" {status} {bytes_sent} "{referer}" "{user_agent}"'

    def generate_error_log(self):
        """Generate a single error log entry."""
        timestamp = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
        level = random.choice(self.error_levels)
        message = random.choice(self.error_messages)
        pid = random.randint(1000, 9999)
        
        return f'{timestamp} [{level}] {pid}#0: *{random.randint(1, 999999)}: {message}, client: {self.generate_ip()}'

    def write_logs(self, num_entries=1, delay=0.1):
        """Write the specified number of log entries with a delay between each."""
        try:
            for _ in range(num_entries):
                # Generate and write access log
                with open(self.access_log, 'a') as f:
                    access_entry = self.generate_access_log()
                    f.write(access_entry + '\n')
                
                # Generate and write error log (with 30% probability)
                if random.random() < 0.3:
                    with open(self.error_log, 'a') as f:
                        error_entry = self.generate_error_log()
                        f.write(error_entry + '\n')
                
                if delay > 0:
                    time.sleep(delay)
                
        except Exception as e:
            print(f"Error writing logs: {e}")
            return False
        
        return True

def main():
    parser = argparse.ArgumentParser(description="Generate sample Nginx access and error logs")
    parser.add_argument("--access-log", default="/var/log/nginx/access.log", help="Path to access log file")
    parser.add_argument("--error-log", default="/var/log/nginx/error.log", help="Path to error log file")
    parser.add_argument("--entries", type=int, default=10, help="Number of entries to generate")
    parser.add_argument("--delay", type=float, default=1.0, help="Delay between entries in seconds")
    parser.add_argument("--continuous", action="store_true", help="Run continuously")
    args = parser.parse_args()
    
    generator = NginxLogGenerator(args.access_log, args.error_log)
    
    print(f"\nStarting Nginx Log Generator:")
    print(f"* Access log: {args.access_log}")
    print(f"* Error log: {args.error_log}")
    print(f"* Delay between entries: {args.delay} seconds")
    
    try:
        if args.continuous:
            print("* Running in continuous mode (Ctrl+C to stop)")
            entries_generated = 0
            while True:
                if generator.write_logs(1, args.delay):
                    entries_generated += 1
                    if entries_generated % 10 == 0:
                        print(f"Generated {entries_generated} entries...")
        else:
            print(f"* Generating {args.entries} entries...")
            generator.write_logs(args.entries, args.delay)
            print("Done!")
    
    except KeyboardInterrupt:
        print("\nStopping log generation...")
    except Exception as e:
        print(f"\nError: {e}")
        return 1
    
    return 0

if __name__ == "__main__":
    exit(main())
