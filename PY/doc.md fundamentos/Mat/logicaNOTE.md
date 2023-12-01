# LOGICA

## Indice

* [Conjucion](#conjuncion)
* [Disyucion](#disyucion)
* [Disyucion](#disyucion)
* [Negación](#negación)
* [Condicionales](#condicionales)
* [Tabla](#tabla)
* [Disyucion](#disyucion)

## Conjuncion

La disyuncion p o q denotada por p ^ q, es la propocición.

p: El departamento de matemáticas obtiene $40,000 adicionales,
q: El departamento de matemáticas contrata un nuevo académico,

p ^ q == p && q

## Disyucion

La disyuncion p o q denotada por p v q, es la propocición.

p: El departamento de matemáticas obtiene $40,000 adicionales,
q: El departamento de matemáticas contrata un nuevo académico,

p v q == p || q

## Negación

q: no se contrará un nuevo academico

p ^ ~q == p && ~q

## Condicionales

Si p y q son proposiciones, la proposición "si" p "entonces" q se llama proposición condicional y se denota por

La proposición p se llama hipótesis (o antecedente) y la proposición q recibe el nombre de
conclusión (o consecuente).

p: El departamento de matemáticas obtiene $40,000 adicionales,
q: El departamento de matemáticas contrata un nuevo académico,

si *p → q == p -> q* es True, entonces *q → p == q -> p*(**reciproca**) es False.

La proposición **condicional** puede ser *True* mientras que su **reciproca** sea *False*.

Otra proposición útil **es p si y sólo si q**, que se considera verdadera precisamente cuando p y q tienen el mismo valor de verdad (es decir, si p y q son ambas verdaderas o ambas falsas).

p ↔ q == p <-> q

## TABLA

| p | q | ~p | ~q |p ^ q|p v q|p ^ ~q|p -> q|p <-> q|
|---|---|----|----|-----|-----|------|------|-------|
| T | T |  F |  F |  T  |  T  |   F  |   T  |   T   |
| T | F |  F |  T |  F  |  T  |   T  |   F  |   F   |
| F | T |  T |  F |  F  |  T  |   T  |   T  |   F   |
| F | F |  T |  T |  T  |  F  |   F  |   T  |   T   |

Dos proposiciones diferentes tienen los mismos valores de verdad sin importar qué valores de verdad tengan las proposiciones que las constituyen. Tales proposiciones se conocen como **equivalentes lógicos** (**P ≡ Q**).

## Cuantificadores

Sea P una función proposicional con dominio de discurso D. Se dice que la afirmación para toda x, P(x) es una afirmación cuantificada universalmente. El símbolo ∀ significa “para toda”, “Para cada”, “Para cualquier”. Entonces, la afirmación
para toda x, P(x) se escribe ∀ x P(x).

Un valor x en el dominio de discurso que hace que P(x) sea falsa se llama **contraejemplo** de la afirmación.
