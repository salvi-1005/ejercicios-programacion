public abstract class Animal {

    protected String nombre;
    protected double peso;

    public Animal(String n, double p){
        //Si el peso no es positivo lanza IllegalArgumentException y no crea el animal
        if (p <= 0) {
            throw new IllegalArgumentException("El peso debe ser positivo");
        }
        this.nombre = n;
        this.peso = p;
    }

    public String getNombre(){
        return this.nombre;
    }

    public double getPeso(){
        
        return this.peso;
    }

    public abstract String emitirSonido();

}
