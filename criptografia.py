def criptografar(texto):
 resultado = ""
 for char in texto:
   if char.isalpha():
     shift = 7
     if char.islower():
       ascii_offset = ord('a')
     else:
       ascii_offset = ord('A')
     criptografado = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
     resultado += criptografado
   else:
     resultado += char
   return resultado
def descriptografar(texto):
 resultado = ""
 for char in texto:
   if char.isalpha():
     shift = 7
     if char.islower():
       ascii_offset = ord('a')
     else:
       ascii_offset = ord('A')
     descriptografado = chr((ord(char) - ascii_offset - shift) % 26 + ascii_offset)
     resultado += descriptografado
   else:
 resultado += char
   return resultado
texto_original = input("Digite o texto que você deseja criptografar: ")
texto_criptografado = criptografar(texto_original)
print("\nTexto criptografado:")
print(texto_criptografado)
print("\n---------------------------------\n")
while True:
 escolha = input("Escolha uma opção:\n1 - Descriptografar\n2 - Sair\n")
 if escolha == "1":
   print("\nTexto original:")
   print(texto_original)
   print("\n---------------------------------\n")
 elif escolha == "2":
   break
 else:
   print("Opção inválida. Por favor