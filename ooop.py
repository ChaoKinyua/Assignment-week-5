# -----------------------------
# 📱 Smartphone OOP Example
# -----------------------------

# Base Class (Parent)
class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self._battery = 100   # protected attribute
        self.__serial = "SN123456"  # private attribute (encapsulation)

    def get_serial(self):
        """Public method to access private serial safely."""
        return f"Serial Number: {self.__serial}"

    def device_info(self):
        return f"{self.brand} {self.model} | Battery: {self._battery}%"

    def charge(self, amount):
        self._battery = min(100, self._battery + amount)
        print(f"🔋 Charged! Battery now at {self._battery}%")

# Derived Class (Child)
class Smartphone(Device):
    def __init__(self, brand, model, os, storage):
        super().__init__(brand, model)  # inheritance
        self.os = os
        self.storage = storage
        self.apps = []

    # Polymorphism (method overriding)
    def device_info(self):
        return f"{self.brand} {self.model} | OS: {self.os} | Storage: {self.storage}GB | Battery: {self._battery}%"

    def install_app(self, app):
        self.apps.append(app)
        print(f"📲 Installed {app}!")

    def show_apps(self):
        return f"Installed Apps: {', '.join(self.apps)}" if self.apps else "No apps installed."

# Another Derived Class (Polymorphism Demo)
class Tablet(Device):
    def __init__(self, brand, model, pen_support):
        super().__init__(brand, model)
        self.pen_support = pen_support

    # Polymorphism → overriding method
    def device_info(self):
        pen_status = "Yes" if self.pen_support else "No"
        return f"{self.brand} {self.model} | Pen Support: {pen_status} | Battery: {self._battery}%"

# -----------------------------
# ✅ Testing the Classes
# -----------------------------
phone = Smartphone("Samsung", "Galaxy S25", "Android", 256)
tablet = Tablet("Apple", "iPad Pro", True)

# Encapsulation
print(phone.get_serial())  

# Using methods
phone.install_app("WhatsApp")
phone.install_app("Spotify")
print(phone.show_apps())

# Polymorphism in action
print(phone.device_info())  
print(tablet.device_info())

# Battery interaction
phone.charge(15)
