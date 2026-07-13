import uuid
from datetime import datetime

class Patient:

    def __init__(self, patient_id, name, age, gender,
                 height, weight,
                 temperature,
                 systolic,
                 diastolic,
                 sugar,
                 spo2):

        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.gender = gender

        self.height = height
        self.weight = weight

        self.temperature = temperature
        self.systolic = systolic
        self.diastolic = diastolic
        self.sugar = sugar
        self.spo2 = spo2

def generate_patient_id():
    return str(uuid.uuid4())


def current_time():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")