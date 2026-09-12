import java.time.LocalDate;

public abstract class Automovil {

    protected String patente;
    protected boolean habilitado;

    public abstract void habilitar(LocalDate fecha);
}
