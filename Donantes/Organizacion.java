import java.util.ArrayList;
import java.time.LocalDate;

public class Organizacion {

    private String nombre;
    private ArrayList<Donante> donantes;
    private ArrayList<Donacion> donaciones;
    

    public Organizacion(String nombre){
        this.nombre = nombre;
        this.donantes = new ArrayList<>();
        this.donaciones = new ArrayList<>();
    }

    public String getNombre() {
        return nombre;
    }


    public Donante registrarDonante(String nombre, String apellido){
        
        Donante donante = new Donante(nombre, apellido);
    
        for (Donante d : donantes){
            if (d.getId() == donante.getId() && d.getNombre().equals(donante.getNombre()) && d.getApellido().equals(donante.getApellido())){
                System.out.println("El donante ya ha sido registrado.");
                return donante;
            }
        }
        this.donantes.add(donante);
        donante.setId(donantes.size()); //Se le asigna un ID al donante, que corresponde a su posición en la lista de donantes.
        return donante;
    }

    public Donacion cargarDonacion(Donante donante, LocalDate fecha, double monto){
        if (!donantes.contains(donante)){
            System.out.println("El donante no ha sido registrado. Por favor, registre al donante antes de registrar la donación.");  
        }
        Donacion donacion = new Donacion(donante, fecha, monto); //Se crea una donación con el monto y fecha proporcionados.
        this.donaciones.add(donacion);
        donacion.setId(donaciones.size()); //Se le asigna un ID a la donación, que corresponde a su posición en la lista de donaciones.
        donacion.toString();
        return donacion;
    }

    public void mostrarDonantes(){
        System.out.println("Listado de donantes de " + nombre + ":");
        for (Donante donante : donantes){
            System.out.println(donante.toString());
        }
    }

    public void mostrarDonacionesOrdenadasPorFecha(){
        System.out.println("Listado de donaciones de " + nombre);
        donaciones.sort((d1, d2) -> d1.getFecha().compareTo(d2.getFecha())); //Se ordenan las donaciones por fecha utilizando un comparador.
        for (Donacion donacion : donaciones){
            System.out.println("donacion " + donacion.getId());
            System.out.println(donacion.toString());
        }
    }

    public void mostrarResultadoALaFecha(LocalDate fecha){
        System.out.println("Estado de Resultado de " + nombre + " al " + fecha + ":");
        int cant_donaciones_pendientes = 0;
        int cant_donaciones_cobradas = 0;
        int cant_donaciones_rechazadas = 0;
        for (Donacion donacion : donaciones){
            if (donacion.getFecha().isBefore(fecha) || donacion.getFecha().isEqual(fecha)){
                switch (donacion.getEstado()) {
                    case PENDIENTE:
                        cant_donaciones_pendientes++;
                        break;
                    case COBRADA:
                        cant_donaciones_cobradas++;
                        break;
                    case RECHAZADA:
                        cant_donaciones_rechazadas++;
                        break;
                }
            }
            }

            System.out.println("- Cobradas: " + cant_donaciones_cobradas);
            System.out.println("- Rechazadas: " + cant_donaciones_rechazadas);
            System.out.println("- Pendientes: " + cant_donaciones_pendientes);
            
            if (cant_donaciones_cobradas >= 1 ){
                double monto_total_cobrado = 0;
                for (Donacion donacion : donaciones){
                    if (donacion.getEstado() == Donacion.Estado.COBRADA && (donacion.getFecha().isBefore(fecha) || donacion.getFecha().isEqual(fecha))){
                        monto_total_cobrado += donacion.getMonto();
                    }
                }
                System.out.println("- Monto total: $ " + monto_total_cobrado);
                double monto_cobrado_maximo = 0;
                double monto_cobrado_minimo = Double.MAX_VALUE;
                for (Donacion donacion : donaciones){
                    if (donacion.getEstado() == Donacion.Estado.COBRADA && (donacion.getFecha().isBefore(fecha) || donacion.getFecha().isEqual(fecha))){
                        if (donacion.getMonto() > monto_cobrado_maximo){
                            monto_cobrado_maximo = donacion.getMonto();
                        }
                        if (donacion.getMonto() < monto_cobrado_minimo){
                            monto_cobrado_minimo = donacion.getMonto();
                        }
                    }
                }
                System.out.println("- Monto máximo: $ " + monto_cobrado_maximo);
                System.out.println("- Monto mínimo: $ " + monto_cobrado_minimo);
                double monto_cobrado_promedio = cant_donaciones_cobradas > 0 ? monto_total_cobrado / cant_donaciones_cobradas : 0;
                System.out.println("- Monto medio: $ " + monto_cobrado_promedio);
                
            
            }
        }

        
    }

