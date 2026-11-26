---
{
  "module": "src/Formalism/HermitianCurvature/HermitianCurvatureProofs/GrowthOfBasic.lean",
  "declarations": [
    "Formalism.FourierDecayAlt.P.pair_bound_abstract"
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

## A norm bound from grouped pair sums

[Theorem ALG.1156](https://andrewodesky.com/rh/lean/Formalism.FourierDecayAlt.P.pair_bound_abstract/)

Assume the abstract Gram and summation package described below. Let $H,H_1$ be complex inner product spaces, with $H_1$ complete, $I$ finite, and $T,R$ sets. Take absolutely summable families $u_t\in H$, $v_t\in H_1$, maps $r:T\to R$, $i:R\to I$, numbers $g_t\in\mathbb R$, an integer-valued function $c:T^2\to\mathbb N$, a predicate $P$ on $T$, a predicate $C$ on $T^2$, a subset $Z\subset T$, a matrix $B\in M_I(\mathbb C)$, and $\gamma>0$. Put $$U=\{t:g_t\ne0\},\quad S=\{t\in U:P(t)\},\quad S'=U\setminus S,\quad u(A)=\sum_{t\in A}u_t,\quad v_j(A)=\sum_{\substack{t\in A\\i(r(t))=j}}v_t.$$ For $A\subset T$, let $Q(A)=\{(t,t')\in A^2:r(t)=r(t')\}$, and use subscripts $\ge2$, $1$, $1,C$, $1,\neg C$ to restrict $Q(A)$ by the indicated condition on $c(t,t')$ and $C(t,t')$. Define $$p(Q)=\gamma\sum_{(t,t')\in Q}\operatorname{Re}\langle v_t,v_{t'}\rangle,\qquad p_{\rm abs}(Q)=\gamma\sum_{(t,t')\in Q}|\langle v_t,v_{t'}\rangle|.$$ Let $P_g,A_0,\varepsilon,\varepsilon',d\in\mathbb R$ with $P_g,d\ge0$. Assume $P_g\gamma I-B$ is positive semidefinite, $$\|u(A)\|^2=\operatorname{Re}\sum_{j,k}B_{jk}\langle v_j(A),v_k(A)\rangle\qquad(A=S,S'),$$ that $v_t\perp v_{t'}$ whenever $i(r(t))=i(r(t'))$ but $r(t)\ne r(t')$, and that $c(t,t')\ge1$ whenever $t,t'\in U$ and $r(t)=r(t')$. Finally assume $$u(Z)=0,\quad p_{\rm abs}(Q(U)_{\ge2})\le\varepsilon d,\quad p_{\rm abs}(Q(S)_{1,\neg C})\le\varepsilon d,$$ $$p(Q(S)_{1,C})\le A_0d,\qquad p(Q(S')_1)\le\varepsilon'd.$$ Then $$\|u(Z)+u(S)+u(S')\|^2\le \left(\sqrt{P_g(A_0+2\varepsilon)}+\sqrt{P_g(\varepsilon+\varepsilon')}\right)^2d.$$
