import pygame
import algorithm

pygame.init()
screen = pygame.display.set_mode((800, 600), pygame.RESIZABLE)

running = True
screen.fill("black")

radius = 20
ball_color = "white"

clicked = 0
max_nodes = 50

selected_color = "white"

class Node:
    def __init__(self,x,y,color,id):
        self.x = x
        self.y = y
        self.id = id
        self.color = color

    def draw(self):
        pygame.draw.circle(screen,self.color, [self.x, self.y], radius)

start_node = Node(100,50,"Green",0)

nodes = [start_node]
graph = [[0 for i in range(max_nodes)] for j in range(max_nodes)]
last_node = start_node
count = 1

class Button:
    def __init__(self,x,y,w,h,text,color):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.text = text
        self.color = color
        self.rect = None

    def draw(self):
        self.rect = pygame.draw.rect(screen,self.color,[self.x,self.y,self.w,self.h])
        smallfont = pygame.font.SysFont('Corbel', 25,bold=True)
        text = smallfont.render(self.text, True, "white")
        screen.blit(text , (self.x+5,self.y+5))


def inCircle(cx,cy,mx,my):
    #cx,cy,cr --> circle x,y
    #mx,my    --> mouse x,y
    return (cx-mx)**2 + (cy-my)**2 < radius**2

def NodeClicked(nodes,pos):
    for node in nodes:
        if inCircle(node.x, node.y, pos[0], pos[1]):
            return node
    return None

def addEdge(i,j):
    if i == j:
        return
    graph[i][j] = 1
    graph[j][i] = 1

def drawEdges(graph):
    for i in range(max_nodes):
        for j in range(max_nodes):
            if graph[i][j]:
                node1 = nodes[i]
                node2 = nodes[j]
                pygame.draw.line(screen,"white",(node1.x,node1.y),(node2.x,node2.y))

def printGraph(graph):
    for i in range(max_nodes):
        print(graph[i])



start_button = Button(700,30,65,30,"Start","purple")
reset_button = Button(700,100,70,30,"Reset","red")

while running:
    screen.fill("black")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            node = NodeClicked(nodes,event.pos)
            if node:
                addEdge(node.id,last_node.id)
                last_node = node

            else:
                if count >= max_nodes:
                    print("MAX NO OF NODES REACHED !!")
                    exit()
                if start_button.rect.collidepoint(event.pos[0],event.pos[1]):
                    path = algorithm.pathFinder.PathFinder(graph, start_node.id, nodes[-1].id).Find()
                    if path:
                        for m in path:
                            nodes[m].color = "blue"
                elif reset_button.rect.collidepoint(event.pos[0],event.pos[1]):
                    start_node.color = "white"
                    nodes = [start_node]
                    last_node = start_node
                    count = 1
                    graph = [[0 for i in range(max_nodes)] for j in range(max_nodes)]

                else:
                    newNode = Node(event.pos[0],event.pos[1],"red",count)
                    if len(nodes) > 1:
                        nodes[-1].color = "white"
                    addEdge(count,last_node.id)
                    nodes.append(newNode)
                    count += 1

    drawEdges(graph)
    [n.draw() for n in nodes]

    start_node.draw()
    start_button.draw()
    reset_button.draw()

    pygame.display.flip()

pygame.quit()
