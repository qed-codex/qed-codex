---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/CycZpowCrysDRJump.lean",
  "declarations": [
    "GlobalTheory.CycPow.cyc_zpow_crys_dR_jump"
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

## Crystalline cyclotomic powers and their filtration jumps

[Theorem PHT.0549](https://andrewodesky.com/rh/lean/GlobalTheory.CycPow.cyc_zpow_crys_dR_jump/)

Let $\ell$ be prime and fix the crystalline, de Rham and integral period data of ([De Rham subrepresentations and strict quotient maps](https://andrewodesky.com/rh/lean/GlobalTheory.DRSubQuot.deRham_sub_quot/)), with the identifications specified below. Let $K,L$ be finite extensions of $\mathbb Q_\ell$ in a fixed algebraic closure, let $k\in\mathbb Z$, and let $\chi_\ell:G_K\to L^\times$ be the cyclotomic character. The one-dimensional representation $L(\chi_\ell^k)$ is crystalline and de Rham. For every $\mathbb Q_\ell$-embedding $\tau:K\hookrightarrow L$ and every $a\in\mathbb Z$, $$\dim_L\operatorname{gr}^a D_{\mathrm{dR},\tau}(L(\chi_\ell^k))=\begin{cases}1&a=-k,\\0&a\ne-k.\end{cases}$$
