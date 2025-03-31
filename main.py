from app.io.input import input_from_console, read_from_file_builtin, read_from_file_pandas
from app.io.output import output_to_console, write_to_file_builtin
import os
def main():
    os.makedirs('data', exist_ok=True)
    file = 'data/s.txt'
    csvh = 'data/s.csv'
    output_file = 'data/out.txt'
    #print("clown me")

    output_to_console("\nEnter smth")
    console_text = input_from_console()
    output_to_console("\nText from console")
    output_to_console(console_text)
    write_to_file_builtin(output_file, "Text from console\n" + console_text + "\n\n")

    output_to_console("\nReading from file-")
    file_text = read_from_file_builtin(file)
    output_to_console("\nText from file")
    output_to_console(file_text)
    with open(output_file, 'a', encoding='utf-8') as f:
        f.write("Text from file\n" + file_text + "\n\n")

    output_to_console("\n pandas ")
    try:
        df = read_from_file_pandas(csvh)
        
        # Output dataframe to console
        output_to_console("\n pandas")
        output_to_console(df)
        with open(output_file, 'a', encoding='utf-8') as f:
            f.write("pandas \n" + df.to_string() + "\n")
    except Exception as e:
        output_to_console(f" {e}")

if __name__ == "__main__":
    main()