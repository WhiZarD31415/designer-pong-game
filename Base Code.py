from designer import *
from dataclasses import dataclass
import random

@dataclass
class Player:
    box: DesignerObject
    up_active: bool
    down_active: bool
    
@dataclass
class World:
    title: DesignerObject
    timer: DesignerObject
    score: DesignerObject
    message1: DesignerObject
    message2: DesignerObject
    world_lp: Player
    world_rp: Player
    ball: DesignerObject
    boundary1: DesignerObject
    boundary2: DesignerObject
    set_score: DesignerObject

center_x = get_width() / 2
center_y = get_height() / 2

def create_player(x: int, y: int) -> Player:
    return Player(rectangle("black", 20, 200, x, y), False, False)
left_player = create_player(10,center_y)
right_player = create_player(790,center_y)

def create_the_world() -> World:
    global real_time
    global lp_score
    global rp_score
    global lp_set_score
    global rp_set_score
    global i
    global a
    global b
    global c
    i = 0
    a = 0
    b = 0
    c = 0
    real_time = 0
    lp_score = 0
    rp_score = 0
    lp_set_score = 0
    rp_set_score = 	0
    return World(
        text("black", "Welcome to Pong", 50, center_x, center_y - 200),
        text("black", "Game time: 0:00", 20, center_x, 588),
        text("black", "Score: 0 - 0", 20, center_x, 10),
        text("black", "Left player uses 'W' and 'S'  |  Right player uses 'O' and 'L'", 20, center_x, center_y - 100),
        text("black", "First to 10 wins! Press 'Space' to serve the ball", 20, center_x, center_y - 50),
        left_player.box,
        right_player.box,
        circle("black", 15, center_x, center_y),
        rectangle("black", 800, 202, center_x, y=-100),
        rectangle("black", 800, 202, center_x, y=700),
        text("black", "Set Score: 0 - 0", 20, center_x, 30))

def reset_the_world(world: World, keep: bool):
    global real_time
    global lp_score
    global rp_score
    global lp_set_score
    global rp_set_score
    global i
    global a
    global b
    global c
    i = 0
    a = 0
    b = 0
    c = 0
    real_time = 0
    lp_score = 0
    rp_score = 0
    if not keep:
        lp_set_score = 0
        rp_set_score = 0
    world.title.text = ""
    world.title = text("black", "Welcome to Pong", 50, center_x, center_y - 200)
    world.timer.text = ""
    world.timer = text("black", "Game time: 0:00", 20, center_x, 588)
    world.score.text = ''
    world.score = text("black", "Score: 0 - 0", 20, center_x, 10)
    world.message1.text = ""
    world.message1 = text("black", "Left player uses 'W' and 'S'  |  Right player uses 'O' and 'L'", 20, center_x, center_y - 100)
    world.message2.text = ""
    world.message2 = text("black", "First to 10 wins! Press 'Space' to serve the ball", 20, center_x, center_y - 50)
    world.world_lp = left_player.box
    world.world_lp.y = center_y
    world.world_rp = right_player.box
    world.world_rp.y = center_y
    world.ball = circle("black", 15, center_x, center_y)
    world.set_score.text = ""
    world.set_score = text("black", "Set Score: " + str(lp_set_score) + " - " + str(rp_set_score), 20, center_x, 30)
    
def world_with_set_score(world: World):
    global lp_set_score
    global rp_set_score
    reset_the_world(world,True)
    if rp_win:
        rp_set_score += 1
    if lp_win:
        lp_set_score += 1
    world.title.text = ""
    world.message1.text = ""
    world.set_score.text = ""
    world.set_score = text("black", "Set Score: " + str(lp_set_score) + " - " + str(rp_set_score), 20, center_x, 30)
    

def press_key(world: World, key: str):
    global left_player
    global right_player
    global i
    global a
    global c
    if (key == " ") and (i == 0):
        i = 1
    if (key == " ") and (a == 0):
        a = 1
    if (key == "r") and (c == 1):
        reset_the_world(world,False)
    if (key == "k") and (c == 1):
        world_with_set_score(world)
    if key == "w":
        left_player.up_active = True
    if key == "s":
        left_player.down_active = True
    if key == "o":
        right_player.up_active = True
    if key == "l":
        right_player.down_active = True

def release_key(key: str):
    global left_player
    global right_player
    if key == "w":
        left_player.up_active = False
    if key == "s":
        left_player.down_active = False
    if key == "o":
        right_player.up_active = False
    if key == "l":
        right_player.down_active = False

