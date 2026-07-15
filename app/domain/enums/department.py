from enum import Enum

class Department(str, Enum):
    ENGINEERING = "Engineering"
    IT = "IT"
    BUSINESS = "Business"
    MARKETING = "Marketing"
    HR = "HR"
    ACCOUNTING = "Accounting"
    SALES = "Sales"
    OTHER = "Other"