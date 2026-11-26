---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/ExistsCharpoly.lean",
  "declarations": [
    "GlobalTheory.MemN.SerInhab.exists_isSer"
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

## Central idempotents indexed by monic polynomials

[Theorem REP.0615](https://andrewodesky.com/rh/lean/GlobalTheory.MemN.SerInhab.exists_isSer/)

Let $g$ be prime, $r\ge0$, and $N\ge1$ with $|\operatorname{GL}_r(\mathbb F_g)|$ dividing $N$. For every polynomial $f\in\mathbb F_g[X]$, there is an element $e_f$ of the complex group algebra $\mathbb C[\operatorname{GL}_r(\mathbb F_g)]$ such that $$e_f^2=e_f,\qquad e_fa=ae_f\quad(a\in\mathbb C[\operatorname{GL}_r(\mathbb F_g)]),\qquad e_fe_{f'}=0\quad(f\ne f').$$ Moreover, $e_f\ne0$ exactly when $f$ is monic of degree $r$ with nonzero constant coefficient, and $$\sum_{\substack{f\ \mathrm{monic}\\\deg f=r,\ f(0)\ne0}}e_f=1.$$ Every group-algebra coefficient of every $e_f$ belongs to $\mathbb Q(e^{2\pi i/N})$.
