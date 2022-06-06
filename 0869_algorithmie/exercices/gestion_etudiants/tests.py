import unittest
import gestion_etudiants as ge



class StudentTests(unittest.TestCase):
    students = [
        {
            "id": 998,
            "firstname": "Maximilien",
            "lastname": "Denis",
            "age": 23
        },
        {
            "id": 999,
            "firstname": "Jeanne",
            "lastname": "Petit",
            "age": 20
        }
    ]

    student = {
        'id': 23,
        'firstname': 'max',
        'lastname': 'denis',
        'age': 13
    }

    def test_add_student(self):
        self.assertEqual(ge.add_student(23, ['max', 'denis', 13]), self.student)
        self.assertFalse(ge.add_student(-1, ['max', 'denis', 13]))
        self.assertFalse(ge.add_student(1, [23, 'denis', 13]))
        self.assertFalse(ge.add_student(1, ['max', '', 13]))
        self.assertFalse(ge.add_student(1, ['max', 'denis', -1]))
        self.assertFalse(ge.add_student(1, ['max', 'denis', 0]))
        self.assertFalse(ge.add_student(1, ['max', 'denis', 5345]))
        self.assertFalse(ge.add_student(1, ['', 'denis', 10]))
        self.assertFalse(ge.add_student(1, ['lax', '', 10]))

    def test_remove_student(self):
        self.assertEqual(ge.remove_student(998, self.students), [
            {
                "id": 999,
                "firstname": "Jeanne",
                "lastname": "Petit",
                "age": 20
            }
        ])
        self.assertFalse()


if __name__ == '__main__':
    unittest.main()