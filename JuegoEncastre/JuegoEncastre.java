public class JuegoEncastre {
    
    private Hueco[] huecos;
    private Bloque[] bloques;

    public JuegoEncastre(Hueco[] huecos, Bloque[] bloques) {
        this.huecos = huecos;
        this.bloques = bloques;
    }

    public int intentosNecesarios() {
    int intentos = 0;
    boolean[] bloqueUsado = new boolean[bloques.length];

    for (Hueco hueco : huecos) {
        boolean encontrado = false;

        for (int i = 0; i < bloques.length; i++) {
            if (!bloqueUsado[i]) {
                intentos++;

                if (encaja(bloques[i], hueco)) {
                    bloqueUsado[i] = true;
                    encontrado = true;
                    break;
                }
            }
        }

        if (!encontrado) {
            throw new RuntimeException("No se pudo llenar un hueco");
        }
    }

    return intentos;
}

    public boolean encaja(Bloque bloque, Hueco hueco) {
        
        return bloque.getProfundidad() == hueco.getProfundidad() && bloque.getAncho() == hueco.getAncho() && bloque.getLargo() == hueco.getLargo();

    }

}
