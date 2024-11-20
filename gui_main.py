from textual.app import App
from textual.widgets import DirectoryTree, Header, Footer, DataTable

class Slither(App):
    def compose(self):
        yield DirectoryTree("/")
        yield Header()
        yield Footer()
        
if __name__ == "__main__":
    Slither().run()
