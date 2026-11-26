---
{
  "module": "src/Development/WeilBound/ThetaLifts/LocalTheory/ConeShifts/PureIte.lean",
  "declarations": [
    "PositivityTheory.ThKG.Loc.Cone.gen"
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

## Tensor factorization of a weighted global cone integral

[Theorem THETA.1610](https://andrewodesky.com/rh/lean/PositivityTheory.ThKG.Loc.Cone.gen/)

Assume the source's local-action existence, idele and compact-group Fubini identities, vacuum invariance and shift formulas, archimedean cone construction, finite-place Schwartz preservation, pure-tensor factorization, and spanning by pure Schwartz tensors. Fix number fields $F\subseteq E$, an involution $\sigma$, the source's good Weil base, Hermitian–skew-Hermitian spaces $(X,W)$ and $(X_1,W_1)$, compatible Weil models $M,M_1$, and adapted hyperbolic-plane data. Let $e$ be one of the source's corresponding restriction maps, and $U(l)$ its matching rank-one Heisenberg shift, for $l\in\mathbb A_E^\times$. Fix local restriction maps $e_\infty,e_v$ compatible with pure tensors, with $e_\infty\ne0$ and each $e_v$ mapping Schwartz space onto Schwartz space and carrying the standard vacuum $\phi_v^0$ to $\phi_{1,v}^0$.

Let $K\subseteq U(X)(\mathbb A_F)$ be the source's stabilizer of the Cartan involutions and finite integral lattice. Choose Haar measures $dk,dl$ on $K,\mathbb A_E^\times$ and normalized local measure data, and let $\mathfrak a\ne0$ be a fractional ideal such that $U(l)$ lies in the model's integral lattice at $v$ exactly when $l$ lies in $\mathfrak a$ there. Fix an integer $z\ge2$.

There is $\kappa\in\mathbb C^\times$, independent of the following character choices, with this property. Choose a compatible Weil representation $\omega$ and splitting characters $\chi_X,\chi_W$, a continuous character $\nu$ of $\mathbb A_E^\times$, and finite sets $S_0\subseteq S$ of places of $F$. Assume all three characters are unramified outside $S$, and for every $w|v\in S$ assume $\nu_w$ is ramified and $\operatorname{ord}_w\mathfrak a=0$. Define $$(\mathcal C\Phi)(y)=\int_K\int_{\mathbb A_E^\times}e\bigl(\rho_\psi(U(l))\omega(k,1)\Phi\bigr)(y)\nu(l)|l|_E^z\,dl\,dk.$$ There are a continuous linear archimedean operator $A_\infty$, linear finite-place operators $A_v$, and $u_v\in\mathbb C$ such that $A_\infty$ is the analogous local double integral and preserves polynomial Fock vectors, and each $A_v$ is the local double integral and preserves Schwartz functions. For $v\notin S$, $u_v\ne0$ and $A_v\phi_v^0=u_v\phi_{1,v}^0$. The global operator is complex linear on Schwartz space, and for every finite $T\supseteq S$ and pure tensor $\Phi=f_\infty\otimes\bigotimes_v\phi_v$ with $\phi_v=\phi_v^0$ outside $T$, $$\left(\prod_{v\in T\setminus S}u_v\right)\mathcal C\Phi=\kappa\nu(\mathfrak a)L^{S_0}(z,\nu)\left(A_\infty f_\infty\otimes\bigotimes_{v\in T}A_v\phi_v\otimes\bigotimes_{v\notin T}\phi_{1,v}^0\right).$$ Here $L^{S_0}$ omits the Euler factors in $S_0$, and $\nu(\mathfrak a)$ is the product of uniformizer values raised to the prime exponents of $\mathfrak a$.
