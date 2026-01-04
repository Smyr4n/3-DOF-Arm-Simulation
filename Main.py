import Config
import Robot
import Plot

if __name__ == "__main__":

    d, a, alpha = Config.Read_Config("Config.json")

    robot = Robot.Robot(d, a, alpha)

    Plot.Make_Plot(robot)