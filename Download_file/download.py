import requests

def fajl_letoltes(url, cel_fajlnev):
    try:
        response = requests.get(url, cel_fajlnev)
        response.raise_for_status()  # Hibát dob, ha nem sikerült a letöltés
        with open(cel_fajlnev, 'wb') as f:
            f.write(response.content)
        print(f"Sikeresen letöltve: {cel_fajlnev}")
    except requests.exceptions.RequestException as e:
        print(f"Hiba történt a letöltés során: {e}")
# Példa használat:
# url = "https://example.com/fajl.pdf"  # Cseréld ki a kívánt URL-re
# cel_fajlnev = "letoltott_fajl.pdf"     # Cseréld ki a kívánt fájlnévre
url = "https://www.mcdstuff.co.uk/portal.php?site=portal&page=spa#view=employeefiles"  # Cseréld ki a kívánt URL-re
cel_fajlnev = "04039745-Payslip-2025_05-18_05_2025.pdf"     # Cseréld ki a kívánt fájlnévre
fajl_letoltes(url, cel_fajlnev)

-------------------------------------------------------------

# mport requests

# # Replace these with your actual login URL and PDF URL
# login_url = 'https://example.com/login'
# pdf_url = 'https://example.com/secure/file.pdf'

# # Your login credentials
# payload = {
#     'username': 'your_username',
#     'password': 'your_password'
# }

# # Create a session to persist cookies
# session = requests.Session()

# # Log in to the website
# login_response = session.post(login_url, data=payload)

# # Check if login was successful
# if login_response.ok:
#     print("Login successful!")

#     # Now download the PDF
#     pdf_response = session.get(pdf_url)

#     # Save the PDF to a file
#     if pdf_response.ok:
#         with open('downloaded_file.pdf', 'wb') as f:
#             f.write(pdf_response.content)
#         print("PDF downloaded successfully!")
#     else:
#         print("Failed to download PDF.")
# else:
#     print("Login failed.")
