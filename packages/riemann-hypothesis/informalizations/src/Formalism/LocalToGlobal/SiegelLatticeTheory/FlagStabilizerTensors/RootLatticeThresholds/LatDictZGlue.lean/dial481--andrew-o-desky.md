---
{
  "module": "src/Formalism/LocalToGlobal/SiegelLatticeTheory/FlagStabilizerTensors/RootLatticeThresholds/LatDictZGlue.lean",
  "declarations": [
    "Formalism.L2.SG.Pf.LatDictZ.Z5.adelic_gluing"
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

## Adelic gluing of lattices while fixing prescribed vectors

[Theorem ALG.0629](https://andrewodesky.com/rh/lean/Formalism.L2.SG.Pf.LatDictZ.Z5.adelic_gluing/)

Fix a CM extension $E/F$ with conjugation, a nondegenerate Hermitian matrix $J\in M_n(E)$, and a full finitely generated self-dual $\mathcal O_E$-lattice $L\subseteq E^n$. Fix the archimedean diagonalizations and finite-adelic topology specified in the conventions. Let $s_1,\ldots,s_r,z\in E^n$, and let $M\subseteq E^n$ be a full finitely generated $\mathcal O_E$-lattice. Assume $M_{\mathfrak p}=L_{\mathfrak p}$ for all but finitely many maximal ideals $\mathfrak p\subseteq\mathcal O_E$.

Suppose a family $\gamma_{\mathfrak p}\in U(J)(E)$ is specified for every ideal $\mathfrak p$ of $\mathcal O_E$, each fixing all the $s_a$ and $z$, and satisfying $$\gamma_{\mathfrak p}L_{\mathfrak p}=M_{\mathfrak p}\qquad(\mathfrak p\text{ maximal}).$$ There is $x\in U(J)(\mathbb A_{F,f})$ fixing the finite-adelic images of every $s_a$ and $z$ such that $$M=\{v\in E^n:x^{-1}v\in\widehat L\}.$$
