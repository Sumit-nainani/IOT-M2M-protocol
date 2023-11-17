import hashlib
import random
import string
import secrets

database = ["Existing_IDs", "Other_Existing_IDs"]

# Simulated functions to represent hashing and key generation
def h(data):
    return hashlib.sha256(data.encode()).hexdigest()

class SensorNode:
    def register_with_GWN(self, IDj, Xj, Rshrd, TS1, TGWN, delta_T):
        S1 = IDj ^ int(h(str(Rshrd) + str(TS1)), 16)
        S2 = int(h(str(IDj) + str(Xj) + str(Rshrd) + str(TS1)), 16)

        # Simulating sending ⟨S1, S2, TS1⟩ to GWN through an insecure channel
        confirmation = self.send_to_GWN(S1, S2, TS1, TGWN, delta_T)
        if confirmation:
            IDj_prime = S1 ^ int(h(str(Rshrd) + str(TS1)), 16)
            Xj_prime = int(h(str(IDj_prime) + XGWN), 16)
            S2_prime = int(h(str(IDj_prime) + str(Xj) + str(Rshrd) + str(TS1)), 16)
            if S2_prime == S2:
                self.authenticate_and_store(IDj)
                return "Registration successful"
        return "Registration failed"

    def send_to_GWN(self, S1, S2, TS1, TGWN, delta_T):
        if abs(TGWN - TS1) <= delta_T:
            return True
        else:
            return False

    def authenticate_and_store(self, IDj):
        # Simulated storage of IDj into the database
        database.append(IDj)
        # Simulated confirmation message
        print("Confirmation message sent to Sensor Node")


def generate_random_string():
    alphabet = string.ascii_letters + string.digits  # You can add other characters as needed
    return ''.join(secrets.choice(alphabet) for _ in range(random.randint(1, 100)))
# Simulating the sensor node registration process
sensor_node = SensorNode()
IDj = 123
Xj = 456
Rshrd = 789
TS1 = 111
TGWN = 222
delta_T = 10
XGWN = generate_random_string()  # Simulated GWN secret key
registration_status = sensor_node.register_with_GWN(IDj, Xj, Rshrd, TS1, TGWN, delta_T)
print("Registration Status:", registration_status)

# Simulating Step 3 - Sensor Node deletes Rshrd from its memory
Rshrd = None  # Delete Rshrd from memory
