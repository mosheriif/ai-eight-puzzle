class validator():
    def convert_to_list(input_string):
        return [int(digit) for digit in input_string]

    def count_inversions(arr):
        inv_count = 0
        empty_value = 0
        for i in range(9):
            for j in range(i + 1, 9):
                if arr[j] != empty_value and arr[i] != empty_value and arr[i] > arr[j]:
                    inv_count += 1
                    
        return inv_count
    
    def check_digits(input_string):
        allowed_digits = set('012345678')
        
        for char in input_string:
            if char not in allowed_digits:
                return (False, "INVALID INPUT - Only digits from 0 to 8 are allowed")
        
        if len(set(input_string)) < len(input_string):
            return (False, "INVALID INPUT - Repeated digits")
        
        return (True, "valid")

    def isSolvable(puzzle):
        
        if len(puzzle) < 9:
            return (False, "INVALID INPUT - Input is too short")
        elif len(puzzle) > 9:
            return (False, "INVALID INPUT - Input is too long")
        
        valid, comment = validator.check_digits(puzzle)
        if not puzzle.isdigit():
            return (False, "INVALID INPUT - Letters and special characters are not allowed")
        elif not valid:
            return (valid, comment)
        
        board = validator.convert_to_list(puzzle)
        inversions_count = validator.count_inversions(board)
        if inversions_count % 2 == 0:
            return (True, "solvable")
        else:
            return (False, "INVALID INPUT - Unsolvable Board")