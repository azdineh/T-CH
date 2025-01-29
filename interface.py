import tkinter as tk
from tkinter import ttk
import random

class NumberGame:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("T-CH")
        self.root.geometry("800x900")
        self.root.configure(bg="#202A37")  # Bleu foncé élégant
        
        # Variables
        self.digits = [""] * 4
        self.selected_box = None
        
        self.setup_ui()
        
    def setup_ui(self):
        # Style personnalisé moderne
        style = ttk.Style()
        style.configure("Game.TButton", 
                       padding=20,
                       font=('Montserrat', 18, 'bold'),
                       background="#4CAF50",
                       foreground="white")
        
        # Titre stylisé
        title_frame = tk.Frame(self.root, bg="#202A37")
        title_frame.pack(pady=30)
        
        # "T" en grand
        tk.Label(title_frame, 
                text="T", 
                font=('Montserrat', 50, 'bold'),
                fg="#00BCD4",  # Bleu clair brillant
                bg="#202A37").pack(side=tk.LEFT, padx=5)
        
        # Séparateur stylisé
        tk.Label(title_frame,
                text="-",
                font=('Montserrat', 50, 'bold'),
                fg="#FFD700",  # Or
                bg="#202A37").pack(side=tk.LEFT, padx=5)
        
        # "CH" en grand
        tk.Label(title_frame,
                text="CH",
                font=('Montserrat', 50, 'bold'),
                fg="#00BCD4",  # Bleu clair brillant
                bg="#202A37").pack(side=tk.LEFT, padx=5)
        
        # Cadre pour les 4 boîtes avec effet de profondeur
        self.boxes_frame = tk.Frame(self.root, bg="#202A37", pady=20)
        self.boxes_frame.pack(pady=40)
        
        # Création des 4 boîtes avec style moderne
        self.digit_boxes = []
        for i in range(4):
            # Créer un cadre pour l'effet de profondeur
            box_frame = tk.Frame(self.boxes_frame, bg="#202A37", padx=5, pady=5)
            box_frame.pack(side=tk.LEFT, padx=15)
            
            # Boîte principale
            box = tk.Label(box_frame,
                          width=4,
                          height=2,
                          relief="flat",
                          font=('Montserrat', 28, 'bold'),
                          bg="#2E3B4E",  # Bleu foncé pour le fond
                          fg="#FFFFFF",   # Texte blanc
                          borderwidth=0)
            box.pack(padx=2, pady=2)
            box.bind('<Button-1>', lambda e, i=i: self.select_box(i))
            self.digit_boxes.append(box)
        
        # Cadre pour les boutons numériques avec style moderne
        buttons_frame = tk.Frame(self.root, bg="#202A37")
        buttons_frame.pack(pady=40)
        
        # Création des boutons numériques stylisés
        for i in range(10):
            btn = tk.Button(buttons_frame,
                          text=str(i),
                          font=('Montserrat', 18, 'bold'),
                          fg='white',
                          bg='#364559',  # Bleu gris élégant
                          activebackground='#4A5F7A',  # Plus clair au survol
                          width=3,
                          height=1,
                          relief='flat',
                          command=lambda x=i: self.add_digit(x))
            btn.grid(row=i//3, column=i%3, padx=8, pady=8)
            
            # Effet hover
            btn.bind('<Enter>', lambda e, b=btn: b.configure(bg='#4A5F7A'))
            btn.bind('<Leave>', lambda e, b=btn: b.configure(bg='#364559'))
        
        # Bouton OK stylisé
        ok_btn = tk.Button(buttons_frame,
                          text="OK",
                          font=('Montserrat', 18, 'bold'),
                          fg='white',
                          bg='#00BCD4',  # Bleu clair
                          activebackground='#00ACC1',
                          width=3,
                          height=1,
                          relief='flat',
                          command=self.validate_number)
        ok_btn.grid(row=3, column=1, padx=8, pady=8)
        
        # Effet hover pour le bouton OK
        ok_btn.bind('<Enter>', lambda e: ok_btn.configure(bg='#00ACC1'))
        ok_btn.bind('<Leave>', lambda e: ok_btn.configure(bg='#00BCD4'))
        
    def select_box(self, index):
        # Réinitialiser l'apparence de toutes les boîtes
        for box in self.digit_boxes:
            box.configure(bg="#2E3B4E")
            
        # Sélectionner la nouvelle boîte avec animation
        self.selected_box = index
        self.animate_selection(self.digit_boxes[index])
        
        # Effacer uniquement le chiffre sélectionné
        self.digits[index] = ""
        self.digit_boxes[index].configure(text="")
        
    def animate_selection(self, widget):
        # Séquence d'animation plus fluide
        def animation_step(step=0):
            colors = ['#3F51B5', '#5C6BC0', '#7986CB', '#5C6BC0', '#3F51B5', '#2E3B4E']
            if step < len(colors):
                widget.configure(bg=colors[step])
                self.root.after(50, lambda: animation_step(step + 1))
        
        animation_step()
        
    def add_digit(self, digit):
        if self.selected_box is not None:
            if self.selected_box == 0 and digit == 0:
                return
                
            if str(digit) not in self.digits:
                self.digits[self.selected_box] = str(digit)
                self.animate_addition(self.digit_boxes[self.selected_box], str(digit))
                
    def animate_addition(self, widget, digit):
        # Animation d'apparition du chiffre
        def fade_in(opacity=0):
            if opacity <= 1:
                widget.configure(fg=f'#{int(opacity * 255):02x}FFFFFF')
                self.root.after(5, lambda: fade_in(opacity + 0.1))
            else:
                widget.configure(fg='#FFFFFF')
                
        widget.configure(text=digit, fg='#202A37')
        fade_in()
        
    def validate_number(self):
        if "" not in self.digits:
            number = "".join(self.digits)
            # Animation de validation
            for box in self.digit_boxes:
                box.configure(bg="#4CAF50")  # Vert de succès
            self.root.after(500, lambda: [box.configure(bg="#2E3B4E") for box in self.digit_boxes])
            print(f"Nombre validé: {number}")
        
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    game = NumberGame()
    game.run()