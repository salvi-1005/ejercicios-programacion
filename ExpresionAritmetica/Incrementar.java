public class Incrementar extends ExpresionAritmetica {
    private ExpresionAritmetica expresion;

    public Incrementar(ExpresionAritmetica exp) {
        this.expresion = exp;
    }

    @Override
    public int evaluar() {
        return expresion.evaluar() + 1;
    }
}