import secrets
import string

def gerar_senha(tamanho = 1):
    
    #Primeiro definir os conjuntos de caracteres

    maiusculas = string.ascii_uppercase
    minusculas = string.ascii_lowercase
    digitos = string.digits
    especiais = string.punctuation

    #Segundo: garantir pelo menos 1 caracter de cada tipo
    
    senha = [
        secrets.choice(maiusculas),
        secrets.choice(minusculas),
        secrets.choice(digitos),
        secrets.choice(especiais)
    ]

    #Terceiro: completar o restante da senha com caracteres de todos os tipos

    todos_caracteres = maiusculas + minusculas + digitos + especiais

    for _ in range(tamanho - 4):
        senha.append(secrets.choice(todos_caracteres))

    #Quarto: Embaralhar a senha

    secrets_random = secrets.SystemRandom()
    secrets_random.shuffle(senha)

    return "".join(senha)

    #Teste de validacao de senhas(Se a senha nao for valida, gera uma nova)

def validar_senha(tamanho = 10):
    while True:
        senha = gerar_senha(tamanho)
        #Validar se tem ao menos 1 caracter de cada tipo
        tem_maiuscula = any(c.isupper() for c in senha)
        tem_minuscula = any(c.islower() for c in senha)
        tem_digito = any(c.isnumeric() for c in senha)
        tem_especial = any(c in string.punctuation for c in senha)

        if tem_maiuscula and tem_minuscula and tem_digito and tem_especial:
            return senha

for i in range (3):
    senha = validar_senha(10)
    print(f"Senha Validada {i+1}: {senha}")