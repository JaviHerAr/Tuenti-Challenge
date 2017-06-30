# Description: Tuenti Challenge 5 - Problem 5 - The One Treasure.
# Author: Javier Herrero Arnanz.
# Date: 03/04/2015.

import copy

class Island(object):
    """
    This class represents an island.
    """
    
    def __init__(self,name,islandCost):
        """
        Class constructor.
        """
        self.name = name
        self.islandCost = islandCost
        self.paths = []
        self.enemies = {}
        
    def getName(self):
        """
        Return the name of the island.
        """
        return self.name
    
    def getCost(self):
        """
        Return the cost of the island.
        """
        return self.islandCost
        
    def addPath(self,path):
        """
        Add a path to the island. The island is the origin of the path.
        """
        self.paths.append(path)
        
    def getPaths(self):
        """
        Returns all the paths from this island.
        """
        return self.paths
        
    def addEnemy(self,enemy):
        """
        Add an enemy to the island.
        """
        self.enemies[enemy.getName()] = enemy
        
    def removeEnemy(self,enemy):
        """
        Remove an enemy from the island.
        """
        del self.enemies[enemy.getName()]
        
    def getEnemies(self):
        """
        Returns all the enemies in this island.
        """
        return self.enemies
     
        
              
class Path(object):
    """
    This class represents a path.
    """
    
    def __init__(self,destiny,cost):
        """
        Class constructor.
        """
        self.destiny = destiny
        self.cost = cost
        
    def getDestiny(self):
        """
        Returns the destiny island.
        """
        return self.destiny
        
    def getCost(self):
        """
        Returns the cost of the path.
        """
        return self.cost
     
                               
        
class Boat(object):
    """
    This class represents a boat.
    """
    
    def __init__(self,number,name,gold,position):
        """
        Class constructor.
        """
        self.number = number
        self.name = name
        self.gold = gold
        self.position = position
        
    def getNumber(self):
        """
        Returns the number of the boat.
        """
        return self.number
    
    def getName(self):
        """
        Returns the name of the boat.
        """
        return self.name
        
    def getGold(self):
        """
        Returns the total amount of gold of the boat.
        """
        return self.gold
        
    def setGold(self,gold):
        """
        Set the total amount of gold of the boat.
        """
        self.gold = gold
        
    def getPosition(self):
        """
        Returns the current position (island name) of the boat.
        """
        return self.position
        
    def setPosition(self,position):
        """
        Set the current position (island name) of the boat.
        """
        self.position = position
    
    
        
def doBoatMove(boat,graph,enemies):
    """
    This method moves myBoat one position taking in advice the enemies' position.
    """
    
    def bellmanFord(graph,source):
        """
        This method implements Bellman-Ford algorithm.
        """
        # Initialization.
        d = {}
        prev = {}
        in_queue = {}
        for i in graph:
            d[i]=-1
            prev[i]=-1
            in_queue[i] = False
        d[source] = 0
        queue = [source]
        in_queue[source] = True
        
        # Main loop.
        while (len(queue) != 0):
            i = queue.pop(0)
            in_queue[i] = False
            for p in graph[i].getPaths():
                dest = p.getDestiny()
                enemyCost = 0
                enemies = graph[dest].getEnemies()
                for e in enemies: # Calculate enemies cost.
                    enemyCost += enemies[e].getGold()
                if ((d[dest] == -1) or (d[dest] > (p.getCost()+graph[dest].getCost()+d[i]+enemyCost))):
                    d[dest] = p.getCost()+graph[dest].getCost()+d[i]+enemyCost
                    prev[dest] = graph[i].getName()
                    if (in_queue[dest] == False):
                       queue.append(dest)
                       in_queue[dest] = True
            
        # Return results.
        return prev
        
        
    # Check enemies movement.
    graphC = copy.deepcopy(graph)
    enemiesC = copy.deepcopy(enemies)
    boatC = copy.deepcopy(boat)
    doEnemieMove(enemiesC,graphC,boatC)
    
    # Select movement.
    prev = bellmanFord(graphC,boat.getPosition())
    selPath = "Raftel"
    islandPrev = prev[selPath]
    visited = ["Raftel"]
    while (islandPrev != boat.getPosition()):
        selPath = islandPrev
        islandPrev = prev[selPath]
        if (selPath in visited): # Cycle.
            # Pillage.
            boat.setGold(boat.getGold() + 10)
            return
        else:
            visited.append(selPath)
    
    # Calculate the move cost.
    paths = graph[boat.getPosition()].getPaths()
    for p in paths:
        if (p.getDestiny() == selPath):
            pathCost = p.getCost() + graph[selPath].getCost()
    
    # Move boat if you have sufficient gold.
    if (boat.getGold() >= pathCost):
        boat.setPosition(selPath)
        
        # Update amount of gold.
        boat.setGold(boat.getGold() - pathCost)
        if (boat.getGold() < 0):
            boat.setGold(0)
            
    else: # Pillage.
        boat.setGold(boat.getGold() + 10)      
        
        
        
