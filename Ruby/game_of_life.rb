require 'rubygems'
require 'bundler/setup'

require 'ncurses'

def getwinyx(win)
    lines, columns = [], []
    Ncurses.getmaxyx(win, lines, columns)
    return lines[0], columns[0]
end

def init_grid(win, lines, columns)
    (1...lines - 1).each do |y|
        (1...columns - 1).each do |x|
            if Random.rand >= 0.90
                win.mvaddch(y, x, 'X'.ord)
            end
        end
    end
end

begin
    Ncurses::initscr()
    Ncurses::noecho()
    Ncurses::cbreak()
    Ncurses::nodelay(Ncurses.stdscr, true)

    lines, columns = getwinyx(Ncurses.stdscr)
    Ncurses.box(Ncurses.stdscr, 0, 0)
    init_grid(Ncurses.stdscr, lines, columns)

    while true
        (1...lines - 1).each do |y|
            (1...columns - 1).each do |x|
                if (y <= 2 or y >= lines - 2) or (x <= 2 or x >= columns - 2)
                    next
                end

                cell = Ncurses.mvinch(y, x).chr
                alive = 0
                (y - 1..y + 1).each do |cell_y|
                    (x - 1..x + 1).each do |cell_x|
                        if cell_y == y and cell_x == x
                            next
                        end

                        neighbour = Ncurses.mvinch(cell_y, cell_x).chr
                        if neighbour == 'X'
                            alive += 1
                        end
                    end
                end

                if cell != 'X'
                    if alive == 3
                        Ncurses.mvaddch(y, x, 'X'.ord)
                    end
                else
                    if alive < 2 or alive > 3
                        Ncurses.mvaddch(y, x, ' '.ord)
                    end
                end

            end
        end

        case (Ncurses.getch())
        when 'q'.ord, 'Q'.ord
            Ncurses.endwin()
            exit
        end
        Ncurses.refresh()
    end
ensure
    Ncurses::refresh()
    Ncurses::endwin()
end
