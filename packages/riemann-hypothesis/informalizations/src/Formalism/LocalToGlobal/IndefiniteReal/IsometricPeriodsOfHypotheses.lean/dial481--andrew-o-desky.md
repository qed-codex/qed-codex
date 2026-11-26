---
{
  "module": "src/Formalism/LocalToGlobal/IndefiniteReal/IsometricPeriodsOfHypotheses.lean",
  "declarations": [
    "Formalism.IndefR.Cx.CxData.AuNZ",
    "Formalism.IndefR.Cx.CxData.MIDat",
    "Formalism.IndefR.Cx.CxData.MIid"
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

## A period identity with norm-preserving maps and local units

[Definition / hypothesis THETA.D061](https://andrewodesky.com/rh/lean/Formalism.IndefR.Cx.CxData.MIstar2/)

The following is a condition on a selected record and its realisation, using the vocabulary of ([Rational families of forms, their realisations by theta maps, and the rationality test](https://andrewodesky.com/rh/lean/Formalism.IndefR.Rat.RowTest/)). Let $K$ be its coefficient field, $\iota:K\to\mathbb C$ the chosen embedding, $t$ range over its tuples, $t_0$ be the base tuple, and $u$ range over a further index set. At every finite place $w$ of $K$ the record gives a tuple $t_w$. It also gives:

- a finite-dimensional complex inner product space $H$, a subspace $H_0$, a complex inner product space $H'$ and a conjugate-linear map $s:H\to H'$;
- for each $u$, a nonnegative integer $a_u$, a complex $a_u\times a_u$ matrix $X_u$ and a linear map $P_u:\mathbb C^{a_u}\to H'$;
- for each $t$, a $K$-linear map $e_t:K^{d_t}\to R_t$, a semilinear map $j_t:R_t\to H_t$ and a complex-linear map $\Theta_t:H_t\to H$; and for each $u,t$ a $K$-valued pairing $B_{u,t}$ on $K^{a_u}\times K^{d_t}$.

The construction of these objects from the record is not expanded. Define $\|x\|_{X_u}=\|X_u^{-1}x\|_2$. The *period identity with norm-preserving maps and local units* holds if there are a complex-linear map $V:H\to H$, complex matrices $U_u$ of size $a_u$, nonzero complex numbers $c_u$, and nonzero complex numbers $\zeta_{u,t}$ such that:

1. $V(H_0)\subseteq H_0$ and $\|Vh\|=\|h\|$ for every $h\in H_0$; also $\|U_ux\|_{X_u}=\|x\|_{X_u}$ for every $u$ and $x\in\mathbb C^{a_u}$.
2. $\zeta_{u,t_0}=1$ for every $u$. If $\zeta_{u,t_w}=\iota(k)$ for $k\in K$, then $\operatorname{ord}_w(k)=0$, for every $u$ and every finite place $w$.
3. For every $u,t$, $\phi\in K^{a_u}$ and $F\in K^{d_t}$, $$\zeta_{u,t}\,\iota\bigl(B_{u,t}(\phi,F)\bigr)=c_u\,\bigl⟨ s\bigl(V\Theta_t(j_t(e_tF))\bigr),\ P_u(U_u\iota(\phi))\bigr⟩.$$ Here $\iota(\phi)$ means entrywise application, and the inner product is conjugate-linear in its first argument.
