import json
import xml.etree.ElementTree as ET
from typing import List, Union


class CustomError(Exception):
    """Исключение для обработки ошибок в клинике."""
    pass


class Person:
    def __init__(self, name: str, age: int) -> None:
        try:
            if not isinstance(name, str) or not name:
                raise ValueError("Имя должно быть непустой строкой.")
            if not isinstance(age, int) or age < 0:
                raise ValueError("Возраст должен быть неотрицательным целым числом.")
            self.name = name
            self.age = age
        except ValueError as ex:
            print(ex)


class Insurance:
    def __init__(self, provider: str, policy_number: str) -> None:
        try:
            if not isinstance(provider, str) or not provider:
                raise ValueError("Поставщик страховки должен быть непустой строкой.")
            if not isinstance(policy_number, str) or not policy_number:
                raise ValueError("Номер полиса должен быть непустой строкой.")
            self.provider = provider
            self.policy_number = policy_number
        except ValueError as ex:
            print(ex)

    def __str__(self) -> str:
        return f"Insurance(Provider: {self.provider}, Policy_number: {self.policy_number})"

    def to_dict(self) -> dict:
        return {
            'provider': self.provider,
            'policy_number': self.policy_number
        }


class MedicalRecord:
    def __init__(self, diagnosis: str, treatment: str) -> None:
        try:
            if not isinstance(diagnosis, str) or not diagnosis:
                raise ValueError("Диагноз должен быть непустой строкой.")
            if not isinstance(treatment, str) or not treatment:
                raise ValueError("Лечение должно быть непустой строкой.")
            self.diagnosis = diagnosis
            self.treatment = treatment
        except ValueError as ex:
            print(ex)

    def to_dict(self) -> dict:
        return {
            'diagnosis': self.diagnosis,
            'treatment': self.treatment
        }


class Prescription:
    def __init__(self, medication: str) -> None:
        try:
            if not isinstance(medication, str) or not medication:
                raise ValueError("Название лекарства должно быть непустой строкой.")
            self.medication = medication
        except ValueError as ex:
            print(ex)

    def to_dict(self) -> dict:
        return {
            'medication': self.medication
        }


class Patient(Person):
    def __init__(self, name: str, age: int, insurance: Insurance) -> None:
        try:
            super().__init__(name, age)
            if not isinstance(insurance, Insurance):
                raise ValueError("Страховка должна быть объектом класса Insurance.")
            self.insurance = insurance
            self.medical_records: List[MedicalRecord] = []
            self.prescriptions: List[Prescription] = []
            self.treatment_plans: List['TreatmentPlan'] = []
        except ValueError as ex:
            print(ex)

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

    def to_dict(self) -> dict:
        return {
            'name': self.name,
            'age': self.age,
            'insurance': self.insurance.to_dict(),
            'medical_records': [record.to_dict() for record in self.medical_records],
            'prescriptions': [prescription.to_dict() for prescription in self.prescriptions],
            'treatment_plans': [plan.to_dict() for plan in self.treatment_plans]
        }


class Doctor(Person):
    def __init__(self, name: str, age: int, specialty: str) -> None:
        super().__init__(name, age)
        self.specialty = specialty

    def __str__(self) -> str:
        return f"Doctor(Name: {self.name}, Age: {self.age}, Specialty: {self.specialty})"

    def to_dict(self) -> dict:
        return {
            'name': self.name,
            'age': self.age,
            'specialty': self.specialty
        }


class Staff(Person):
    def __init__(self, name: str, age: int, position: str) -> None:
        super().__init__(name, age)
        self.position = position

    def __str__(self) -> str:
        return f"Staff(Name: {self.name}, Age: {self.age}, Position: {self.position})"

    def to_dict(self) -> dict:
        return {
            'name': self.name,
            'age': self.age,
            'position': self.position
        }


