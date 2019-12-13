# -*- coding: utf-8 -*-



#Ejercicios unidad 4
import re
path = "Archivo.txt"

try:
    archivo = open(path,'r')
except:
    print ("el archivo que intentas abrir no existe")
    quit()

texto = ""

for linea in archivo:
    texto += linea

print ("\nOperadores relacionales")
patron = r"[|<|>|!=|<=|>=|=]+"
result = re.findall(patron,texto)
print ("Resultado\n", result)

print ("\nVariables válidas")
patron = r'[A-Za-z0-9-]+\s+[=]+'
resultado = re.findall(patron,texto)
print ("Resultado\n", resultado)

print ("\nOperadores aritméticos")
patron = r"[\+|\-|\*|\/]"
result = re.findall(patron,texto)
print ("Resultado\n", result)

print ("\nEnteros y decimales")
patron = r"([0-9]+.[0-9]+|[0-9]+)"
result = re.findall(patron,texto) 
print ("Resultado\n", result)

print ("\nPalabras reservadas")
patron = r"(else|for|import|class|try|while|False|def|if|raise|None|return )"
result = re.findall(patron,texto)
print ("Resultado\n", result)


#Ejercicios Unidad 5


try:
	archivo = open(path,'r')
except:
	print("El archivo no se encuentra")
	quit()

texto = ""
 
for linea in archivo:
	texto += linea


print ("\nSentencia de asignación")
patron = r"([a-z0-9]+\s*=\s*[a-z0-9+]+)"
resultado = re.findall(patron,texto)
print ("Resultado\n", resultado)

print ("\nOperaciones booleanas")
patronA = r"([A-Za-z0-9|a-z0-9]+\s*[=|<|>|!|<=|>=]+\s*[A-Za-z0-9|a-z0-9]+)"
resultadoA = re.findall(patronA, texto)
print ("Resultado\n", resultadoA)

print ("\nOperaciones aritmeticas")
patronB = r"([A-Za-z0-9-_]+\s*[=]+\s*[A-Za-z0-9-_|0-9.0-9]+\s*[\+,\-,\*,\/,\%]+\s*[A-Za-z0-9-_|0-9.0-9]+)"
resultadoB = re.findall(patronB,texto)
print ("Resultado\n", resultadoB)

print ("\nFormulas complejas")
patronC = r'([A-Za-z0-9]+\s*=+\s*[A-Za-z0-9]+\s*[|<|>|!|<=|>=|\+|\-\*\/]\s*[(]+\s*[A-Za-z0-9]+\s*[|<|>|!|<=|>=|\+|\-\*\/]+\s*[A-Za-z0-9]+\s*[)])'
resultadoC = re.findall(patronC,texto)
print ("Resultado\n", resultadoC)

print ("\nOperaciones de encabezado FOR,WHILE,IF,TRY")
patronD= r'(for+\s*[A-Za-z0-9-_]+\s*[in]+\s*[A-Za-z0-9-_]+\s*:)'
resultadoD = re.findall(patronD, texto)
print ("Resultado\n", resultadoD)

patronE = r'(while+\s*[A-Za-z0-9-_]+\s*[|<|>|!|<=|>=]=+\s*[A-Za-z0-9-_]+\s*:)'
resultadoE = re.findall(patronE,texto)
print ("Resultado\n", resultadoE)

patronF = r'(if+\s*[A-Za-z0-9-_]+\s*[|<|>|!|<=|>=]=+\s*[A-Za-z0-9-_]+\s*:)'
resultadoF = re.findall(patronF,texto)
print ("Resultado\n", resultadoF)

patronG = r'(try:+\s*[A-Za-z0-9-_]+\s*except+\s*[A-Za-z0-9-_]+\s*:)'
resultadoG = re.findall(patronG,texto)
print ("Resultado\n", resultadoG)