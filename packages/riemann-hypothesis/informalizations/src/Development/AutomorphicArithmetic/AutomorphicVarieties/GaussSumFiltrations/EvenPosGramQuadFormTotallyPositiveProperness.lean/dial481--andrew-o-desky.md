---
{
  "module": "src/Development/AutomorphicArithmetic/AutomorphicVarieties/GaussSumFiltrations/EvenPosGramQuadFormTotallyPositiveProperness.lean",
  "declarations": [
    "GlobalTheory.T.evenPosGram_quadForm_totallyPositive_properness"
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

## Positivity and finite fibres of an integral quadratic form

[Theorem ANT.0978](https://andrewodesky.com/rh/lean/GlobalTheory.T.evenPosGram_quadForm_totallyPositive_properness/)

Let $F$ be a totally real number field, $I$ a finite set, and $G\in M_I(\mathbb Z)$ have positive definite real image and even diagonal entries. Put $$Q(x)=\frac12x^tGx\qquad(x\in F^I).$$ For $x\ne0$, $Q(x)$ is totally positive. There is $c>0$ such that for every $x\in F^I$ and every real place $v$, $$c\sum_{i\in I}v(x_i)^2\le v(Q(x)).$$ For every $a,\xi\in F$, the set $$\{x\in a\mathcal O_F^I:Q(x)=\xi\}$$ is finite.
