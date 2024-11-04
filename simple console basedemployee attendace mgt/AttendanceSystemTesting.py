from employe_atendance import Employee, AttendanceSystem
import unittest
class attendanc_sys_testing(unittest.TestCase):
  def setUp(self):
    self.employee1 = Employee("abel","nsr/020/14")
    self.attendance = AttendanceSystem()
    self.attendance.add_employee(self.employee1)

  def test_check_in(self):
    self.employee1.check_in()
    self.assertTrue(self.employee1.is_present)
    self.assertIsNotNone(self.employee1.get_check_in_time())
    self.assertTrue(self.employee1.is_late())
  def test_check_out(self):
    self.employee1.check_out()
    self.assertFalse(self.employee1.is_present)
    self.assertIsNotNone(self.employee1.get_check_out_time())
  def test_obj_repr(self):
    self.assertEqual(str(self.employee1), "Employe Name: abel Employe_id: nsr/020/14 Present: False")

if __name__ == "__main__":
  unittest.main()