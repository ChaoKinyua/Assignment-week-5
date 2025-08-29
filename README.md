# 📱 OOP Assignment 1 — Smartphone & Device Classes

## 📖 Project Overview

This project is part of **Assignment 1: Design Your Own Class** in Python.
It demonstrates **Object-Oriented Programming (OOP)** concepts by creating classes that represent real-world devices such as **Smartphones** and **Tablets**.

The project covers key OOP pillars:

* **Classes & Objects**
* **Constructors (`__init__`)**
* **Encapsulation (public, protected, and private attributes)**
* **Inheritance**
* **Polymorphism (method overriding)**

---

## 🏗️ Classes Implemented

### 🔹 `Device` (Base Class)

* Attributes: `brand`, `model`, `_battery` (protected), `__serial` (private)
* Methods:

  * `get_serial()` → safely access private serial number
  * `device_info()` → show basic device info
  * `charge()` → recharge the device battery

### 🔹 `Smartphone` (Child Class of `Device`)

* Additional Attributes: `os`, `storage`, `apps`
* Methods:

  * `install_app(app)` → install an app
  * `show_apps()` → display installed apps
  * `device_info()` → overridden method with smartphone-specific details

### 🔹 `Tablet` (Child Class of `Device`)

* Additional Attribute: `pen_support` (boolean)
* Methods:

  * `device_info()` → overridden method with tablet-specific details

---

## ⚙️ How It Works

1. **Create objects** from classes (e.g., a smartphone or tablet).
2. **Encapsulation**: Access hidden details like serial number via a method.
3. **Inheritance**: Both smartphone and tablet inherit from the base `Device`.
4. **Polymorphism**: The `device_info()` method behaves differently depending on the object type.
5. **Methods** like `install_app()` and `charge()` simulate real-world interactions.

---

## ▶️ Example Usage

```python
# Create objects
phone = Smartphone("Samsung", "Galaxy S25", "Android", 256)
tablet = Tablet("Apple", "iPad Pro", True)

# Encapsulation
print(phone.get_serial())  

# Install apps
phone.install_app("WhatsApp")
phone.install_app("Spotify")
print(phone.show_apps())

# Polymorphism in action
print(phone.device_info())  
print(tablet.device_info())

# Battery interaction
phone.charge(15)
```

---

## 🖥️ Sample Output

```
Serial Number: SN123456
📲 Installed WhatsApp!
📲 Installed Spotify!
Installed Apps: WhatsApp, Spotify
Samsung Galaxy S25 | OS: Android | Storage: 256GB | Battery: 100%
Apple iPad Pro | Pen Support: Yes | Battery: 100%
🔋 Charged! Battery now at 100%
```

---

## 📌 Key Learning Outcomes

✅ Mastered class creation and initialization with `__init__()`
✅ Understood **Encapsulation** with private & protected attributes
✅ Applied **Inheritance** by extending `Device` into `Smartphone` & `Tablet`
✅ Practiced **Polymorphism** by overriding `device_info()`
✅ Made code more **realistic and reusable** with methods like `install_app()`

---

📂 **Files in Project Folder**

* `device.py` → contains the class definitions
* `main.py` → test file to run and interact with objects
* `README.md` → project documentation (this file)

---

