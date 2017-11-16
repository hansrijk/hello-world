import re



phoneNumRegex=re.compile(r'\d\d-\d\d\d\d\d\d\d\d')
print(phoneNumRegex.findall('Bel me morgen op dit nummer: 0633843423 of op mijn kantoornummer: 0320-288215.'))

