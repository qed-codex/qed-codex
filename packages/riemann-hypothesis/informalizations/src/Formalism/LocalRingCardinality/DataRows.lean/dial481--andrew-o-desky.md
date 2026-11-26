---
{
  "module": "src/Formalism/LocalRingCardinality/DataRows.lean",
  "declarations": [
    "Formalism.BasicNotions.Rows.Data",
    "Formalism.BasicNotions.Rows.OLat",
    "Formalism.BasicNotions.Rows.Places"
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

## Complex vector spaces and integral spans

[Definition / hypothesis THETA.D128](https://andrewodesky.com/rh/lean/Formalism.BasicNotions.Rows.Data/)

Hypothesis (complex vector spaces and integral spans). Let $k,m,t,f$ and the signatures $(p_j,q_j)=(k+j-1,m-j)$ be the rank data of ([Family fields and Galois data](https://andrewodesky.com/rh/lean/Formalism.HC.Frame/)). Choose a field $K$ with an embedding $\jmath:K\hookrightarrow\mathbb C$, a commutative ring $O$ and a homomorphism $O\to K$. An integral span in a complex vector space means the $O$-span, through $O\to K\xrightarrow{\jmath}\mathbb C$, of a specified finite subset whose complex span is the whole space.

There is a set $\mathcal P$ of places, an involution $w\mapsto\bar w$, an additive valuation $v_w:K\to\mathbb Z\cup\{\infty\}$, a prime $\ell_w$ and a positive integer $e_w$ for every $w\in\mathcal P$. Require $v_w(K^\times)=\mathbb Z$, $v_w(\ell_w)=e_w$ and $\bar{\bar w}=w$.

Choose a finite set $\mathcal T$ of cardinality $f$, a set $\mathcal M$ with distinguished elements $\mu_0,\mu_*,\mu_*'$, and maps $w\mapsto\mu_w,\nu_w$ from $\mathcal P$ to $\mathcal M$. Require $$\mu_{\bar w}=\mu_w,\qquad\nu_{\bar w}=\nu_w,\qquad\mu_w\in\{\mu_0,\nu_w\}.$$ There is a set $\mathcal W$ of source indices.

Choose finite-dimensional complex inner-product spaces $H,H_0$, natural numbers $D,D_0,D_{\rm all}$ and orthonormal bases $(h_a)_{0\le a<D}$, $(h^0_a)_{0\le a<D_0}$. Choose a real $\delta\le1$ with $D=(1-\delta)D_{\rm all}$, a finite set $\mathcal F$ of type labels, maps $a\mapsto\pi_a$ and $a\mapsto\pi^0_a$ from these two bases to $\mathcal F$, and a real number $D_*$.

For every $\mu\in\mathcal M$ and every integer $j\ge0$, choose finite-dimensional complex inner-product spaces $A_\mu,V_{\mu,j}$, complex-linear isometries $$V_{\mu,0}\simeq H,\qquad V_{\mu,m}\simeq A_\mu,$$ and complex-linear maps $i_{\mu,j}:V_{\mu,j+1}\to V_{\mu,j}$. Choose an integral span $\widetilde M_\mu\subseteq A_\mu$, a self-adjoint complex-linear idempotent $e_\mu$ on $A_\mu$, and a positive integer $d_G$. For every source $z\in\mathcal W$, choose a finite-dimensional complex inner-product space $U_z$, functions $$P_{z,\mu}:U_z\times A_\mu\longrightarrow\mathbb C,\qquad B_z:U_z\times H\longrightarrow\mathbb C,$$ and units $c_{z,\mu}\in K^\times$ with $c_{z,\mu_0}=1$.

For every $j\ge0$, choose a finite-dimensional complex inner-product space $M_j$ with an integral span, integer arrays $a^+_{j,\tau,i}$ for $\tau\in\mathcal T$, $0\le i<p_j$, and $a^-_{j,\tau,i}$ for $0\le i<q_j$. For $j=0$ and for $j>m$, the signature formulas use natural-number subtraction. For every $(\mu,j)$ choose a finite-dimensional complex inner-product space $T_{\mu,j}$ with an integral span, a $K$-vector space $T^K_{\mu,j}$ and a $\jmath$-semilinear map $$j_{\mu,j}:T^K_{\mu,j}\longrightarrow T_{\mu,j}.$$ Require $j_{\mu,j}$ to carry every $K$-basis of $T^K_{\mu,j}$ to a complex basis of $T_{\mu,j}$. Every specified generator of the integral span of $T_{\mu,j}$ lies in the image of $j_{\mu,j}$.

Choose self-adjoint complex-linear idempotents $e_{\mu,j}$ on $T_{\mu,j}$ preserving $j_{\mu,j}(T^K_{\mu,j})$, complex-linear maps $\theta_{\mu,j}:T_{\mu,j}\to M_j$, and subspaces $M_{j,\pi}\subseteq M_j$ for $\pi\in\mathcal F$. Choose reals $\lambda_{\mu,j,\pi}$, integers $I_{\mu,j,w},J_{\mu,j,w}$, nonnegative rationals $\eta_{j,w}$ and nonnegative rationals $h_{\ell,e}$ for all natural numbers $\ell,e$.
