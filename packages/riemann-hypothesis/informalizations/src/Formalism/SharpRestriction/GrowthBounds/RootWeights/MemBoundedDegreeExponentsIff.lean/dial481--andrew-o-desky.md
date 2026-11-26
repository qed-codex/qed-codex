---
{
  "module": "src/Formalism/SharpRestriction/GrowthBounds/RootWeights/MemBoundedDegreeExponentsIff.lean",
  "declarations": [
    "Formalism.MainNotions.G.GLWeightTheory.asm_clause2"
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

## Truncating a binomial expansion modulo a prime power

[Theorem PHT.0863](https://andrewodesky.com/rh/lean/Formalism.MainNotions.G.GLWeightTheory.asm_clause2/)

Let $p$ be prime and $f,a:\mathbb N\to\mathbb Q$ satisfy $$f(m)=\sum_{j=0}^m a(j)\binom mj,\qquad v_p(a(j))\ge j/4.$$ For every integer $c\ge0$ there is $q:\mathbb N\to\mathbb Q$ with $v_p(q(j))\ge0$ for all $j$, such that $$v_p\left(f(m)-\sum_{j=0}^{4c}q(j)\binom mj\right)\ge c\qquad(m\ge0).$$
