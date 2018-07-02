import datetime as dt
import random as r
import copy

# GLOBOVARS
bid = 0
#movequeue = queue()

# size is [x,y]
# heights are in integer metres
class hmap:
    def __init__(self,size=[100,100],maxstep=1,algo="tl",file=""):
        self.vals = []
        self.size = size
        if algo == "tl":
            for x in range(0,size[0]):
                #print("x is " + str(x))
                for y in range(0,size[1]):
                    #print("y is " + str(y))
                    if x > 0 and y > 0 and y < size[1]- 1:
                        surrond = [self.vals[x-1][y-1],self.vals[x-1][y],self.vals[x][y-1],self.vals[x-1][y+1]]
                        maxi = max(surrond) + maxstep
                        mini = min(surrond) - maxstep
                        self.vals[x].append(r.randint(mini,maxi))
                    elif x > 0 and y > 0:
                        surrond = [self.vals[x-1][y-1],self.vals[x-1][y],self.vals[x][y-1]]
                        maxi = max(surrond) + maxstep
                        mini = min(surrond) - maxstep
                        self.vals[x].append(r.randint(mini,maxi))
                    elif x > 0:
                        surrond = [self.vals[x-1][y]]
                        maxi = max(surrond) + maxstep
                        mini = min(surrond) - maxstep
                        self.vals.append([r.randint(mini,maxi)])
                    elif y > 0:
                        surrond = [self.vals[x][y-1]]
                        maxi = max(surrond) + maxstep
                        mini = min(surrond) - maxstep
                        self.vals[x].append(r.randint(mini,maxi))
                    else:
                        self.vals.append([r.randint(-5,100)])
        elif algo == "load":
            with open(file,"r") as f:
                f.readline()
                f.readline()
                f.readline()
                f.readline()
                f.readline()
                s = f.readline().split(" ")
                while s != ['']:
                    print(s)
                    t = []
                    for z in s[:len(s)-1]:
                        t.append(int(z))
                    self.vals.append(t)
                    s=f.readline().split(" ")
        elif algo == "rev":
            tf = []
            tr = []
            for x in range(0,size[0]):
                #print("x is " + str(x))
                for y in range(0,size[1]):
                    #print("y is " + str(y))
                    if x > 0 and y > 0 and y < size[1]- 1:
                        surrond = [tf[x-1][y-1],tf[x-1][y],tf[x][y-1],tf[x-1][y+1]]
                        maxi = max(surrond) + maxstep
                        mini = min(surrond) - maxstep
                        tf[x].append(r.randint(mini,maxi))
                    elif x > 0 and y > 0:
                        surrond = [tf[x-1][y-1],tf[x-1][y],tf[x][y-1]]
                        maxi = max(surrond) + maxstep
                        mini = min(surrond) - maxstep
                        tf[x].append(r.randint(mini,maxi))
                    elif x > 0:
                        surrond = [tf[x-1][y]]
                        maxi = max(surrond) + maxstep
                        mini = min(surrond) - maxstep
                        tf.append([r.randint(mini,maxi)])
                    elif y > 0:
                        surrond = [tf[x][y-1]]
                        maxi = max(surrond) + maxstep
                        mini = min(surrond) - maxstep
                        tf[x].append(r.randint(mini,maxi))
                    else:
                        tf.append([r.randint(-5,100)])
            for x in range(0,size[0]):
                #print("x is " + str(x))
                for y in range(0,size[1]):
                    #print("y is " + str(y))
                    if x > 0 and y > 0 and y < size[1]- 1:
                        surrond = [tr[x-1][y-1],tr[x-1][y],tr[x][y-1],tr[x-1][y+1]]
                        maxi = max(surrond) + maxstep
                        mini = min(surrond) - maxstep
                        tr[x].append(r.randint(mini,maxi))
                    elif x > 0 and y > 0:
                        surrond = [tr[x-1][y-1],tr[x-1][y],tr[x][y-1]]
                        maxi = max(surrond) + maxstep
                        mini = min(surrond) - maxstep
                        tr[x].append(r.randint(mini,maxi))
                    elif x > 0:
                        surrond = [tr[x-1][y]]
                        maxi = max(surrond) + maxstep
                        mini = min(surrond) - maxstep
                        tr.append([r.randint(mini,maxi)])
                    elif y > 0:
                        surrond = [tr[x][y-1]]
                        maxi = max(surrond) + maxstep
                        mini = min(surrond) - maxstep
                        tr[x].append(r.randint(mini,maxi))
                    else:
                        tr.append([r.randint(-5,100)])
            temp = []
            ylen = len(tr[0])
            for x in range(0,len(tr)):
                tempy = []
                tempr = tr.pop()
                for y in range(0,ylen):
                    tempy.append(tempr.pop())
                temp.append(tempy)
            tr = temp
            for x in range(0,size[0]):
                for y in range(0,size[1]):
                    if x > 0 and y > 0 and y < size[1]- 1:
                        surrond = [tr[x][y],tf[x][y]]
                        maxi = max(surrond) + maxstep
                        mini = min(surrond) - maxstep
                        self.vals[x].append(r.randint(mini,maxi))
                    elif x > 0 and y > 0:
                        surrond = [tr[x][y],tf[x][y]]
                        maxi = max(surrond) + maxstep
                        mini = min(surrond) - maxstep
                        self.vals[x].append(r.randint(mini,maxi))
                    elif x > 0:
                        surrond = [tr[x][y],tf[x][y]]
                        maxi = max(surrond) + maxstep
                        mini = min(surrond) - maxstep
                        self.vals.append([r.randint(mini,maxi)])
                    elif y > 0:
                        surrond = [tr[x][y],tf[x][y]]
                        maxi = max(surrond) + maxstep
                        mini = min(surrond) - maxstep
                        self.vals[x].append(r.randint(mini,maxi))
                    else:
                        surrond = [tr[x][y],tf[x][y]]
                        maxi = max(surrond) + maxstep
                        mini = min(surrond) - maxstep
                        self.vals.append([r.randint(mini,maxi)])
    def __outimg__(self,format="asc",file="output.asc"):
        with open(file,"w") as f:
            f.write("NCOLS " + str(self.size[0]) + "\nNROWS " + str(self.size[1]) + "\nXLLCORNER 0\nYLLCORNER 0\nCELLSIZE 1000\n")    
        with open(file,"a") as f:
            for x in self.vals:
                outstr = ""
                for y in x:
                    outstr += str(y) + " " 
                f.write(outstr + "\n")

