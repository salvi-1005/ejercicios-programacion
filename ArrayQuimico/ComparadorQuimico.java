import java.util.Comparator;

public class ComparadorQuimico implements Comparator<ComponenteQuimico> {

    @Override
    public int compare(ComponenteQuimico a, ComponenteQuimico b) {
        return Integer.compare(
            getElectronegatividad(a),
            getElectronegatividad(b)
        );
    }

    private int getElectronegatividad(ComponenteQuimico c) {
        if (c.getSimbolo().equals("C")) return 1;
        if (c.getSimbolo().equals("H")) return 2;
        return 3;
    }
}
