---
{
  "module": "src/ReciprocityTheory/AnalyticForms/PlurisubharmonicFunctions/ProjectiveLineZeroFormHolds.lean",
  "declarations": [
    "ReciprocityTheory.AnForm.A.log_norm_integral_formula"
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

## A logarithmic integral formula for a coordinate hyperplane

[Theorem AG.1503](https://andrewodesky.com/rh/lean/ReciprocityTheory.AnForm.A.log_norm_integral_formula/)

For real functions $f_1,\ldots,f_D$ on $\mathbb C^D$, define the real density $$\mathcal D_D(f_1,\ldots,f_D)=\left(\frac2\pi\right)^D\operatorname{Re}\sum_{S\subseteq\{1,\ldots,D\}}(-1)^{D-|S|}\det\!\left(\sum_{j\in S}\left(\frac{\partial^2 f_j}{\partial z_a\partial\bar z_b}\right)_{a,b}\right),$$ with $\mathcal D_0=1$. Let $n\ge0$, $U\subset\mathbb C^{n+1}$ be open, $v:\mathbb C^{n+1}\to\mathbb R$ be $C^3$ with compact support contained in $U$, and let $\phi_1,\ldots,\phi_n$ be real functions smooth on $U$. Put $\iota(w)=(0,w)$.

Both integrands below are absolutely integrable with respect to Euclidean Lebesgue measure, and $$\int_{\mathbb C^{n+1}}\log|z_1|\,\mathcal D_{n+1}(v,\phi_1,\ldots,\phi_n)(z)\,dz=\int_{\mathbb C^n}v(\iota(w))\mathcal D_n(\phi_1\circ\iota,\ldots,\phi_n\circ\iota)(w)\,dw.$$ The value assigned to $\log|z_1|$ on $z_1=0$ does not affect the first integral.
