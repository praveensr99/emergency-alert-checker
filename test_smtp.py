"""
SMTP Connection Tester
Tests if email credentials are correct
"""

import smtplib
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get SMTP configuration
SMTP_SERVER = os.getenv("SMTP_SERVER", "smtp.gmail.com")
SMTP_PORT = int(os.getenv("SMTP_PORT", "587"))
SENDER_EMAIL = os.getenv("SENDER_EMAIL", "")
SENDER_PASSWORD = os.getenv("SENDER_PASSWORD", "")

print("=" * 60)
print("SMTP Connection Test")
print("=" * 60)
print(f"\n📧 Email: {SENDER_EMAIL}")
print(f"🔧 Server: {SMTP_SERVER}:{SMTP_PORT}")
print(f"🔑 Password: {'*' * len(SENDER_PASSWORD) if SENDER_PASSWORD else 'NOT SET'}")
print("\n" + "-" * 60)

# Check if credentials are set
if not SENDER_EMAIL or not SENDER_PASSWORD:
    print("❌ ERROR: Missing SENDER_EMAIL or SENDER_PASSWORD in .env")
    print("\nPlease update .env with:")
    print("  SENDER_EMAIL=your-email@gmail.com")
    print("  SENDER_PASSWORD=your-16-char-app-password")
    exit(1)

# Test SMTP connection
try:
    print("\n🔄 Connecting to SMTP server...")
    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        print("✅ Connected to server")
        
        print("🔄 Starting TLS encryption...")
        server.starttls()
        print("✅ TLS encryption enabled")
        
        print("🔄 Authenticating...")
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        print("✅ Authentication successful!")
        
    print("\n" + "=" * 60)
    print("✅ SMTP CONNECTION VERIFIED!")
    print("=" * 60)
    print("\n📧 Email service is ready to send messages!")
    print("Your credentials are working correctly.\n")
    
except smtplib.SMTPAuthenticationError as e:
    print("\n" + "=" * 60)
    print("❌ AUTHENTICATION FAILED")
    print("=" * 60)
    print(f"\n⚠️  Error: {str(e)}")
    print("\nPossible issues:")
    print("  1. Wrong email address or password")
    print("  2. Gmail: Using account password instead of App Password")
    print("  3. Gmail: App Password not generated correctly (should be 16 chars)")
    print("  4. Gmail: 2-Step Verification not enabled")
    print("\n✅ To fix:")
    print("  1. Go to https://myaccount.google.com/security")
    print("  2. Enable 2-Step Verification")
    print("  3. Generate an App Password")
    print("  4. Copy the 16-char password to SENDER_PASSWORD in .env")
    print("  5. Re-run this test\n")
    
except smtplib.SMTPException as e:
    print("\n" + "=" * 60)
    print("❌ SMTP ERROR")
    print("=" * 60)
    print(f"\n⚠️  Error: {str(e)}")
    print("\nPossible issues:")
    print("  1. Internet connection problem")
    print("  2. SMTP server not responding")
    print("  3. Firewall blocking SMTP port 587")
    print("  4. Wrong SMTP server address\n")
    
except Exception as e:
    print("\n" + "=" * 60)
    print("❌ CONNECTION ERROR")
    print("=" * 60)
    print(f"\n⚠️  Error: {str(e)}\n")
