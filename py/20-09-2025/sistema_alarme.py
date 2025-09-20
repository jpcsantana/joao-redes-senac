
def entrada_dados() -> dict[str, int]:
    print('Para cada dado solicitado, utilize: 0 para NÃO; 1 para SIM')

    tem_fumaca = int(input('Existe algum sinal de fumaça dentro da fábrica?: '))
    tem_botao_emergencia = int(input('O botão de emergência foi pressionado?: '))
    tem_chave_seguranca = int(input('A chave de segurança está ativa?: '))
    tem_movimento = int(input('Há algum movimento nas áreas restritas?: '))

    dados = {
        "f": tem_fumaca,
        "b": tem_botao_emergencia,
        "c": tem_chave_seguranca,
        "m": tem_movimento
    }

    for chave in dados:
        valor: int = dados[chave]
        if valor != 0 and valor != 1:
            raise Exception("Valor diferente de 0 ou 1 encontrado na entrada do usuário. Tente novamente.")
    
    return dados

def alarme_deve_ser_acionado(entrada_dados: dict[str, int]) -> bool:
    result = False
    if bool(entrada_dados["f"]) or (bool(entrada_dados["b"]) and bool(entrada_dados["c"]) or (bool(entrada_dados["m"]) and not bool(entrada_dados["c"]))):
        result = True
    return result

def sistema_alarme() -> None:
    entrada = entrada_dados()
    if(alarme_deve_ser_acionado(entrada)):
        print("\nCom base nos dados fornecidos, o alarme foi ACIONADO.")
    else:
        print("\nDados fornecidos não indicam necessidade de acionar alarme.")
        
try:
    sistema_alarme()
except ValueError as e:
    print('\nValor de entrada inválido.')
except Exception as e:
    print(f"\n{e}")