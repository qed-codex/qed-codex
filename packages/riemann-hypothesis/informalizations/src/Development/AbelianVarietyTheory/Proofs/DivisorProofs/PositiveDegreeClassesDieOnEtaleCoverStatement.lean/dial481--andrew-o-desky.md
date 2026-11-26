---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/DivisorProofs/PositiveDegreeClassesDieOnEtaleCoverStatement.lean",
  "declarations": [
    "GlobalTheory.T.positiveDegreeClasses_die_on_etaleCover"
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

## Positive-degree cohomology classes vanish on an etale cover

[Theorem AG.1209](https://andrewodesky.com/rh/lean/GlobalTheory.T.positiveDegreeClasses_die_on_etaleCover/)

Let $R$ be a commutative ring, $X$ a scheme, and $\mathcal F$ an etale sheaf of $R$-modules. For every integer $n>0$ and every class $x\in H^n_{\mathrm{et}}(X,\mathcal F)$, there is an etale surjective morphism $f:Y\to X$ such that $$f^*x=0\quad\text{in }H^n_{\mathrm{et}}(Y,f^*\mathcal F).$$
