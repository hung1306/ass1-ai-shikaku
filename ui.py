from turtle import Turtle, Screen
from tkinter import Button, Radiobutton, IntVar, Label
from tkinter.ttk import Style
from block import BlockManager, Block
from search import Solver
FONT = ("Merriweather", 22, "bold")
WIDTH = 60


class GUI:
    # Khởi tạo giao diện người dùng, bao gồm việc tạo ra các nút, khung, và khởi tạo trạng thái ban đầu.
    def __init__(self, block_manager: BlockManager, solver: Solver):
        self.step = 0
        self.manager = block_manager
        self.solver = solver
        # list Turtle
        self.all_segment = []
        self.screen = Screen()
        self.screen.title("Shikaku - Puzzle Game")
        self.screen.bgcolor("#1f2e2e")
        self.screen.setup(width=800, height=800)
        
        self.screen.tracer(0)
        # self.create_logo()
        self.create_hint_button()
        self.create_new_button()
        self.create_radio_button()
        self.create_frame()
        self.intialize()

        self.drawer = Turtle()
        self.drawer.hideturtle()
        self.drawer.penup()
        
        self.screen.mainloop()

    # Vẽ khung và các dấu chấm trên màn hình.
    def create_frame(self):
        start_pos = (-WIDTH * 2 - 30, -WIDTH * 2 - 30)
        drawer = Turtle()
        drawer.hideturtle()
        drawer.penup()
        drawer.pencolor("#f0f5f5")
        def draw_dots():
            for i in range(20):
                if i % 4 == 0:
                    drawer.dot(8)
                else:
                    drawer.dot(3, "#f0f5f5")
                drawer.forward(WIDTH / 4)

        drawer.goto(start_pos)
        for i in range(6):
            if i > 0:
                drawer.goto(-drawer.xcor(), drawer.ycor() + WIDTH)
            draw_dots()

        drawer.goto(start_pos)
        drawer.setheading(90)
        for i in range(6):
            if i > 0:
                drawer.goto(drawer.xcor() + WIDTH, -drawer.ycor())
            draw_dots()

        drawer.goto(start_pos)
        drawer.pendown()
        drawer.pensize(8)
        
        for _ in range(4):
            drawer.forward(WIDTH*5)
            drawer.right(90)
        self.screen.update()

    # Kích hoạt nút "Hint", cho phép người dùng nhấn vào nút này.
    def create_hint_button(self):
        canvas = self.screen.getcanvas()
        self.hint_button = Button(canvas.master, text="Gợi ý", command=self.hint)
        self.hint_button.config(foreground="#001a00", activeforeground="#f9f6f2", background="#fafafa", activebackground="#001a00", font=("Comic Sans MS", 12, 'bold'))
        self.hint_button.config(disabledforeground="#661a00")
        self.hint_button.config(state="disabled")
        canvas.create_window(-50, -230, window=self.hint_button)
    #  Kích hoạt nút "Hint", cho phép người dùng nhấn vào nút này.
    def active_hint_button(self):
        self.alert.clear()
        self.hint_button.config(state="normal")
    #  Tạo nút "New Game" trên màn hình, khi nhấn vào nút này sẽ gọi đến hàm new.
    def create_new_button(self):
        canvas = self.screen.getcanvas()
        self.new_button = Button(canvas.master, text="New Game", command=self.new)
        self.new_button.config(foreground="#001a00", activeforeground="#f9f6f2", background="#fafafa", activebackground="#001a00", font=("Comic Sans MS", 12, 'bold'))
        self.new_button.config(disabledforeground="#661a00")
        canvas.create_window(50, -230, window=self.new_button)
    # Tạo các nút radio cho phép người dùng chọn thuật toán.
    def create_radio_button(self):
        self.radio_state = IntVar()
        canvas = self.screen.getcanvas()
        label = Label(canvas.master, text="Chọn thuật toán:")
        label.config(width=15, font=("Comic Sans MS", 13, 'bold'), foreground="#001a00", background="#fafafa")
        self.radiobutton1 = Radiobutton(canvas.master, text="Chơi bằng BFS", value=1, variable=self.radio_state, command=self.active_hint_button)
        self.radiobutton2 = Radiobutton(canvas.master, text="Chơi bằng Backtracking", value=2, variable=self.radio_state, command=self.active_hint_button)
        self.radiobutton1.config(foreground="#001a00", activeforeground="#001a00", background="#fafafa", activebackground="#fafafa", font=("Comic Sans MS", 10, 'bold'))
        self.radiobutton2.config(foreground="#001a00", activeforeground="#001a00", background="#fafafa", activebackground="#fafafa", font=("Comic Sans MS", 10, 'bold'))
        canvas.create_window(240, -235, window=label)
        canvas.create_window(230, -205, window=self.radiobutton1)
        canvas.create_window(258, -175, window=self.radiobutton2)

        self.alert = Turtle()
        self.alert.hideturtle()
        self.alert.penup()
        self.alert.goto(0, 170)
        self.alert.pencolor('#fafafa')
        self.alert.write('Hãy chọn thuật toán!', align='center', font=("Comic Sans MS", 17, 'bold'))
    # Khởi tạo trạng thái ban đầu của trò chơi, bao gồm việc vẽ các số trên màn hình.
    def intialize(self):
        start_pos = -2 * WIDTH
        for block in self.manager.all_block:
            segment = Turtle()
            segment.hideturtle()
            segment.penup()
            segment.goto(start_pos + 60*block.pos_num[1], start_pos + 60*block.pos_num[0] - 15)
            segment.pencolor("#f0f5f5")
            segment.write(block.number, align='center', font=FONT)
            self.all_segment.append(segment)

    # Vẽ một khối trên màn hình.
    def draw_block(self, block: Block):
        start_val = -WIDTH * 2 - 30
        start_pos = block.start_pos
        width = block.width
        height = block.height

        self.drawer.goto(start_val + 60*start_pos[1], start_val + 60*start_pos[0])
        self.drawer.pendown()
        self.drawer.pensize(8)
        self.drawer.pencolor("#f0f5f5")
        for _ in range(2):
            self.drawer.forward(60*width)
            self.drawer.left(90)
            self.drawer.forward(60*height)
            self.drawer.left(90)
        self.drawer.penup()
        
    # Hiển thị gợi ý cho người chơi dựa trên thuật toán đã chọn.
    def hint(self):
        if self.step == 0:
            if self.radio_state.get() == 1:
                goal_node = self.solver.bfs()
            elif self.radio_state.get() == 2:
                goal_node = self.solver.backtracking()
            self.manager.goal_state = goal_node.state
        
        goal_state = self.manager.goal_state
        if self.step < len(goal_state) - 1:
            self.new_button.config(state="disabled")
            block = goal_state[self.step]
            self.draw_block(block)
            self.step += 1
            self.screen.update()
        else:
            self.alert.write('Đã tìm thấy trạng thái mục tiêu!', align='center', font=("Comic Sans MS", 15, 'bold'))
            self.new_button.config(state="normal")
            
    # Khởi tạo lại trạng thái ban đầu của trò chơi.
    def new(self):
        for segment in self.all_segment:
            segment.clear()
        self.drawer.clear()
        self.alert.clear()
        self.alert.write('Hãy chọn thuật toán', align='center', font=("Comic Sans MS", 17, 'bold'))
        self.radio_state.set(0)

        self.step = 0
        self.hint_button.config(state="disabled")
        self.all_segment.clear()
        if self.manager.generate():
            self.manager.create()
            self.intialize()
        else:
            self.game_over()
    # Hiển thị thông báo "GAME OVER" khi trò chơi kết thúc.
    def game_over(self):
        drawer = Turtle()
        drawer.hideturtle()
        drawer.penup()
        drawer.goto(0, -30)
        drawer.pencolor('#361500')
        drawer.write('GAME OVER', align='center', font=("Comic Sans MS", 50, 'normal'))
