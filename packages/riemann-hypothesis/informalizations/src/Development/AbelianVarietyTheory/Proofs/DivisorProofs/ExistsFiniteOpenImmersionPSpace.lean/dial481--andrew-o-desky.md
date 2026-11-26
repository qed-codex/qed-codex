---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsFiniteOpenImmersionPSpace.lean",
  "declarations": [
    "GlobalTheory.ZMain.exists_finite_openImmersion_pSpace"
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

## Finite factorization of a quasi-finite morphism

[Theorem AG.1175](https://andrewodesky.com/rh/lean/GlobalTheory.ZMain.exists_finite_openImmersion_pSpace/)

Let $\mathcal O$ be a commutative Noetherian ring of finite type over $\mathbb Z$, let $m\ge0$, and let $X$ be a normal integral scheme. If $f:X\to\mathbb P^m_{\mathcal O}$ is locally of finite type, quasi-compact, separated, and locally quasi-finite, then there exist a normal integral scheme $Z$, a finite morphism $z:Z\to\mathbb P^m_{\mathcal O}$, and an open immersion $i:X\hookrightarrow Z$ such that $$f=z\circ i,\qquad \overline{i(X)}=Z.$$
