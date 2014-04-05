import unittest

def createAMarsRoverAt (point):
	return ({'x':point['x'], 'y':point['y'], 'f':point['f']})

def fordward(mr):
	return (createAMarsRoverAt({'x':mr['x'],'y':mr['y']+1,'f':mr['f']}))

def backward(mr):
	return (createAMarsRoverAt({'x':mr['x'],'y':mr['y']-1,'f':mr['f']}))

def move (marsrover,commads):
	if len(commads) > 1:
		newmarsrover = createAMarsRoverAt(move(marsrover,commads[:-1]))
	else:
		newmarsrover = createAMarsRoverAt(marsrover)

	if (commads[-1] == 'f'):
		return(fordward(newmarsrover))
	else:
		return(backward(newmarsrover))

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

	def test_MoveMarsRoverOneStepFordward(self):
		#Given a mars rover at origin point and facing to north
		originPointAndFacingToNorth = {'x':0, 'y':0, 'f':'N'}
		marsrover = createAMarsRoverAt (originPointAndFacingToNorth)
		#When we move mars rover one step fordward
		newmarsrover = createAMarsRoverAt(move(marsrover,'f'))
		#Then new mars rover is at one setp fordward to north
		self.assertEqual(newmarsrover['x'],0)
		self.assertEqual(newmarsrover['y'],1)
		self.assertEqual(newmarsrover['f'],'N')

	def test_MoveMarsRoverOneStepBackward(self):
		#Given a mars rover at origin point and facing to north
		originPointAndFacingToNorth = {'x':0, 'y':0, 'f':'N'}
		marsrover = createAMarsRoverAt (originPointAndFacingToNorth)
		#When we move mars rover one step backward
		newmarsrover = createAMarsRoverAt(move(marsrover,'b'))
		#Then new mars rover is at one setp backward to north
		self.assertEqual(newmarsrover['x'],0)
		self.assertEqual(newmarsrover['y'],-1)
		self.assertEqual(newmarsrover['f'],'N')

	def test_MoveMarsRoverThreeStepsFordwardAndOneBackward(self):
		#Given a mars rover at origin point and facing to north
		originPointAndFacingToNorth = {'x':0, 'y':0, 'f':'N'}
		marsrover = createAMarsRoverAt (originPointAndFacingToNorth)
		#When we move mars rover three steps fordward and one backward
		newmarsrover = createAMarsRoverAt(move(marsrover,'fffb'))
		#Then new mars rover is at two setps fordward to north
		self.assertEqual(newmarsrover['x'],0)
		self.assertEqual(newmarsrover['y'],2)
		self.assertEqual(newmarsrover['f'],'N')

if __name__ == '__main__':
	unittest.main()
