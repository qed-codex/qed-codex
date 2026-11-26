---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/ModuliProofs/TateIsometryOfFiniteLevelIsometriesStatement.lean",
  "declarations": [
    "GlobalTheory.T.tateIsometry_of_finiteLevel_isometries"
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

## Compatible torsion isometries from finite-level realizations

[Theorem AV.0635](https://andrewodesky.com/rh/lean/GlobalTheory.T.tateIsometry_of_finiteLevel_isometries/)

Fix the source's CM lattice datum, consisting of a CM number field $E$ with its auxiliary field and polarization data, an $\mathcal O_E$-module $\Lambda$, and its integral alternating form $B$. Let $K$ be a field, $Q$ a multiplicative group, $a:\mathcal O_E\times Q\to Q$ a prescribed action function, and $e_n(x,y,c)$ a relation for $n\ge0$, $x,y\in Q$, and $c\in K^\times$. Assume every $Q[n]=\{x:x^n=1\}$ is finite for $n>0$. Suppose, for $n,m>0$ and $x,x'\in Q[nm]$, $$e_{nm}(x,x',c)\ \Longrightarrow\ e_n(x^m,(x')^m,c^m).$$ Fix $k>0$, $z\in K$, and families $\lambda_i\in\Lambda$, $y_i\in Q$ indexed by any set. Suppose that for every $m>0$ there are a primitive $(km)$th root $\zeta\in K^\times$ and a map $u:\Lambda\to Q$ satisfying $$u(v+w)=u(v)u(w),\quad u(cv)=a(c,u(v)),\quad\ker u=km\Lambda,\quad\operatorname{im}u=Q[km],$$ $$e_{km}(u(v),u(w),\zeta^{B(v,w)}),\quad\zeta^m=z,\quad u(\lambda_i)^m=y_i.$$ Then there are maps $u_n:\Lambda\to Q$ and roots $\zeta_n\in K^\times$ for all $n\ge0$ satisfying additivity and the $\mathcal O_E$ action identity for every $n$, and, for $n,m>0$, $$\ker u_n=n\Lambda,\quad\operatorname{im}u_n=Q[n],\quad \zeta_n\text{ is primitive of order }n,$$ $$u_{nm}(v)^m=u_n(v),\quad\zeta_{nm}^{m}=\zeta_n,\quad e_n(u_n(v),u_n(w),\zeta_n^{B(v,w)}).$$ They also satisfy $\zeta_k=z$ in $K$ and $u_k(\lambda_i)=y_i$ for every $i$.
