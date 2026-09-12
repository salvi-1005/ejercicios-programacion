import java.util.Iterator;
import java.util.List;
import java.util.ListIterator;
import java.util.Collection;

public class EnumeradorString implements Iterator<Character>, List<Character>, Estadistica<Character> {

    private String texto;
    private int actual;

    public EnumeradorString(String texto) {
        this.texto = texto;
        this.actual = 0;
    }

    public Character getInicial() {
        return texto.charAt(0);
    }

    public Character getFinal() {
        return texto.charAt(texto.length() - 1);
    }

    public int sumar() {
        int suma = 0;
        for (int i = 0; i < texto.length(); i++) {
            suma += texto.charAt(i);
        }
        return suma;
    }

    public double getPromedio() {
        if (texto.length() == 0) return 0;
        return (double) sumar() / texto.length();
    }

    // =========================
    // ITERATOR
    // =========================

    @Override
    public boolean hasNext() {
        return actual < texto.length();
    }

    @Override
    public Character next() {
        return texto.charAt(actual++);
    }

    // =========================
    // LIST (métodos principales)
    // =========================

    @Override
    public int size() {
        return texto.length();
    }

    @Override
    public boolean isEmpty() {
        return texto.isEmpty();
    }

    @Override
    public Character get(int index) {
        if (index < 0 || index >= texto.length()) {
            throw new IndexOutOfBoundsException();
        }
        return texto.charAt(index);
    }

    @Override
    public boolean contains(Object o) {
        if (!(o instanceof Character)) return false;

        char c = (Character) o;

        return texto.indexOf(c) != -1;
    }

    @Override
    public int indexOf(Object o) {
        if (!(o instanceof Character)) return -1;
        return texto.indexOf((Character) o);
    }

    @Override
    public int lastIndexOf(Object o) {
        if (!(o instanceof Character)) return -1;
        return texto.lastIndexOf((Character) o);
    }

    @Override
    public Iterator<Character> iterator() {
        return this;
    }

    // =========================
    // MÉTODOS NO IMPLEMENTADOS
    // =========================

    @Override
    public boolean add(Character e) {
        throw new UnsupportedOperationException();
    }

    @Override
    public void add(int index, Character element) {
        throw new UnsupportedOperationException();
    }

    @Override
    public boolean addAll(Collection<? extends Character> c) {
        throw new UnsupportedOperationException();
    }

    @Override
    public boolean addAll(int index, Collection<? extends Character> c) {
        throw new UnsupportedOperationException();
    }

    @Override
    public void clear() {
        throw new UnsupportedOperationException();
    }

    @Override
    public Character remove(int index) {
        throw new UnsupportedOperationException();
    }

    @Override
    public boolean remove(Object o) {
        throw new UnsupportedOperationException();
    }

    @Override
    public Character set(int index, Character element) {
        throw new UnsupportedOperationException();
    }

    @Override
    public Object[] toArray() {
        throw new UnsupportedOperationException();
    }

    @Override
    public <U> U[] toArray(U[] a) {
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
    public List<Character> subList(int fromIndex, int toIndex) {
        throw new UnsupportedOperationException();
    }

    @Override
    public ListIterator<Character> listIterator() {
        // TODO Auto-generated method stub
        throw new UnsupportedOperationException("Unimplemented method 'listIterator'");
    }

    @Override
    public ListIterator<Character> listIterator(int index) {
        // TODO Auto-generated method stub
        throw new UnsupportedOperationException("Unimplemented method 'listIterator'");
    }
}
