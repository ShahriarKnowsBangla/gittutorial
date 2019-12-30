import re, pyperclip

emailRegex = re.compile(r'[a-zA-Z0-9.+]+[@][a-zA-Z0-9.+]+')
phoneRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

text = pyperclip.paste()

extractedEmailRegex = emailRegex.findall(text)
extractedPhoneRegex = phoneRegex.findall(text)

print(extractedEmailRegex)
print(extractedPhoneRegex)
#Commit
