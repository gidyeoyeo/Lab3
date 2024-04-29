import Lab2.bmi as bmi

def test_bmi_normal_weight():
    assert(bmi.calculate_bmi(weight =57,height=1.73)==0)
def test_bmi_over_weight():
    assert(bmi.calculate_bmi(weight=102,height=1.60)==1)
def test_bmi_under_weight():
    assert(bmi.calculate_bmi(weight=52,height=1.84)==-1)