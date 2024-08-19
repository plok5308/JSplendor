from jsplendor.game import Game

def main():
    game = Game()
    episode_log = []
    number_of_games = 10
    step_n = 100

    for i in range(number_of_games):
        game.reset()
        for j in range(step_n):
            is_done = game.run_step()
            if is_done:
                episode_log.append(j+1)
                break

    print(episode_log)
    print('done')
    

if __name__ == "__main__":
    main()