class Bill:
    def __init__(self, patient: Patient, amount: float) -> None:
        self.patient = patient
        self.amount = amount

    def __str__(self) -> str:
        return f"Bill(Patient: {self.patient.name}, Amount: {self.amount})"

    def to_dict(self) -> dict:
        return {
            'patient': self.patient.name,
            'amount': self.amount
        }


class Appointment:
    def __init__(self, patient: Patient, doctor: Doctor, date: str, time: str) -> None:
        self.patient = patient
        self.doctor = doctor
        self.date = date
        self.time = time

    def __str__(self) -> str:
        return f"Appointment(Patient: {self.patient.name}, Doctor: {self.doctor.name}, Date: {self.date}, Time: {self.time})"

    def to_dict(self) -> dict:
        return {
            'patient': self.patient.name,
            'doctor': self.doctor.name,
            'date': self.date,
            'time': self.time
        }


class Department:
    def __init__(self, name: str) -> None:
        self.name = name
        self.doctors: List[Doctor] = []

    def __str__(self) -> str:
        return f"Department(Name: {self.name}, Doctors: {[doctor.name for doctor in self.doctors]})"

    def add_doctor(self, doctor: Doctor) -> None:
        self.doctors.append(doctor)

    def to_dict(self) -> dict:
        return {
            'name': self.name,
            'doctors': [doctor.to_dict() for doctor in self.doctors]
        }


class TreatmentPlan:
    def __init__(self, diagnosis: str, treatment_steps: List[str]) -> None:
        self.diagnosis = diagnosis
        self.treatment_steps = treatment_steps

    def to_dict(self) -> dict:
        return {
            'diagnosis': self.diagnosis,
            'treatment_steps': self.treatment_steps
        }


