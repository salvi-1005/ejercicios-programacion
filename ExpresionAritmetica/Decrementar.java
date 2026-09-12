public class Decrementar extends ExpresionAritmetica {

    private ExpresionAritmetica expresion;

    public Decrementar(ExpresionAritmetica exp) {
        this.expresion = exp;
    }

    @Override
    public int evaluar() {
        return expresion.evaluar() - 1;
    }
}
