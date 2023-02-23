from flask import Flask, render_template

#model
class ModelMahasiswa:
    def __init__(self, nama, nim):
        self.nama = nama
        self.nim = nim

#view
class MahasiswaView:
    def show(self,mahasiswa):
        return render_template("mahasiswa.html", mahasiswa=mahasiswa)

#controller
class MahasiswaController:
    def __init__(self,model, view):
        self.model = model
        self.view = view
        
        def set_nama(self, nama):
            self.model.nama = nama

        def set_nim(self, nim):
            self.model.nim = nim
        
        def update_view(self):
            return self.view.show(self.model)

#ini adalah alikasinya
app = Flask("testing")

@app.route("/mahasiswa")
def mahasiswa():
    mahasiswa = ModelMahasiswa("tes","123838282")
    view = MahasiswaView()
    controller = MahasiswaController(mahasiswa, view)
    return controller.update_view()

if __name__ == "__main__":
    app.run()