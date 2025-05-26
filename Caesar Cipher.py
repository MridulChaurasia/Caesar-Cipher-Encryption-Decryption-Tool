def caeser_cipher(text, shift, mode='encrypt'):
	result = ''
	if mode == 'decrypt':
		shift = -shift
	for char in text:
		if char.isalpha():
			base = ord('A') if char.isupper() else ord('a')
			shifted = (ord(char) - base + shift) % 26 + base
			result += chr(shifted)
		else:
			result += char
	return result
def main():
	print("===== Caesar_Cipher_Tool =====")
	choice = input(" Type 'encrypt' to encrypt or 'decrypt' to decrypt : ").strip().lower()
	if choice not in ['encrypt', 'decrypt']:
		print("Invalid choice. Exiting...")
		return
	message = input("Enter your message : ")
	try:
		shift = int(input("Enter shift value (e.g., 4) : "))
	except ValueError:
		print("Shift value must be an integer. Exiting...")
		return
	result = caeser_cipher(message, shift, mode=choice)
	print(f"\nResult ({choice.title()}ed Text) : {result}")
if __name__ == "__main__":
	main()
