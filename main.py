import pygame
import pickle
import sys

running = True
width, height = 800, 800
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Convays game of Life")
unit = 20


def background_gird():
    screen.fill((255, 255, 255))
    for i in range(int(width / unit) + 1):
        pygame.draw.line(screen, (0, 0, 0), (0, unit * i), (width, unit * i))
        pygame.draw.line(screen, (0, 0, 0), (unit * i, 0), (unit * i, height))

initial_load = (len(sys.argv) == 2)
# print(initial_load)
row = int(height / unit) + 2
col = int(width / unit) + 2
Life = [[0] * row for i in range(col)]
old_Life = [[0] * row for i in range(col)]
null_Life = [[0] * row for i in range(col)]
temp_Life = [[0] * row for i in range(col)]
LifeCount = [[0] * (row - 2) for i in range(col - 2)]
mouse_x = 0
mouse_y = 0
change = False
click_x = 0
click_y = 0


def save_life():
    global Life
    
    filename = input("Enter the name of save file : ")
    if filename.endswith('.data'):
        filename = filename[:-5]
    
    with open(str(filename) + '.data', 'wb') as filehandle:
        pickle.dump(Life, filehandle)


def oldLife_eq_Life():
    global Life
    global old_Life
    for i in range(0, row):
        for j in range(0, col):
            old_Life[i][j] = Life[i][j]


def load_life():
    global Life
    global old_Life
    global initial_load
    
    if initial_load:
        filename = sys.argv[1]
        initial_load = False
    else:    
        filename = input("Enter the name of file to load: ")
    
    if filename.endswith('.data'):
        filename = filename[:-5]
    
    with open(str(filename) + '.data', 'rb') as filehandle:
        Life = pickle.load(filehandle)
        oldLife_eq_Life()


def draw_rect():
    for i in range(row):
        for j in range(col):
            if not Life[i][j]:
                color = (255, 255, 255)
            else:
                color = (255, 0, 0)
            pygame.draw.rect(screen, color, (((i - 1) * unit + 1, (j - 1) * unit + 1), (unit - 1, unit - 1)))


def tempLife_eq_Life():
    global Life
    global temp_Life
    for i in range(0, row):
        for j in range(0, col):
            temp_Life[i][j] = Life[i][j]


def update():
    global Life
    global temp_Life
    tempLife_eq_Life()
    # print(Life)
    # print(temp_Life)
    for i in range(1, row - 1):
        for j in range(1, col - 1):
            count = 0
            for k in range(i - 1, i + 2):
                for l in range(j - 1, j + 2):
                    if not (k == i and l == j):
                        # print (temp_Life[k][l])
                        if temp_Life[k][l]:
                            # print("("+str(k)+","+str(l)+"), ",end='')
                            count += 1
                            # print("Yes it got into here")
                            # print(str(k) + " " + str(l) + "=" + str(Life[k][l]))

            # print()
            # print(str(i-1)+","+str(j-1)+" to "+str(i+1)+","+str(j+1))
            LifeCount[i - 1][j - 1] = count  # print(str(i)+" "+str(j)+" "+str(count))
            if count == 3:
                Life[i][j] = 1
            elif count == 2:
                Life[i][j] = temp_Life[i][j]
            else:
                Life[i][j] = 0
                



end = False
end2 = False
if initial_load:
    load_life()

while not end:
    running = True
    while running:
        background_gird()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                end = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    running = False
                if event.key == pygame.K_s:
                    save_life()
                if event.key == pygame.K_l:
                    load_life()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                change = True
            if change:
                click_x = int(mouse_x / unit) + 1
                click_y = int(mouse_y / unit) + 1
                change = False
                if Life[click_x][click_y]:
                    Life[click_x][click_y] = 0
                else:
                    Life[click_x][click_y] = 1
            draw_rect()
            pygame.display.update()

    if not end:
        running = True
    while running:
        oldLife_eq_Life()
        background_gird()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                end = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    running = False
        update()
        draw_rect()
        pygame.display.update()
        if Life == null_Life or Life == old_Life:
            running = False
        pygame.time.wait(100)
        # print(LifeCount)
