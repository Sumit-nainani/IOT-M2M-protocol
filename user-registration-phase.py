import hashlib
import secrets
import random
import string


smart_card_data_list=[]
smart_card_updated_data_list=[]
database = ["Existing_IDs", "Other_Existing_IDs"]
# Simulated functions to represent hashing and key generation
def h(data):
    return hashlib.sha256(data.encode()).hexdigest()

def simulated_BK_function(data):
    return int.from_bytes(data.encode(), byteorder='big')  # Example transformation

class SmartCard:
    def __init__(self, Ai, Li, SCNi, BK):
        self.Ai = Ai
        self.Li = Li
        self.SCNi = SCNi
        self.BK = BK
    
    def reinitialise(self,Di,Ci,Ei,Ai,Li):
        self.Di=Di
        self.Ci=Ci
        self.Ei=Ei
        self.Ai = ""
        self.Li = ""


class SystemAdministrator:
    def check_database(self, ID):
        return ID in database

    def register_user(self, ID):
        if self.check_database(ID):
            return "Request new identity"
        else:
            RSAi = random.randint(1, 100)  # Simulated random number generation
            Ai = h(ID + str(RSAi) + XGWN)
            SCNi = random.randint(1, 100)  # Simulated random number generation
            Li = h(str(SCNi) + XGWN)
            BK = simulated_BK_function  # Assigning the function, not a string
            return Ai,Li,SCNi,BK



class User:
    def insert_smart_card(self, smart_card, fingerprint, ID, PW):
        RNi = random.randint(1, 100)  # Simulated random number generation
        Bi_hash = h(fingerprint)  # Simulated biometric data hashing
        Ci = smart_card.BK(Bi_hash) ^ RNi  # Simulated masked biometric data computation
        RPWi = h(ID + PW + str(RNi))
        Di = RPWi + smart_card.Ai
        Ei = h(ID + PW + str(RNi)) + smart_card.Li
        return Di, Ci, Ei, smart_card.SCNi, smart_card.BK
    

def generate_random_string():
    alphabet = string.ascii_letters + string.digits  # You can add other characters as needed
    return ''.join(secrets.choice(alphabet) for _ in range(random.randint(1, 100)))

# Simulating the registration and storage process
SA = SystemAdministrator()
XGWN = generate_random_string()  # Simulated GWN secret key

ID = generate_random_string()
Ai, Li, SCNi, BK = SA.register_user(ID)
smart_card = SmartCard(Ai, Li, SCNi, BK)
smart_card_data_list.append([Ai,Li,SCNi,BK])


user = User()
fingerprint_data = "Simulated_Fingerprint"
password = "Simulated_Password"


Di, Ci, Ei, SCNi, BK = user.insert_smart_card(smart_card, fingerprint_data, ID, password)
smart_card.reinitialise(Di,Ci,Ei,"y","")
smart_card_updated_data_list.append([Di,Ci,Ei,smart_card.Ai,smart_card.Li,SCNi,BK])

