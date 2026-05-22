import requests, re

# Check reserve page (public)
r = requests.get("http://localhost:5001/reserve")
print(f"Status: {r.status_code}")

imgs = re.findall(r'<img\s+src="([^"]*)"', r.text)
print(f"\nFound {len(imgs)} images on /reserve page:")
for i, img in enumerate(imgs):
    print(f"  {i+1}. {img[:150]}")

# Check via login session
s = requests.Session()
s.post("http://localhost:5001/", data={"username": "admin", "password": "admin123"})
r2 = s.get("http://localhost:5001/new-booking")
print(f"\nNew Booking page status: {r2.status_code}")
imgs2 = re.findall(r'<img\s+src="([^"]*)"', r2.text)
print(f"Found {len(imgs2)} images on /new-booking page:")
for i, img in enumerate(imgs2):
    print(f"  {i+1}. {img[:150]}")
