pen_num = prisoner
        for _ in range(50):
            open_num = boxes[open_num]
            if open_num == prisoner:
                break
        else:
            return 0
    return 1
