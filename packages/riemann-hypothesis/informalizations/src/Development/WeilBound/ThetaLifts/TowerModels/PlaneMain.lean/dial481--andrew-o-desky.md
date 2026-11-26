---
{
  "module": "src/Development/WeilBound/ThetaLifts/TowerModels/PlaneMain.lean",
  "declarations": [
    "PositivityTheory.ThKG.Tow.Pln.exists_plane"
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

## A hyperbolic plane adapted to lattices and split bases

[Theorem ALG.1565](https://andrewodesky.com/rh/lean/PositivityTheory.ThKG.Tow.Pln.exists_plane/)

Let $E/F$ be a CM extension with conjugation $\sigma$, and fix the good base datum specified in the conventions, including selected split places $P$, embeddings $\tau_v:E\hookrightarrow F_v$ and archimedean embeddings. Let $\varepsilon\in\{1,-1\}$ and $\kappa\in\mathbb C$ satisfy $\kappa\bar\kappa=1$ and $\bar\kappa\,\eta(\varepsilon)=\kappa$ for every embedding $\eta:E\hookrightarrow\mathbb C$. Let $D\subseteq E$ be an $\mathcal O_E$-submodule containing $1$, with $|\tau_v(c)|_v\le1$ for $c\in D$ and $v\in P$.

Let $n=n_1+2$ with $n_1\ge1$, and let $J\in M_n(E)$ satisfy $\sigma(J_{ji})=\varepsilon J_{ij}$. Write $h(x,y)=x^tJ\sigma(y)$. Suppose $\kappa\eta(J)$ has constant signature $(r,s)$, $r,s\ge1$, at the chosen infinite embeddings. Let $L\subset E^n$ be an $\mathcal O_E$-lattice satisfying $$y\in L\quad\Longleftrightarrow\quad h(y,L)\subseteq D.$$ Specify Cartan involutions for these archimedean forms and bases of the split local lattices at the selected places. Fix $0\le i_0<i_1<n$.

The Cartan involutions and split bases can be replaced, retaining $J,L$, so that there are $x,y\in E^n$, a map $\iota:E^{n_1}\to E^n$, a fractional ideal $\mathfrak b$ of $E$, and an $\varepsilon$-Hermitian lattice $(J_1,L_1)$ with the same conditions relative to $D$ and signature $(r-1,s-1)$, satisfying $$h(x,x)=h(y,y)=0,\quad h(x,y)=1,\quad h(\iota u,x)=h(\iota u,y)=0,$$ $$J_1=\iota^tJ\sigma(\iota),\qquad u\in L_1\ \Longleftrightarrow\ \iota u\in L,\qquad a\in\mathfrak b\ \Longleftrightarrow\ ax\in L.$$ Every $z\in L$ has an expression $z=ax+\iota u+by$, with $ax,by\in L$ and $u\in L_1$. At infinity the new Cartan involutions $\theta,\theta_1$ satisfy $\theta\eta(\iota)=\eta(\iota)\theta_1$ and $\eta(y)$ is a nonzero complex multiple of $\theta\eta(x)$. At each selected split place, the new basis has columns $\tau_v(x),\tau_v(y)$ at positions $i_0,i_1$, and the remaining columns are $\tau_v(\iota)$ times the basis for $L_1$, in their original order with those positions omitted.
