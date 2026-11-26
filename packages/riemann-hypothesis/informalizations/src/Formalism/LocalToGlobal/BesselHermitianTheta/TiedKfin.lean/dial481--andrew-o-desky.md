---
{
  "module": "src/Formalism/LocalToGlobal/BesselHermitianTheta/TiedKfin.lean",
  "declarations": [
    "Formalism.L2.Theta.IsFockCx",
    "Formalism.L2.Theta.KfinTied"
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

## Polynomial Fock vectors and compact frames

[Definition / hypothesis ARAK.D224](https://andrewodesky.com/rh/lean/Formalism.L2.Theta.KfinTied/)

Use ([Adelic oscillator actions and theta integrals](https://andrewodesky.com/rh/lean/Formalism.L2.Theta.WeilTied/)), with its matrix space $Z_{V,W}$, alternating form $[x,y]$, Heisenberg translations $T_u$ and group action $(g,h)\cdot x$. Use ([Automorphic theta functions and their measures](https://andrewodesky.com/rh/lean/Formalism.L2.Theta.ThetaTied/)) for compatible infinite embeddings. Call $x\in Z_{V,W}$ real if its finite part is zero, and a real direction any continuous additive $L:\mathbb R\to Z_{V,W}$ with real image. Define $$D_Lf(x)=\left.\frac d{dt}T_{L(t)}f(x)\right|_0,\qquad A_{J,L}=D_L+iD_{J\circ L}.$$

Hypothesis (compact frames). For every Hermitian space $V$, choose complex matrices $C_{V,\tau}$ from its rational coordinates to its signed signature coordinates, and a square matrix $B_V\in M_{\dim_E V}(E)$. Whenever the specified signatures equal the Gram signatures, require $$C_{V,\tau}^*J_{p_\tau,q_\tau}C_{V,\tau}=G_{V,\tau},\qquad\det B_V\ne0,$$ and require $B_V^*G_V^0B_V$ to be diagonal. In every row of $C_{V,\tau}\tau(B_V)$ at most one entry is nonzero. Relative to these frames, let $K_{V,\infty}$ be the purely infinite elements $g$ such that, for every $\tau$, some block diagonal matrix $b_\tau$ satisfies $b_\tau C_{V,\tau}=C_{V,\tau}g_\tau$.

For every compatible infinite embedding family, every unequal-rank pair $V,W$ with correct Gram signatures and every $\Phi\in\mathcal S(V,W)$, require membership of $\Phi$ in the specified subspace $\mathcal S_{\rm fin}(V,W)$ to be equivalent to the following condition. There is a continuous additive map $J:Z_{V,W}\to Z_{V,W}$ preserving real vectors, with $J^2x=-x$ on real vectors and $[Jx,Jy]=[x,y]$ for real $x,y$. It commutes on real vectors with every $(k,k')\in K_{V,\infty}\times K_{W,\infty}$. There is one sign $\epsilon\in\{1,-1\}$ such that, for every real $x$, $$\epsilon\,[Jx,x]_\tau\ge0\quad\text{at every infinite place }\tau,$$ and $[Jx,x]_\tau=0$ at every $\tau$ forces $x=0$. Here $a_\tau$ is the real part of the $\tau$-evaluation of an adelic $F$-scalar. Finally there is $N\ge0$ such that $$A_{J,L_1}\cdots A_{J,L_N}(e_{V,W}\Phi)=0$$ for every list of $N$ real directions. The embedding families required by this hypothesis exist, as in ([Automorphic theta functions and their measures](https://andrewodesky.com/rh/lean/Formalism.L2.Theta.ThetaTied/)).
