errores = []  # Lista para guardar errores
try:
    print(4 + "3")
except Exception as e:
    errores.append(str(e))  # Guardamos el error en la lista
    print(f"Error capturado: {e}")

"""En línea: 2 Carácter: 22
+ Python 3.9.6 (default, Jun 28 2021, 15:26:21)
+                      ~
Falta un argumento en la lista de parámetros.
En línea: 3 Carácter: 7
+ [Clang 11.0.0 (clang-1100.0.33.8)] on darwin
+       ~
Falta ] al final del atributo o literal de tipo.
En línea: 3 Carácter: 15
+ [Clang 11.0.0 (clang-1100.0.33.8)] on darwin
+               ~
Token '(' inesperado en la expresión o la instrucción.
En línea: 3 Carácter: 34
+ [Clang 11.0.0 (clang-1100.0.33.8)] on darwin
+                                  ~
Token ']' inesperado en la expresión o la instrucción.
En línea: 7 Carácter: 30
+   File "<stdin>", line 1, in <module>
+                              ~
El operador '<' está reservado para uso futuro.
    + CategoryInfo          : ParserError: (:) [], ParentContainsErrorRecordException
    + FullyQualifiedErrorId : MissingArgument
    + CategoryInfo          : ParserError: (:) [], ParentContainsErrorRecordException
    + CategoryInfo          : ParserError: (:) [], ParentContainsErrorRecordException
    + FullyQualifiedErrorId : MissingArgument
"""