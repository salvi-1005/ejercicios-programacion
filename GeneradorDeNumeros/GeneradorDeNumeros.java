import java.util.Iterator;
import java.util.List;
import java.util.ListIterator;
import java.util.Collection;

public class GeneradorDeNumeros implements Iterator<Integer>, List<Integer>, Estadistica<Integer> {

    private int vinicial;
    private int vfinal;
    private int incremento;
    private int actual;

    public GeneradorDeNumeros(int ini, int fin, int inc) {
        this.vinicial = ini;
        this.vfinal = fin;
        this.incremento = inc;
        this.actual = ini;
    }

    public int getInicial() {
        return vinicial;
    }

    public int getFinal() {
        return vfinal;
    }

    public int sumar() {
        int suma = 0;
        for (int i = vinicial; i <= vfinal; i += incremento) {
            suma += i;
        }
        return suma;
    }

    public int getPromedio() {
        if (size() == 0) return 0;
        return (vinicial + vfinal) / 2;
    }

    // =========================
    // ITERATOR
    // =========================

    @Override
    public boolean hasNext() {
        return actual <= vfinal;
    }

    @Override
    public Integer next() {
        int valor = actual;
        actual += incremento;
        return valor;
    }

    // =========================
    // LIST (métodos principales)
    // =========================

    @Override
    public int size() {
        if (vinicial > vfinal) return 0;
        return ((vfinal - vinicial) / incremento) + 1;
    }

    @Override
    public boolean isEmpty() {
        return size() == 0;
    }

    @Override
    public Integer get(int index) {
        if (index < 0 || index >= size()) {
            throw new IndexOutOfBoundsException();
        }
        return vinicial + index * incremento;
    }

    @Override
    public boolean contains(Object o) {
        if (!(o instanceof Integer)) return false;

        int val = (Integer) o;

        if (val < vinicial || val > vfinal) return false;

        return (val - vinicial) % incremento == 0;
    }

    // =========================
    // MÉTODOS NO IMPLEMENTADOS
    // =========================

    @Override
    public boolean add(Integer e) {
        throw new UnsupportedOperationException();
    }

    @Override
    public void add(int index, Integer element) {
        throw new UnsupportedOperationException();
    }

    @Override
    public boolean addAll(Collection<? extends Integer> c) {
        throw new UnsupportedOperationException();
    }

    @Override
    public boolean addAll(int index, Collection<? extends Integer> c) {
        throw new UnsupportedOperationException();
    }

    @Override
    public void clear() {
        throw new UnsupportedOperationException();
    }

    @Override
    public Integer remove(int index) {
        throw new UnsupportedOperationException();
    }

    @Override
    public boolean remove(Object o) {
        throw new UnsupportedOperationException();
    }

    @Override
    public Integer set(int index, Integer element) {
        throw new UnsupportedOperationException();
    }

    @Override
    public int indexOf(Object o) {
        throw new UnsupportedOperationException();
    }

    @Override
    public int lastIndexOf(Object o) {
        throw new UnsupportedOperationException();
    }

    @Override
    public Iterator<Integer> iterator() {
        return this;
    }

    @Override
    public Object[] toArray() {
        throw new UnsupportedOperationException();
    }

    @Override
    public <T> T[] toArray(T[] a) {
        throw new UnsupportedOperationException();
    }

    @Override
    public boolean containsAll(Collection<?> c) {
        throw new UnsupportedOperationException();
    }

    @Override
    public boolean removeAll(Collection<?> c) {
        throw new UnsupportedOperationException();
    }

    @Override
    public boolean retainAll(Collection<?> c) {
        throw new UnsupportedOperationException();
    }

    @Override
    public List<Integer> subList(int fromIndex, int toIndex) {
        throw new UnsupportedOperationException();
    }

    @Override
    public ListIterator<Integer> listIterator() {
        // TODO Auto-generated method stub
        throw new UnsupportedOperationException("Unimplemented method 'listIterator'");
    }

    @Override
    public ListIterator<Integer> listIterator(int index) {
        // TODO Auto-generated method stub
        throw new UnsupportedOperationException("Unimplemented method 'listIterator'");
    }
}
