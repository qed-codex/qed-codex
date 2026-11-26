---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/FontaineInequalityDcrisFiniteConcreteRingsStatement.lean",
  "declarations": [
    "GlobalTheory.T.fontaine_inequality_dcris_finite_concrete_rings"
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

## Fontaine dimension bound for a finite-dimensional representation

[Theorem PHT.1280](https://andrewodesky.com/rh/lean/GlobalTheory.T.fontaine_inequality_dcris_finite_concrete_rings/)

Fix a prime $\ell$ and the local period-data package, compatible integral period-ring data and identifications with $B_{\mathrm{cris}}$ and $B_{\mathrm{dR}}$ in ([De Rham subrepresentations and strict quotient maps](https://andrewodesky.com/rh/lean/GlobalTheory.DRSubQuot.deRham_sub_quot/)). Let $K,L\subseteq\overline{\mathbb Q}_\ell$ be finite extensions of $\mathbb Q_\ell$, and let $K_0$ be the specified unramified subfield of $K$. For every finite-dimensional $L$-vector space $V$, with its compatible restricted $\mathbb Q_\ell$-scalar structure, and every $L$-linear representation $\rho:G_K\to\mathrm{GL}_L(V)$, put $$D_{\mathrm{cris}}(V)=(B_{\mathrm{cris}}\otimes_{\mathbb Q_\ell}V)^{G_K},$$ using the given period datum. Then $D_{\mathrm{cris}}(V)$ is finite-dimensional over $L$ and $$\dim_L D_{\mathrm{cris}}(V)\le[K_0:\mathbb Q_\ell]\dim_L V.$$ No continuity hypothesis on $\rho$ is present in this statement.
