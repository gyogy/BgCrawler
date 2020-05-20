import unittest
from project.db.controller import DBController


class TestDBController(unittest.TestCase):

    def setUp(self):
        self.dbc = DBController()

    def test_update_q_method(self):
        before = self.dbc.q_count()

        self.dbc.update_q('marked.url', '18:32:07', True)
        self.dbc.update_q('www.example.com', '18:32:07')

        after = self.dbc.q_count()

        self.assertGreater(after, before)

    # def test_get_first_unmarked_q(self):
    #     q = self.dbc.get_q()
    #     # print(q)
    #     print(q.queue_id)

    def test_delete_q_method(self):
        self.dbc.delete_q('www.example.com')
        count_after_delete = self.dbc.q_count()
        expected = 1

        self.assertEqual(count_after_delete, expected)


if __name__ == '__main__':
    unittest.main()
