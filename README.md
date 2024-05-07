This Python code implements the Caesar cipher algorithm, a simple substitution cipher technique used for encryption and decryption of text. Here's a brief description of how the code works:

1. **Caesar Cipher Algorithm Function (`caesar_cipher`)**:
   - Parameters:
     - `text`: The input text to be encrypted or decrypted.
     - `shift`: An integer representing the amount of shift for the cipher.
     - `decrypt`: A boolean flag indicating whether to encrypt (`False`) or decrypt (`True`) the text.
   - Description:
     - The function iterates through each character in the input text.
     - For each alphabetic character, it calculates the new character after applying the Caesar cipher shift.
     - Non-alphabetic characters remain unchanged.
     - The shift can be either positive (for encryption) or negative (for decryption).
     - The modulus operator `% 26` ensures that the shift wraps around within the range of the alphabet (26 letters).
     - Upper-case characters are preserved as upper-case after encryption/decryption.

2. **Main Function (`main`)**:
   - Contains the main program logic.
   - It continuously prompts the user to choose between encryption, decryption, or exiting the program.
   - Depending on the user's choice, it takes input text, shift value, and calls the `caesar_cipher` function accordingly.
   - It handles invalid user inputs by displaying an appropriate message.

3. **User Interaction**:
   - Users can choose to encrypt or decrypt text by entering their choice (1 or 2).
   - For encryption, they input the plaintext and the shift value.
   - For decryption, they input the ciphertext and the shift value (along with setting the `decrypt` flag to `True`).
   - The program continues to run until the user chooses to exit.

Overall, the code provides a basic implementation of the Caesar cipher algorithm, allowing users to encrypt and decrypt messages with a specified shift value. However, it's important to note that the Caesar cipher is relatively weak in terms of security, as it can be easily cracked through brute force or frequency analysis, especially with modern computing power.
