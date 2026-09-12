import java.time.LocalDate;

public class AutoMediano extends Automovil {

    private LocalDate fechaPermiso;

    public LocalDate getFechaPermiso() {
        return fechaPermiso;
    }

    public void habilitar(LocalDate fecha) {
        this.fechaPermiso = fecha;
        this.habilitado = true;
    }
}
