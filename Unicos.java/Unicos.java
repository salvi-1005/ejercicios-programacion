public class Unicos<T> {

    private T[] datos;

    public Unicos(T[] datos){
        this.datos = datos;
    }

    public T[] sacarRepetidos() {
    @SuppressWarnings("unchecked")
    T[] resultado = (T[]) new Object[this.datos.length];
    int indice = 0;

    for (int i = 0; i < this.datos.length; i++) {
        boolean yaEsta = false;

        for (int j = 0; j < indice; j++) {
            if (resultado[j].equals(this.datos[i])) {
                yaEsta = true;
                break;
            }
        }

        if (!yaEsta) {
            resultado[indice] = this.datos[i];
            indice++;
        }
    }

    // achicar array
    @SuppressWarnings("unchecked")
    T[] finalRes = (T[]) new Object[indice];

    for (int i = 0; i < indice; i++) {
        finalRes[i] = resultado[i];
    }

    return finalRes;
}
    
}
