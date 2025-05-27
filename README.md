
# 🧠 HSN Code Validation Agent

This project implements an intelligent agent using the conceptual **Agent Developer Kit (ADK)** by Google. The agent's goal is to **validate HSN (Harmonized System Nomenclature) codes** against a master dataset.

---

## 📌 Objective

To design and outline the architecture of an agent that can:
- Take in HSN code(s) as input
- Validate each against a provided master dataset
- Return appropriate validation feedback

---

## 📂 Dataset

A sample Excel file named `HSN_SAC.xlsx` is used, containing:

| Column      | Description                                      |
|-------------|--------------------------------------------------|
| HSNCode     | The HSN code (string)                            |
| Description | Description of goods associated with the code    |

🔗 Dataset link: [HSN_SAC.xlsx](https://docs.google.com/spreadsheets/d/1UD4JAAQ6Fgeyc5a1OwBiLV2cPTAK_D2q/edit)

---

## 🧩 Agent Design (ADK Framework)

### Key Components:
- **Intents**: Validate single or multiple HSN codes
- **Entities**: `HSNCode`, `HSNCodesList`
- **Fulfillment Logic**: Uses backend logic to process and validate codes
- **Data Store**: Reads from the provided Excel file

### Input Handling:
- Accepts a single HSN code or a list of codes
- Supports both textual and numeric input

### Output:
- Returns confirmation with product description for valid codes
- Returns detailed error messages for invalid or malformed codes

---

## ⚙️ Validation Logic

### ✅ Format Validation:
- Ensures code is numeric
- Acceptable lengths: 2, 4, 6, or 8 digits (per international HSN standards)

### ✅ Existence Validation:
- Checks if the code exists in the master dataset

### ✅ (Optional) Hierarchical Validation:
- Validates parent codes (e.g., for `01011010`, it also checks `01`, `0101`, `010110`)

---

## 🔄 Data Handling Strategy

- **Loading**: Loads the entire dataset into memory on startup for faster lookup
- **Efficiency**: Uses dictionary-based lookup for O(1) validation
- **Pre-processing**: Data cleaned to remove trailing spaces and ensure consistency

---

## 📤 Agent Response

| Case             | Response Format                                              |
|------------------|--------------------------------------------------------------|
| Valid Code       | "✅ Valid HSN Code. Description: [description]"              |
| Invalid Code     | "❌ Invalid HSN Code. Reason: Not found in master dataset."  |
| Invalid Format   | "⚠️ Invalid format. HSN codes must be numeric and 2-8 digits."|

---
Screenshots

![image](https://github.com/user-attachments/assets/76d0a067-503d-470a-a91f-777972d71183)
![image](https://github.com/user-attachments/assets/92da54c6-4c97-48b4-832a-7b0a3f1b8afd)
![image](https://github.com/user-attachments/assets/74258962-80bc-46dc-8d3b-a1c8b367eb21)
![image](https://github.com/user-attachments/assets/361aba39-cb58-4a9e-8516-dbf6c76eb56f)





---

## 📝 References

- [ADK Documentation](https://google.github.io/adk-docs/)
- [HSN Master Dataset (Google Sheet)](https://docs.google.com/spreadsheets/d/1UD4JAAQ6Fgeyc5a1OwBiLV2cPTAK_D2q/edit)
