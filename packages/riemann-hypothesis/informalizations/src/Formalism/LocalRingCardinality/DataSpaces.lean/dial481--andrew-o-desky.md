---
{
  "module": "src/Formalism/LocalRingCardinality/DataSpaces.lean",
  "declarations": [
    "Formalism.BasicNotions.CMData",
    "Formalism.BasicNotions.HSpace",
    "Formalism.BasicNotions.Spaces"
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

## Hermitian spaces in the theta constructions

[Definition / hypothesis THETA.D132](https://andrewodesky.com/rh/lean/Formalism.BasicNotions.CMData/)

Hypothesis (Hermitian spaces). Let $E/F$, $k,m,t,n,f,r,N_j=k+j(t+1)$, $n_V=r+t$ and $s=m/2-1$ be as in ([Family fields and Galois data](https://andrewodesky.com/rh/lean/Formalism.HC.Frame/)). Require that $F$ be totally real, $[E:F]=2$, and that the fixed elements of conjugation on $E$ be exactly $F$. Require that $E$ be totally complex, that every embedding of $E$ into $\mathbb C$ carry its involution to complex conjugation, and that for every maximal ideal $\mathfrak p$ of $\mathcal O_E$ there be $\theta\in\mathcal O_E$ with $\theta-\bar\theta\notin\mathfrak p$.

A Hermitian space with recorded lattice data consists of a finite-dimensional $E$-vector space $V$, its restricted $\mathcal O_E$-module structure, a nondegenerate Hermitian form $h$ conjugate-linear in its first argument, a natural number $d=\dim_E V$, a basis $(v_i)_{0\le i<d}$, a function $\tau\mapsto(p_\tau,q_\tau)$ on complex embeddings of $E$, and a full $\mathcal O_E$-lattice $L_0\subset V$ equal to its Hermitian dual $$L_0^\vee=\{y\in V:h(x,y)\in\mathcal O_E\text{ for every }x\in L_0\}.$$ For every space chosen below, require that $(p_\tau,q_\tau)$ be the actual signature of its Gram matrix after applying $\tau$. Choose a real-valued volume function $\operatorname{vol}$ on all Hermitian spaces with these recorded data, with $\operatorname{vol}(V)>0$ for every $V$.

Choose a prime $T$ and such spaces $X_j,Y_j,W_j,V_j$ for every integer $j\ge0$, and a space $X'$. For $j\le m$, require $$\dim_E X_j=N_j,\qquad X_j\text{ definite at every complex embedding},\qquad \dim_E Y_j=r+jt.$$ Require $\dim_E X'=r+mt$. There is an isometric $E$-linear map $i':X'\to X_m$ and a vector $z\in X_m$ such that $h_{X_m}(z,z)\ne0$ and $i'(X')$ is orthogonal to $z$. There are $E$-linear maps $i_j:X_j\to Y_j$, isometric for $j<m$, and an isometric $E$-linear isomorphism $X'\simeq Y_m$.

Choose $z_-\in Y_0$ with $h_{Y_0}(z_-,z_-)=-T$, orthogonal to $i_0(X_0)$, and vectors $e_a,f_a$ for $0\le a<s$ satisfying $$h(e_a,e_b)=h(f_a,f_b)=0,\qquad h(e_a,f_b)=\delta_{ab}.$$ Every $e_a,f_a$ is orthogonal to $i_0(X_0)$ and to $z_-$. At every complex embedding, the recorded signature of $Y_0$ is $(k+s,s+1)$.

For $1\le j\le m$, require $\dim_E W_j=r$ and signature $(k+j-1,m-j)$ at every complex embedding. Require that $W_j$ and $Y_0$ be isometric over $E\otimes_F\mathbb A_{F,f}$: after a bijective reindexing of their recorded bases, there is an invertible matrix $g$ with $$\bar g^{,T}G_{Y_0}g=G_{W_j}.$$ Here $\mathbb A_{F,f}$ is the finite adele ring and $G$ denotes the Gram matrix in the recorded basis; conjugation acts on the $E$ factor.

For $1\le j\le m$, require $\dim_E V_j=n_V$. Choose signs $\epsilon_j\in\{1,-1\}$ so that the recorded lattice of $V_j$ has an $\mathcal O_E$-basis that is an $E$-basis and is orthonormal for $\epsilon_j h_{V_j}$.
