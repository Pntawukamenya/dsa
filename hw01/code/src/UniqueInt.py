import os

class UniqueInt:
    def __init__(self):
        self.min_value = -1023
        self.max_value = 1023
        self.range_size = self.max_value - self.min_value + 1
        self.seen_integers = [False] * self.range_size
    
    def _index(self, value):
        return value - self.min_value
    
    def read_next_item_from_file(self, inputFileStream):
        while True:
            line = inputFileStream.readline()
            if not line:
                return None
            line = line.strip()
            if line == "":
                continue
            parts = line.split()
            if len(parts) != 1:
                continue
            try:
                value = int(parts[0])
                if self.min_value <= value <= self.max_value:
                    return value
            except ValueError:
                continue

    def process_file(self, inputFilePath, outputFilePath):
        try:
            with open(inputFilePath, 'r') as inputFileStream:
                while True:
                    value = self.read_next_item_from_file(inputFileStream)
                    if value is None:
                        break
                    index = self._index(value)
                    self.seen_integers[index] = True
        except IOError as e:
            print(f"Error reading file {inputFilePath}: {e}")
            return

        unique_integers = []
        for i in range(self.range_size):
            if self.seen_integers[i]:
                unique_integers.append(self.min_value + i)

        try:
            with open(outputFilePath, 'w') as outputFileStream:
                for value in unique_integers:
                    outputFileStream.write(f"{value}\n")
        except IOError as e:
            print(f"Error writing file {outputFilePath}: {e}")

def main():
    input_dir = '/dsa/hw01/sample_inputs/'
    output_dir = '/dsa/hw01/sample_results/'

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