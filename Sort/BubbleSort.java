
public class BubbleSort<T extends Comparable<T>> extends Sort<T> {

    @Override
    public void algoritmo() {
        int n = datos.size();
        for (int i = 0; i < n - 1; i++) {
            for (int j = 0; j < n - 1 - i; j++) {
                if (comparar(j, j + 1)) {
                    intercambiar(j, j + 1);
                }
            }
        }
    }
}

