public class FiltrarElementos<E extends Comparable<E>> {
    
    private E[] elementos;
    private E elemento;

    public FiltrarElementos(E[] elementos, E elemento) {
        this.elementos = elementos;
        this.elemento = elemento;
    }

    public void filtrarElementosMenoresACiertoValor() {
        for (E e : elementos) {
            if (e.compareTo(elemento) < 0) {
                System.out.println(e);
            }
        }
    }

    public void filtrarElementosDistintosACiertoValor() {
        for (E e : elementos) {
            if (!e.equals(elemento)) {
                System.out.println(e);
            }
        }
    }
    


}
