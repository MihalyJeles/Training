import requests

# Replace these with your actual login URL and PDF URL
login_url = 'https://gas.mcd.com/adfs/ls/?SAMLRequest=fZFPU4MwEMW%2FCpN7CSB%2F2kxhBtuDnanKFPTgxQkQWsaQYDYR%2FfZC0bFeet73fm%2F37Rpox3uSGn0SB%2FZuGGjrs%2BMCyHkQI6MEkRRaIIJ2DIiuSJ7e74lnO6RXUstKcmSlAEzpVoqNFGA6pnKmPtqKPR32MTpp3QPBeBgGu6tq0KZp7Era5g0DSDzhPJw95gWytmN%2BK%2BhE%2BvMdKUy%2B0dJhWjeAOWBk7bYxel26vtusfN8N%2FCiKwpUfOnW4ZE5Z3ixZGXmjDMCwnQBNhY6R53jBwgkWXli4AXF94q1ekJX93HHbiroVx%2BtHl7MIyF1RZIt57Wem4LzyKEDJeqqOnIPVRZnXsfS3QZRc72uNL%2FBzVk8eRt5um0neVl9WyrkcNopRzWLkIpzMlv9fTr4B&RelayState=ss%3Amem%3Af67795e7801a3c0a354eea19710a9de954d61f46a8049227328dde47043c3b57&SigAlg=http%3A%2F%2Fwww.w3.org%2F2001%2F04%2Fxmldsig-more%23rsa-sha256&Signature=IgKBfWFQcKAzpsJtx6YXt1Ln4ko8731S3D9k3ghMcZzjBA8jdVP209QcPg%2FEKN3PAuuKvOczr1k6zB3mVJWHWzZhe2hMYzDM02Ft8LsV4u9E7MJa8lBdnwAPW%2ByxmfKSRXJyrl1XV21%2BqgIG0B5NotNqLAKoivU6kcAbtfEq%2BUHqmyE0LzO3wVj4ti0sdHuMmR4UVd3SUvgAFZu5sALiYTHik89%2FLOrDjOeKQ3RxxddkSfkbc%2FGAgbWQGGVgrQtJcbZcRX2U7BYMXxe3PhdARUjTmypQt3K4zNz7RdhGH5sN3h56bCmcrQ0iOscFiAfOH07aT9SLGp97WR%2BubpGanm%2BODgAqy2CC8CfUo90uZvqahIvVv%2FHxKH7cnovl4KAy7ffKycGUOB4yxoFL%2F75XYKINQLU4XVIEs7pFx3M732oryv8j6uwM7zGVmEsWdYn059tnlE%2BflMhpRRNTbHpHh2%2BTR%2BczUgu4tMrEeHLIHQIYJJP77hfOQxpjWd53Zqw6'
pdf_url = 'https://example.com/secure/file.pdf'

# Your login credentials
payload = {
    'username': 'e8002577',
    'password': 'Bruhaha4444444444!'
}

# Create a session to persist cookies
session = requests.Session()

# Log in to the website
login_response = session.post(login_url, data=payload)

# Check if login was successful
if login_response.ok:
    print("Login successful!")

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
#     print("Login failed.")j

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

# -------------------------------------------------------------

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
