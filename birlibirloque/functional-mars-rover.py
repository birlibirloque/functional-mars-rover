import unittest

def createAMarsRoverAt (point):
	return ({'x':point['x'], 'y':point['y'], 'f':point['f']})

class TestMarsRover (unittest.TestCase):

	def test_CreateAMarsRoverAtOriginPointAndFacingToNorth(self):
		#Given a Origin Point And Facing to North
		originPointAndFacingToNorth = {'x':0, 'y':0, 'f':'N'}
		#When We Create A Mars Rover
		marsrover = createAMarsRoverAt (originPointAndFacingToNorth)
		#Then He Is At the Origin Point And Facing to North
		self.assertEqual(marsrover['x'],0)
		self.assertEqual(marsrover['y'],0)
		self.assertEqual(marsrover['f'],'N')		

if __name__ == '__main__':
	unittest.main()
