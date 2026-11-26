---
{
  "module": "src/Formalism/LocalRingCardinality/DataAmbForm.lean",
  "declarations": [
    "Formalism.BasicNotions.AmbForm"
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

## Hermitian row lattices and their rational models

[Definition / hypothesis ARAK.D122](https://andrewodesky.com/rh/lean/Formalism.BasicNotions.DivData/)

Use ([Rational Hermitian lattices with specified frames](https://andrewodesky.com/rh/lean/Formalism.BasicNotions.HLat/)) for rational spaces, bases, archimedean matrices, integral submodules, norms, nonsingularity and fullness.

Hypothesis (source and target lattice data). Fix a number field $K$ with a ring involution and a finite source set $\mathcal W$. There is a rational Hermitian target lattice $R$, rational Hermitian source lattices $N_z$ for $z\in\mathcal W$, $K$-linear maps $B_z:(N_z)_K\to R_K^\vee$, real heights $h_z$, and reals $H_{\rm bd},\eta_F,\delta_P$, with $\delta_P\le1$, together with a natural number $D_{\rm all}$. If $d_z$ is the $K$-dimension of the span of $N_z$, put $$s=\frac{\sum_zd_z\{\mu(N_z)-h_z\}}{\sum_zd_z}.$$ Require $s+\mu_{\max}(R)\le H_{\rm bd}$.

For the row data below, use the coefficient number field $K\hookrightarrow\mathbb C$ of ([Identifications for arithmetic family members](https://andrewodesky.com/rh/lean/Formalism.MainNotions.N.LocTie/)).

For a row datum on a finite-dimensional complex Hermitian space $H$, choose the spaces, endpoint isometries, downward maps and integral spans of ([Complex vector spaces and integral spans](https://andrewodesky.com/rh/lean/Formalism.BasicNotions.Rows.Data/)), writing $B_{\mu,j}$ and $d_{\mu,j}$ for its $V_{\mu,j}$ and $i_{\mu,j}$ and taking $H$ as the initial space. Use its twist set and coefficient ring; the choices range over every twist $\mu$ and integer $j\ge0$.

Write $\mathcal G=G_{\rm fin}$ and $e_0=e^{\rm sel}$ as in ([Finite types and idempotents for the family](https://andrewodesky.com/rh/lean/Formalism.BasicNotions.NTypes/)). Choose a complex algebra action of the center of $\mathbb C[\mathcal G]$ on each $A_\mu$, and a self-adjoint idempotent $e_\mu$ equal to the action of $e_0$ when $e_0$ is central, and equal to zero otherwise.

Choose a rational Hermitian lattice $R$ over $K$, all of whose matrices $X_v$ are nonsingular, and a semilinear map $j_R:R_K\to H$ for the fixed embedding $K\hookrightarrow\mathbb C$. It takes the specified rational basis to a complex basis and satisfies $\|x\|_{v_0}=\|j_Rx\|$ at the distinguished infinite place $v_0$.

Define $\iota_\mu:A_\mu\to H$ by the endpoint isometries and the composite $d_{\mu,0}\cdots d_{\mu,m-1}$. Put $$V^0_\mu=\operatorname{im}e_\mu,\quad U_\mu=V^0_\mu\cap\ker\iota_\mu,\quad Q_\mu=V^0_\mu\cap U_\mu^\perp,$$ $$\Lambda_\mu=\operatorname{pr}_{Q_\mu}(\widetilde M_\mu\cap V^0_\mu),\qquad R_\mu=\iota_\mu(\Lambda_\mu).$$ Hypothesis (rational row lattice), imposed when cited, is the following exact local description of the integral submodule of $R$: $$x\in R\quad\Longleftrightarrow\quad \text{for every finite }w\text{ there is }a\in\mathcal O_K\setminus\mathfrak p_w \text{ with }ax\in\mathcal O_K\{y:j_Ry\in R_{\mu_w}\}.$$ The initial row datum takes $H$ to be the initial space in ([Complex vector spaces and integral spans](https://andrewodesky.com/rh/lean/Formalism.BasicNotions.Rows.Data/)). A base finite-level row datum is a separate choice with $H$ equal to its base finite-level space.

Hypothesis (ambient rational models). Given either row datum, for every $\mu$ choose a rational Hermitian lattice $H_\mu$ over $K$ and a semilinear map $j_\mu:(H_\mu)_K\to A_\mu$. For every used index $$\mu\in\{\mu_0,\mu_*,\mu_*'\}\cup\{\mu_w:w\text{ finite}\},$$ require nonsingularity and fullness of $H_\mu$, require $j_\mu$ to take its specified rational basis to a complex basis, and require $$x\in H_\mu\quad\Longleftrightarrow\quad j_\mu x\in\mathcal O_K\text{-span}(G_\mu),$$ where $G_\mu$ is the specified finite integral-generator set in $A_\mu$. Every $g\in G_\mu$ lies in the range of $j_\mu$, and $\|x\|_{v_0}=\|j_\mu x\|$.
