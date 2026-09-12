public class Fecha{
    private int dia;
    private int mes;
    private int año;

    public Fecha(int dd, int mm, int aa){
        this.dia = dd;
        this.mes = mm;
        this.año = aa;
    }

    public Boolean esMayor(Fecha f1, Fecha f2){
        return (f1.año > f2.año) || ((f1.año == f2.año) && (f1.mes > f2.mes)) || ((f1.año == f2.año) && (f1.mes == f2.mes) && (f1.dia > f2.dia));
    }

    @Override
    public String toString() {
        return dia + "/" + mes + "/" + año;
    }
}