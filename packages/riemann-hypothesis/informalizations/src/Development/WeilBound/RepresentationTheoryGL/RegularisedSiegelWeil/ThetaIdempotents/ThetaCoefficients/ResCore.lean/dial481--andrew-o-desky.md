---
{
  "module": "src/Development/WeilBound/RepresentationTheoryGL/RegularisedSiegelWeil/ThetaIdempotents/ThetaCoefficients/ResCore.lean",
  "declarations": [
    "PositivityTheory.Rg.Rsw.resCore"
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

## A simple Eisenstein pole controlled by theta kernels

[Theorem THETA.0032](https://andrewodesky.com/rh/lean/PositivityTheory.Rg.Rsw.resCore/)

Fix the source's full CM unitary arithmetic datum. Let $B,W$ be Hermitian spaces with a chosen hyperbolic decomposition $B\simeq H^t\oplus W$. Put $w=\dim W$, $n=w+t$, and assume $$w\ge1,\qquad w<t,\qquad w+2<2t.$$ Let $\psi$ be a continuous nontrivial unitary additive character of $\mathbb A_F/F$, $\chi$ a unitary Hecke character of $\mathbb A_E^\times$ satisfying the restriction condition below, and $\theta$ compatible infinite embeddings. On the adelic matrix spaces of sizes $\dim B\times n$ and $w\times n$, choose additive Haar measures of rational covolume one and compatible Schwartz Weil actions $\omega_B,\omega_W$ of the split group $G=U(n,n)$, with character data $\psi,\chi,\theta$.

Let $H:G(\mathbb A_F)\to\mathbb R_{>0}$ be a continuous Siegel height with finite open level, $\Phi$ a Schwartz vector for $B$, and $s_0=t/2$. Suppose $U,d,E,\sigma$ give the continuation data below for the Eisenstein family attached to $g\mapsto(\omega_B(g)\Phi)(0)$ and $H$. Choose $\epsilon>0$ with $\overline{D}(s_0,\epsilon)\subseteq U$ and $d(z)\ne0$ on this disk away from $s_0$. Define $$c_k(g)=\frac1{2\pi i}\oint_{|z-s_0|=\epsilon}(z-s_0)^{k-1}\frac{E(z,g)}{d(z)}\,dz.$$ Then $c_k=0$ for every $k\ge2$.

Moreover, let $(X,\pi)$ be any finite measure space, $a:X\to G(\mathbb A_F)$ measurable with relatively compact range, and $\kappa:X\to\mathbb C$ integrable. If $$\int_X\Theta_{\omega_W}(\Psi)(a(x),h)\kappa(x)\,d\pi(x)=0$$ for every Schwartz vector $\Psi$ for $W$ and every $h\in U(W)(\mathbb A_F)$, then $$\int_Xc_1(a(x))\kappa(x)\,d\pi(x)=0.$$
