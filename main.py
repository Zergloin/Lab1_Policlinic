from typing import List, Union


class CustomError(Exception):
    """Исключение для обработки ошибок в клинике."""
    pass


class Person:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age


class Insurance:
    def __init__(self, provider: str, policy_number: str) -> None:
        self.provider = provider
        self.policy_number = policy_number

    def __str__(self) -> str:
        return f"Insurance(Provider: {self.provider}, Policy_number: {self.policy_number})"


class MedicalRecord:
    def __init__(self, diagnosis: str, treatment: str) -> None:
        self.diagnosis = diagnosis
        self.treatment = treatment


class Prescription:
    def __init__(self, medication: str) -> None:
        self.medication = medication


class Patient(Person):
    def __init__(self, name: str, age: int, insurance: Insurance) -> None:
        super().__init__(name, age)
        self.insurance = insurance
        self.medical_records: List[MedicalRecord] = []
        self.prescriptions: List[Prescription] = []
        self.treatment_plans: List['TreatmentPlan'] = []

    def __str__(self) -> str:
        return f"Patient(Name: {self.name}, Age: {self.age}, Insurance: {self.insurance.provider})"

    def add_medical_record(self, record: MedicalRecord) -> None:
        self.medical_records.append(record)

    def update_medical_record(self, index: int, diagnosis: str, treatment: str) -> None:
        try:
            if 0 <= index < len(self.medical_records):
                self.medical_records[index].diagnosis = diagnosis
                self.medical_records[index].treatment = treatment
            else:
                raise CustomError("Ошибка: Индекс медицинской записи вне диапазона.")
        except CustomError as ex:
            print(ex)

    def add_prescription(self, prescription: Prescription) -> None:
        self.prescriptions.append(prescription)

    def update_prescription(self, index: int, medication: str) -> None:
        try:
            if 0 <= index < len(self.prescriptions):
                self.prescriptions[index].medication = medication
            else:
                raise CustomError("Ошибка: Индекс рецепта вне диапазона.")
        except CustomError as ex:
            print(ex)

    def add_treatment_plan(self, treatment_plan: 'TreatmentPlan') -> None:
        self.treatment_plans.append(treatment_plan)


class Doctor(Person):
    def __init__(self, name: str, age: int, specialty: str) -> None:
        super().__init__(name, age)
        self.specialty = specialty

    def __str__(self) -> str:
        return f"Doctor(Name: {self.name}, Age: {self.age}, Specialty: {self.specialty})"


class Staff(Person):
    def __init__(self, name: str, age: int, position: str) -> None:
        super().__init__(name, age)
        self.position = position

    def __str__(self) -> str:
        return f"Staff(Name: {self.name}, Age: {self.age}, Position: {self.position})"


class Bill:
    def __init__(self, patient: Patient, amount: float) -> None:
        self.patient = patient
        self.amount = amount

    def __str__(self) -> str:
        return f"Bill(Patient: {self.patient.name}, Amount: {self.amount})"


class Appointment:
    def __init__(self, patient: Patient, doctor: Doctor, date: str, time: str) -> None:
        self.patient = patient
        self.doctor = doctor
        self.date = date
        self.time = time

    def __str__(self) -> str:
        return f"Appointment(Patient: {self.patient.name}, Doctor: {self.doctor.name}, Date: {self.date}, Time: {self.time})"


class Department:
    def __init__(self, name: str) -> None:
        self.name = name
        self.doctors: List[Doctor] = []

    def __str__(self) -> str:
        return f"Department(Name: {self.name}, Doctors: {[doctor.name for doctor in self.doctors]})"

    def add_doctor(self, doctor: Doctor) -> None:
        self.doctors.append(doctor)


class TreatmentPlan:
    def __init__(self, diagnosis: str, treatment_steps: List[str]) -> None:
        self.diagnosis = diagnosis
        self.treatment_steps = treatment_steps


if __name__ == "__main__":
    pass
