public class Libro extends Publicacion{

    private int nroDePaginas;
    private int año;

    public Libro(String titulo, int nroDePaginas, double precio, int año){
        super(titulo,precio);
        this.nroDePaginas = nroDePaginas;
        this.año = año;
    }

    

    public int getNroDePaginas(){
        return nroDePaginas;
    }

    public int getAño(){
        return año;
    }

    @Override
    public void mostrarDatos() {
        super.mostrarDatos();
        System.out.println("Número de páginas: " + nroDePaginas + ", Año: " + año);
    }

}
