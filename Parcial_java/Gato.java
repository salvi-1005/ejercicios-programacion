public class Gato extends Animal {

    private String color;
    private String sonido;

    public Gato(String nombre, double peso){
        super(nombre, peso);
        this.color = "Negro";
        this.sonido = "Miau";
    }

    public String getColor(){
        return this.color;
    }

    @Override
    public String emitirSonido(){
        return sonido;
    }

    public String toString(){
        return (nombre + " (Gato) - Peso: " + peso + " - Sonido: " + sonido);
    }
    
}
