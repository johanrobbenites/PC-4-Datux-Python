import re
texto = '@robot9! @robot4& I have a good feeling that the show isgoing to be amazing! @robot9$ @robot7%'
regex='@robot\d\D'

print(re.findall(regex, texto))