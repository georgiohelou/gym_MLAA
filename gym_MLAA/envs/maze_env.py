import numpy as np

import gym
from gym import error, spaces, utils
from gym.utils import seeding
from gym_MLAA.envs.maze_view_2d import MazeView2D


class MazeEnv(gym.Env):
    metadata = {
        "render.modes": ["human", "rgb_array"],
    }

    ACTION = ["N", "S", "E", "W"]

    def __init__(self, maze_size=None, mode=None, enable_render=True, fire_ratio=0):

        self.viewer = None
        self.enable_render = enable_render

        if maze_size:
            if mode == "plus":
                has_loops = True
                num_portals = int(round(min(maze_size)/3))
                num_fires = 0.5*fire_ratio*(min(maze_size)**2)
                #num_fires = 20
            else:
                has_loops = False
                num_portals = 0
                num_fires = 0 

            self.maze_view = MazeView2D(maze_name="OpenAI Gym - Maze (%d x %d)" % maze_size,
                                        maze_size=maze_size, screen_size=(640, 640),
                                        has_loops=has_loops, num_portals=num_portals,num_fires=num_fires,
                                        enable_render=enable_render)
        else:
            raise AttributeError("One must supply the maze_size (tuple of length 2)")

        self.maze_size = self.maze_view.maze_size

        # forward or backward in each dimension
        self.action_space = spaces.Discrete(2*len(self.maze_size))

        # observation is the x, y coordinate of the grid
        low = np.zeros(len(self.maze_size), dtype=int)
        high =  np.array(self.maze_size, dtype=int) - np.ones(len(self.maze_size), dtype=int)
        self.observation_space = spaces.Box(low, high, dtype=np.int64)

        # initial condition
        self.state = None
        self.steps_beyond_done = None

        # Simulation related variables.
        self.seed()
        self.reset()

        # Just need to initialize the relevant attributes
        self.configure()

    def __del__(self):
        if self.enable_render is True:
            self.maze_view.quit_game()

    def configure(self, display=None):
        self.display = display

    def seed(self, seed=None):
        self.np_random, seed = seeding.np_random(seed)
        return [seed]

    def step(self, action):
        if isinstance(action, int):
            self.maze_view.move_robot(self.ACTION[action])
        else:
            self.maze_view.move_robot(action)

        if np.array_equal(self.maze_view.robot, self.maze_view.goal):
            reward = 1
            done = True
        elif self.maze_view.fire:
            reward = -1/(self.maze_size[0]*self.maze_size[1])
            done = False
        else:
            reward = -0.1/(self.maze_size[0]*self.maze_size[1])
            done = False

        self.state = self.maze_view.robot

        info = {}

        return self.state, reward, done, info

    def reset(self):
        self.maze_view.reset_robot()
        self.state = np.zeros(2)
        self.steps_beyond_done = None
        self.done = False
        return self.state

    def is_game_over(self):
        return self.maze_view.game_over

    def render(self, mode="human", close=False):
        if close:
            self.maze_view.quit_game()

        return self.maze_view.update(mode)


class MazeEnvRandom3x3(MazeEnv):

    def __init__(self, enable_render=True):
        super(MazeEnvRandom3x3, self).__init__(maze_size=(3, 3), enable_render=enable_render)

class MazeEnvRandom5x5(MazeEnv):

    def __init__(self, enable_render=True):
        super(MazeEnvRandom5x5, self).__init__(maze_size=(5, 5), enable_render=enable_render)


class MazeEnvRandom10x10(MazeEnv):

    def __init__(self, enable_render=True):
        super(MazeEnvRandom10x10, self).__init__(maze_size=(10, 10), enable_render=enable_render)

class MazeEnvRandom30x30(MazeEnv):

    def __init__(self, enable_render=True):
        super(MazeEnvRandom30x30, self).__init__(maze_size=(30, 30), enable_render=enable_render)


class MazeEnvRandom100x100(MazeEnv):

    def __init__(self, enable_render=True):
        super(MazeEnvRandom100x100, self).__init__(maze_size=(100, 100), enable_render=enable_render)

class MazeEnvRandom5x5Plus(MazeEnv):

    def __init__(self, enable_render=True):
        super(MazeEnvRandom5x5Plus, self).__init__(maze_size=(5, 5), mode="plus", enable_render=enable_render)

class MazeEnvRandom10x10Plus(MazeEnv):

    def __init__(self, enable_render=True):
        super(MazeEnvRandom10x10Plus, self).__init__(maze_size=(10, 10), mode="plus", enable_render=enable_render)


class MazeEnvRandom20x20Plus(MazeEnv):

    def __init__(self, enable_render=True):
        super(MazeEnvRandom20x20Plus, self).__init__(maze_size=(20, 20), mode="plus", enable_render=enable_render)


class MazeEnvRandom30x30Plus(MazeEnv):
    def __init__(self, enable_render=True):
        super(MazeEnvRandom30x30Plus, self).__init__(maze_size=(30, 30), mode="plus", enable_render=enable_render)

#
class MazeEnvRandom5x5Ratio30(MazeEnv):

    def __init__(self, enable_render=True):
        super(MazeEnvRandom5x5Ratio30, self).__init__(maze_size=(5, 5), enable_render=enable_render, fire_ratio=0.32)

class MazeEnvRandom10x10Ratio30(MazeEnv):

    def __init__(self, enable_render=True):
        super(MazeEnvRandom10x10Ratio30, self).__init__(maze_size=(10, 10), enable_render=enable_render, fire_ratio=0.32)

class MazeEnvRandom30x30Ratio30(MazeEnv):
    def __init__(self, enable_render=True):
        super(MazeEnvRandom30x30Ratio30, self).__init__(maze_size=(30, 30), enable_render=enable_render, fire_ratio=0.32)
#
class MazeEnvRandom5x5PlusRatio30(MazeEnv):

    def __init__(self, enable_render=True):
        super(MazeEnvRandom5x5PlusRatio30, self).__init__(maze_size=(5, 5),mode="plus", enable_render=enable_render, fire_ratio=0.32)

class MazeEnvRandom10x10PlusRatio30(MazeEnv):

    def __init__(self, enable_render=True):
        super(MazeEnvRandom10x10PlusRatio30, self).__init__(maze_size=(10, 10), mode="plus", enable_render=enable_render, fire_ratio=0.32)

class MazeEnvRandom30x30PlusRatio30(MazeEnv):
    def __init__(self, enable_render=True):
        super(MazeEnvRandom30x30PlusRatio30, self).__init__(maze_size=(30, 30), mode="plus", enable_render=enable_render, fire_ratio=0.32)
        
