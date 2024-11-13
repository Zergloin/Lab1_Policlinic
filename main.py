from typing import List, Union


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


if __name__ == "__main__":
    pass
