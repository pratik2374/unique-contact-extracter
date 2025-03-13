import streamlit as st
import re

# Function to extract contacts from a VCF file
def extract_contacts(vcf_file):
    """Extracts names and phone numbers from a VCF file."""
    contacts = []
    with open(vcf_file, 'r', encoding='utf-8') as file:
        content = file.read()

    vcard_entries = content.split("END:VCARD")
    
    for entry in vcard_entries:
        entry = entry.strip()
        if entry:
            name_match = re.search(r'FN:(.*)', entry)  # Extract name
            phone_match = re.search(r'TEL(?:;[^:]+)*:(\+?\d+)', entry)  # Updated regex for phone numbers
            
            if name_match:
                name = name_match.group(1).strip()
                phone = phone_match.group(1).strip() if phone_match else "No Number"
                contacts.append((name, phone, entry + "\nEND:VCARD"))  # Store name, phone & full entry
    
    return contacts


# Load contacts from the VCF file
vcf_file_path = "contacts.vcf"  # Update this to your actual .vcf file path
all_contacts = extract_contacts(vcf_file_path)

# Extract names separately for filtering
names = [name for name, _, _ in all_contacts]

# Streamlit UI
st.title("📞 Contact Search from VCF")

# Search input
query = st.text_input("🔍 Search for a contact:", "").strip()

# Filter contacts based on user input
filtered_contacts = []
if query:
    if query == "#":
        # Show all names NOT starting with A-Z (special characters, numbers)
        filtered_contacts = [(name, phone, contact) for name, phone, contact in all_contacts if not re.match(r'^[A-Za-z]', name)]
    else:
        # Show names starting with query (case-sensitive)
        filtered_contacts = [(name, phone, contact) for name, phone, contact in all_contacts if name.lower().startswith(query.lower())]

# Extract filtered names
filtered_names = [name for name, _, _ in filtered_contacts]

# Dropdown selection
selected_name = st.selectbox("Select a Contact:", filtered_names) if filtered_names else None

# Show selected contact in a simple box format
if selected_name:
    for name, phone, contact in filtered_contacts:
        if name == selected_name:
            st.markdown(
                f"""
                <div style="
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    text-align: center;
                    padding: 15px; 
                    border: 1px solid #ddd; 
                    border-radius: 8px; 
                    background-color: #000; 
                    width: 100%;
                    margin: auto;
                ">
                    <h4 style="color: grey; margin-bottom: 2px;">{name}</h4>
                    <p style="font-size: 18px; color: #555; margin: 0;">📞 {phone}</p>
                </div>
                """,
                unsafe_allow_html=True
            )
            break

            break
