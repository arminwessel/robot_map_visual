import numpy as np

class Turtle:
    explorer_map=0
    anchor_position=0
    #codes={0:unexplored,1:free,2:obstacle}
    def __init__(self):
        self.explorer_map=np.zeros((5,5))
        self.anchor_position=(2,2) #center
        self.explorer_map[self.anchor_position]=1
        print('Turte initialized')
        
    def add_info_to_map(self,info):
        x=info['x']
        y=info['y']
        state=info['state']

        h,w = np.shape(self.explorer_map)

        # maximal darstellbare Koordinaten
        xmin=-self.anchor_position[1]
        xmax=w-self.anchor_position[1]-1
        ymin=-self.anchor_position[0]
        ymax=h-self.anchor_position[0]-1

        # expand the array
        if int(x)<xmin:
            self.explorer_map = np.pad(self.explorer_map,((0,0),(abs(int(x)-xmin),0)))
            self.anchor_position = (self.anchor_position[0],self.anchor_position[1] + abs(int(x)-xmin))
            print('anchor position: {}'.format(self.anchor_position))
        if int(x)>xmax:
            self.explorer_map = np.pad(self.explorer_map,((0,0),(0,abs(int(x)-xmax))))
            print('anchor position: {}'.format(self.anchor_position))
        if int(y)<ymin:
            self.explorer_map = np.pad(self.explorer_map,((abs(int(y)-ymin),0),(0,0)))
            self.anchor_position = (self.anchor_position[0] + abs(int(y)-ymin),self.anchor_position[1])
            print('anchor position: {}'.format(self.anchor_position))
        if int(y)>ymax:
            self.explorer_map = np.pad(self.explorer_map,((0,abs(int(y)-ymax)),(0,0)))
            print('anchor position: {}'.format(self.anchor_position))

        self.explorer_map[self.anchor_position[0]+y,self.anchor_position[1]+x]=state
