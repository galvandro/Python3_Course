v = input('Digite algo... ')

print(f'''
Vejamos... você digitou {v}.
     
Tipo primitivo: {type(v)}
Está numerado? {v.isnumeric()}
Está alfabético? {v.isalpha()}
Está alfanumérico? {v.isalnum()}
Estão somente espaços? {v.isspace()}
Estão somente maiúsculas? {v.isupper()}
Estão somente minusculas? {v.islower()}
Está capitalizado? {v.istitle()}
''')