import informe_final_final

class Lote:
    def __init__(self, nombre, cajones, precio):
        self.nombre = nombre
        self.cajones = cajones
        self.precio = precio
    def costo(self):
        return self.cajones*self.precio 
    def vender(self, cant_cajones):
        self.cajones -= cant_cajones

class MiLote(Lote):
    def rematar(self):
        self.vender(self.cajones)
    def costo(self):
        # Fijate cómo usamos `super`
        costo_orig = super().costo()
        return 1.25 * costo_orig
        
c = MiLote('Pera', 100, 490.1)

class FormatoTabla:
    def encabezado(self, headers):
        '''
        Crea el encabezado de la tabla.
        '''
        raise NotImplementedError()

    def fila(self, rowdata):
        '''
        Crea una única fila de datos de la tabla.
        '''
        raise NotImplementedError()
        
class FormatoTablaTXT(FormatoTabla):
    '''
    Generar una tabla en formato TXT
    '''
    def encabezado(self, headers):
        for h in headers:
            print(f'{h:>10s}', end=' ')
        print()
        print(('-'*10 + ' ')*len(headers))

    def fila(self, data_fila):
        for d in data_fila:
            print(f'{d:>10s}', end=' ')
        print()
        
class FormatoTablaCSV(FormatoTabla):
    '''
    Generar una tabla en formato CSV
    '''
    def encabezado(self, headers):
        print(','.join(headers))

    def fila(self, data_fila):
        print(','.join(data_fila))
        
class FormatoTablaHTML(FormatoTabla):
    '''
    Generar una tabla en formato CSV
    '''
    def encabezado(self, headers):
        """Imprime la fila de encabezados (lista de strings)."""
        fila_th = ''.join(f'<th>{h}</th>' for h in headers)
        print(f'<tr>{fila_th}</tr>')

    def fila(self, data_fila):
        """Imprime una fila de datos (lista de valores)."""
        fila_td = ''.join(f'<td>{d}</td>' for d in data_fila)
        print(f'<tr>{fila_td}</tr>')

    def tabla_completa(self, headers, filas):
        """Imprime una tabla completa (<table> ... </table>) dado headers y lista de filas."""
        print('<table>')
        self.encabezado(headers)
        for fila in filas:
            self.fila(fila)
        print('</table>')
        
a = r"https://campusvirtualecyt.unsam.edu.ar/pluginfile.php/397971/mod_resource/content/1/Parcial%202%20-%20prog1.pdf"