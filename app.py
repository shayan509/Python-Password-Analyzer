import streamlit as st
import re
import string
import random
def check_password_strength(password: str):
    score = 0
    feedback = []
    
    if len(password) > 0:
        score += 1

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Make your password at least 8 characters long.")
    
    if any(char.islower() for char in password) and any(char.isupper() for char in password):
        score += 1
    else:
        feedback.append("Include both uppercase and lowercase letters.")
    
    if any(char.isdigit() for char in password):
        score += 1
    else:
        feedback.append("Add at least one numeric digit (0-9).")
    
    if re.search(r'[!@#$()[}%^&*/.,><\|?]', password):
        score += 1
    else:
        feedback.append("Include at least one special character (!@#$%^&*).")
    
    return score, feedback

def generate_password(length=12):
    # Ensure the generated password has at least one lowercase, one uppercase, one digit, and one special character
    password = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(string.digits),
        random.choice("!@#$%^&*")
    ]
    # Fill the remaining length with random characters from all groups
    all_chars = string.ascii_letters + string.digits + "!@#$%^&*"
    for _ in range(length - 4):
        password.append(random.choice(all_chars))
    
    random.shuffle(password)
    return "".join(password)

def main():
    st.title("🔐 Password Strength Checker")

    st.markdown("### Password Requirements:")
    st.markdown("* Be at least 8 characters long")
    st.markdown("* Contain uppercase and lowercase letters")
    st.markdown("* Include at least one digit (0-9)")
    st.markdown("* Have one special character (!@#$%^&*)")
    
    st.header("Examples of Strong Passwords:")
    st.markdown("* Abc123!@#")
    st.markdown("* MynameCity21!")
    
    st.header("Enter your password to check its strength:")
    
    password = st.text_input("Enter your password:", type="password")
    check = st.button("Check Password")
    
    if check or password:
        score, feedback = check_password_strength(password)
        if score == 5:
            st.success("✅ Strong Password! Your password meets all security criteria.")
        elif score >= 3:
            st.warning("⚠️ Moderate Password. Consider making it stronger.")
        elif score >= 1:
            st.error("❌ Weak Password. Improve your password using the suggestions below.")
        else:
            st.error("❌ Empty Password. Please enter a password.")
        st.progress(score / 5)
        
        if feedback and score > 0:
            st.subheader("🔧 Suggestions to Improve:")
            for tip in feedback:
                st.write(f"- {tip}")
    
    st.header("Generate Strong Password")
    password_length = st.slider("Select password length:", min_value=8, max_value=20, value=12, step=1)
    st.write("Click the button below to generate a random and strong password:")
    gen_button = st.button("Generate Password")
    if gen_button:
        generated_password = generate_password(password_length)
        st.write("Generated Password:")
        st.success(generated_password)

    st.header("Importance of Strong Passwords:")
    st.write("In today's digital world, strong passwords are essential as they serve as the first line of defense against cyber threats. They protect our personal information, financial assets, and sensitive data from unauthorized access and cyberattacks. By using complex combinations of characters, numbers, and symbols, strong passwords make it significantly more difficult for hackers to breach our accounts and compromise our digital security.")
    
    st.subheader("Built by Muhammad Shayan Imran")
    
if __name__ == "__main__":
    main()
