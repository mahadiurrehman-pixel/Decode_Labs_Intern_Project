# 🔐 Enterprise Random Password Generator

A secure Python-based random password generator that creates **cryptographically strong passwords** using Python's built-in `secrets` module.

Unlike the standard `random` module, this project uses `secrets` for secure password generation, making it suitable for creating passwords for real-world applications.

---

## ✨ Features

- 🔒 Cryptographically secure password generation
- 🔢 Supports custom password length
- 🔤 Includes:
  - Uppercase letters
  - Lowercase letters
  - Numbers
  - Special characters
- 📊 Calculates password entropy (security strength)
- ✅ Simple command-line interface
- ⚡ Lightweight and fast

---

## 📂 Project Structure

```
password-generator/
│── password_generator.py
│── README.md
```

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/password-generator.git
```

### 2. Navigate to the Project

```bash
cd password-generator
```

### 3. Run the Program

```bash
python password_generator.py
```

---

## 💻 Example Output

```
=== Enterprise Random Password Generator ===

Enter desired password length (Recommended >= 15): 16

--- Generated Credentials ---
Password: Tm#4pW!9x@Q2L$eK
Entropy : 104.87 bits
```

---

## 🧠 How It Works

The program:

1. Asks the user for the desired password length.
2. Creates a character pool consisting of:
   - Letters (A-Z, a-z)
   - Digits (0-9)
   - Symbols
3. Uses Python's `secrets.choice()` to randomly select characters.
4. Joins the selected characters into a secure password.
5. Calculates password entropy using:

```text
Entropy = Password Length × log₂(Character Pool Size)
```

Higher entropy means a stronger and more difficult-to-crack password.

---

## 📦 Requirements

- Python 3.8+
- No external libraries required

The project only uses Python's standard library:

- `math`
- `secrets`
- `string`

---

## 🔒 Why Use `secrets` Instead of `random`?

The `random` module is designed for simulations and games, not security.

The `secrets` module:

- Uses cryptographically secure random numbers
- Is recommended by Python for password generation
- Makes passwords significantly harder to predict

---

## 📈 Entropy Guide

| Entropy (bits) | Strength |
|---------------:|----------|
| < 40 | Weak |
| 40–60 | Moderate |
| 60–80 | Strong |
| 80–100 | Very Strong |
| 100+ | Excellent |

---

## 🎯 Future Improvements

- Copy password to clipboard
- Save generated passwords securely
- Exclude confusing characters (O, 0, l, I)
- Require at least one uppercase, lowercase, digit, and symbol
- Generate multiple passwords at once
- GUI version using Tkinter or PyQt
- Export passwords to encrypted storage

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a new feature branch
3. Commit your changes
4. Push to your branch
5. Open a Pull Request

---

## 📄 License

This project is open source and available under the **MIT License**.

---

## 👨‍💻 Author

**Mahadi Ur Rehman Siddiqui**

- AI & Machine Learning Enthusiast
- Python Developer
- Future AI Entrepreneur

If you found this project useful, consider giving it a ⭐ on GitHub!
