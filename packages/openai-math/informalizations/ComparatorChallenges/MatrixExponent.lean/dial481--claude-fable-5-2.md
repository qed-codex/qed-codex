---
{
  "module": "ComparatorChallenges/MatrixExponent.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude Fable 5.2",
  "kind": "ai",
  "origin": "generated",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "license": "CC-BY-4.0"
}
---

# Informalization of MatrixExponent.lean: what the three matrix multiplication theorems say

**This file states three theorems and proves none of them. It fixes a way to count the cost of multiplying two matrices over a field $F$: programs that only add, subtract and multiply, where each such operation costs $1$. It defines the exponent of a family of matrix formats as an infimum. It then states that the exponent for square matrices is exactly $9/4$ over every field, that the dual exponent is exactly $1/2$, and that a closed formula gives the exponent of every rectangular format.** Each of the three theorems ends in `sorry`. The source's configuration names another module as holding the proofs, and this file exists so that the claim can be read on its own.

AI drafted this autoinformalization from the original source. It is open for mathematical review.

## What kind of file this is

The file imports only Mathlib. [Line 1](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/ComparatorChallenges/MatrixExponent.lean#L1) It contains the definitions needed to state the result and three theorem statements whose bodies are `sorry`. The source's Comparator configuration names the module that is meant to prove them, `OAI.LinearAlgebra.SpectralBooks.ExactExponent`, lists the three theorem names, and permits the axioms `propext`, `Quot.sound` and `Classical.choice`. [Configuration](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/ComparatorChallenges/MatrixExponent.json)

So this file answers one question: what exactly is claimed? It does not depend on any of the 592 files that the named module imports, directly or indirectly, counting itself. Those files declare the same definitions again under the same names, and the named module does not import this file. That the two sets of definitions agree is what Comparator is meant to check. The writer of this note has not built the project and has not run Comparator.

## The cost model

**Gates.** A gate loads a constant of $F$, loads an input variable, or adds, subtracts or multiplies the contents of two registers. There is no division gate. [Lines 13–18](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/ComparatorChallenges/MatrixExponent.lean#L13-L18)

**Cost.** Loading a constant or an input is free. Each addition, subtraction and multiplication costs $1$. [Lines 24–29](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/ComparatorChallenges/MatrixExponent.lean#L24-L29) Multiplying by a constant is a multiplication like any other and costs $1$. The count is therefore the total number of arithmetic operations.

**Programs.** A program is a finite list of gates. Each gate reads registers filled earlier and fills one new register. A register may be read any number of times. The cost of a program is the sum of the costs of its gates. [Lines 33–43](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/ComparatorChallenges/MatrixExponent.lean#L33-L43)

**Matrix algorithms.** For natural numbers $a$, $b$, $c$ the inputs are the entries $x_{ij}$ of an $a \times b$ matrix $X$ and the entries $y_{jk}$ of a $b \times c$ matrix $Y$. An algorithm is a program together with a choice, for each position $(i, k)$ of the product, of the register that is to hold that entry. [Lines 47–58](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/ComparatorChallenges/MatrixExponent.lean#L47-L58)

**Correctness.** Every register holds a polynomial in the input variables with coefficients in $F$. An algorithm is formally correct when the register chosen for position $(i, k)$ holds exactly the polynomial $\sum_j x_{ij} y_{jk}$. [Lines 76–89](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/ComparatorChallenges/MatrixExponent.lean#L76-L89) This is equality of polynomials. Over a finite field it is strictly stronger than giving the right values on all inputs, because two different polynomials can take the same value at every point. Over an infinite field the two requirements agree.

## The exponent

The formats are indexed by a scale $N$ and three real weights $w_{12}$, $w_{23}$, $w_{31}$. A side of weight $w$ has length $\lceil N^{w} \rceil$. [Lines 93–94](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/ComparatorChallenges/MatrixExponent.lean#L93-L94) At scale $N$:

- $X$ has $\lceil N^{w_{31}} \rceil$ rows and $\lceil N^{w_{12}} \rceil$ columns;
- $Y$ has $\lceil N^{w_{12}} \rceil$ rows and $\lceil N^{w_{23}} \rceil$ columns.

So $w_{12}$ is the weight of the side the two matrices share, $w_{31}$ the weight of the rows of the product and $w_{23}$ the weight of its columns.

A real number $\tau$ is admissible when, for every $\varepsilon > 0$, there is a constant $C > 0$ such that for every $N \ge 1$ some formally correct algorithm for the format at scale $N$ has cost at most $C N^{\tau + \varepsilon}$. [Lines 96–100](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/ComparatorChallenges/MatrixExponent.lean#L96-L100) The exponent $\omega(F; w_{12}, w_{23}, w_{31})$, written `formalOmega F w12 w23 w31` in the source, is the infimum of the admissible $\tau$. [Lines 102–104](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/ComparatorChallenges/MatrixExponent.lean#L102-L104)

One convention matters when reading the theorems. In Mathlib the infimum of a set of real numbers that is empty or has no lower bound is defined to be $0$. A theorem that gives the infimum a nonzero value therefore also says that admissible exponents exist and are bounded below. The same convention applies to the supremum in statement 2. In statement 3 the right side is $0$ when all three weights are at most $0$, and there this remark gives no information.

## The three statements

**1. Square matrices.** For every field $F$,

$$\omega(F; 1, 1, 1) = \frac{9}{4}.$$

[Lines 106–108](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/ComparatorChallenges/MatrixExponent.lean#L106-L108) Both matrices are $N \times N$. The equality has two halves. For every $\varepsilon > 0$ there are division-free programs that multiply $N \times N$ matrices with at most $C N^{9/4 + \varepsilon}$ operations. And no exponent below $9/4$ has that property. The second half is a lower bound on all programs of this kind. This is the exponent of matrix multiplication over $F$ as it is usually defined through the total number of arithmetic operations, here for programs without division. The statement therefore asserts an exact value for it.

**2. The dual exponent.** For a function $\omega$ of one real variable, the source defines its dual exponent as the supremum of the $t \in [0, 1]$ with $\omega(t) = 2$. It applies this to $t \mapsto \omega(F; 1, 1, t)$ and calls the result $\alpha(F)$. [Lines 110–115](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/ComparatorChallenges/MatrixExponent.lean#L110-L115) At weights $(1, 1, t)$ the matrix $X$ has $\lceil N^{t} \rceil$ rows and $N$ columns, and $Y$ is $N \times N$. The dual exponent is usually stated for an $N \times N^{t}$ matrix times an $N^{t} \times N$ matrix, and the format here is a rotation of that one. The theorem states that for every field $F$,

$$\alpha(F) = \frac{1}{2}.$$

[Lines 117–119](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/ComparatorChallenges/MatrixExponent.lean#L117-L119)

**3. All rectangular formats.** Let $a$, $b$, $c$ be any real numbers. Replace each negative one by $0$, and let $x \ge y \ge z \ge 0$ be the three resulting numbers in decreasing order. The theorem states that for every field $F$,

$$\omega(F; a, b, c) = x + y + \frac{\max((x + y) z - x y,\ 0)^2}{4 x y z}.$$

[Lines 121–132](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/ComparatorChallenges/MatrixExponent.lean#L121-L132)

Four remarks on reading the formula.

- It depends only on the sorted weights, so the exponent is the same for all six orders of $a$, $b$, $c$.
- A negative weight counts as $0$. This agrees with the definition of the formats: for $N \ge 1$ and $w \le 0$ the number $N^{w}$ lies in $(0, 1]$, so the side has length $1$.
- Lean defines division by zero as zero. When $z = 0$ the numerator and the denominator of the fraction are both $0$, so the fraction is $0$ and the exponent is $x + y$. The source's comment says the same: on the coordinate planes the correction term is zero.
- For nonnegative weights the three matrices $X$, $Y$ and $XY$ have about $N^{w_{31} + w_{12}}$, $N^{w_{12} + w_{23}}$ and $N^{w_{31} + w_{23}}$ entries, and the largest of these exponents is $x + y$. The fraction is $0$ exactly when $(x + y) z \le x y$. For $x, y > 0$ this means $z \le \frac{x y}{x + y}$. In that range the exponent equals the exponent of the size of the largest matrix. Above it, the fraction is positive.

Statements 1 and 2 agree with statement 3. At $a = b = c = 1$ the formula gives $2 + \frac{1}{4} = \frac{9}{4}$. At weights $(1, 1, t)$ with $0 < t \le 1$ it gives $2 + \frac{\max(2 t - 1,\ 0)^2}{4 t}$, which equals $2$ exactly when $t \le \frac{1}{2}$, and at $t = 0$ it gives $2$.

## What the file does not say

- It says nothing about constants. The constant $C$ may depend on $\varepsilon$, and the statements are about growth rates only.
- It concerns one model: no division, all additions, subtractions and multiplications counted, and correctness as an identity of polynomials. Whether division changes the exponent is not a question this file asks.
- It certifies nothing by itself. The three theorem bodies are `sorry`. The statements become theorems only together with the module that proves them.
