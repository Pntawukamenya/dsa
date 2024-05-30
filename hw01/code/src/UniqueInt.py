#!/usr/bin/python3
import os

def is_integer(value):
    try:
        int(value)
        return True
    except Exception:
        return False
    

input_dir = os.getcwd()+'\hw01\sample_inputs'
output_dir = os.getcwd()+'\hw01\sample_results'

# Iterate through files in the target directory
for filename in os.listdir(input_dir):
    file_path = os.path.join(input_dir, filename)
    output_path = os.path.join(output_dir, f"{filename}_results.txt")
    
    with(open(file_path, 'r') as file):
        file_lines = file.readlines()
        my_dict = {}
        unique = []  
        for num in file_lines:
            num = num.strip()
            if not is_integer(num):
                continue

            if int(num) not in range(-1023, 1024):
                continue

            if num in my_dict.keys():
                my_dict[num] += 1
            else:    
                my_dict[num] = 1

        print(my_dict)        

        for key in my_dict.keys():
            if my_dict[key] == 1:
                unique.append(key)

<<<<<<< HEAD
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for input_filename in os.listdir(input_dir):
        if input_filename.endswith('.txt'):
            input_file_path = os.path.join(input_dir, input_filename)
            output_file_path = os.path.join(output_dir, f"{input_filename}_result.txt")
            unique_int_processor = UniqueInt()
            unique_int_processor.process_file(input_file_path, output_file_path)

if __name__ == "__main__":
    main()
=======
        with(open(output_path, 'w') as output_file):
            for num in unique:
                output_file.write(num)
                output_file.write('\n')
>>>>>>> ad38b76a6d0f1661219c068b5441e3136533f94b
