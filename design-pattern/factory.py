from utils import Patient,generate_patient_id
from abc import ABC, abstractmethod

get_id = generate_patient_id()
patient = Patient(
    patient_id=get_id,
    name="Santhi",
    age=18,
    gender="F",
    height=165,
    weight=58,
    temperature=37,
    systolic=120,
    diastolic=80,
    sugar=95,
    spo2=99
)

class Diagnosis():
    @abstractmethod
    def diagnosis(self, test_name,patient_details):
        pass

class mri_scan(Diagnosis):

    def diagnosis(self, patient):

        return f"""
        Running MRI Scan
        Patient_ID : {patient.patient_id}
        Patient : {patient.name}
        Age     : {patient.age}
        Result  : Normal
        """

class ct_scan(Diagnosis):
    def diagnosis(self, patient):

        return f"""
        Running CT Scan
        Patient_ID : {patient.patient_id}
        Patient : {patient.name}
        Age     : {patient.age}
        Result  : Normal
        """
    
class ultrasound(Diagnosis):
    def diagnosis(self, patient):

        return f"""
        Running UltraSound Scan

        Patient : {patient.name}
        Age     : {patient.age}
        Result  : Normal
        """

class pet_scan(Diagnosis):
    def diagnosis(self, patient):

        return f"""
        Running  PET Scan

        Patient : {patient.name}
        Age     : {patient.age}
        Result  : Normal
        """

class DiagnosisFactory:
    @staticmethod
    def get_diagnosis(type):
        if type == "mri":
           return mri_scan()
        elif type == "ct":
            return ct_scan()
        elif type == "ultra":
            return ultrasound()
        elif type == "pet":
            return pet_scan()

if __name__ == "__main__":
    diagnosis = DiagnosisFactory.get_diagnosis("ct")

    result = diagnosis.diagnosis(patient)

print(result)