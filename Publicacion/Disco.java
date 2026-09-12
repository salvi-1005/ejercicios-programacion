public class Disco extends Publicacion{

    private int minutos;
    
    public Disco(String titulo, double precio, int minutos){
        super(titulo,precio);
        this.minutos = minutos;
    }

    public int getMinutos(){
        return minutos;
    }

    @Override
    public void mostrarDatos() {
        super.mostrarDatos();
        System.out.println("Duración en minutos: " + minutos);
    }
}
