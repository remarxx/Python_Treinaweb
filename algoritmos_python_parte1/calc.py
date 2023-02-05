import tkinter as tk

def calculate():
    try:
        first_number = float(first_number_entry.get())
        second_number = float(second_number_entry.get())
        if radio_var.get() == 1:
            result = first_number + second_number
        else:
            result = first_number - second_number
        result_label.config(text="Resultado: " + str(result))
    except ValueError:
        result_label.config(text="Entrada inválida")

root = tk.Tk()
root.title("Calculadora")

first_number_label = tk.Label(root, text="Primeiro número:", font=("Helvetica", 16))
first_number_label.grid(row=0, column=0, padx=10, pady=10)

first_number_entry = tk.Entry(root, font=("Helvetica", 16))
first_number_entry.grid(row=0, column=1, padx=10, pady=10)

second_number_label = tk.Label(root, text="Segundo número:", font=("Helvetica", 16))
second_number_label.grid(row=1, column=0, padx=10, pady=10)

second_number_entry = tk.Entry(root, font=("Helvetica", 16))
second_number_entry.grid(row=1, column=1, padx=10, pady=10)

radio_var = tk.IntVar()
addition_radio = tk.Radiobutton(root, text="Soma", variable=radio_var, value=1, font=("Helvetica", 16))
addition_radio.grid(row=2, column=0, padx=10, pady=10)

subtraction_radio = tk.Radiobutton(root, text="Subtração", variable=radio_var, value=2, font=("Helvetica", 16))
subtraction_radio.grid(row=2, column=1, padx=10, pady=10)

calculate_button = tk.Button(root, text="Calcular", command=calculate, font=("Helvetica", 16), bg="#3498DB", fg="white")
calculate_button.grid(row=3, column=0, columnspan=2, pady=10)

result_label = tk.Label(root, text="", font=("Helvetica", 16))
result_label.grid(row=4, column=0, columnspan=2, pady=10)

root.mainloop()
