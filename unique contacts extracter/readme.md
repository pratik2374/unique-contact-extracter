# Contact Extractor

This project provides a Python script to extract and save unique contacts from multiple VCF (vCard) files. The extracted contacts are saved in both `.vcf` and `.txt` formats.
Also this project provides a Python script where you can search contacts from generated unique comtacts with a beautiful UI


## Features

- Extracts individual contacts from VCF files.
- Removes duplicate contacts.
- Saves unique contacts in `.vcf` and `.txt` formats.

## Requirements

- Python 3.x

## Usage

1. Clone the repository or download the script.
2. Place your VCF files in a directory (e.g., `data`).
3. Update the `input_directory` variable in the script to point to your directory containing VCF files.
4. Run the script.

```bash
python contact_extractor.py
```

## Output

- `unique_contacts.vcf`: Contains all unique contacts in VCF format.
- `unique_contacts.txt`: Contains all unique contacts in a readable text format.

## License

This project is licensed under the MIT License.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## Contact

For any questions or suggestions, please open an issue.
