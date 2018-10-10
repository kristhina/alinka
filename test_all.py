from tkinter import Tk
import unittest

from frontend.frames.actualdata import StudentData
from frontend.mainwindow import MainWindow


class testTest(unittest.TestCase):
    def setUp(self):
        self.instance = MainWindow(Tk())

    def test_mainwindow_and_frames_contains_a_name(self):
        self.assertEqual(self.instance.notebook['text'], "Baza danych")
        self.assertEqual(self.instance.actual_student['text'], "Dane dziecka")
        self.assertEqual(
            self.instance.applicationframe['text'],
            "Wnioskodawcy"
        )
        self.assertEqual(
            self.instance.staff_meeting_frame['text'],
            "Zespół orzekający"
        )

    def test_pesel_validation(self):
        student1 = StudentData()
        student1.pesel_string = "10211529111"

