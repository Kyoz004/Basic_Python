import random

def play_game():
    # Danh sách các lựa chọn
    choices = ['bao', 'búa', 'kéo']
    # Khởi tạo điểm số cho người chơi và máy tính
    player_score = 0
    computer_score = 0
    # Vòng lặp chơi game
    while True:
        # Nhập lựa chọn của người chơi
        player_choice = input('Mời bạn nhập kéo, búa, bao: ')
        # Kiểm tra tính hợp lệ của lựa chọn
        if player_choice in choices:
            # Tạo lựa chọn cho máy
            computer_choice = random.choice(choices)
            print('Máy ra:', computer_choice)
            print('Bạn ra:', player_choice)
            print('---KẾT QUẢ---')
            # Xác định người chiến thắng trong vòng đấu
            if player_choice == computer_choice:
                print('Hòa')
            elif (player_choice == 'bao' and computer_choice == 'búa') or (player_choice == 'búa' and computer_choice == 'kéo') or (player_choice == 'kéo' and computer_choice == 'bao'):
                print('Bạn thắng')
                player_score += 1
            else:
                print('Bạn thua')
                computer_score += 1
            # Hiển thị điểm số hiện tại
            print(f'Điểm số hiện tại: Bạn {player_score} - Máy {computer_score}')
            # Yêu cầu chơi vòng đấu tiếp theo
            play_again = input('Bạn có muốn chơi tiếp không? (y/n): ')
            if play_again.lower() != 'y':
                break
        else:
            print('Bạn phải nhập kéo, búa hoặc bao')
# Bắt đầu chơi game
play_game()