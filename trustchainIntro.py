#Everything in TrustChain will use dictionaries — because credentials are structured as JSON (which maps to Python dicts).
vendor_credentials= {
    "legal_name": "vendor xyx ",
    "vendor id": 1234,
    "iso27001_certified": True
}
print(vendor_credentials["legal_name"])

def issue_credential(vendor_name, vendor_id):
    
        credentials={
            "legal_name": "VendorXYZ",
            "VendorID":1234,
            "iso27001certified": True
        }
        return credentials
issued =issue_credential("Vendor ABC", "12355")
print(issued)
    