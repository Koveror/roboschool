import roboschool
import gym
import numpy as np

env = gym.make('RoboschoolAnt-v1')
env.reset()

i = 0

action_dim = len(env.action_space.sample())
one_action = np.zeros(action_dim)
flag_save_complete = False
max_save_id = 50
max_interval = 5
while True:

    # Save 10 states
    if i % max_interval == 0 and i < max_save_id and not flag_save_complete:
        env.unwrapped.save()

    # Load state
    if i == max_save_id:
        flag_save_complete = True
        _id = np.random.randint(0, int(max_save_id / max_interval))
        env.unwrapped.load(_id)
        i = _id * max_interval

    env.step(one_action)
    env.render()

    i += 1