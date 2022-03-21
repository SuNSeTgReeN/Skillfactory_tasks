board = list(range(1, 10))


def draw_board(board):
    print("-------------")
    for i in range(3):
        print("|", board[0 + i * 3], "|", board[1 + i * 3], "|", board[2 + i * 3], "|")
        print("-------------")


def users_input(player_token):
    while True:
        player_answer = input("Куда поставим " + player_token + "? ")
        if not (player_answer.isdigit()):
            print("Ошибка! Введите числа, без пробелов.")
            continue
        player_answer = int(player_answer)
        if 1 <= player_answer <= 9:
            if str(board[player_answer - 1]) not in "XO":
                board[player_answer - 1] = player_token
            else:
                print("Эта клеточка уже занята")
                continue
        else:
            print("Ошибка! Введите число от 1 до 9")
            continue
        break
    return player_answer


def check_win(board):
    win_coord = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for each in win_coord:
        if board[each[0]] == board[each[1]] == board[each[2]]:
            return True
    return False


def main(board):
    count = 0
    win = False
    while not win:
        draw_board(board)
        if count % 2 == 0:
            player_token = "X"
        else:
            player_token = "O"
        count += 1
        if count > 4:
            tmp = check_win(board)
            if tmp:
                print("Выиграл!")
                draw_board(board)
                win = True
                break
        if count == 9:
            print("Ничья")
            break
        users_input(player_token)


main(board)
