public class ComponenteQuimico implements Comparable<ComponenteQuimico> {

    private String simbolo;

    public ComponenteQuimico(String simbolo) {
        this.simbolo = simbolo;
    }

    public String getSimbolo() {
        return simbolo;
    }

    @Override
    public int compareTo(ComponenteQuimico otro) {
        return Integer.compare(this.getElectronegatividad(), otro.getElectronegatividad());
    }

    private int getElectronegatividad() {
        if (simbolo.equals("C")) return 1;
        if (simbolo.equals("H")) return 2;
        return 3; // el resto
    }

    @Override
    public String toString() {
        return simbolo;
    }
}
