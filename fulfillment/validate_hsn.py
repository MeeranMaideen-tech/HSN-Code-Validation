import pandas as pd

# Load and clean Excel data
df = pd.read_excel('data/HSN_SAC.xlsx')

# ✅ Strip unwanted spaces from column names
df.columns = df.columns.str.strip()

# ✅ Ensure HSNCode is string
df['HSNCode'] = df['HSNCode'].astype(str).str.strip()

# Validation logic
def validate_hsn_code(hsn_code):
    hsn_code = str(hsn_code).strip()

    if not hsn_code.isdigit():
        return {"hsn_code": hsn_code, "valid": False, "reason": "HSN code must be numeric."}
    
    if len(hsn_code) not in [2, 4, 6, 8]:
        return {"hsn_code": hsn_code, "valid": False, "reason": "HSN code must be 2, 4, 6, or 8 digits."}

    match = df[df['HSNCode'] == hsn_code]
    if match.empty:
        return {"hsn_code": hsn_code, "valid": False, "reason": "HSN code not found in master data."}
    
    return {
        "hsn_code": hsn_code,
        "valid": True,
        "description": match.iloc[0]['Description']
    }

# Entry point used by main.py (simulates ADK fulfillment)
def fulfill(params):
    codes = params.get("hsncode", [])
    if not isinstance(codes, list):
        codes = [codes]
    
    results = [validate_hsn_code(code) for code in codes]
    return {"validation_results": results}
