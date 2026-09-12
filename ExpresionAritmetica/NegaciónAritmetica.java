public class NegaciónAritmetica extends ExpresionAritmetica {

    private ExpresionAritmetica expresion;

    public NegaciónAritmetica(ExpresionAritmetica exp) {
        this.expresion = exp;
    }

    @Override
    public int evaluar() {
        return -expresion.evaluar();
    }
}
