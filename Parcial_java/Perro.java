public class Perro extends Animal {

    private String raza;
    private String sonido;

    public Perro(String nombre, double peso){
        super(nombre, peso);
        this.raza = "Pastor Aleman";
        this.sonido = "Guau";
    }

    public String getRaza(){
        return this.raza;
    }

    @Override
    public String emitirSonido(){
        return sonido;
    }

    public String toString(){
        return (nombre + " (Perro) - Peso: " + peso + " - Sonido: " + sonido);
    }
    
}
