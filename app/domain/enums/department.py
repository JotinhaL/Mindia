from enum import Enum

class DepartmentEnum(str, Enum):
    ENGINEERING = "Engineering"
    IT = "IT"
    BUSINESS = "Business"
    MARKETING = "Marketing"
    HR = "HR"
    ACCOUNTING = "Accounting"
    SALES = "Sales"
    OTHER = "Other"