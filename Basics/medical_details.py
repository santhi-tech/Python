# class for medical requirements
class MedicalRequirements:
    def __init__(self, patient_name, age, blood_type):
        self.patient_name = patient_name
        self.age = age
        self.blood_type = blood_type

    def display_info(self):
        return f"Patient Name: {self.patient_name}, Age: {self.age}, Blood Type: {self.blood_type}"
    
    def is_eligible_for_donation(self):
        # Example eligibility criteria for blood donation
        if self.age >= 18 and self.age <= 65 and self.blood_type in ['A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-']:
            return True
        else:
            return False
        
    def update_blood_type(self, new_blood_type):
        self.blood_type = new_blood_type
        return f"Blood type updated to {self.blood_type}"
    
# scan type class
class Scan_type:
    def __init__(self, scan_name, scan_date):
        self.scan_name = scan_name
        self.scan_date = scan_date

    def display_scan_info(self):
        return f"Scan Name: {self.scan_name}, Scan Date: {self.scan_date}"
    
    def update_scan_date(self, new_scan_date):
        self.scan_date = new_scan_date
        return f"Scan date updated to {self.scan_date}"
    
# class for medical requirements with scan type
class MedicalRequirementsWithScan(MedicalRequirements):
    def __init__(self, patient_name, age, blood_type, scan_name, scan_date):
        super().__init__(patient_name, age, blood_type)
        self.scan = Scan_type(scan_name, scan_date)

    def display_full_info(self):
        medical_info = self.display_info()
        scan_info = self.scan.display_scan_info()
        return f"{medical_info}, {scan_info}"
    
    def update_scan(self, new_scan_name, new_scan_date):
        self.scan.scan_name = new_scan_name
        self.scan.scan_date = new_scan_date
        return f"Scan updated to {self.scan.scan_name} on {self.scan.scan_date}"

# Donate Blood class
class DonateBlood:
    def __init__(self, donor_name, donor_age, donor_blood_type):
        self.donor_name = donor_name
        self.donor_age = donor_age
        self.donor_blood_type = donor_blood_type
    
    def display_donor_info(self):
        medical_info = MedicalRequirements(self.donor_name, self.donor_age, self.donor_blood_type)
        return medical_info.display_info()
