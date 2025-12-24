```markdown
# 🔐 Password Strength Checker

## Overview
A Python program that evaluates password strength based on common security requirements. Continuously prompts user until a strong password is entered.

## ✨ Features
- Minimum 8 characters length check
- At least 1 uppercase letter (A-Z)
- At least 1 lowercase letter (a-z)
- At least 1 number (0-9)
- At least 1 special character (non-alphanumeric)
- Real-time feedback with specific error messages
- Loop continues until strong password provided

## 🚀 Usage
```
Enter your password to check its strength: abc123
Password should contain at least one uppercase letter.

Enter your password to check its strength: Abc123
Password should contain at least one special character.

Enter your password to check its strength: Abc123!
Your password is strong!
```

## 🧠 Concepts Used
- **String methods**: `isupper()`, `islower()`, `isdigit()`, `isalnum()`, `isspace()`
- **Generators**: `any()` and `all()` with generator expressions
- **Infinite loop**: `while True` with `break`
- **Conditional logic**: Nested `if/elif/else` chain
- **Input validation**: Continuous prompting

## 🔍 Code Structure
```
while True:
    1. Check length < 8 → "Too short"
    2. Check NO uppercase → "Need uppercase"  
    3. Check NO lowercase → "Need lowercase"
    4. Check NO digits → "Need number"
    5. Check ALL alphanumeric/space → "Need special char"
    6. ELSE → "Strong!" + break
```

## ❌ Error Messages (Priority Order)
1. **Length** < 8 chars
2. **No uppercase** letters
3. **No lowercase** letters
4. **No numbers**
5. **No special chars**
6. ✅ **Strong password**

## ✅ Requirements Met
- [x] Strings & string methods
- [x] Multiple conditions (`if/elif`)
- [x] Loop control (`while True`, `break`)
- [x] Input validation
- [x] Clean, readable code

---
**Python Week 1 Practice Project**
```

**Complete README.md content - Copy-paste ready! 🚀**
