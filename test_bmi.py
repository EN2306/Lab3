import ET0735_Lab2.bmi as bmi

def test_bmi_normal_weight():
    assert bmi.calculate_bmi(1.7, 60) == 0

def test_bmi_over_weight():
    assert bmi.calculate_bmi(1.7, 90) == 1

def test_bmi_under_weight():
    assert bmi.calculate_bmi(1.7, 45) == -1