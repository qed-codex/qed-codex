---
{
  "module": "src/Development/AutomorphicArithmetic/AutomorphicVarieties/CommutativeAlgebra/FramedUniv.lean",
  "declarations": [
    "UpperTheory.V.Alg.framed_univ"
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

## Existence of a universal framed deformation ring

[Theorem AGR.1299](https://andrewodesky.com/rh/lean/UpperTheory.V.Alg.framed_univ/)

Let $\ell$ be prime and $O$ a complete Noetherian local commutative ring with finite residue field $k$ of characteristic $\ell$, with $2\in O^\times$. Let $I$ be a finite set, $X$ an abelian group, and $w:I\to X$. Fix an invertible matrix $J\in M_I(O)$ with $J^t=J$ or $J^t=-J$, a map $\beta:I\to B_0$, an involution $\sigma$ of $B_0$, and $c\in X$ such that $$J_{ab}\ne0\Longrightarrow\beta(b)=\sigma(\beta(a))\text{ and }w(a)+w(b)=c.$$ Let $\mathcal C_O$ be the class of complete Noetherian local commutative $O$-algebras whose structure maps are local and induce isomorphisms on residue fields. For $A\in\mathcal C_O$, put $$H(A)=\{h\in M_I(A):h^tJ_Ah=J_A,\ h_{ab}=0\text{ if }\beta(a)\ne\beta(b),\ h\bmod\mathfrak m_A=1\},$$ where $J_A$ is the image of $J$. Let $\Gamma$ be a profinite group such that every open subgroup has only finitely many continuous homomorphisms to the additive group $\mathbb Z/\ell\mathbb Z$. Fix a residual representation $\bar r:\Gamma\to\mathrm{GL}_I(k)$ and a continuous lift $r_0$ over $O$. Assume that both preserve $J$ up to a scalar and have zero entries between distinct $w$-weights, and that for each representation there is a homomorphism $\pi:\Gamma\to\operatorname{Perm}(B_0)$ such that a nonzero $(a,b)$ entry at $g$ implies $\beta(a)=\pi(g)\beta(b)$.

Fix finite sets $T,Q$, with $v_0\in T$, topological groups $\Gamma_v,\Gamma_q$, continuous homomorphisms $\phi_v:\Gamma_v\to\Gamma$ and $\psi_q:\Gamma_q\to\Gamma$, and subgroups $N_q\subseteq\Gamma_q$. Assume $\bar r\psi_q$ is trivial on $N_q$. A lift $r$ over $A$ is called compatible with $r_0$ when $$r(g)r_0(g)^{-1}\in H(A)\qquad(g\in\Gamma).$$ For each $q$ fix a local deformation condition $\mathcal L_q$ satisfying the five local-condition axioms described below, with $\mathcal L_q(r_0\psi_q)$ true. Let $B\in\mathcal C_O$, and for each $v$ let $\rho_v$ be a continuous lift of $\bar r\phi_v$ over $B$ compatible with $r_0\phi_v$.

There exist $R\in\mathcal C_O$, an $O$-algebra map $i:B\to R$, a continuous lift $r$ of $\bar r$ over $R$, and $\alpha_v\in H(R)$ such that $r$ is compatible with $r_0$, $\mathcal L_q(r\psi_q)$ holds for every $q$, $\alpha_{v_0}=1$, and $$r(\phi_v(g))\alpha_v=\alpha_v\,i(\rho_v(g)).$$ For every other tuple $(R',i',r',\alpha')$ satisfying these same conditions, there is a unique $O$-algebra map $f:R\to R'$ with $$f\circ i=i',\qquad f(r)=r',\qquad f(\alpha_v)=\alpha'_v\quad(v\in T).$$
