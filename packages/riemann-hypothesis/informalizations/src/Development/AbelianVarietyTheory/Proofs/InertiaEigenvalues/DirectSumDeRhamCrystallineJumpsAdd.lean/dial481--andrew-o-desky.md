---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/DirectSumDeRhamCrystallineJumpsAdd.lean",
  "declarations": [
    "GlobalTheory.Per.DirectSumHT.directSum_hodgeTate"
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

## De Rham and crystalline periods of direct sums

[Theorem PHT.1350](https://andrewodesky.com/rh/lean/GlobalTheory.Per.DirectSumHT.directSum_hodgeTate/)

Let $\ell$ be prime and fix a local prime datum with compatible $A_{\inf}$ comparison data as specified in the conventions. Let $K,L\subseteq\overline{\mathbb Q}_\ell$ be finite extensions of $\mathbb Q_\ell$. Let $V,V_1,V_2$ be finite-dimensional $L$-linear representations of $G_K$, equipped with their compatible $\mathbb Q_\ell$-module structures, and let $e:V\simeq V_1\oplus V_2$ be an $L$-linear $G_K$-equivariant isomorphism. Then $$V\text{ is de Rham}\ \Longleftrightarrow\ V_1,V_2\text{ are de Rham},$$ $$V\text{ is crystalline}\ \Longleftrightarrow\ V_1,V_2\text{ are crystalline}.$$ For every embedding $\tau:K\hookrightarrow L$ over $\mathbb Q_\ell$ and every integer $a$, $$m_\tau(V,a)=m_\tau(V_1,a)+m_\tau(V_2,a),$$ where $m_\tau(V,a)$ is $\dim_L\operatorname{Fil}^a_\tau D_{\mathrm{dR}}(V)-\dim_L\operatorname{Fil}^{a+1}_\tau D_{\mathrm{dR}}(V)$ in the chosen period construction.
