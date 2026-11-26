---
{
  "module": "ComparatorChallenges/MatrixExponent.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Codex (GPT-6.2 Astra)",
  "kind": "ai",
  "origin": "generated",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "license": "CC-BY-4.0"
}
---

# Which algorithms does the matrix exponent measure?

AI drafted this autoinformalization from the original source. It is open for mathematical review.

Imagine computing just one output entry of a matrix product. The program must leave a register containing exactly the polynomial obtained by multiplying row entries by their corresponding column entries and summing. This has to hold for every output position as an equality of formal polynomials, even over a finite field. [Register contents and output condition](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/ComparatorChallenges/MatrixExponent.lean#L76-L89)

The program builds its registers one at a time. A gate can load a field constant or an input for free. Each addition, subtraction or multiplication of earlier registers costs one. The two input matrices have shapes $a \times b$ and $b \times c$, and the algorithm designates an output register for each of the $a c$ entries. [Gates, cost and outputs](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/ComparatorChallenges/MatrixExponent.lean#L13-L58)

## How size becomes an exponent

Choose three real weights. At scale $N$ a wire of weight $w$ has integer dimension $\lceil N^w\rceil$. The outer row dimension uses the third weight, the shared dimension the first, and the outer column dimension the second. An exponent $t$ is admissible if for every positive slack $\varepsilon$ there is one positive constant $C$ that works at every integer scale $N\geq1$. The algorithm may depend on the scale, and its cost must be at most $C N^{t+\varepsilon}$. The formal exponent is the infimum of those admissible values. [Dimensions and quantifiers](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/ComparatorChallenges/MatrixExponent.lean#L93-L104)

## Three target values

With all weights equal to one, the target is $9/4$ over every field. If two weights are one and the third ranges over $[0,1]$, the dual exponent is the supremum of weights for which the cost exponent equals two. The second target says that supremum is $1/2$. [Square and dual targets](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/ComparatorChallenges/MatrixExponent.lean#L106-L119)

The rectangular target first replaces each negative weight by zero. Write $x\geq y\geq z$ for the resulting three weights in descending order. The expression starts with $x+y$ and adds a correction with numerator $\max((x+y)z-xy,0)^2$ and denominator $4xyz$. For the square case the three ones give a correction of $1/4$, recovering the first target directly from the formula. [Rectangular target](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/ComparatorChallenges/MatrixExponent.lean#L121-L132)

I read the challenge file at the linked revision. All three theorem bodies here use `sorry`. I did not build the project or audit the implementation supplying these targets. [First target body](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/ComparatorChallenges/MatrixExponent.lean#L106-L108) · [Other target bodies](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/ComparatorChallenges/MatrixExponent.lean#L117-L132)
