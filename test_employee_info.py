import pytest
import employee_info


# Test employees within age range
def test_get_employees_by_age_range():
    result = employee_info.get_employees_by_age_range(24, 36)

    names = [employee["name"] for employee in result]

    assert names == ["John", "Jane", "Chloe", "Mike"]


# Test average salary
def test_calculate_average_salary():
    result = employee_info.calculate_average_salary()

    assert result == pytest.approx(60166.67, abs=0.01)


# Test employees in Sales department
def test_get_employees_by_dept_sales():
    result = employee_info.get_employees_by_dept("Sales")

    names = [employee["name"] for employee in result]

    assert names == ["John", "Peter"]


# Test employees in Marketing department
def test_get_employees_by_dept_marketing():
    result = employee_info.get_employees_by_dept("Marketing")

    names = [employee["name"] for employee in result]

    assert names == ["Jane", "Mary"]


# Test employees in Engineering department
def test_get_employees_by_dept_engineering():
    result = employee_info.get_employees_by_dept("Engineering")

    names = [employee["name"] for employee in result]

    assert names == ["Chloe", "Mike"]
