---
{
  "module": "src/Formalism/LocalToGlobal/SiegelLatticeTheory/FlagStabilizerTensors/CountT.lean",
  "declarations": [
    "Formalism.L2.SG.ThmSOwn.PLevT'"
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

## Multiplicity estimate at the selected character level

[Definition / hypothesis AGR.D248](https://andrewodesky.com/rh/lean/Formalism.MainNotions.S.CountE.CountAllPointsClass/)

The restricted counting condition for a supplied family and constants $n_0\in\mathbb N$, $A,C,c,c_b\in\mathbb R$ requires $c>0$, $c_b>0$ and the following assertion at every family member. It is a condition on that family, rather than an unconditional assertion for arbitrary unitary groups.

Use the arithmetic unitary-group datum of ([Cusp projection and multiplicity data](https://andrewodesky.com/rh/lean/Formalism.MainNotions.S.AutInst/)), with $n=\dim_E V$, $f=[F:\mathbb Q]$ and root discriminant $\mathrm{rd}_E$. Choose complete local discrete-series spaces, weights $\lambda_v$, unit lowest-type vectors $w_v$, their compatible Hilbert tensor product $\sigma_\infty$, a sigma-finite finite-factor measure $\mu_f$, a rational fundamental domain $\mathcal F$, its right regular action $R$, and an operator $R_e$ realizing finite-factor convolution by $e$. Assume $\mu_f$ is Haar measure and all the discrete-series, lowest-vector, tensor-product, fundamental-domain, right-action and convolution identifications just specified hold. Let $$D_{\mathrm{mult}}=\dim e\operatorname{Hom}_{G_\infty}(\sigma_\infty,L^2(\mathcal F)),\qquad D_*=\left(\prod_vd(\sigma_v)\right)\operatorname{vol}(\mathcal F)\operatorname{Re}e(1),$$ where $D_{\mathrm{mult}}$ is the natural-number dimension, assigned zero for an infinite-dimensional image, and the degrees have the matrix-coefficient normalization in ([Cusp projection and multiplicity data](https://andrewodesky.com/rh/lean/Formalism.MainNotions.S.AutInst/)).

Take $b,h\in\mathbb R$ and integers $g,g_0\ge0$. Assume constant real signature $(p,q)$ with $q^2\le n$, $n\ge n_0$, $b\ge2$, $\log\log\mathrm{rd}_E\le n$, and strictly decreasing Harish-Chandra parameters $\lambda_v$ satisfying $\lambda_{v,a}-(n-1)/2\in\mathbb Z$ and $|\lambda_{v,a}|\le b^2$. Require the idempotent and selected-character-level conditions in the conventions, and $$1\le g\le b^A,\qquad g_0\text{ prime},\quad g_0>4n,\quad g_0\text{ splits completely in }E,$$ $$|\lambda_{v,a}-\lambda_{v,b}|\ge h\quad\text{when the two indices have opposite signature signs},$$ $$h\ge Cn^{19}f^5\log(b\,\mathrm{rd}_E),\qquad\log f\le\sqrt n,\qquad\log\log b\le c_bnf\log n.$$ Then the required assertion is $$|D_{\mathrm{mult}}-D_*|\le e^{-cnf\log n}D_*.$$
