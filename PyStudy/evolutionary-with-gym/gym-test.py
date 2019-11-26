import gym
env = gym.make('MountainCar-v0')
for i_episode in range(20):
    observation = env.reset()
    action = 0
    for t in range(200):
        env.render()
        print(observation)
        observation, reward, done, info = env.step(action)
        print(action, reward)
        if done:
            print("Episode finished after {} timesteps".format(t+1))
            break
        if action == 0:
          action = 2
        else: action = 0
env.close()