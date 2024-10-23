import random
import string

def generate_otp(length):
    letters_and_digits = string.ascii_letters + string.digits
    otp = ''.join(random.choice(letters_and_digits) for _ in range(length))
    return otp
# Example usage
otp_length = 8
otp = generate_otp(otp_length)
print("Generated OTP:", otp)