from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class StulenApp(App):
    def build(self):
        self.title = "Stulen App"

        layout = BoxLayout(
            orientation="vertical",
            padding=30,
            spacing=15
        )

        layout.add_widget(Label(
            text="STULEN APP",
            font_size="30sp",
            bold=True
        ))

        self.nama = TextInput(
            hint_text="Masukkan nama kamu",
            multiline=False,
            size_hint_y=None,
            height=50
        )
        layout.add_widget(self.nama)

        tombol = Button(
            text="MULAI",
            size_hint_y=None,
            height=55
        )
        tombol.bind(on_press=self.sapa)
        layout.add_widget(tombol)

        self.hasil = Label(text="Selamat datang!")
        layout.add_widget(self.hasil)

        return layout

    def sapa(self, instance):
        nama = self.nama.text.strip()
        self.hasil.text = (
            f"Halo, {nama}!" if nama
            else "Silakan masukkan nama!"
        )


if __name__ == "__main__":
    StulenApp().run()
