public class Vaca extends Animal {

    private double produccionLeche;
    private String sonido;

    public Vaca(String nombre, double peso){
        super(nombre, peso);
        this.produccionLeche = 25.0;
        this.sonido = "Muu";
    }

    public double getProduccionLeche(){
        return this.produccionLeche;
    }

    @Override
    public String emitirSonido(){
        return sonido;
    }

    public String toString(){
        return (nombre + " (Vaca) - Peso: " + peso + " - Sonido: " + sonido);
    }
    
}
