import re

def extract_emails(file_path):
    try:
        with open(file_path, "r") as file:
            text = file.read()
            emails = re.findall(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b", text)
            return emails
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return []

def save_emails(emails, output_file):
    with open(output_file, "w") as file:
        for email in emails:
            file.write(email + "\n")
    print(f"Emails saved to '{output_file}'")

if __name__ == "__main__":
    file_path = input("Enter .txt file path: ")
    output_file = input("Enter output file path: ")
    emails = extract_emails(file_path)
    save_emails(emails, output_file)