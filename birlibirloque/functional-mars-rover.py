import unittest

def createAMarsRoverAt (point):
	return ({'x':point['x'], 'y':point['y'], 'f':point['f']})

def fordward(mr):
    return {
        'N': createAMarsRoverAt({'x':mr['x'],'y':mr['y']+1,'f':mr['f']}),
        'S': createAMarsRoverAt({'x':mr['x'],'y':mr['y']-1,'f':mr['f']}),
        'E': createAMarsRoverAt({'x':mr['x']+1,'y':mr['y'],'f':mr['f']}),
        'W': createAMarsRoverAt({'x':mr['x']-1,'y':mr['y'],'f':mr['f']}),
        }[mr['f']]

def backward(mr):
    return {
        'N': createAMarsRoverAt({'x':mr['x'],'y':mr['y']-1,'f':mr['f']}),
        'S': createAMarsRoverAt({'x':mr['x'],'y':mr['y']+1,'f':mr['f']}),
        'E': createAMarsRoverAt({'x':mr['x']-1,'y':mr['y'],'f':mr['f']}),
        'W': createAMarsRoverAt({'x':mr['x']+1,'y':mr['y'],'f':mr['f']}),
        }[mr['f']]

def right(mr):
    return {
        'N': createAMarsRoverAt({'x':mr['x'],'y':mr['y'],'f':'E'}),
        'E': createAMarsRoverAt({'x':mr['x'],'y':mr['y'],'f':'S'}),
        'S': createAMarsRoverAt({'x':mr['x'],'y':mr['y'],'f':'W'}),
        'W': createAMarsRoverAt({'x':mr['x'],'y':mr['y'],'f':'N'}),
        }[mr['f']]

def left(mr):
    return {
        'N': createAMarsRoverAt({'x':mr['x'],'y':mr['y'],'f':'W'}),
        'E': createAMarsRoverAt({'x':mr['x'],'y':mr['y'],'f':'N'}),
        'S': createAMarsRoverAt({'x':mr['x'],'y':mr['y'],'f':'E'}),
        'W': createAMarsRoverAt({'x':mr['x'],'y':mr['y'],'f':'S'}),
        }[mr['f']]

def move (marsrover,commads):
	if len(commads) > 1:
		newmarsrover = createAMarsRoverAt(move(marsrover,commads[:-1]))
	else:
		newmarsrover = createAMarsRoverAt(marsrover)

	return {
		'f': fordward(newmarsrover),
		'b': backward(newmarsrover),
		'r': right(newmarsrover),
		'l': left(newmarsrover),
	}[commads[-1]]

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

	def test_MoveMarsRoverThreeStepsFordwardAndOneBackwardFacingEast(self):
		#Given a mars rover at origin point and facing to north
		originPointAndFacingToNorth = {'x':0, 'y':0, 'f':'E'}
		marsrover = createAMarsRoverAt (originPointAndFacingToNorth)
		#When we move mars rover three steps fordward and one backward
		newmarsrover = createAMarsRoverAt(move(marsrover,'fffb'))
		#Then new mars rover is at two setps fordward to north
		self.assertEqual(newmarsrover['x'],2)
		self.assertEqual(newmarsrover['y'],0)
		self.assertEqual(newmarsrover['f'],'E')

	def test_MoveMarsRoverTurnRightThreeStepsAndOneLeftFacingEast(self):
		#Given a mars rover at origin point and facing to north
		originPointAndFacingToNorth = {'x':0, 'y':0, 'f':'E'}
		marsrover = createAMarsRoverAt (originPointAndFacingToNorth)
		#When we move mars rover three steps fordward and one backward
		newmarsrover = createAMarsRoverAt(move(marsrover,'rrrl'))
		#Then new mars rover is at two setps fordward to north
		self.assertEqual(newmarsrover['x'],0)
		self.assertEqual(newmarsrover['y'],0)
		self.assertEqual(newmarsrover['f'],'W')

	def test_MoveMarsRoverTwoStepFordwardTurnRightAndTwoStepsFordwardFacingNorth(self):
		#Given a mars rover at origin point and facing to north
		originPointAndFacingToNorth = {'x':0, 'y':0, 'f':'N'}
		marsrover = createAMarsRoverAt (originPointAndFacingToNorth)
		#When we move mars rover three steps fordward and one backward
		newmarsrover = createAMarsRoverAt(move(marsrover,'ffrff'))
		#Then new mars rover is at two setps fordward to north
		self.assertEqual(newmarsrover['x'],2)
		self.assertEqual(newmarsrover['y'],2)
		self.assertEqual(newmarsrover['f'],'E')

if __name__ == '__main__':
	unittest.main()
