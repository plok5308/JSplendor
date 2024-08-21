from jsplendor.game import Game

def main():
    game = Game(verbose=True)
    episode_log = []
    number_of_games = 10
    step_n = 1000

    for i in range(number_of_games):
        game.reset()
        for j in range(step_n):
            is_done = game.run_step()
            if is_done:
                episode_log.append(j+1)
                break

    print(episode_log)
    termination_rate = len(episode_log) / number_of_games
    print('termination rate: {}'.format(termination_rate))
    print('done')
    

if __name__ == "__main__":
    main()