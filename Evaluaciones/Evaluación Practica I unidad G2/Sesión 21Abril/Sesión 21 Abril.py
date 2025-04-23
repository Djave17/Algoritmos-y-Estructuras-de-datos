class Track:
    def __init__(self, title, artist, next_=None):
        self.title = title
        self.artist = artist
        self.next = next_

    def __repr__(self):
        return f"{self.title} – {self.artist}"

class Playlist:
    def __init__(self):
        self.head = None        # 1. referencia al primer tema
        self.tail = None        # 2. apuntador opcional al último (inserción O(1))

    # Añadir al final (como “Agregar a la cola” en Spotify)
    def enqueue(self, title, artist):
        new_track = Track(title, artist)
        if not self.head:       # lista vacía
            self.head = self.tail = new_track
        else:
            self.tail.next = new_track
            self.tail = new_track

    # “Siguiente canción”
    def skip(self):
        if self.head:
            print(f"▶ Reproduciendo: {self.head}")
            self.head = self.head.next
            if self.head is None:        # llegamos al final
                self.tail = None
        else:
            print("La playlist terminó 🎵")

    # Recorrido (visión de toda la cola)
    def show(self):
        cur = self.head
        idx = 1
        while cur:
            print(f"{idx}. {cur}")
            cur = cur.next
            idx += 1
        if idx == 1:
            print("(vacía)")

# --- Construimos la playlist ---
pl = Playlist()
pl.enqueue("Feel Good Inc.", "Gorillaz")
pl.enqueue("Crimen", "Gustavo Cerati")
pl.enqueue("Te para tres", "Soda Stereo")
pl.enqueue("Overcompesate", "Twenty One Pilots")
pl.enqueue("The Less I Know the Better", "Tame Impala")
pl.enqueue("Take on Me", "A-ha")
pl.enqueue("Radioactive", "Imagine Dragons")
pl.enqueue("Seven Nation Army", "The White Stripes")
pl.enqueue("Boulevard of Broken Dreams", "Green Day")
pl.enqueue("Zombie", "The Cranberries")
pl.enqueue("Stressed Out", "Twenty One Pilots")
pl.enqueue("Creep", "Radiohead")
pl.enqueue("Wonderwall", "Oasis")
pl.enqueue("Wish You Were Here", "Pink Floyd")
pl.enqueue("Black Hole Sun", "Soundgarden")
pl.enqueue("Enter Sandman", "Metallica")

print("🎧  Lista actual:")
pl.show()

# --- Reproducción — saltar dos canciones ---
print("\nSaltamos un tems:")
pl.skip()


print("\nEstado de la cola:")
pl.show()