def movement_players(world: World):
    if left_player.up_active:
        if world.world_lp.y >= 105:
            world.world_lp.y -= 10
    if left_player.down_active:
        if world.world_lp.y <= 495:
            world.world_lp.y += 10
    if right_player.up_active:
        if world.world_rp.y >= 105:
            world.world_rp.y -= 10
    if right_player.down_active:
        if world.world_rp.y <= 495:
            world.world_rp.y += 10
            
def game_start(world: World):
    if a == 1:
        world.title.text = ""
        world.message1.text = ""
        world.message2.text = ""
        start_ball(world)
        
def start_ball(world: World):
    global b
    global y_move
    global direction
    if b == 0:
        b = 1
        y_move = random.randint(-3,3)
        direction = 10
    if b == -1:
        b = 1
        y_move = random.randint(-3,3)
        direction = -10
    if not y_move:
        y_move += 1
    if colliding(world.ball, world.world_rp):
        direction = direction*-1
        if direction > 0:
            direction += 1
        if direction < 0:
            direction += -1
        if world.ball.y < world.world_rp.y:
            y_move = (world.world_rp.y - world.ball.y) * -0.1  
        if world.ball.y > world.world_rp.y:
            y_move = (world.world_rp.y - world.ball.y) * -0.1
    if colliding(world.ball, world.world_lp):
        direction = direction*-1
        if direction > 0:
            direction += 1
        if direction < 0:
            direction += -1
        if world.ball.y < world.world_lp.y:
            y_move = (world.world_lp.y - world.ball.y) * -0.1
        if world.ball.y > world.world_lp.y:
            y_move = (world.world_lp.y - world.ball.y) * -0.1
    if colliding(world.ball, world.boundary1):
        y_move = y_move*-1
    if colliding(world.ball, world.boundary2):
        y_move = y_move*-1
    if y_move > 30:
        y_move = 30
    if y_move < -30:
        y_move = -30
    if direction > 30:
        direction = 30
    if direction < -30:
        direction = -30
    world.ball.x += direction
    world.ball.y += y_move
    if world.ball.x < 0:
        score(world, "right_p")
    if world.ball.x > 800:
        score(world, "left_p")

def score(world: World, scorer: str):
    global rp_score
    global lp_score
    global b
    global a
    if scorer == "right_p":
        rp_score += 1
        b = -1
        a = 0
        world.ball.x = center_x - 200
    if scorer == "left_p":
        lp_score += 1
        b = 0
        a = 0
        world.ball.x = center_x + 200
    world.score.text = "Score: " + str(lp_score) + " - " + str(rp_score)
    world.ball.y = center_y

def advance_the_timer(world: World):
    global real_time
    global min_time
    global sec_time
    if i == 1:
        real_time += 1
        total_sec_time = real_time//30
        min_time = total_sec_time//60
        sec_time = total_sec_time - 60*min_time
        if sec_time < 10:
            world.timer.text = "Game time: " + str(min_time) + ":0" + str(sec_time)
        else:
            world.timer.text = "Game time: " + str(min_time) + ":" + str(sec_time)

def end_game(world: World):
    return (rp_score >= 10) or (lp_score >= 10)

def end_game_screen(world: World):
    global i
    global a
    global b
    global c
    global rp_win
    global lp_win
    i = 0
    a = 0
    b = 0
    c = 1
    if sec_time < 10:
        timer_text = "Game time: " + str(min_time) + ":0" + str(sec_time)
    else:
        timer_text = "Game time: " + str(min_time) + ":" + str(sec_time)
    score_text = "Score: " + str(lp_score) + " - " + str(rp_score)
    if rp_score == 10:
        final_text = "The right player wins!"
        rp_win = True
        lp_win = False
    if lp_score == 10:
        final_text = "The left player wins!"
        rp_win = False
        lp_win = True
    world.title.text = "Game Over!"
    world.timer.text = timer_text
    world.score.text = score_text
    world.message1.text = final_text
    world.message2.text = "Press 'R' to reset. Press K to keep set score"
    world.world_rp.y = -1000
    world.world_lp.y = -1000
    world.ball.y = -1000

when("starting", create_the_world)
when("updating", movement_players)
when("updating", game_start)
when("updating", advance_the_timer)
when("typing", press_key)
when("done typing", release_key)
when(end_game, end_game_screen)

start()