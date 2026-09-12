enum Estado {
        PENDIENTE, RECHAZADA, COBRADA
    }

public class EnumEstado {
    Estado estado;
    
    public EnumEstado(Estado estado) {
        this.estado = estado;
    }
    
    public void definirEstado() {
        switch (estado) {
            case PENDIENTE:
                System.out.println("La donación está pendiente.");
                break;

            case RECHAZADA:
                System.out.println("La donación ha sido rechazada.");
                break;

            case COBRADA:
                System.out.println("La donación ha sido cobrada.");
                break;

            default:
                System.out.println("Estado de donación no válido.");
                break;
        }
    }
}
                
