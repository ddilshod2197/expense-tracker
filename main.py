class ArxitektorDasturchi:
    def __init__(self, ism, familiya, tajriba):
        self.ism = ism
        self.familiya = familiya
        self.tajriba = tajriba

    def google_tajriba(self):
        return f"{self.ism} {self.familiya} Google tajribasida ishlaydi."

    def meta_tajriba(self):
        return f"{self.ism} {self.familiya} Meta tajribasida ishlaydi."

    def ishlaydi(self):
        return f"{self.ism} {self.familiya} ishlaydi."

class ArxitektorDasturchiGoogleMeta(ArxitektorDasturchi):
    def __init__(self, ism, familiya, google_tajriba, meta_tajriba):
        super().__init__(ism, familiya, google_tajriba)
        self.google_tajriba = google_tajriba
        self.meta_tajriba = meta_tajriba

    def google_tajriba(self):
        return f"{self.ism} {self.familiya} Google tajribasida ishlaydi."

    def meta_tajriba(self):
        return f"{self.ism} {self.familiya} Meta tajribasida ishlaydi."

    def ishlaydi(self):
        return f"{self.ism} {self.familiya} ishlaydi."

class ArxitektorDasturchiGoogleMetaTajriba(ArxitektorDasturchiGoogleMeta):
    def __init__(self, ism, familiya, google_tajriba, meta_tajriba, tajriba):
        super().__init__(ism, familiya, google_tajriba, meta_tajriba)
        self.tajriba = tajriba

    def google_tajriba(self):
        return f"{self.ism} {self.familiya} Google tajribasida ishlaydi."

    def meta_tajriba(self):
        return f"{self.ism} {self.familiya} Meta tajribasida ishlaydi."

    def ishlaydi(self):
        return f"{self.ism} {self.familiya} ishlaydi."

    def tajriba(self):
        return f"{self.ism} {self.familiya} {self.tajriba} tajribaga ega."

arxitektor = ArxitektorDasturchiGoogleMetaTajriba("Ali", "Vali", "Google", "Meta", "10 yil")
print(arxitektor.google_tajriba())
print(arxitektor.meta_tajriba())
print(arxitektor.ishlaydi())
print(arxitektor.tajriba())
```

```python
class ArxitektorDasturchi:
    def __init__(self, ism, familiya, tajriba):
        self.ism = ism
        self.familiya = familiya
        self.tajriba = tajriba

    def google_tajriba(self):
        return f"{self.ism} {self.familiya} Google tajribasida ishlaydi."

    def meta_tajriba(self):
        return f"{self.ism} {self.familiya} Meta tajribasida ishlaydi."

    def ishlaydi(self):
        return f"{self.ism} {self.familiya} ishlaydi."

class ArxitektorDasturchiGoogleMeta(ArxitektorDasturchi):
    def __init__(self, ism, familiya, google_tajriba, meta_tajriba):
        super().__init__(ism, familiya, google_tajriba)
        self.meta_tajriba = meta_tajriba

    def google_tajriba(self):
        return f"{self.ism} {self.familiya} Google tajribasida ishlaydi."

    def meta_tajriba(self):
        return f"{self.ism} {self.familiya} Meta tajribasida ishlaydi."

    def ishlaydi(self):
        return f"{self.ism} {self.familiya} ishlaydi."

class ArxitektorDasturchiGoogleMetaTajriba(ArxitektorDasturchiGoogleMeta):
    def __init__(self, ism, familiya, google_tajriba, meta_tajriba, tajriba):
        super().__init__(ism, familiya, google_tajriba, meta_tajriba)
        self.tajriba = tajriba

    def google_tajriba(self):
        return f"{self.ism} {self.familiya} Google tajribasida ishlaydi."

    def meta_tajriba(self):
        return f"{self.ism} {self.familiya} Meta tajribasida ishlaydi."

    def ishlaydi(self):
        return f"{self.ism} {self.familiya} ishlaydi."

    def tajriba(self):
        return f"{self.ism} {self.familiya} {self.tajriba} tajribaga ega."

arxitektor = ArxitektorDasturchiGoogleMetaTajriba("Ali", "Vali", "Google", "Meta", "10 yil")
print(arxitektor.google_tajriba())
print(arxitektor.meta_tajriba())
print(arxitektor.ishlaydi())
print(arxitektor.tajriba())
