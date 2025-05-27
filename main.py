from fulfillment.validate_hsn import fulfill

print("✅ Agent 'HSN Code Validator' loaded successfully")
print('Type an input like: "Validate HSN code 0101"\n')

while True:
    user_input = input("You: ")
    
    # Extract HSN codes from the input (basic digit matcher)
    import re
    hsn_codes = re.findall(r"\b\d{2,8}\b", user_input)
    
    if not hsn_codes:
        print("🤖 Agent: I couldn't find any HSN code in your input. Please enter a numeric code.")
        continue

    # Call the validation function
    response = fulfill({"hsncode": hsn_codes})

    # Print each result
    for result in response["validation_results"]:
        if result["valid"]:
            print(f"✅ HSN code {result['hsn_code']} is valid: {result['description']}")
        else:
            print(f"❌ HSN code {result['hsn_code']} is NOT valid. Reason: {result['reason']}")
    
    print("\n--- Type another input or press Ctrl+C to exit ---\n")
