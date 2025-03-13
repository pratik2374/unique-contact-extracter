import os
import glob

def extract_contacts_from_vcf(vcf_file):
    """Extracts individual contacts from a VCF file."""
    with open(vcf_file, 'r', encoding='utf-8') as file:
        content = file.read()
    
    contacts = content.split("END:VCARD")
    unique_contacts = set()

    for contact in contacts:
        contact = contact.strip()
        if contact:
            contact += "\nEND:VCARD"
            unique_contacts.add(contact)

    return unique_contacts

def save_contacts(contacts, vcf_output, txt_output):
    """Saves unique contacts in .vcf and .txt format."""
    with open(vcf_output, 'w', encoding='utf-8') as vcf_file, open(txt_output, 'w', encoding='utf-8') as txt_file:
        for contact in contacts:
            vcf_file.write(contact + "\n\n")
            txt_file.write(contact.replace("\n", " | ") + "\n")  # Convert newlines to a readable format

def process_vcf_files(directory, output_vcf, output_txt):
    """Processes multiple .vcf files and saves unique contacts."""
    all_contacts = set()
    vcf_files = glob.glob(os.path.join(directory, "*.vcf"))

    for vcf_file in vcf_files:
        contacts = extract_contacts_from_vcf(vcf_file)
        all_contacts.update(contacts)

    save_contacts(all_contacts, output_vcf, output_txt)
    print(f"✅ Processed {len(vcf_files)} files and saved {len(all_contacts)} unique contacts.")

# Directory containing .vcf files
input_directory = "data"  # Change this to your folder path
output_vcf_file = "unique_contacts.vcf"
output_txt_file = "unique_contacts.txt"

# Run the script
process_vcf_files(input_directory, output_vcf_file, output_txt_file)
