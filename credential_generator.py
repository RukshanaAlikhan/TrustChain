import json
from datetime import datetime

print("=== TrustChain Credential Generator ===")

# 1️⃣ Collect input from the user
vendor_name = input("Enter vendor company name: ")
vendor_id = input("Enter vendor ID (e.g., VND-001): ")

# 2️⃣ Simple yes/no input for ISO certification
iso_cert_input = input("Is the vendor ISO27001 certified? (yes/no): ").strip().lower()
iso_certified = True if iso_cert_input == "yes" else False

cyber_ess = input("Cyber Essentials level (None / Basic / Plus): ").strip().capitalize()
certificate_number = input("Enter certificate number (or press Enter to skip): ").strip() or None

# 3️⃣ Build the credential as a dictionary
credential = {
    "legal_name": vendor_name,
    "vendor_id": vendor_id,
    "iso27001_certified": iso_certified,
    "cyber_essentials": cyber_ess,
    "certificate_number": certificate_number,
    "issued_at": datetime.utcnow().isoformat() + "Z"
}

# 4️⃣ Convert dictionary -> JSON string (pretty print)
json_data = json.dumps(credential, indent=2)

# 5️⃣ Save to a JSON file
filename = f"{vendor_id}_credential.json"
with open(filename, "w") as f:
    f.write(json_data)

print(f"\n✅ Credential saved to {filename}")
