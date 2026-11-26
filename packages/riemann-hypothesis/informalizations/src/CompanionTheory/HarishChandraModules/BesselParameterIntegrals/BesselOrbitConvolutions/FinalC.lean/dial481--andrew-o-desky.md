---
{
  "module": "src/CompanionTheory/HarishChandraModules/BesselParameterIntegrals/BesselOrbitConvolutions/FinalC.lean",
  "declarations": [
    "CompanionTheory.D.Upq.BesselFunctionalConstruction.shapeC"
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

## A rank-one factorization of a Bessel convolution

[Theorem REP.1237](https://andrewodesky.com/rh/lean/CompanionTheory.D.Upq.BesselFunctionalConstruction.shapeC/)

Assume ([Decay of matrix coefficients on the lowest compact type](https://andrewodesky.com/rh/lean/CompanionTheory.FamilyDerivativeExpansion.DecS.decay_low_range/)), ([Decay of discrete-series coefficients controlled by finitely many derivatives](https://andrewodesky.com/rh/lean/CompanionTheory.FamilyDerivativeExpansion.DecS.decay_infinite_range/)), and that every compact-finite vector in every such discrete-series model is smooth. Fix $k,r\ge0$, $n=2r+k+1$, a sign sequence $\varepsilon\in\{\pm1\}^n$, a real Harish–Chandra parameter $\lambda$, and a real gap $h$. Let $H$ be a complex Hilbert space, $\sigma:M_n(\mathbb C)\to\mathcal B(H)$ an operator family, $w_0\in H$, $W$ a finite-dimensional complex Hilbert space, $z\in\mathbb C^n$, $c\in\mathbb C$, $u\in\mathbb R^k$, and $\pi:M_n(\mathbb C)\to\mathcal B(W)$ an operator family. Choose measures $\mu_W,\mu_N,\mu_G,\nu_q$ on the matrix space. Assume the Bessel side-condition package in the conventions for these data.

Let $G,U_z,N,\psi_{z,c}$ be the unitary group, compact stabilizer, unipotent subgroup and character of ([Nonvanishing of a Bessel integral of translated lowest-type vectors](https://andrewodesky.com/rh/lean/Formalism.L2.SG.Closed.BM.BesselNVGap_holds/)), with all character coefficients equal to $c$. Put $D=\operatorname{span}_{\mathbb C}\{\sigma(g)w_0:g\in G\}$ and $$B(x,v)=\int_{U_z\times N}\langle v,\sigma(gm)x\rangle\,\overline{\psi_{z,c}(m)}\,\pi(g)^{-1}\,d\mu_W(g)\,d\mu_N(m).$$ Suppose $B(x,v)\ne0$ for some $x,v\in D$. There is a map $l:H\to W$, nonzero on $D$, whose restriction to the smooth vectors is complex-linear and satisfies $$l(\sigma(gm)x)=\psi_{z,c}(m)\pi(g)l(x)\qquad(g\in U_z,\ m\in N).$$ This restriction is bounded by a constant times a finite sum of norms of Lie derivatives, and for every smooth $x\in H$, $v\in D$, $\xi\in W$, $$B(x,v)\xi=\langle l(v),\xi\rangle l(x).$$
