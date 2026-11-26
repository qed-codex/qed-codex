---
{
  "module": "src/Formalism/LocalToGlobal/Columns/DecoFin.lean",
  "declarations": [
    "Formalism.L2.Col.glue_unimodular"
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

## A unimodular lattice from two conjugate coprime ideals

[Theorem ANT.1050](https://andrewodesky.com/rh/lean/Formalism.L2.Col.glue_unimodular/)

Let $E$ be a number field with an involution $a\mapsto\bar a$, and equip $E^n$ with $h(x,y)=\sum_i\bar x_i y_i$. Let $I,J\subseteq\mathcal O_E$ be ideals such that $\bar I\subseteq J$, $\bar J\subseteq I$, and $I+J=\mathcal O_E$. Let $N,B\subseteq E^n$ be $\mathcal O_E$-submodules such that $$N=N^\#,\qquad B\text{ is a full lattice},\qquad IN\subseteq B\subseteq N.$$ Then $$B+IB^\#$$ is a full lattice and is equal to its Hermitian dual.
