# Here is the first parent class providing camera capabilities
class Camera:
    def take_photo(self):
        print("Taking a high-resolution photo...")

# Here is the second parent class providing phone call capabilities
class Phone:
    def make_call(self, phone_number):
        print(f"Calling {phone_number}...")

# Here is a child class Smartphone inheriting from both Camera and Phone
class Smartphone(Camera, Phone):
    def browse_internet(self):
        print("Browsing the web on smartphone...")

# Here is creating a Smartphone object with access to methods from both parents
my_phone = Smartphone()
my_phone.make_call("+7-777-123-4567")
my_phone.take_photo()
my_phone.browse_internet()