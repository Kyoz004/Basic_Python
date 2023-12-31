import random
import time

# Hàm sinh số ngẫu nhiên từ 1 đến 100
def generate_random_number():
    return random.randint(1, 100)

# Hàm tính thời gian đã trôi qua từ thời điểm bắt đầu
def calculate_time_taken(start_time):
    end_time = time.time()
    return int(end_time - start_time)

# Hàm chơi trò chơi đoán số
def play_game():
    # Tạo một danh sách các số cho phép từ 1 đến 100
    allowed_numbers = list(range(1, 101))
    player = 0
    count = 0
    computer_guess = generate_random_number()
    start_time = time.time()

    while player != computer_guess:
        try:
            player = int(input("Nhập vào số của bạn (1-100): "))  # Nhập số từ người chơi
            count += 1
            if player not in allowed_numbers:
                print("Số của bạn không nằm trong khoảng quy định!!")  # Kiểm tra sự hợp lệ của số nhập vào
            elif count > 6:
                print('Hết lượt đoán!')
                print(f'Số của máy là: {computer_guess}')
                break
            elif player < computer_guess:
                print("THUA")  # Hiển thị kết quả so sánh và thông báo
            elif player > computer_guess:
                print("Thắng")
                print(f'Số của máy là: {computer_guess}')
                break
        except ValueError:
            print("Sai kiểu dữ liệu nhập vào!")  # Xử lý ngoại lệ nếu người chơi nhập sai kiểu dữ liệu

    time_taken = calculate_time_taken(start_time)  # Tính thời gian đã trôi qua
    print(f'Thời gian người chơi đoán số là {time_taken} giây!')  # Hiển thị thời gian người chơi đã đoán
# Bắt đầu chơi trò chơi
play_game()