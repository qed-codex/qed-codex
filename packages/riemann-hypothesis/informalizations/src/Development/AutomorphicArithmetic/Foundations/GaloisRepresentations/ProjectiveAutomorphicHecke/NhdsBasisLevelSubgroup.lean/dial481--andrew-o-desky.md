---
{
  "module": "src/Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/ProjectiveAutomorphicHecke/NhdsBasisLevelSubgroup.lean",
  "declarations": [
    "UpperTheory.Gal.CertificateRingHomMap.finToHecke_holds"
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

## Extending a finite idelic character to a Hecke character

[Theorem ANT.1541](https://andrewodesky.com/rh/lean/UpperTheory.Gal.CertificateRingHomMap.finToHecke_holds/)

Let $E$ be a number field, $\psi:\mathbb A_{E,f}^{\times}\to\mathbb C^{\times}$ a homomorphism with open kernel, and $m_\phi\in\mathbb Z$ for every embedding $\phi:E\hookrightarrow\mathbb C$. Suppose $$\psi(k)=\left(\prod_{\phi:E\hookrightarrow\mathbb C}\phi(k)^{m_\phi}\right)^{-1}\qquad(k\in E^{\times}),$$ where $k$ on the left is diagonally embedded. There is a Hecke character $\kappa$ of $E$ whose local component at every finite place $w$ satisfies $$\kappa_w(y)=\psi(\iota_w(y))\qquad(y\in E_w^{\times}),$$ where $\iota_w$ inserts $y$ at $w$ and $1$ elsewhere. Its infinite part satisfies $$\kappa_\infty(k)=\prod_\phi\phi(k)^{m_\phi}$$ for every $k\in E^{\times}$ positive under all real embeddings.
