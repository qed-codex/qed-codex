---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/DeRhamSubrepQuotientAndStrictness.lean",
  "declarations": [
    "GlobalTheory.DRSubQuot.deRham_sub_quot"
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

## De Rham subrepresentations and strict quotient maps

[Theorem PHT.0226](https://andrewodesky.com/rh/lean/GlobalTheory.DRSubQuot.deRham_sub_quot/)

Let $\ell$ be prime, let $K,L\subseteq\overline{\mathbb Q}_\ell$ be finite extensions of $\mathbb Q_\ell$, and put $G_K=\operatorname{Gal}(\overline{\mathbb Q}_\ell/K)$. For this prime, choose data satisfying Hypothesis (local period data) in ([Local period rings and coefficient comparisons](https://andrewodesky.com/rh/lean/Formalism.BasicNotions.LocRings/)). Use its de Rham ring $D$, filtration $(\operatorname{Fil}_K^aD)_{a\in\mathbb Z}$, invariant spaces $D_{\mathrm{dR}}$ and de Rham condition.

Let $V,V'$ be finite-dimensional $L$-vector spaces with $L$-linear $G_K$-actions, and let $f:V\to V'$ be an $L$-linear equivariant map.

If $f$ is injective and $V'$ is de Rham, then $V$ is de Rham. If $f$ is surjective and $V$ is de Rham, then $V'$ is de Rham and, for every $a\in\mathbb Z$, $$D_{\mathrm{dR}}(f)\bigl(\operatorname{Fil}^aD_{\mathrm{dR}}(V)\bigr)=\operatorname{Fil}^aD_{\mathrm{dR}}(V').$$