def doEnemieMove(enemies,graph,boat):
    """
    This method moves enemy boats one position.
    """
    for enemy in enemies:
        # Select path.
        e = enemies[enemy]
        paths = graph[e.getPosition()].getPaths()
        
        if (len(paths) != 0):
            selPath = paths[0]
            if (e.getNumber()%2 == 0): # Even number.
                for p in paths:
                    if (p.getCost() >  selPath.getCost()):
                        selPath = p
            else: # Odd number.
                for p in paths:
                    if (p.getCost() <  selPath.getCost()):
                        selPath = p
        
            # Move enemy boat.
            graph[e.getPosition()].removeEnemy(e)
            e.setPosition(selPath.getDestiny())
            graph[e.getPosition()].addEnemy(e)
        
            # Is myBoat in the new island?. Update the amount gold.
            if ((boat.getPosition() == e.getPosition()) and (boat.getPosition() != 'Raftel')):
                boat.setGold(boat.getGold() - e.getGold())
      
                                            
        
################################  MAIN  #######################################

# Read data (islands, paths and boats) and store it. (Change the path to the file).
f = open('submitInput', 'r', 0)
# 1- Islands.
graph = {} # Dict of islands. Name->Node.
nIslands = int(f.readline())
for island in range(nIslands):
    islandData = f.readline().split()
    island = Island(islandData[0],int(islandData[1]))
    graph[islandData[0]] = island

# 2- Paths.
nPaths = int(f.readline())
for paths in range(nPaths):
    pathData = f.readline().split()
    path = Path(pathData[1],int(pathData[2]))
    graph[pathData[0]].addPath(path)

# 3- Boats.
nBoats = int(f.readline())
enemies = {} # Dict of enemy boats. Name->Boat.
for boats in range(nBoats):
    boatData = f.readline().split()
    boat = Boat(int(boatData[0]),boatData[1],int(boatData[2]),boatData[3])
    if (boatData[0] == '1'):
        myBoat = boat
    else:
        enemies[boatData[1]] = boat
        graph[boat.getPosition()].addEnemy(boat)

# Travel to Raftel.
route = [myBoat.getPosition()]
while (myBoat.getPosition() != 'Raftel'):
    # Move my boat.
    doBoatMove(myBoat,graph,enemies)
    
    # Move enemies.
    doEnemieMove(enemies,graph,myBoat)
    
    # Update route.
    route.append(myBoat.getPosition())
    
# My boat can pillage until an enemy arrives to Raftel.
enemiesinRaftel = len(graph["Raftel"].getEnemies())
while (enemiesinRaftel == 0):
    # Pillage.
    myBoat.setGold(myBoat.getGold() + 10)
    
    # Move enemies.
    doEnemieMove(enemies,graph,myBoat)
    
    # Check enemies position.
    enemiesinRaftel = len(graph["Raftel"].getEnemies())
    
# Show the final amount of gold and the route.
print "Final amount of gold: " + str(myBoat.getGold())
print route

# Close the file.
f.close()
