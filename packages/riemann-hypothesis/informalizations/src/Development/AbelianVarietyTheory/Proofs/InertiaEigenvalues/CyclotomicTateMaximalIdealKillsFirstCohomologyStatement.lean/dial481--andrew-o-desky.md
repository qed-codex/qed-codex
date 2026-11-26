---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/CyclotomicTateMaximalIdealKillsFirstCohomologyStatement.lean",
  "declarations": [
    "GlobalTheory.T.cyclotomic_tate_maximalIdeal_kills_first_cohomology"
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

## Small cyclotomic scalars kill integral first cocycles

[Theorem PHT.0682](https://andrewodesky.com/rh/lean/GlobalTheory.T.cyclotomic_tate_maximalIdeal_kills_first_cohomology/)

Let $l$ be prime and let $G_{\mathbb Q_l}$ act on $\mathbb C_l$ by field automorphisms, extending its natural action on $\overline{\mathbb Q}_l$ and preserving the norm. Let $K/\mathbb Q_l$ be a finite extension in $\overline{\mathbb Q}_l$, put $$F=K_0(\mu_{l^\infty}),\qquad H=\operatorname{Gal}(\overline{\mathbb Q}_l/F),$$ where $K_0$ is the maximal unramified subfield of $K$. For $r\ge0$, let $c:G_{\mathbb Q_l}\to\mathbb C_l^r$ be continuous on $H$, with $\|c(g)_i\|\le1$ and $c(gh)=c(g)+g(c(h))$ for $g,h\in H$. If $a\in F\subset\mathbb C_l$ and $\|a\|<1$, there is $x\in\mathbb C_l^r$ with $\|x_i\|\le1$ such that $$a\,c(g)=g(x)-x\qquad(g\in H).$$
