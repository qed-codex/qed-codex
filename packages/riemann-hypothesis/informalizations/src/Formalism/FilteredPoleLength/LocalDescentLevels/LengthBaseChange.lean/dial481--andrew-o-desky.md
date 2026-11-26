---
{
  "module": "src/Formalism/FilteredPoleLength/LocalDescentLevels/LengthBaseChange.lean",
  "declarations": [
    "Formalism.LatticeBaseChangeAlt.LengthBaseChangeAlt.length_baseChange_eq_mul",
    "Formalism.LatticeBaseChangeAlt.lengthBaseChangeLocal"
  ],
  "author": "dial481",
  "writer": "Andrew O'Desky",
  "origin": "other-author",
  "source": "https://andrewodesky.com/rh/",
  "source_commit": "40e56bab026552e089d7afcfeff08d2defb9c005",
  "license": "with-permission"
}
---

As published on 26 November 2026.

## Module length under flat base change

[Theorem ALG.0879](https://andrewodesky.com/rh/lean/Formalism.LatticeBaseChangeAlt.LengthBaseChangeAlt.length_baseChange_eq_mul/)

Let $O\to O_1$ be a homomorphism of commutative rings with $O_1$ flat over $O$, and let $\varepsilon\in\mathbb N\cup\{\infty\}$. Suppose every simple $O$-module $S$ satisfies $$\operatorname{length}_{O_1}(O_1\otimes_O S)=\varepsilon.$$ For every finite-length $O$-module $Q$, $$\operatorname{length}_{O_1}(O_1\otimes_O Q)=\varepsilon\operatorname{length}_O(Q).$$

## Length under base change between discrete valuation rings

[Theorem ALG.0934](https://andrewodesky.com/rh/lean/Formalism.LatticeBaseChangeAlt.lengthBaseChangeLocal/)

Let $O\to O_1$ be a homomorphism of commutative discrete valuation domains, and let $Q$ be an $O$-module of finite length. Let $\varpi\in O$ and $\varpi_1\in O_1$ be irreducible, $u\in O_1^\times$, and $e\ge0$ satisfy $$\varpi=u\varpi_1^e\quad\text{in }O_1.$$ Then $$\operatorname{length}_{O_1}(O_1\otimes_O Q)=e\operatorname{length}_O Q.$$
