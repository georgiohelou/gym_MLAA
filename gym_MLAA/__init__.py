from gym.envs.registration import register

register(
    id='maze-random-3x3-v0',
    entry_point='gym_MLAA.envs:MazeEnvRandom3x3',
    max_episode_steps=1000,
    nondeterministic=True,
)

register(
    id='maze-random-5x5-v0',
    entry_point='gym_MLAA.envs:MazeEnvRandom5x5',
    max_episode_steps=2000,
    nondeterministic=True,
)

register(
    id='maze-random-10x10-v0',
    entry_point='gym_MLAA.envs:MazeEnvRandom10x10',
    max_episode_steps=10000,
    nondeterministic=True,
)

register(
    id='maze-random-30x30-v0',
    entry_point='gym_MLAA.envs:MazeEnvRandom30x30',
    max_episode_steps=1000000,
    nondeterministic=True,
)

register(
    id='maze-random-100x100-v0',
    entry_point='gym_MLAA.envs:MazeEnvRandom100x100',
    max_episode_steps=1000000,
    nondeterministic=True,
)

register(
    id='maze-random-5x5-plus-v0',
    entry_point='gym_MLAA.envs:MazeEnvRandom5x5Plus',
    max_episode_steps=1000000,
    nondeterministic=True,
)


register(
    id='maze-random-10x10-plus-v0',
    entry_point='gym_MLAA.envs:MazeEnvRandom10x10Plus',
    max_episode_steps=1000000,
    nondeterministic=True,
)

register(
    id='maze-random-20x20-plus-v0',
    entry_point='gym_MLAA.envs:MazeEnvRandom20x20Plus',
    max_episode_steps=1000000,
    nondeterministic=True,
)

register(
    id='maze-random-30x30-plus-v0',
    entry_point='gym_MLAA.envs:MazeEnvRandom30x30Plus',
    max_episode_steps=1000000,
    nondeterministic=True,
)

register(
    id='maze-random-5x5-Ratio-30-v0',
    entry_point='gym_MLAA.envs:MazeEnvRandom5x5Ratio30',
    max_episode_steps=2000,
    nondeterministic=True,
)

register(
    id='maze-random-10x10-Ratio-30-v0',
    entry_point='gym_MLAA.envs:MazeEnvRandom10x10Ratio30',
    max_episode_steps=2000,
    nondeterministic=True,
)

register(
    id='maze-random-30x30-Ratio-30-v0',
    entry_point='gym_MLAA.envs:MazeEnvRandom30x30Ratio30',
    max_episode_steps=2000,
    nondeterministic=True,
)

register(
    id='maze-random-5x5-plus-Ratio-30-v0',
    entry_point='gym_MLAA.envs:MazeEnvRandom5x5PlusRatio30',
    max_episode_steps=10000,
)

register(
    id='maze-random-10x10-plus-Ratio-30-v0',
    entry_point='gym_MLAA.envs:MazeEnvRandom10x10PlusRatio30',
    max_episode_steps=10000,
)

register(
    id='maze-random-30x30-plus-Ratio-30-v0',
    entry_point='gym_MLAA.envs:MazeEnvRandom30x30PlusRatio30',
    max_episode_steps=1000000,
    nondeterministic=True,
)
