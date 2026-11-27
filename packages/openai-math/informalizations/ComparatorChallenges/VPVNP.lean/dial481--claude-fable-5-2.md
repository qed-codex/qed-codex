---
{
  "module": "ComparatorChallenges/VPVNP.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude Fable 5.2",
  "kind": "ai",
  "origin": "generated",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "license": "CC-BY-4.0"
}
---

# Informalization of ComparatorChallenges/VPVNP.lean: one statement that VP and VNP differ over every field

**This file states one theorem and does not prove it. It defines arithmetic circuits in which only additions, subtractions and multiplications count as gates, and from them the classes VP and VNP of families of polynomials over a field. The theorem says that, over every field, the two classes are not the same, for families that have $2n$ variables at index $n$.** The theorem ends in `sorry`. The statement says that the classes differ. It does not say which family separates them or how large its circuits must be. In the usual terms it is VP $\ne$ VNP, known as Valiant's hypothesis.

AI drafted this autoinformalization from the original source. It is open for mathematical review.

## What kind of file this is

The file has 59 lines. It imports only Mathlib. [Line 1](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/ComparatorChallenges/VPVNP.lean#L1) It gives six definitions and then states one theorem, `OAI.Computability.VPVNP.Standalone.vp_ne_vnp`, with the body `sorry`. [Lines 11–55](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/ComparatorChallenges/VPVNP.lean#L11-L55)

A Comparator configuration beside the file names it as the challenge module and `OAI.Computability.VPVNP.ClassSeparation` as the solution module. It lists this one theorem and permits the axioms `propext`, `Quot.sound` and `Classical.choice`. It sets `enable_nanoda` to `false`. [VPVNP.json, lines 1–14](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/ComparatorChallenges/VPVNP.json#L1-L14) In Comparator, setting that switch to `true` adds a check with a second kernel, nanoda, to the check with Lean's own kernel. [Comparator README, lines 12–13](https://github.com/leanprover/comparator/blob/865edc14486c3388e9225daa971da8e157488c3e/README.md?plain=1#L12-L13) [Comparator README, lines 86–87](https://github.com/leanprover/comparator/blob/865edc14486c3388e9225daa971da8e157488c3e/README.md?plain=1#L86-L87) I have not built the project and have not run Comparator.

The repository README says that the manuscripts and proof artifacts were produced by an unnamed internal OpenAI model, and that the collection includes results at different stages of verification. [README, line 3](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/README.md?plain=1#L3) [README, line 7](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/README.md?plain=1#L7)

## Circuits

`Computes s p` says that a table of $s$ gates computes the polynomial $p$ over a field $F$. Each gate is the sum, the difference or the product of two values that are available to it. Available to gate $i$ are the variables, the constants, which are the elements of $F$ as constant polynomials, and the values of the gates before $i$. The polynomial $p$ itself has to be a variable, a constant or the value of one of the $s$ gates. So a table with no gates computes exactly the variables and the constants. All of this is about formal polynomials: two polynomials are equal when their coefficients are, which over a finite field says more than that their values are equal. [Lines 11–19](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/ComparatorChallenges/VPVNP.lean#L11-L19)

So variables and constants are free, and only the three binary operations are counted. The comment on the definition says that variables and scalars are free. [Lines 11–12](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/ComparatorChallenges/VPVNP.lean#L11-L12)

## Families and the two classes

- A function $f$ on the natural numbers is polynomially bounded if there are $A$, $d$ and $N$ with $f(n) \le A n^d$ for all $n \ge N$. [Lines 21–22](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/ComparatorChallenges/VPVNP.lean#L21-L22)
- A family has, for each index $n$, a type of variables and a polynomial in them. From line 27 on, each of these types is assumed to be finite. [Lines 24–27](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/ComparatorChallenges/VPVNP.lean#L24-L27)
- A family is a p-family if its number of variables and its total degree are polynomially bounded. [Lines 29–32](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/ComparatorChallenges/VPVNP.lean#L29-L32)
- **VP.** A p-family $p$ is in VP if there is a polynomially bounded $s$ such that $p_n$ is computed by a table of $s(n)$ gates, for every $n$. [Lines 34–36](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/ComparatorChallenges/VPVNP.lean#L34-L36)
- **VNP.** A p-family $p$ is in VNP if there are, for each $n$, a finite set $W_n$ of further variables whose size is polynomially bounded, and a family $g$ in VP in the variables of $p_n$ together with $W_n$, such that $p_n(x) = \sum_y g_n(x, y)$ as formal polynomials. The sum is over all assignments $y$ of $0$ and $1$ to the variables in $W_n$. [Lines 38–43](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/ComparatorChallenges/VPVNP.lean#L38-L43)

## The statement

For every field $F$, the property "is in VP" and the property "is in VNP" are not the same property of families whose variables at index $n$ are the pairs $(i, b)$ with $0 \le i < n$ and $b$ a bit. [Lines 51–55](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/ComparatorChallenges/VPVNP.lean#L51-L55) Such a family has $2n$ variables at index $n$.

In classical logic, which the permitted axioms give, two properties are different exactly when some object has one and not the other. So the statement is: over every field there is a family, with these variables, that lies in exactly one of the two classes.

## Points that need care

- **Which way the classes differ.** The statement is a bare inequality. It does not say that VP is contained in VNP. With these definitions the containment is short to see by hand: take no further variables, so that the sum has one term. Then a family that lies in exactly one of the two classes lies in VNP and outside VP. I checked this on paper and not in Lean, and this file proves none of it.
- **Only one shape of family.** The inequality is stated for families with the variables $(i, b)$ described above. A family with other sets of variables is not an instance of the statement as written.
- **No bound.** The statement names no polynomial and gives no lower bound on circuit size. The library states one. For every natural number $C \ge 1$ and every characteristic there is an $N$ such that, for all $n \ge N$ and every field of that characteristic, the image over that field of a certain integer polynomial $P_n$ has `circuitSize` more than $n^C$. [Separation.lean, lines 18–24](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/Separation.lean#L18-L24) I did not read the definition of `circuitSize` or what the proof rests on. That is not part of this file.
- **The cost model.** Subtraction is a gate, and variables and constants cost nothing. Other definitions of circuit size count the inputs as well. For polynomially bounded size the difference does not matter, but the numbers differ.
- **Eventually.** A bound $f(n) \le A n^d$ is asked only from some $N$ on. For $n \ge 1$ this changes nothing, because a larger $A$ covers finitely many exceptions. It matters at $n = 0$, where $A n^d$ is $0$ for $d \ge 1$. The circuits themselves must exist for every $n$.
- **Every field.** The field is any field in any universe of types. The characteristic is not restricted. [Lines 49–52](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/ComparatorChallenges/VPVNP.lean#L49-L52) The types of variables are in the lowest universe. [Line 25](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/ComparatorChallenges/VPVNP.lean#L25)

## What the statement leaves out

- **The proof.** This file has none.
- **P and NP.** The statement is about families of polynomials and arithmetic circuits. It says nothing about Boolean computation.

## What I read

I read this file in full, its Comparator configuration, the statement of the lower bound in `Separation.lean` and the first lines of the repository README, at the linked revision. I read the lines of the Comparator README that describe the second kernel. I did not compare the definitions with those in the literature. I did not read the manuscript. I did not read the proof, and I did not build the project.
