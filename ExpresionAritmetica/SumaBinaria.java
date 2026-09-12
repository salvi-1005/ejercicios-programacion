public class SumaBinaria extends ExpresionAritmetica {
        
    private ExpresionAritmetica izquierda;
    private ExpresionAritmetica derecha;

    public SumaBinaria(ExpresionAritmetica izq, ExpresionAritmetica der) {
        this.izquierda = izq;
        this.derecha = der;
    }

    @Override
    public int evaluar() {
        return izquierda.evaluar() + derecha.evaluar();
    }
}


