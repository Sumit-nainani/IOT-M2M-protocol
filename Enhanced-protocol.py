
# Three party secure data transmission in IoT networks through design of a lightweight authenticated key agreement scheme

# In order to overcome the security weaknesses of Amin et al.’s
# protocol and Jiang et al.’s protocol, a secure and efficient
# authentication and key agreement protocol for WSNs is proposed
# in this section. The proposed protocol consists of four phases:
# system setup phase, registration phase, login and verification
# phase, and password change phase.

import hashlib
import random
import string
import secrets


                                         # SYSTEM SETUP PHASE STARTS
                            #*********************************************#

# Step 1:The System administrator selects an identity IDj for every sensor node (Sj) and a master key XGWN ,which is unknown to everyone except the GWN

tamper_proof_memory=[]       # memory of sensor nodes stores <IDj,Xj,Rshrd>
smart_card_data_list=[]      # user smart card details before inserting the card ,stores <Ai,Li,SCNi,BK()>
smart_card_updated_data_list=[]  # user smart card details after inserting the card ,stores <Di,Ci,Ei,SCNi,BK()>


database = [] #sample database of User IDs
sensor_database=[]
# I have taken sample sensor nodes Sj for registration phase 
sensor_nodes = {
    "S1": "123",
    "S2": "456",
    "S3": "789"
}

# Generate a random string of random length 
def generate_random_string():
    alphabet = string.ascii_letters + string.digits  +string.punctuation
    return ''.join(secrets.choice(alphabet) for _ in range(random.randint(1, 20)))

# Simulated functions to represent hashing and key generation
def h(data):
    return hashlib.sha256(data.encode()).hexdigest() + hashlib.sha1(combined_data.encode()).hexdigest()

XGWN = generate_random_string() # secret key of gateway node



# Step 2: GWN computes the secret key for each sensor node
secret_keys = {}
for sensor, IDj in sensor_nodes.items():
    # Combine IDj and XGWN using a hash function to create the secret key Xj
    combined_data = IDj + XGWN
    # hash sha-256 and hash sha-1
    secret_keys[sensor] = h(combined_data)

# Step 3: System administartor chooses a random number Rshrd and shares it between Sj and GWN
shared_random = generate_random_string()

# Storing (IDj, Xj, Rshrd) in a secure manner in tamper-proof memory of sensor nodes
for sensor, IDj in sensor_nodes.items():
    tamper_proof_memory.append([IDj,secret_keys[sensor],shared_random])


print("STORED DATA FOR SENSOR NODES IN FORMAT <IDj,Xj,Rshrd>")
print("*****************************************************\n")
for i in range(3):
    print(tamper_proof_memory[i])
    print("\n")


                                             # SYSTEM SETUP PHASE ENDS
                                  #*********************************************#

#********************************************************************************************************************************************#                                

                                            # USER REGISTRATION PHASE STARTS
                                 #*************************************************#


# simulated_BK_function is a placeholder function intended to simulate a biometric key function. 
# This function doesn't perform any real biometric computations but instead stands 
# as a representation of such a function for the purposes of demonstrating the registration process.
def simulated_BK_function(data):
    return int.from_bytes(data.encode(), byteorder='big')  

# User Ui holds the smart card
# SCNi->unique smart card number
# BK->biometric key generation

class SmartCard:
     # User Ui is registered 
    def __init__(self, Ai, Li, SCNi, BK):
        self.Ai = Ai
        self.Li = Li
        self.SCNi = SCNi
        self.BK = BK

    # User Ui is authenticated 
    def reinitialise(self,Di,Ci,Ei):
        self.Di=Di
        self.Ci=Ci
        self.Ei=Ei
        self.Ai = None
        self.Li = None


class SystemAdministrator:
    # System administrator checks  checks the existence of IDi in the database. If it exists, the SA requests another identity; 
    def check_Ui(self, ID):
        return ID in database

    def register_user(self, ID):
        if self.check_Ui(ID):
            return "Request new identity\n"
        else:
            RSAi = random.randint(1, 100)  # Simulated random number generation specific for each user
            Ai = h(ID + str(RSAi) + XGWN1)
            SCNi = random.randint(1, 100)  # Simulated random number generation for each smart card
            Li = h(str(SCNi) + XGWN1)
            BK = simulated_BK_function  # Assigning the function, not a string
            return Ai,Li,SCNi,BK



class User:
    # The Ui inserts the smart card into a card reader. The Ui inputs fingerprint Bi at the sensor device and ⟨IDi, PWi⟩ in the smart card. At that moment, the smart card selects
    # a random number RNi. The smart card computes 
    # masked biometric Ci = BK(H(Bi)) ⊕ RNi,
    # RPWi = h(IDi∥PWi∥RNi),
    # Di = RPWi ⊕ Ai,
    # Ei = h(IDi∥PWi∥RNi) ⊕ Li. 
    # Finally, the reader stores ⟨Di, Ci, Ei, SCNi, BK()⟩ into the memory and removes ⟨Ai, Li⟩ from it.

    def insert_smart_card(self, smart_card, fingerprint, ID, PW):
        RNi = random.randint(1, 100)  # Simulated random number generation
        Bi_hash = h(fingerprint)  # Simulated biometric data hashing
        Ci = smart_card.BK(Bi_hash) ^ RNi  # Simulated masked biometric data computation
        RPWi = h(ID + PW + str(RNi))
        Di = RPWi + smart_card.Ai
        Ei = h(ID + PW + str(RNi)) + smart_card.Li
        return Di, Ci, Ei, smart_card.SCNi, smart_card.BK
    
    


