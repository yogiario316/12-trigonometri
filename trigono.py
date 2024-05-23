import math
import ctypes
import sys

def run_as_admin():
    if sys.platform == 'win32':
        try:
            if ctypes.windll.shell32.IsUserAnAdmin():
                print("Anda sudah menjalankan program sebagai administrator.")
            else:
                ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
                sys.exit()
        except Exception as e:
            print(f"Gagal meminta izin administrator: {e}")

def menu():
    print("\nPilih operasi trigonometri:")
    print("1. Sin")
    print("2. Cos")
    print("3. Tan")
    print("4. Konversi Derajat ke Radian")
    print("5. Konversi Radian ke Derajat")
    print("6. Masukkan soal trigonometri")
    print("7. Keluar")

def calculate_sine(angle, is_degree):
    if is_degree:
        angle = math.radians(angle)
    return math.sin(angle)

def calculate_cosine(angle, is_degree):
    if is_degree:
        angle = math.radians(angle)
    return math.cos(angle)

def calculate_tangent(angle, is_degree):
    if is_degree:
        angle = math.radians(angle)
    return math.tan(angle)

def degree_to_radian(angle):
    return math.radians(angle)

def radian_to_degree(angle):
    return math.degrees(angle)

def solve_trigonometry_problem(problem):
    try:
        if 'sin' in problem:
            angle = float(problem.split('sin(')[1].split(')')[0])
            return calculate_sine(angle, True), f"Menggunakan formula sin({angle}) = hasil"
        elif 'cos' in problem:
            angle = float(problem.split('cos(')[1].split(')')[0])
            return calculate_cosine(angle, True), f"Menggunakan formula cos({angle}) = hasil"
        elif 'tan' in problem:
            angle = float(problem.split('tan(')[1].split(')')[0])
            return calculate_tangent(angle, True), f"Menggunakan formula tan({angle}) = hasil"
        else:
            return "Soal tidak dikenali", ""
    except Exception as e:
        return f"Error: {e}", ""

def how_to_use():
    print("=== Cara Menggunakan Kalkulator Trigonometri ===")
    print("1. Pilih operasi trigonometri yang ingin Anda hitung.")
    print("2. Ikuti petunjuk untuk memasukkan sudut.")
    print("3. Jika Anda memilih 'Masukkan soal trigonometri', masukkan soal trigonometri dalam format yang benar.")
    print("4. Hasil perhitungan akan ditampilkan beserta cara menghitungnya.")
    print("5. Anda dapat memilih untuk menghitung lagi atau keluar dari kalkulator.")

def main():
    run_as_admin()

    print("=== Kalkulator Sederhana Trigonometri oleh Yogi Ario ===")
    while True:
        how_to_use()
        menu()
        choice = input("Masukkan pilihan (1/2/3/4/5/6/7): ")

        if choice == '1':
            angle = float(input("Masukkan sudut: "))
            is_degree = input("Apakah sudut dalam derajat? (y/n): ").lower() == 'y'
            result, calculation_method = calculate_sine(angle, is_degree), f"Menggunakan formula sin({angle}) = hasil"
            print(f"Sinus dari sudut tersebut adalah: {result}")
            print(f"Cara menghitung: {calculation_method}")
        
        elif choice == '2':
            angle = float(input("Masukkan sudut: "))
            is_degree = input("Apakah sudut dalam derajat? (y/n): ").lower() == 'y'
            result, calculation_method = calculate_cosine(angle, is_degree), f"Menggunakan formula cos({angle}) = hasil"
            print(f"Kosinus dari sudut tersebut adalah: {result}")
            print(f"Cara menghitung: {calculation_method}")

        elif choice == '3':
            angle = float(input("Masukkan sudut: "))
            is_degree = input("Apakah sudut dalam derajat? (y/n): ").lower() == 'y'
            result, calculation_method = calculate_tangent(angle, is_degree), f"Menggunakan formula tan({angle}) = hasil"
            print(f"Tangen dari sudut tersebut adalah: {result}")
            print(f"Cara menghitung: {calculation_method}")

        elif choice == '4':
            angle = float(input("Masukkan sudut dalam derajat: "))
            result, calculation_method = degree_to_radian(angle), f"Menggunakan formula radian = derajat * pi / 180"
            print(f"{angle} derajat setara dengan {result} radian")
            print(f"Cara menghitung: {calculation_method}")

        elif choice == '5':
            angle = float(input("Masukkan sudut dalam radian: "))
            result, calculation_method = radian_to_degree(angle), f"Menggunakan formula derajat = radian * 180 / pi"
            print(f"{angle} radian setara dengan {result} derajat")
            print(f"Cara menghitung: {calculation_method}")

        elif choice == '6':
            problem = input("Masukkan soal trigonometri (contoh: sin(30), cos(45), tan(60)): ")
            result, calculation_method = solve_trigonometry_problem(problem)
            print(f"Hasil dari {problem} adalah: {result}")
            print(f"Cara menghitung: {calculation_method}")

        elif choice == '7':
            print("Terima kasih telah menggunakan kalkulator ini.")
            break

        else:
            print("Pilihan tidak valid, silakan coba lagi.")

        next_calculation = input("\nTekan 1 untuk menghitung lagi atau enter untuk keluar: ")
        if next_calculation != '1':
            break

if __name__ == "__main__":
    main()
