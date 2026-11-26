---
{
  "module": "src/Development/EtaleCohomology/EtaleSheaves/TorEtPf.lean",
  "declarations": [
    "LateralTheory.E.TorEtPf.localEF_of"
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

## Finite etaleness from two split principal localizations

[Theorem AG.0642](https://andrewodesky.com/rh/lean/LateralTheory.E.TorEtPf.localEF_of/)

Let $S,C$ be commutative rings with an $S$-algebra structure on $C$, let $I$ be a finite nonempty set, and let $f,g\in S$ generate the unit ideal. Suppose there are $S$-algebra isomorphisms $$C[1/f]\simeq\prod_{i\in I}S[1/f],\qquad C[1/g]\simeq\prod_{i\in I}S[1/g].$$ Then $C$ is finite and etale over $S$.
