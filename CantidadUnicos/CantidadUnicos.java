public class CantidadUnicos<T> {

    private T[] datos;

    public CantidadUnicos(T[] datos){
        this.datos = datos;
    }

    public int contarUnicos(){
        int contador = 0;
        for (int i = 0; i < this.datos.length; i++) {
            boolean esUnico = true;
            for (int j = 0; j < this.datos.length; j++) {
                if (i != j && this.datos[i].equals(this.datos[j])) {
                    esUnico = false;
                    break;
                }
            }
            if (esUnico) {
                contador++;
            }
        }
        return contador;
    }
    
}