# placestructs places a number of structs in a location on a sizedmap according to the given algorithm
def placestructs(numstructs,sizemap,algo="random"):
    outlocs = []
    if algo == "random":
        for x in range(0,numstructs):
            outlocs.append([r.randint(0,sizemap[0]),r.randint(0,sizemap[1])])
    return outlocs

class structure:
    def __init__(self,location,typ,name="Building",prates={'house':{'passengers':0.05}}):
        self.loc = location
        self.typ = typ
        #self.id = bid
        #bid += 1
        self.production = prates[self.typ]
        self.stock = copy.deepcopy(self.production)
        for x in self.stock.keys():
            self.stock[x] = self.stock[x] * r.randint(0,10)
    def __upd__(self,ratemods=[]):
        if len(ratemods) == 0:
            for x in self.stock.keys():
                #print(self.stock[x])
                self.stock[x] += self.production[x]
        else:
            for x in ratemods:
                self.production[x[0]] = x[1]

class locale:
    def __init__(self,hmap,size=[100,100],structuresloc="random",structuresdist="random",structpresent=["house"],numstructs=100):
        self.dimensions = size
        self.structures = []
        if structuresloc == "random" and structuresdist == "random":
            structloc = placestructs(numstructs,self.dimensions,structuresloc)
            for x in structloc:
                self.structures.append(structure(x,'house'))
    def __upd__(self):
        for x in self.structures:
            x.__upd__()
        

# loads a map into memory, returning a map object
def memorize(file):
    outhmap = []
    outstruct = 2

def process(action,game):
    print(action.type + " " + action.player)

defaultsets = {'mapsize':[100,100],'halgo':'tl'}

def sett(file='default'):
    if file == 'default':
        return defaultsets

class game:
    # locale is the map
    def __init__(self,name,localefile='default',year=1914,settingsfile='default',new=True):
        if new:
            self.name = name
            self.tick = 0
            self.date = dt.date(year,1,1)
            self.setting = sett(file=settingsfile)
            self.locale = locale(hmap(size=self.setting['mapsize'],algo=self.setting['halgo']))#paramshere
            self.simu = True
    def __mainl__(self):
        while self.simu:
            #do stuff
            self.tick += 1
            # this is where the multithreading could start
            #if len(movequeue) > 0:
            #    action = movequeue.dequeue()
            #    process(action,self)
            self.locale.__upd__()
            if self.tick > 1800:
                self.simu = False

