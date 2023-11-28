import tkinter as tk
from tkinter import messagebox
import os
import datetime

class TabunganApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplikasi Tabungan")
        self.root.geometry("400x350")
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.root.configure(bg="lightblue")

        self.username = ""
        self.password = ""
        self.logged_in = False
        self.is_registering = False

        self.user_data_directory = "user_data"
        self.deposit_file = "deposits.txt"
        self.history_file = "history.txt"
        self.users_file = "users.txt"
        self.users = {}

        self.login_label = tk.Label(root, text="Masukkan Username dan Password", bg="lightblue", font=("Helvetica", 14))
        self.login_label.pack(pady=10)

        self.username_label = tk.Label(root, text="Username:", bg="lightblue", font=("Helvetica", 12))
        self.username_label.pack()

        self.username_entry = tk.Entry(root, font=("Helvetica", 12))
        self.username_entry.pack()

        self.password_label = tk.Label(root, text="Password:", bg="lightblue", font=("Helvetica", 12))
        self.password_label.pack()

        self.password_entry = tk.Entry(root, show="*", font=("Helvetica", 12))
        self.password_entry.pack()

        self.login_button_text = "Login" if not self.is_registering else "Registrasi"
        self.login_button = tk.Button(root, text=self.login_button_text, command=self.login, bg="green", fg="white", font=("Helvetica", 12))
        self.login_button.pack(pady=10)

        self.register_label = tk.Label(root, text="Atau, registrasi baru:", bg="lightblue", font=("Helvetica", 14))
        self.register_label.pack(pady=10)

        self.switch_button_text = "Registrasi" if not self.is_registering else "Login"
        self.switch_button = tk.Button(root, text=self.switch_button_text, command=self.register, bg="blue", fg="white", font=("Helvetica", 12))
        self.switch_button.pack(pady=10)

        self.welcome_label = tk.Label(root, text="", bg="lightblue", font=("Helvetica", 14))
        self.saldo_label = None
        self.deposit_button = None
        self.tarik_button = None
        self.history_button = None
        self.clear_history_button = None

        self.saldo = 0
        self.history = []

        self.load_deposits()
        self.load_users()

        self.logout_button = None

    def toggle_registration(self):
        if self.is_registering:
            self.register_label.config(text="Atau, registrasi baru:")
            self.login_button.config(text="Login")
            self.switch_button.config(text="Registrasi")
            self.switch_button_text = "Registrasi"
            self.is_registering = False
        else:
            self.register_label.config(text="Buat Username dan Password Baru:")
            self.login_button.config(text="Registrasi")
            self.switch_button.config(text="Login")
            self.switch_button_text = "Login"
            self.is_registering = True

        self.update_interface()

    def login(self):
        if self.is_registering:
            self.register()
        else:
            username = self.username_entry.get()
            password = self.password_entry.get()

            if username in self.users and self.users[username] == password:
                self.logged_in = True
                self.username = username
                self.load_deposits()
                self.load_history(self.username)
                self.update_interface()
                self.logout_button = tk.Button(self.root, text="Logout", command=self.logout, bg="red", fg="white", font=("Helvetica", 12))
                self.logout_button.pack(pady=5)
            else:
                messagebox.showerror("Error", "Login Gagal. Coba lagi.")

    def register(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if not username or not password:
            messagebox.showerror("Error", "Username dan password harus diisi.")
        else:
            self.users[username] = password
            self.saldo = 0
            self.save_users()
            self.save_deposits()
            self.is_registering = False
            self.toggle_registration()
            messagebox.showinfo("Info", "Registrasi berhasil. Silakan login.")

    def logout(self):
        self.logged_in = False
        self.username = ""
        self.saldo = 0
        self.history = []

        if self.logout_button is not None:
            self.logout_button.destroy()

        self.update_interface(login_page=True)

    def update_interface(self, login_page=False):
        if login_page:
            if hasattr(self, "saldo_label"):
                self.saldo_label.destroy()
            if hasattr(self, "deposit_button"):
                self.deposit_button.destroy()
            if hasattr(self, "tarik_button"):
                self.tarik_button.destroy()
            if hasattr(self, "history_button"):
                self.history_button.destroy()
            if hasattr(self, "clear_history_button"):
                self.clear_history_button.destroy()

            self.login_label.config(text="Masukkan Username dan Password")
            self.username_label.config(text="Username:")
            self.login_button.config(text=self.login_button_text)
            self.switch_button.config(text=self.switch_button_text)
            self.username = ""
            self.welcome_label.config(text="", fg="black")
            self.welcome_label.pack(pady=10)
            self.saldo_label = None
            self.deposit_button = None
            self.tarik_button = None
            self.history_button = None
            self.clear_history_button = None
        else:
            if hasattr(self, "login_label"):
                self.login_label.destroy()
            if hasattr(self, "username_label"):
                self.username_label.destroy()
            if hasattr(self, "username_entry"):
                self.username_entry.destroy()
            if hasattr(self, "password_label"):
                self.password_label.destroy()
            if hasattr(self, "password_entry"):
                self.password_entry.destroy()
            if hasattr(self, "login_button"):
                self.login_button.destroy()
            if hasattr(self, "register_label"):
                self.register_label.destroy()
            if hasattr(self, "switch_button"):
                self.switch_button.destroy()

            self.welcome_label.config(text=f"Selamat datang, {self.username}!", fg="green")
            self.welcome_label.pack(pady=10)

            self.saldo_label = tk.Label(self.root, text=f"Saldo saat ini: Rp {self.saldo:.2f}", bg="lightblue", font=("Helvetica", 14))
            self.saldo_label.pack(pady=10)

            self.deposit_button = tk.Button(self.root, text="Tabung", command=self.deposit, bg="green", fg="white", font=("Helvetica", 12))
            self.deposit_button.pack(pady=5)

            self.tarik_button = tk.Button(self.root, text="Tarik", command=self.tarik, bg="red", fg="white", font=("Helvetica", 12))
            self.tarik_button.pack(pady=5)

            self.history_button = tk.Button(self.root, text="Lihat Riwayat", command=self.show_history, bg="blue", fg="white", font=("Helvetica", 12))
            self.history_button.pack(pady=5)

            self.clear_history_button = tk.Button(self.root, text="Hapus Riwayat", command=self.clear_history, bg="red", fg="white", font=("Helvetica", 12))
            self.clear_history_button.pack(pady=5)

    def deposit(self):
        deposit_window = tk.Toplevel(self.root)
        deposit_window.title("Tabung")
        deposit_window.geometry("250x100")

        deposit_label = tk.Label(deposit_window, text="Jumlah Tabungan (Rp):", font=("Helvetica", 12))
        deposit_label.pack()

        deposit_entry = tk.Entry(deposit_window, font=("Helvetica", 12))
        deposit_entry.pack()

        deposit_button = tk.Button(deposit_window, text="Simpan", command=lambda: self.process_deposit(deposit_entry.get()), bg="green", fg="white", font=("Helvetica", 12))
        deposit_button.pack()

    def process_deposit(self, amount):
        try:
            amount = float(amount)
            if amount > 0:
                self.saldo += amount
                self.history.append(f"Tabung: +Rp {amount:.2f} ({datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')})")
                self.saldo_label.config(text=f"Saldo saat ini: Rp {self.saldo:.2f}")
                self.save_deposits()
                self.save_history(self.username)
                messagebox.showinfo("Info", f"Tabung berhasil: +Rp {amount:.2f}")
            else:
                messagebox.showerror("Error", "Jumlah Tabungan tidak valid.")
        except ValueError:
            messagebox.showerror("Error", "Jumlah Tabungan tidak valid.")

    def tarik(self):
        tarik_window = tk.Toplevel(self.root)
        tarik_window.title("Tarik")
        tarik_window.geometry("250x100")

        tarik_label = tk.Label(tarik_window, text="Jumlah Penarikan (Rp):", font=("Helvetica", 12))
        tarik_label.pack()

        tarik_entry = tk.Entry(tarik_window, font=("Helvetica", 12))
        tarik_entry.pack()

        tarik_button = tk.Button(tarik_window, text="Tarik", command=lambda: self.process_withdraw(tarik_entry.get()), bg="red", fg="white", font=("Helvetica", 12))
        tarik_button.pack()

    def process_withdraw(self, amount):
        try:
            amount = float(amount)
            if amount > 0 and amount <= self.saldo:
                self.saldo -= amount
                self.history.append(f"Penarikan: -Rp {amount:.2f} ({datetime.datetime.now().strftime('%Y-%m-%d %H:M:S')})")
                self.saldo_label.config(text=f"Saldo saat ini: Rp {self.saldo:.2f}")
                self.save_deposits()
                self.save_history(self.username)
                messagebox.showinfo("Info", f"Penarikan berhasil: -Rp {amount:.2f}")
            else:
                messagebox.showerror("Error", "Jumlah penarikan tidak valid atau saldo tidak mencukupi.")
        except ValueError:
            messagebox.showerror("Error", "Jumlah penarikan tidak valid.")

    def show_history(self):
        history_window = tk.Toplevel(self.root)
        history_window.title("Riwayat Transaksi")
        history_window.geometry("400x300")

        history_text = tk.Text(history_window, font=("Helvetica", 12))
        history_text.pack()

        clear_history_button = tk.Button(history_window, text="Hapus Riwayat", command=self.clear_history, bg="red", fg="white", font=("Helvetica", 12))
        clear_history_button.pack()

        history = self.load_history(self.username)
        for entry in history:
            history_text.insert(tk.END, entry + "\n")

    def clear_history(self):
        user_directory = self.create_user_directory(self.username)
        history_file = os.path.join(user_directory, self.history_file)
        try:
            os.remove(history_file)
            self.history = []
            self.save_history(self.username)
            messagebox.showinfo("Info", "Riwayat transaksi telah dihapus.")
        except FileNotFoundError:
            messagebox.showerror("Error", "Riwayat transaksi tidak ditemukan.")

    def load_deposits(self):
        try:
            user_directory = self.create_user_directory(self.username)
            deposit_file = os.path.join(user_directory, self.deposit_file)
            with open(deposit_file, "r") as file:
                self.saldo = float(file.read())
        except (FileNotFoundError, ValueError):
            self.saldo = 0

    def save_deposits(self):
        user_directory = self.create_user_directory(self.username)
        deposit_file = os.path.join(user_directory, self.deposit_file)
        with open(deposit_file, "w") as file:
            file.write(str(self.saldo))

    def load_history(self, username):
        try:
            user_directory = self.create_user_directory(username)
            history_file = os.path.join(user_directory, self.history_file)
            with open(history_file, "r") as file:
                history = file.read().splitlines()
            return history
        except FileNotFoundError:
            return []

    def save_history(self, username):
        user_directory = self.create_user_directory(username)
        history_file = os.path.join(user_directory, self.history_file)
        with open(history_file, "w") as file:
            file.write("\n".join(self.history))

    def load_users(self):
        try:
            with open(self.users_file, "r") as file:
                lines = file.read().splitlines()
                for line in lines:
                    username, password = line.split(":")
                    self.users[username] = password
        except (FileNotFoundError, ValueError, IndexError):
            self.users = {}

    def save_users(self):
        with open(self.users_file, "w") as file:
            for username, password in self.users.items():
                file.write(f"{username}:{password}\n")

    def create_user_directory(self, username):
        user_directory = os.path.join(self.user_data_directory, username)
        os.makedirs(user_directory, exist_ok=True)
        return user_directory

    def on_closing(self):
        if self.logged_in:
            self.save_deposits()
            self.save_history(self.username)
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = TabunganApp(root)
    root.mainloop()
