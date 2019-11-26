import retro

def main():
    env = retro.make(game='Airstriker-Genesis')
    obs = env.reset()
    while True:
        action = env.action_space.sample()
        obs, rew, done, info = env.step(action)
        print(action,rew)
        env.render()
        if done:
            obs = env.reset()
    env.close()


if __name__ == "__main__":
    main()