package aed;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertTrue;

import org.junit.jupiter.api.Test;

class CoberturaTests {
    Cobertura cobertura = new Cobertura();

    @Test
    void testFizzBuzz() {
        assertEquals("FizzBuzz", cobertura.fizzBuzz(15));
        assertEquals("Fizz", cobertura.fizzBuzz(3));
        assertEquals("Buzz", cobertura.fizzBuzz(5));
        assertEquals("7", cobertura.fizzBuzz(7));
    }

    @Test
    void testNumeroCombinatorio() {
        assertEquals(10, cobertura.numeroCombinatorio(5, 3));
        assertEquals(70, cobertura.numeroCombinatorio(8, 4));
        assertEquals(84, cobertura.numeroCombinatorio(9, 6));
        assertEquals(252, cobertura.numeroCombinatorio(10, 5));
    }

    @Test
    void testRepeticionesConsecutivas() {
        assertEquals(3, cobertura.repeticionesConsecutivas(new int[]{1,2,3,3,3}));
        assertEquals(2, cobertura.repeticionesConsecutivas(new int[]{4,9,6,8,8}));
        assertEquals(4, cobertura.repeticionesConsecutivas(new int[]{1,1,1,1,2}));
        assertEquals(5, cobertura.repeticionesConsecutivas(new int[]{4,4,4,4,4}));
    }
}