class Clinic:
    def __init__(self) -> None:
        self.patients: List[Patient] = []
        self.doctors: List[Doctor] = []
        self.staff: List[Staff] = []
        self.appointments: List[Appointment] = []
        self.departments: List[Department] = []
        self.bills: List[Bill] = []
        self.insurances: List[Insurance] = []

    def get_patients(self) -> List[dict]:
        return [patient.to_dict() for patient in self.patients]

    def get_doctors(self) -> List[dict]:
        return [doctor.to_dict() for doctor in self.doctors]

    def get_staffs(self) -> List[dict]:
        return [staff_member.to_dict() for staff_member in self.staff]

    def get_appointments(self) -> List[dict]:
        return [appointment.to_dict() for appointment in self.appointments]

    def get_departments(self) -> List[dict]:
        return [department.to_dict() for department in self.departments]

    def get_bills(self) -> List[dict]:
        return [bill.to_dict() for bill in self.bills]

    def get_insurances(self) -> List[dict]:
        return [insurance.to_dict() for insurance in self.insurances]

    def add_patient(self, patient: Patient) -> None:
        self.patients.append(patient)

    def get_patient(self, name: str) -> Patient:
        try:
            for patient in self.patients:
                if patient.name == name:
                    return patient
            raise CustomError("Ошибка: Пациент не найден.")
        except CustomError as ex:
            print(ex)

    def update_patient(self, name: str, updated_patient: Patient) -> None:
        try:
            for index, patient in enumerate(self.patients):
                if patient.name == name:
                    self.patients[index] = updated_patient
                    return
            raise CustomError("Ошибка: Пациент не найден.")
        except CustomError as ex:
            print(ex)

    def remove_patient(self, patient_name: str) -> None:
        self._remove_item(self.patients, patient_name)

    def add_insurance(self, insurance: Insurance) -> None:
        self.insurances.append(insurance)

    def get_insurance(self, policy_number: str) -> Insurance:
        try:
            for insurance in self.insurances:
                if insurance.policy_number == policy_number:
                    return insurance
            raise CustomError("Ошибка: Страховка не найдена.")
        except CustomError as ex:
            print(ex)

    def update_insurance(self, policy_number: str, updated_insurance: Insurance) -> None:
        try:
            for index, insurance in enumerate(self.insurances):
                if insurance.policy_number == policy_number:
                    self.insurances[index] = updated_insurance
                    return
            raise CustomError("Ошибка: Страховка не найдена.")
        except CustomError as ex:
            print(ex)

    def remove_insurance(self, policy_number: str) -> None:
        try:
            for index, insurance in enumerate(self.insurances):
                if insurance.policy_number == policy_number:
                    del self.insurances[index]
                    return
            raise CustomError("Ошибка: Страховка не найдена.")
        except CustomError as ex:
            print(ex)

    def add_doctor(self, doctor: Doctor) -> None:
        self.doctors.append(doctor)

    def get_doctor(self, name: str) -> Doctor:
        try:
            for doctor in self.doctors:
                if doctor.name == name:
                    return doctor
            raise CustomError("Ошибка: Врач не найден.")
        except CustomError as ex:
            print(ex)

    def update_doctor(self, name: str, updated_doctor: Doctor) -> None:
        try:
            for index, doctor in enumerate(self.doctors):
                if doctor.name == name:
                    self.doctors[index] = updated_doctor
                    return
            raise CustomError("Ошибка: Врач не найден.")
        except CustomError as ex:
            print(ex)

    def remove_doctor(self, doctor_name: str) -> None:
        self._remove_item(self.doctors, doctor_name)

    def add_staff(self, staff_member: Staff) -> None:
        self.staff.append(staff_member)

    def get_staff(self, name: str) -> Staff:
        try:
            for staff_member in self.staff:
                if staff_member.name == name:
                    return staff_member
            raise CustomError("Ошибка: Сотрудник не найден.")
        except CustomError as ex:
            print(ex)

    def update_staff(self, name: str, updated_staff: Staff) -> None:
        try:
            for index, staff_member in enumerate(self.staff):
                if staff_member.name == name:
                    self.staff[index] = updated_staff
                    return
            raise CustomError("Ошибка: Сотрудник не найден.")
        except CustomError as ex:
            print(ex)

    def remove_staff(self, staff_name: str) -> None:
        self._remove_item(self.staff, staff_name)

    def add_appointment(self, appointment: Appointment) -> None:
        self.appointments.append(appointment)

    def get_appointment(self, patient_name: str, doctor_name: str) -> Appointment:
        try:
            for appointment in self.appointments:
                if appointment.patient.name == patient_name and appointment.doctor.name == doctor_name:
                    return appointment
            raise CustomError("Ошибка: Назначение не найдено.")
        except CustomError as ex:
            print(ex)

    def update_appointment(self, patient_name: str, doctor_name: str, updated_appointment: Appointment) -> None:
        try:
            for index, appointment in enumerate(self.appointments):
                if appointment.patient.name == patient_name and appointment.doctor.name == doctor_name:
                    self.appointments[index] = updated_appointment
                    return
            raise CustomError("Ошибка: Назначение не найдено.")
        except CustomError as ex:
            print(ex)

    def remove_appointment(self, patient_name: str, doctor_name: str) -> None:
        try:
            for index, appointment in enumerate(self.appointments):
                if appointment.patient.name == patient_name and appointment.doctor.name == doctor_name:
                    del self.appointments[index]
                    return
            raise CustomError("Ошибка: Назначение не найдено.")
        except CustomError as ex:
            print(ex)

    def add_department(self, department: Department) -> None:
        self.departments.append(department)

    def get_department(self, name: str) -> Department:
        try:
            for department in self.departments:
                if department.name == name:
                    return department
            raise CustomError("Ошибка: Отдел не найден.")
        except CustomError as ex:
            print(ex)

    def update_department(self, name: str, updated_department: Department) -> None:
        try:
            for index, department in enumerate(self.departments):
                if department.name == name:
                    self.departments[index] = updated_department
                    return
            raise CustomError("Ошибка: Отдел не найден.")
        except CustomError as ex:
            print(ex)

    def remove_department(self, department_name: str) -> None:
        try:
            for index, department in enumerate(self.departments):
                if department.name == department_name:
                    del self.departments[index]
                    return
            raise CustomError("Ошибка: Отдел не найден.")
        except CustomError as ex:
            print(ex)

    def create_bill(self, patient_name: str, amount: float) -> None:
        patient = self.get_patient(patient_name)
        if patient:
            bill = Bill(patient, amount)
            self.bills.append(bill)

    def get_bill(self, patient_name: str) -> Bill:
        try:
            for bill in self.bills:
                if bill.patient.name == patient_name:
                    return bill
            raise CustomError("Ошибка: Счет не найден.")
        except CustomError as ex:
            print(ex)

    def update_bill(self, patient_name: str, new_amount: float) -> None:
        try:
            for bill in self.bills:
                if bill.patient.name == patient_name:
                    bill.amount = new_amount
                    return
            raise CustomError("Ошибка: Счет не найден.")
        except CustomError as ex:
            print(ex)

    def remove_bill(self, patient_name: str) -> None:
        self._remove_item(self.bills, patient_name, is_bill=True)

    def _remove_item(self, item_list: List[Union[Patient, Doctor, Staff, Bill]], name: str,
                     is_bill: bool = False) -> bool:
        for item in item_list:
            if (is_bill and item.patient.name == name) or (not is_bill and item.name == name):
                item_list.remove(item)
                return True
        print("Ошибка: Не найдено.")
        return False

    def to_dict(self) -> dict:
        return {
            'patients': [patient.to_dict() for patient in self.patients],
            'doctors': [doctor.to_dict() for doctor in self.doctors],
            'staff': [staff_member.to_dict() for staff_member in self.staff],
            'bills': [bill.to_dict() for bill in self.bills],
            'appointments': [appointment.to_dict() for appointment in self.appointments],
            'departments': [department.to_dict() for department in self.departments],
            'insurances': [insurance.to_dict() for insurance in self.insurances]
        }


