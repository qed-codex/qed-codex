---
{
  "module": "src/Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/ProjectiveAutomorphicHecke/CharConjHolds.lean",
  "declarations": [
    "UpperTheory.Gal.CertificateRingHomMap.charConj_holds"
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

## Reciprocal roots at conjugate CM embeddings

[Theorem ALG.1492](https://andrewodesky.com/rh/lean/UpperTheory.Gal.CertificateRingHomMap.charConj_holds/)

Let $E$ be a CM number field with conjugation $c$, let $n\ge0$, $y,P\in\mathrm{GL}_n(E)$, and $s\in\mathbb Q^\times$. Suppose $$c(y)^tPy=sP.$$ Let $\phi:E\hookrightarrow\mathbb C$ and $t_1,\ldots,t_n\in\mathbb C$ satisfy $$\phi(\det(XI-y))=\prod_{i=1}^n(X-t_i).$$ Then every $t_i$ is nonzero, and, with $\bar\phi(a)=\overline{\phi(a)}$, $$\bar\phi(\det(XI-y))=\prod_{i=1}^n(X-s/t_i).$$
