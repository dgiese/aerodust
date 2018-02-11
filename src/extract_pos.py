import logging 
import mylogger
import subprocess

class PlayerConfig:
    def __init__(self):
        self.position_token = (3, "position2d")
        self.type_token = (5, 1)
        self.subtype_token = (6, 1)

class Position:
    def __init__(self, line):
        tokens = line.split(" ")
        
        # Time
        self.time       = float(tokens[0])
        
        # Positions
        self.x_pos      = float(tokens[7])
        self.y_pos      = float(tokens[8])
        self.yaw_pos    = float(tokens[9])
        
        # Velocity
        self.x_vel      = float(tokens[10])
        self.y_vel      = float(tokens[11])
        self.yaw_vel    = float(tokens[12])

        # Motor stall
        # self.motor = tokens[13]
    
    def __repr__(self):
        representation = "Time: %f \n" \
        "\tX Pos: %f \n" \
        "\tY Pos: %f \n" \
        "\tYaw Pos: %f \n" \
        "\tX vel: %f \n" \
        "\tY vel: %f \n" \
        "\tYaw vel: %f\n"\
        % (self.time, self.x_pos, self.y_pos, self.yaw_pos, self.x_vel, self.y_vel, self.yaw_vel)

        return representation

def tail_file(filename):
    """
    Proc every line in a file
    """
    # Holds all of the responses 
    responses = []
    
    f = subprocess.Popen(['tail', '-F', filename],\
            stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    while True:
        for line in f.readlines():
            try:
                response = process_line(line)
                if response is not None:
                    responses.append(response)
                else:
                    pass
            except Exception as e:
                logging.error("Error..." + str(e))
                pass
            
    return responses
    

def read_file(filename):
    """
    Proc every line in a file
    """
    # Holds all of the responses 
    responses = []
    
    with open(filename, "r") as f:
        for line in f.readlines():
            try:
                response = process_line(line)
                if response is not None:
                    responses.append(response)
                else:
                    pass
            except Exception as e:
                logging.error("Error..." + str(e))
                pass
            
    return responses

def process_line(line) -> Position or None:
    """
    Given a line, return either a Position object or None
    """
    logging.debug(line)
    if is_position2d(line):
        return Position(line)
    else:
        return None


def is_position2d(line) -> bool:
    """
    Returns a boolean if the line represents a 2d position line
    """
    tokens = line.split(" ")
    logging.debug(tokens)
    config = PlayerConfig()
    return \
    tokens[config.position_token[0]] == config.position_token[1] and \
    int(tokens[config.type_token[0]]) == config.type_token[1] and \
    int(tokens[config.subtype_token[0]]) == config.subtype_token[1]

if __name__ == "__main__":
    data_file = "data/PLAYER_fprintf.TEST.log"
    mylogger.config_logs()
    responses = read_file(data_file)
    print(responses)








