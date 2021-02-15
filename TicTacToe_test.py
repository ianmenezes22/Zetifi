from TicTacToe import TicTacToe
import unittest
class TicTacToe_test(unittest.TestCase):
  def setUp(self):
    self.t=TicTacToe()

  def test_initialization(self):
    self.assertEqual(self.t.n, 3)
    self.assertNotEqual(self.t.board, None)
    self.assertEqual(self.t.xo, True)

  def test_param1(self):
    self.assertRaises(TypeError, self.t.place_marker, 0, 1, 2)

  def test_param2(self):
    self.assertRaises(TypeError, self.t.place_marker, 'x', 1.5, 2)

  def test_param3(self):
    self.assertRaises(TypeError, self.t.place_marker, 'o', 1, 2.5)

  def test_incorrectSymbol(self):
    self.assertRaises(Exception, self.t.place_marker, 'X', 1, 2)

  def test_rowIndex(self):
    self.assertRaises(Exception, self.t.place_marker, 'x', 3, 2)

  def test_columnIndex(self):
    self.assertRaises(Exception, self.t.place_marker, 'x', 1, -5)

  def test_overwrite(self):
    self.t.place_marker('x', 1, 2)
    self.assertRaises(Exception, self.t.place_marker, 'x', 1, 2)

  def test_consequentX(self):
    self.t.place_marker('x', 1, 2)
    self.assertRaises(Exception, self.t.place_marker, 'x', 1, 1)

  def test_consequentO(self):
    self.t.place_marker('x', 1, 2)
    self.t.place_marker('o', 1, 1)
    self.assertRaises(Exception, self.t.place_marker, 'o', 1, 0)

  def test_OsTurn(self):
    self.assertEqual(self.t.place_marker('x', 1, 2), TicTacToe.STATES.NAUGHT_TURN.value)

  def test_XsTurn(self):
    self.t.place_marker('x', 1, 1)
    self.assertEqual(self.t.place_marker('o', 1, 2), TicTacToe.STATES.CROSS_TURN.value)

  def test_OWins(self):
    self.t.place_marker('x', 2,2)
    self.t.place_marker('o', 1,1)
    self.t.place_marker('x', 0,2)
    self.t.place_marker('o', 1,2)
    self.t.place_marker('x', 2,1)
    self.assertEqual(self.t.place_marker('o', 1, 0), TicTacToe.STATES.NAUGHT_WON.value)

  def test_XWins(self):
    self.t.place_marker('x', 1,1)
    self.t.place_marker('o', 1,2)
    self.t.place_marker('x', 0,2)
    self.t.place_marker('o', 0,1)
    self.assertEqual(self.t.place_marker('x', 2,0), TicTacToe.STATES.CROSS_WON.value)

  def test_Draw(self):
    self.t.place_marker('x', 1,1)
    self.t.place_marker('o', 1,2)
    self.t.place_marker('x', 0,2)
    self.t.place_marker('o', 2,0)
    self.t.place_marker('x', 2,1)
    self.t.place_marker('o', 0,1)
    self.t.place_marker('x', 2,2)
    self.t.place_marker('o', 0,0)
    self.assertEqual(self.t.place_marker('x', 1,0), TicTacToe.STATES.DRAW.value)

  def tearDown(self):
    print("Result:", end=" ")