require 'rubygems'
require 'bundler/setup'

require 'ncurses'

def getwinyx(win)
    lines, columns = [], []
    Ncurses.getmaxyx(win, lines, columns)
    return lines[0], columns[0]
end

class Snake
    def initialize(win, x, y)
        @body = []
        @x, @y = x, y
        @win = win
        @last_move = 'right'

        5.times do |index|
            @body << SnakeCell.new(@x + index, @y)
        end

        redraw()
    end

    def move_right()
        @last_move = 'right'
        move_tail(1, 0)
        redraw()
    end

    def move_left()
        @last_move = 'left'
        move_tail(-1, 0)
        redraw()
    end

    def move_up()
        @last_move = 'up'
        move_tail(0, -1)
        redraw()
    end

    def move_down()
        @last_move = 'down'
        move_tail(0, 1)
        redraw()
    end

    def move()
        self.send("move_#{@last_move}")
    end

    def head
        return @body.last
    end

    def <<(item)
        @body << item
    end

    def append_cell()
        tail = @body.first
        case @last_move
        when 'up'
            cell = SnakeCell.new(tail.x, tail.y + 2)
        when 'down'
            cell = SnakeCell.new(tail.x, tail.y - 2)
        when 'right'
            cell = SnakeCell.new(tail.x + 2, tail.y)
        when 'left'
            cell = SnakeCell.new(tail.x - 2, tail.y)
        end

        @body.unshift(cell)
    end

    private

    def redraw()
        @body.each do |body_part|
            Ncurses.mvaddch(body_part.y, body_part.x, body_part.symbol)
        end
    end

    def move_tail(xd, yd)
        tail = @body.shift
        tail.x = @body.last.x + xd
        tail.y = @body.last.y + yd
        @body << tail
    end
end

class Food
    def initialize(x, y)
        @x, @y = x, y
        @symbol = Ncurses::ACS_DIAMOND
    end

    attr_reader :x, :y, :symbol
end

class SnakeCell
    def initialize(x, y)
        @symbol = 'X'.ord
        @x, @y = x, y
    end

    attr_accessor :x, :y
    attr_reader :symbol
end


begin
    Ncurses::initscr()
    Ncurses::noecho()
    Ncurses::cbreak()
    Ncurses::nodelay(Ncurses.stdscr, true)

    lines, columns = getwinyx(Ncurses.stdscr)
    snake = Snake.new(Ncurses.stdscr, columns / 3, lines / 3)
    foods = []

    50.times do |index|
        foods << Food.new(rand(2..columns - 2), rand(2..lines - 2))
    end

    while true
        Ncurses.clear()
        Ncurses::box(Ncurses.stdscr, 0, 0)
        foods.each do |food|
            Ncurses.mvaddch(food.y, food.x, food.symbol)
        end

        snake_head = snake.head
        foods.each do |food|
            if food.x == snake_head.x and food.y == snake_head.y
                snake.append_cell()
                foods.delete(food)
                break
            end
        end

        case (Ncurses.getch())
        when 'q'.ord, 'Q'.ord
            Ncurses.endwin()
            exit
        when 'a'.ord
            snake.move_left()
        when 'd'.ord
            snake.move_right()
        when 's'.ord
            snake.move_down()
        when 'w'.ord
            snake.move_up()
        else
            snake.move()
        end

        Ncurses.refresh()
        sleep(0.5)
    end

ensure
    Ncurses::refresh()
    Ncurses::endwin()
end
