quant_coca = 150
quant_pepsi = 130
preco_coca = 1.50
preco_pepsi = 1.50
custo_loja = 2500


fatu_pepsi = quant_pepsi * preco_pepsi
fatu_coca = quant_coca * preco_coca
faturamento = fatu_pepsi + fatu_coca
lucro = faturamento - custo_loja


print (fatu_pepsi)
print (fatu_coca)
print (faturamento)
print (lucro)

#Coca -> Código: BEB1300543
#Pepsi -> Código: BEB1300545
#Vinho Primitivo Lucarelli -> Código: BAC1546001
#Vodka Smirnoff -> Código: BAC1767500

codigo = str(input('Qual é o código da bebida? ')).upper() #em maiusculo porque os códigos deverão ser assim
print (codigo)
print("BAC" in codigo)