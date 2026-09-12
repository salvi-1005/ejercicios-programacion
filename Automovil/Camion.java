import java.time.LocalDate;

public class Camion extends Automovil {

    private LocalDate fechaPermiso;
    private boolean autorizado;

    public Camion(LocalDate fechaPermiso, boolean autorizado) {
        this.fechaPermiso = fechaPermiso;
        this.autorizado = autorizado;
    }

    public LocalDate getFechaPermiso() {
        return fechaPermiso;
    }

    public void solicitarAutorizacion(Concesionaria c) {
        this.autorizado = c.verificarCamion(this);
    }

    @Override
    public void habilitar(LocalDate fecha) {
        if (autorizado) {
            this.fechaPermiso = fecha;
            this.habilitado = true;
        } else {
            System.out.println("No autorizado");
        }
    }
    }
