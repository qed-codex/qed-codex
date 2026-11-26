---
{
  "module": "src/Development/AutomorphicArithmetic/AutomorphicVarieties/CommutativeAlgebra/LemmaP.lean",
  "declarations": [
    "UpperTheory.V.Alg.lemmaP"
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

## A homogeneous presentation for a framed deformation problem

[Theorem AGR.0085](https://andrewodesky.com/rh/lean/UpperTheory.V.Alg.lemmaP/)

Let $\ell\ne2$ be prime, $O$ a complete Noetherian local ring with finite residue field $k$ of characteristic $\ell$, and $\Gamma$ a profinite group such that every open subgroup has finitely many continuous homomorphisms to $\mathbb Z/\ell\mathbb Z$. Fix a finite index set $I$, a finite-rank free abelian group $X$, weights $w_i\in X$, and the form datum of ([Existence of a universal framed deformation ring](https://andrewodesky.com/rh/lean/UpperTheory.V.Alg.framed_univ/)): an invertible symmetric or alternating matrix $J$ whose nonzero entries pair specified blocks and have constant weight sum. Let $\bar r:\Gamma\to\operatorname{GL}_I(k)$ have a continuous lift $r_0$ over $O$, with both representations satisfying the form-normalization, block-permutation, and equal-weight support conditions of ([Existence of a universal framed deformation ring](https://andrewodesky.com/rh/lean/UpperTheory.V.Alg.framed_univ/)).

Fix a framing datum as in ([Existence of a universal framed deformation ring](https://andrewodesky.com/rh/lean/UpperTheory.V.Alg.framed_univ/)) with finitely many continuous maps $\phi_v:\Gamma_v\to\Gamma$, one distinguished index $v_0$, finitely many continuous maps $\psi_q:\Gamma_q\to\Gamma$, subgroups $N_q\subseteq\Gamma_q$, and local deformation conditions $\mathcal L_q$. Assume $\bar r\psi_q$ kills $N_q$, the local conditions satisfy the five local-condition axioms of ([Existence of a universal framed deformation ring](https://andrewodesky.com/rh/lean/UpperTheory.V.Alg.framed_univ/)) relative to $r_0\psi_q,N_q$, and $r_0\psi_q$ satisfies them. For every weight $j\in X$, assume the source's framed obstruction space $\mathrm{Ob}_j$ for the weight-$j$ form-preserving adjoint representation is finite-dimensional over $k$.

Let $B$ be a complete Noetherian local $O$-algebra with residue field $k$, supplied with a finite homogeneous formal presentation $B=O[[z_s:s\in S]]/J_B$, with every $z_s\in\mathfrak m_B$. Choose local lifts $\rho_v$ over $B$, differing from $r_0\phi_v$ through the strict form-preserving group $H$ of ([Existence of a universal framed deformation ring](https://andrewodesky.com/rh/lean/UpperTheory.V.Alg.framed_univ/)), and with each matrix entry $(a,b)$ in weight $w_a-w_b$.

There are another such $O$-algebra $R$, a map $B\to R$, a global lift $r$, and strict form-preserving framing matrices $\alpha_v$, with $\alpha_{v_0}=1$, that universally solve $$r(\phi_v(g))\alpha_v=\alpha_v\rho_v(g),\qquad r\psi_q\in\mathcal L_q,$$ with $r$ differing from $r_0$ in the same strict form-preserving group. There is a finite homogeneous relative presentation $$R\simeq O[[z_s\ (s\in S),x_t\ (t\in T)]]/(J_B,f_u\ (u\in U))$$ respecting the presentation of $B$, such that $r(g)_{ab}$ and $(\alpha_v)_{ab}$ have weight $w_a-w_b$. Every new variable has a weight $w_a-w_b$ and is a matrix entry of either $r(g)-r_0(g)$ or $\alpha_v-1$. For every $j\in X$, $$\#\{t:\operatorname{wt}(x_t)=j\}=\dim_k H^1_{\mathrm{fr},j},\qquad\#\{u:\operatorname{wt}(f_u)=j\}=\dim_k\mathrm{Ob}_j.$$ Here $H^1_{\mathrm{fr},j}$ is the source's space of locally constant adjoint cocycles trivial on $N_q$, with specified coboundaries at the $\Gamma_v$ and framing value zero at $v_0$; $\mathrm{Ob}_j$ is its framed two-cocycle obstruction quotient.
