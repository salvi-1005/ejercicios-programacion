public class AgendaTelefonica {

    private Individuo[] individuos;
    private int cantidadIndividuos;

    public AgendaTelefonica(int cantidadIndividuos) {
        this.cantidadIndividuos = cantidadIndividuos;
        this.individuos = new Individuo[cantidadIndividuos];
    }

    public void agregarIndividuo(Individuo individuo, int posicion) {
        if (posicion < cantidadIndividuos) {
            individuos[posicion] = individuo;
        } else {
            System.out.println("No se pueden agregar más individuos, la agenda está llena.");
        }
    }

    public void buscarIndividuo(String nombre) {
        for (int i = 0; i < cantidadIndividuos; i++) {
            if (individuos[i] != null && individuos[i].getNombre().equals(nombre)) {
                System.out.println("Individuo encontrado: " + individuos[i].getNombre() + " - Dirección: " + individuos[i].getDireccion() + " - Teléfono: " + individuos[i].getTelefono());
                return;
            }
        }
        System.out.println("Individuo no encontrado: " + nombre);
    }

    public void eliminarIndividuo(String nombre) {
        for (int i = 0; i < cantidadIndividuos; i++) {
            if (individuos[i] != null && individuos[i].getNombre().equals(nombre)) {
                individuos[i] = null;
                System.out.println("Individuo eliminado: " + nombre);
                return;
            }
        }
        System.out.println("Individuo no encontrado: " + nombre);
    }
    
}
