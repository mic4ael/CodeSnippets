module Constants
    INTEGER = 'INTEGER'
    PLUS = 'PLUS'
    MINUS = 'MINUS'
    EOF = 'EOF'
end

class Token
    attr_reader :type
    attr_reader :value

    def initialize(type, value)
        @type = type
        @value = value
    end

    def to_s
        return "Token(#@type, #@value)"
    end
end

class Interpreter
    def initialize(text)
        @text = text
        @pos = 0
        @current_token = nil
        @current_char = @text[@pos]
    end

    def error
        raise 'Error parsing input'
    end

    def advance
        @pos += 1
        if @pos > @text.length - 1
            @current_char = nil
        else
            @current_char = @text[@pos]
        end
    end

    def skip_whitespace
        while @current_char and @current_char =~ /\s/
            self.advance()
        end
    end

    def integer
        number = ''
        while @current_char and @current_char =~ /[[:digit:]]/
            number += @current_char
            self.advance()
        end
        return number.to_i
    end

    def next_token
        while @current_char
            if @current_char =~ /\s/
                self.skip_whitespace()
                next
            elsif @current_char =~ /[[:digit:]]/
                return Token.new(Constants::INTEGER, self.integer())
            elsif @current_char == '+'
                self.advance()
                return Token.new(Constants::PLUS, '+')
            elsif @current_char == '-'
                self.advance()
                return Token.new(Constants::MINUS, '-')
            else
                self.error()
            end
        end
        return Token.new(Constants::EOF, nil)
    end

    def eat(token_type)
        if @current_token.type == token_type
            @current_token = self.next_token
        else
            self.error()
        end
    end

    def term
        token = @current_token
        self.eat(Constants::INTEGER)
        return token.value
    end

    def expr
        @current_token = self.next_token
        result = self.term()

        while [Constants::PLUS, Constants::MINUS].include?(@current_token.type)
            token = @current_token
            if token.type == Constants::PLUS
                self.eat(Constants::PLUS)
                result += self.term()
            elsif token.type == Constants::MINUS
                self.eat(Constants::MINUS)
                result -= self.term()
            end
        end

        return result
    end
end

while true
    print 'calc> '
    text = gets.chomp
    if not text
        next
    end

    interpreter = Interpreter.new(text)
    puts interpreter.expr()
end
