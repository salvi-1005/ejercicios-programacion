public class ProductoBinario extends ExpresionAritmetica {
    
    private ExpresionAritmetica izquierda;
    private ExpresionAritmetica derecha;

    public ProductoBinario(ExpresionAritmetica izq, ExpresionAritmetica der) {
        this.izquierda = izq;
        this.derecha = der;
    }

    @Override
    public int evaluar() {
        return izquierda.evaluar() * derecha.evaluar();
    }
}


