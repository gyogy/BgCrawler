import unittest
from project.db.controller import DBController
from project.db.setup import Queue


class TestDBController(unittest.TestCase):

    def setUp(self):
        q1 = Queue(url='first.marked.com', collected_at='06:33:02', marked=True)
        q2 = Queue(url='second.marked.bg', collected_at='07:45:16', marked=True)
        q3 = Queue(url='first.freeurl.bg', collected_at='08:24:25', marked=False)
        q4 = Queue(url='wrong.freeurl.bg', collected_at='08:35:36', marked=False)
        qs = [q1, q2, q3, q4]

        self.dbc = DBController()
        for q in qs:
            self.dbc.update_q(q)

    def test_get_first_unmarked_q(self):
        q = self.dbc.get_q()

        result = q.id
        expected = 3

        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