# Simulating the registration and storage process
SA = SystemAdministrator()
XGWN1 = XGWN
#  Three different users 
for i in range(3):
    
    ID = generate_random_string()
    Ai, Li, SCNi, BK = SA.register_user(ID)
    smart_card = SmartCard(Ai, Li, SCNi, BK)
    smart_card_data_list.append([Ai,Li,SCNi,BK])


    user = User()
    fingerprint_data = generate_random_string()
    password = generate_random_string()
    # inserting Bi fingerprint and giving ID , password
    Di, Ci, Ei, SCNi, BK = user.insert_smart_card(smart_card, fingerprint_data, ID, password)
    # updating smart card details
    smart_card.reinitialise(Di,Ci,Ei)
    smart_card_updated_data_list.append([Di,Ci,Ei,SCNi,BK])
print("SMART CARD DETAILS WHILE REGISTRATION PHASE OF EACH USER IN FORMAT <Ai,Li,SCNi,BK>")
print("***********************************************************************************\n")
for i in range(3):
    print(smart_card_data_list[i])
    print("\n")
print("SMART CARD DETAILS WHILE AUTHENTICATION PHASE OF EACH USER IN FORMAT <Di,Ci,Ei,SCNi,BK>")
print("***************************************************************************************\n")
for i in range(3):
    print(smart_card_updated_data_list[i])
    print("\n")

                                          # USER REGISTRATION PHASE ENDS
                                 #*************************************************#

#**********************************************************************************************************************************************

                                         # SENSOR NODE REGISTRATION PHASE STARTS
                                #*************************************************#
                                         
# Each Sj executes the following procedure to register with the GWN.
# Step 1: Having IDj , Xj , and Rshrd, the Sj first computes S1 = IDj ⊕ h(Rshrd∥TS1) and S2 = h(IDj∥Xj∥Rshrd∥TS1) and 
#         then sends⟨S1, S2, TS1⟩ to the GWN through an insecure channel.
# Step 2. The GWN verifies whether |TGWN − TS1| ≤ ∆T holds. If it is incorrect, the GWN rejects the request of the Sj; 
#         otherwise, it computes ID′j = S1 ⊕ h(Rshrd∥TS1), X′j =h(ID′j∥XGWN ), S′2 = h(ID′j∥Xj∥Rshrd∥TS1) and checks whether
#         S′2 = S2 holds. If it is incorrect, the GWN rejects this request; otherwise, authenticates the Sj and stores IDj into the database.
#         After that, the GWN sends a confirmation message to the Sj.
# Step 3. After receiving the confirmation message, the Sj deletes Rshrd from its memorY
# TS1 is a timestamp or a time-related value that's used during the registration process of the sensor node with the GWN (Gateway Node).      It's part of the computations to verify the registration request and establish authenticity.
# TGWN appears to represent a timestamp or time-related value associated with the Gateway Node (GWN). This value is used in the verification process during the registration of the sensor node.
class SensorNode:
    def register_with_GWN(self, IDj, Xj, Rshrd, TS1, TGWN, delta_T):
        S1 = int(IDj) ^ int(h(str(Rshrd) + str(TS1)),16)
        S2 = int(h(str(IDj) + str(Xj) + str(Rshrd) + str(TS1)), 16)

        # Simulating sending ⟨S1, S2, TS1⟩ to GWN through an insecure channel
        confirmation = self.send_to_GWN(S1, S2, TS1, TGWN, delta_T)
        if confirmation:
            IDj_prime = S1 ^ int(h(str(Rshrd) + str(TS1)), 16)
            Xj_prime = int(h(str(IDj_prime) + XGWN2), 16)
            S2_prime = int(h(str(IDj_prime) + str(Xj) + str(Rshrd) + str(TS1)), 16)
            if S2_prime == S2:
                self.authenticate_and_store(IDj)
                return f"Registration successful for sensor ID {IDj}\n"
        return f"Registration failed for sensor ID {IDj}\n"

    def send_to_GWN(self, S1, S2, TS1, TGWN, delta_T):
        if abs(TGWN - TS1) <= delta_T:
            return True
        else:
            return False

    def authenticate_and_store(self, IDj):
        # Simulated storage of IDj into the database
        sensor_database.append(IDj)
        # Simulated confirmation message
        print("Confirmation message is sent to Sensor Node having ID ,",IDj)



# Simulating the sensor node registration process
for sensor, IDj in sensor_nodes.items():
    Rshrd = shared_random
    Xj = secret_keys[sensor]
    XGWN2 = XGWN
    TS1 = random.randint(1,100)
    TGWN = random.randint(1,100)
    delta_T = random.randint(1,100) # constant transmission delay
    sensor_node = SensorNode()
    registration_status = sensor_node.register_with_GWN(IDj, Xj, Rshrd, TS1, TGWN, delta_T)
    print("Registration Status:", registration_status)
# Simulating Step 3 - Sensor Node deletes Rshrd from its memory
    Rshrd = None  

print("Following are Registered sensor Nodes : ",sensor_database)
                                                 
                                                   # SENSOR NODE REGISTRATION PHASE NDS
                                           #*************************************************#

#**********************************************************************************************************************************************