class DataStorage:
    def save(self, clinic: Clinic, filename: str) -> None:
        raise NotImplementedError

    def load(self, filename: str) -> Clinic:
        raise NotImplementedError


class JsonDataStorage(DataStorage):
    def save(self, clinic: Clinic, filename: str) -> None:
        try:
            with open(filename, 'w') as file:
                json.dump(clinic.to_dict(), file, indent=4)
        except Exception as ex:
            print(f"Ошибка при сохранении данных в JSON: {ex}")

    def load(self, filename: str) -> Clinic:
        clinic = Clinic()
        try:
            with open(filename, 'r') as file:
                data = json.load(file)

            for patient_data in data['patients']:
                insurance = Insurance(**patient_data['insurance'])
                new_patient = Patient(patient_data['name'], patient_data['age'], insurance)
                new_patient.medical_records = [MedicalRecord(**record) for record in patient_data['medical_records']]
                new_patient.prescriptions = [Prescription(p['medication']) for p in patient_data['prescriptions']]
                new_patient.treatment_plans = [TreatmentPlan(**t) for t in patient_data['treatment_plans']]
                clinic.add_patient(new_patient)

            clinic.doctors = [Doctor(**doctor) for doctor in data['doctors']]
            clinic.staff = [Staff(**staff) for staff in data['staff']]
            clinic.bills = [clinic.create_bill(b['patient'], b['amount']) for b in data['bills']]
            clinic.appointments = [
                Appointment(
                    next((p for p in clinic.patients if p.name == a['patient']), None),
                    next((d for d in clinic.doctors if d.name == a['doctor']), None),
                    a['date'], a['time']
                ) for a in data['appointments']
            ]
            for department_data in data['departments']:
                dept = Department(department_data['name'])
                dept.doctors = [Doctor(**doc) for doc in department_data['doctors']]
                clinic.add_department(dept)
            clinic.insurances = [Insurance(**insurance) for insurance in data.get('insurances', [])]

        except (FileNotFoundError, json.JSONDecodeError) as ex:
            print(f"Ошибка при загрузке данных из JSON: {ex}")
        return clinic


if __name__ == "__main__":
    pass
