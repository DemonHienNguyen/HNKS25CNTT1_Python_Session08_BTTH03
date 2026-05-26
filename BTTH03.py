""" 
    Input: 
        + Nhập lựa chọn của menu - Choose 
        + Chức năng 1:
            - Tên người gửi
            - Số điện thoại người gửi
            - Địa chỉ lấy hàng
            - Tên người nhận
            - Số điện thoại người nhận
            - Địa chỉ giao hàng
            - Ghi chú giao hàng
        + Chức năng 3:
            - Cho người dùng nhập số điện thoại 
        + Chức năng 4: 
            - Cho người dùng nhập từ khóa cần tìm
    Output:
        + Chức năng 1:
            hiện thong tin cần được định dạng lại
        + Chức năng 2:
            Hiển thị mã đơn hàng ban đầu
            Hiển thị mã đỡn hàng sau khi được chuẩn hóa
        + Chức năng 3:
            Hiển thị thông báo
                + Hợp lệ và không hợp lệ vì lý do gì ?
        + Chức năng 4:
            Hiển thị những từ khóa xuất hiện trong bài
            
    Đề xuất giải pháp:
        + Ta sẽ sử dụng vòng lặp while được sử dụng trong menu
        + Sử dụng match - case cho từng trường hợp của lựa chọn đó
        + NẾU NHẬP SAI DỮ LIỆU HOẶC NHẬP KHÁC MENU 
        => Thông báo không có chức năng đó và cho người dùng nhập lại
        + Còn lại các chức năng ta sử dụng String Method cũng như sử dụng 
        If Elif Else để xét trường hợp
    Thiết kế thuật toán:
        + Ta sẽ để người dùng nhập lựa chọn menu cần phải nhập
        + NẾU LỰA CHỌN MENU KHÔNG PHẢI LÀ SỐ HAY KHÁC CHỨC NĂNG
        = > THÔNG BÁO LỰA CHỌN KHÔNG HỢP LỆ VÀ YÊU CẦU NHẬP LẠ
        + Chức năng 1:
            cho người dùng nhập các giá trị như :
           - Tên người gửi
            - Số điện thoại người gửi
            - Địa chỉ lấy hàng
            - Tên người nhận
            - Số điện thoại người nhận
            - Địa chỉ giao hàng
            - Ghi chú giao hàng
        + Sau khi nhập xong sẽ hiển thị như sau:
            - Tên người gửi sau khi loại bỏ khoảng trắng đầu và cuối, viết hoa chữ cái đầu mỗi từ
            - Tên người nhận sau khi loại bỏ khoảng trắng đầu và cuối, viết hoa chữ cái đầu mỗi từ
            - Địa chỉ lấy hàng sau khi chuẩn hóa khoảng trắng
            - Địa chỉ giao hàng sau khi chuẩn hóa khoảng trắng
            - Ghi chú giao hàng sau khi loại bỏ khoảng trắng đầu và cuối
            - Độ dài ghi chú giao hàng
            - Số lượng từ trong ghi chú giao hàng
            - Ghi chú giao hàng dạng chữ thường
            - Ghi chú giao hàng dạng chữ hoa
        + Chức năng 2: Chuẩn hoắ tên tài khoản tik tok
            + sẽ hiển thị 
                - Tên mã đơn hàng ban đầu
                - Tên mã đơn hàng sau khi được chuẩn hóa
        + Chức năng 3: Kiểm tra
            + cho người dùng nhập một số điện thoại người gửi và người nhận
            có kiểm tra các trường như sau:
                    Số điện thoại không được rỗng
                    Số điện thoại chỉ được chứa chữ số
                    Số điện thoại phải có đúng 10 ký tự
                    Hệ thống chỉ hiển thị 3 số đầu và 2 số cuối
                    Các ký tự ở giữa được thay bằng dấu *
                    
            + chức năng 4: 
                Kiểm tra từ khóa đó có tồn tại trong mô tả hay không
                    + Có thì thay thế bằng từ khóa mới => Hiển thị mô tả sau khi đã được thay thế
                    => Hiển thị số lần khóa cần tìm xuát hiện trong mô tả
                    + Không thì thông pháp phù hợp cho người dùng
            + Chức năng 5:
                + Thông báo cho người dùng và kết thúc chương trình
"""
import time 
width = 48
has_input = False 
sale_total = ""
while True:
    try:
        choose = int(input(
        f"+================================================+\n"
        f"|{"HỆ THỐNG QUẢN LÝ NỘI DUNG ĐƠN HÀNG GRAB EXPRESS".center(width, " ")}|\n"
        f"+================================================+\n"
        f"|{"1. Nhập dữ liệu sản phẩm và xem báo cáo thống kê".ljust(width, " ")}|\n"
        f"|{"2. Chuẩn hóa mã đơn hàng".ljust(width, " ")}|\n"
        f"|{"3. Ẩn số điện thoại khách hàng".ljust(width, " ")}|\n"
        f"|{"4. Tìm kiếm và thay thé từ khóa trong ghi chú đơn hàng".ljust(width, " ")}|\n"
        f"|{"5. Thoát chương trình".ljust(width, " ")}|\n"
        f"+================================================+\n"
        f"{"> Mời bạn chọn chức năng (1-5): ".ljust(25, " ")}"    
        ))
    except:
        print("Dữ liệu không hợp lệ vui lòng nhập lại !")
        continue
    
    match choose:
        case 1:
            print()
            print("Nhập dữ liệu")
            while True:
                code_name = input("Vui lòng nhập mã đơn hàng: ")
                if(not code_name.strip()):
                    print("Lỗi ! mã đơn hàng không được trống")
                    continue 
                
                break
            while True:
                sender_name = input("Vui lòng nhập tên người gửi: ")
                if(not sender_name.strip()):
                    print("Lỗi ! Tên người gửi không được để trống")
                    continue 
                
                break
            
            while True:
                sender_phone_number = input("Vui lòng nhập số điện thoại người gửi: ")
                
                if(not sender_phone_number.strip()):
                    print("số điện thoại không được để trống !")
                    continue 
                    
                if(not sender_phone_number.isdigit()):
                    print("Số điện thoại không phải là số")
                    continue 
                
                if(len(sender_phone_number) != 10):
                    print("Số điện thoại chỉ được 10 KÝ TỰ")
                    continue 
                
                break 
            
            while True:
                pickup_address = input("Vui lòng nhập địa chỉ LẤY HÀNG của sản phẩm: ")
                if(not pickup_address.strip()):
                    print("Địa chỉ không được rỗng")
                    continue 
                break
            while True:
                recipient_name = input("Vui lòng nhập người nhập tên nhận dạng: ")
                if(not recipient_name.strip()):
                    print("Tên người nhận không được để trống")
                    continue
                break 
            
            while True:
                recipient_phone_number = input("Vui lòng nhập số điện thoại người nhận: ")
                
                if(not recipient_phone_number.strip()):
                    print("số điện thoại không được để trống !")
                    continue 
                    
                if(not recipient_phone_number.isdigit()):
                    print("Số điện thoại không phải là số")
                    continue 
                
                if(len(recipient_phone_number) != 10):
                    print("Số điện thoại chỉ được 10 KÝ TỰ")
                    continue 
                
                break
            
            while True:
                delivery_address = input("Vui lòng nhập người nhập Địa chỉ giao hàng: ")
                if(not delivery_address.strip()):
                    print("ĐỊA CHỈ không được để trống")
                    continue
                break 
            while True:
                delivery_notes = input("Nhập ghi chú đơn hàng: ")
                if(not delivery_notes.strip()):
                    print("GHI CHÚ không được để trống")
                    continue
                break
            number_of_letter = 0
            for i in delivery_notes:
                if(i.isalpha()):
                     number_of_letter += 1
            print()
            print(
                f"+================================================+\n"
                f"{"HỆ THỐNG ĐỊNH DẠNG".center(width, " ")} \n"
                f"+================================================+\n"
                f"{"Tên người gửi: ".ljust(width, " ")}{sender_name.strip().title()} \n"
                f"{"Tên người nhận: ".ljust(width, " ")}{recipient_name.strip().title()} \n"
                f"{"Địa chỉ lấy hàng: ".ljust(width, " ")} {pickup_address.strip()} \n"
                f"{"Địa chỉ giao hàng: ".ljust(width, " ")} {delivery_address.strip().capitalize()} \n"
                f"{"Ghi chú giao hàng: ".ljust(width, " ")} {delivery_notes.strip().capitalize()} \n"
                f"{"Đọ dài ghi chú giao hàng: ".ljust(width, " ")} {len(delivery_notes.strip())} \n"
                f"{"Số lượng từ trong ghi chú giao hàng: ".ljust(width, " ")} {number_of_letter} \n"
                f"{"Ghi chú giao hàng được chuyển toàn bộ sang chữ thường: ".ljust(width, " ")} {delivery_notes.strip().lower()} \n"
                f"{"Ghi chú giao hàng được chuyển toàn bộ sang chữ in hoa: ".ljust(width, " ")} {delivery_notes.strip().upper()} \n"
                
            )
            has_input = True
            print()
        case 2:
            if(not has_input):
                print("Bạn chưa nhập tên tài khoản")
            else:
                print()
                print(
                    f"Tên cửa hàng lúc đầu: {code_name} \n"
                    f"Tên cửa hàng sau khi được chuẩn hóa: {f"GRAB-{code_name.strip().upper().replace(" ", "-")}" if("GRAB-" not in code_name) else  f"{code_name.strip().replace(" ", "-")}"} \n"
                    )
                print()
                
        case 3:
            if(not has_input):
                print("Bạn chưa nhập ở chức năng 1")
            else:
                print()
                blind = "*"*5
                print("Output")
                print(
                    f"SĐT người gửi: {sender_phone_number[0:3] + blind + sender_phone_number[-2:]} \n"
                    f"SĐT người nhận: {recipient_phone_number[0:3] + blind + recipient_phone_number[-2:]} \n"
                )
                print()
        case 4:
            if(not has_input):
                print("Bạn chưa nhập ở chức năng  1")
            else:
                print()
                print("=== HỆ THỐNG TÌM THEO TỪ KHÓA ===")
                print()
                print(f"Nội dung cũ: {delivery_notes}")
                print()
                key_word = input("Vui lòng nhập từ khóa cân tìm: ")
                if(delivery_notes.count(key_word) == 0):
                    print(f"Không có từ khóa {key_word} ở trong mô tả video")
                else:

                    new_key_input = input("Vui lòng nhập từ khóa mới: ")
                    print(f"Số lần {key_word} xuất hiện trong mô tả video là: {delivery_notes.count(key_word)}")
                    delivery_notes = delivery_notes.replace(key_word, new_key_input)
                    print(f"Đã thay thế {key_word} => {new_key_input}")
                    
                    print()
                    print(f"Nội dung mới: {delivery_notes}")
                    print()
                print()
            
        case 5:
            message_end = "Cảm ơn vì đã sử dụng chương trình"
            for letter in message_end:
                print(letter, end = "", flush=True)
                time.sleep(0.06)
            break
        case _:
            print("Lựa chọn bạn không hợp lệ :> !")
            
    
    
