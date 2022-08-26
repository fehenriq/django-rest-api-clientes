import re
from validate_docbr import CPF

def cpf_valido(cpf):
    numero_cpf = CPF() 
    return numero_cpf.validate(cpf)

def nome_valido(nome):
    return (nome.isalpha() and nome.isspace() for nome in nome)
    
def rg_valido(rg):
    return len(rg) == 9

def celular_valido(celular):
    """Verifica se o celular é válido (11) 9XXXX-XXXX"""
    modelo = '[0-9]{2}[0-9]{5}[0-9]{4}'
    resposta = re.findall(modelo, celular)
    return resposta