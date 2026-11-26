---
{
  "module": "src/ReciprocityTheory/ReductiveGroups/ArithmeticGeometry/BirationalGeometry/ToroidalCompactification/IsLieBasis.lean",
  "declarations": [
    "ReciprocityTheory.ChartRestriction.G.Geo.Tor.IsTangent",
    "ReciprocityTheory.ChartRestriction.G.Geo.Tor.epsR"
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

## Tangent evaluation and Chern pairings in divided-power cohomology

[Definition / hypothesis PHT.D022](https://andrewodesky.com/rh/lean/GlobalTheory.Cris.SqExt.val/)

Use the categories, cochains, class map $\operatorname{cl}:\mathscr F(X/R)\to H^1_{\rm dR}(X/R)$, primitive submodules and primitive duals of ([Divided-power cohomology and its primitive submodules](https://andrewodesky.com/rh/lean/GlobalTheory.Cris.IsNilDP/)).

**Evaluation on tangent vectors.** Let $A$ be a group scheme over a commutative ring $R$, with identity $e:\operatorname{Spec}R\to A$. Write $R_\epsilon=R[\epsilon]/(\epsilon^2)$, let $\pi:R_\epsilon\to R$ send $\epsilon$ to $0$, and let $\iota:R\to R_\epsilon$ be the inclusion. A tangent vector at the identity is an $R$-morphism $v:\operatorname{Spec}R_\epsilon\to A$ satisfying $v\circ\operatorname{Spec}\pi=e$.

For such $v$, form three objects of $\mathcal C_0(A/R)$. Let $T_0$ be the trivial thickening at $e$, with coefficient and quotient ring $R$; let $T_1$ be the trivial thickening at $v$, with coefficient and quotient ring $R_\epsilon$. Let $T_v$ have coefficient ring $R_\epsilon$, ideal $(\epsilon)$, quotient map $\pi$ and reduced point $e$. Give $(\epsilon)$ the divided powers $\delta_0(a)=1$, $\delta_1(a)=a$ and $\delta_n(a)=0$ for $n\ge2$. There are arrows $$\alpha:T_0\to T_v,\qquad \beta:T_1\to T_v,$$ whose coefficient-ring maps are respectively $\iota$ and $\operatorname{id}_{R_\epsilon}$ and whose quotient-ring maps are respectively $\operatorname{id}_R$ and $\pi$.

For $f\in\mathscr F(A/R)$ define $$\langle v,f\rangle_\epsilon=[\epsilon]\bigl(f(\alpha)-f(\beta)\bigr)\in R,$$ where $[\epsilon](a+b\epsilon)=b$. A functional $\lambda\in D_{\rm dR}(A)$ and a tangent vector $v$ satisfy the *tangent-evaluation relation* if $$\lambda(\operatorname{cl}f)=\langle v,f\rangle_\epsilon$$ for every $f\in\mathscr F(A/R)$ whose class is primitive. The *Lie exactness condition* consists of both assertions: every $\lambda\in D_{\rm dR}(A)$ satisfies this relation with exactly one tangent vector, and every tangent vector satisfies it with at least one such functional.

**The divided-power Chern condition.** Let $I\subseteq R$ carry divided powers $\gamma$, let $X\to\operatorname{Spec}R$ be a morphism, and let $L$ be a line bundle on $X$ with a chosen presentation by an open cover $(U_i)_{i\in\mathcal I}$ and units $g_{ij}\in\Gamma(U_i\cap U_j,\mathcal O_X)^\times$. Use the convention $g_{ii}=1$ and $g_{ij}g_{jk}=g_{ik}$ on triple intersections, with local section coefficients satisfying $s_i=g_{ij}s_j$.

Let $\mathcal C_L$ be the full subcategory of $\mathcal C_\gamma(X/R)$ consisting of the objects $T$ whose reduced point $x_T:\operatorname{Spec}B_{T,0}\to X$ factors through some $U_i$. For $a\in J_T$, put $$\operatorname{Exp}_{\delta_T}(a)=\sum_{n\ge0}\delta_{T,n}(a).$$ This sum has finite support by the nilpotence condition on $\delta_T$.

A class $z\in H^2_\gamma(X/R)$ satisfies the *divided-power Chern condition for $L$* if there exist:

- a choice $i(T)\in\mathcal I$ for every $T\in\mathcal C_L$ such that $x_T$ factors through $U_{i(T)}$;
- an element $u(f)\in B_{T'}$ for every arrow $f:T\to T'$ of $\mathcal C_L$;
- a $2$-cocycle $\ell$ on $\mathcal C_L$ with its coefficient algebras $B_T$;

such that the following conditions hold. For every arrow $f:T\to T'$, $$\pi_{T'}(u(f))=x_{T'}^*g_{i(T'),i(T)}.$$ Here the right side is evaluation in $B_{T',0}$ on the overlap; the arrow ensures that $x_{T'}$ factors through both opens. For every composable pair $T\xrightarrow{f}T'\xrightarrow{g}T''$, require $$\ell(f,g)\in J_{T''},\qquad \operatorname{Exp}_{\delta_{T''}}(\ell(f,g))\,u(g\circ f)=g_*u(f)\,u(g).$$ Finally, the restriction of $z$ to $H^2(\mathcal C_L,B)$ is $[\ell]$.

**Chern pairings on the primitive dual.** Let $A\to S$ be a group scheme and let $S\to\operatorname{Spec}R$ be a morphism. For a line bundle $L$ on $A$, an $R$-bilinear form $\psi$ on $D_\gamma(A/S)$ is a *Chern pairing for $L$* if there exist $n\in\mathbb N$ and classes $a_k,b_k\in P_\gamma(A/S)$ for $0\le k<n$ such that $\sum_{k=0}^{n-1}a_k\smile b_k$ satisfies the divided-power Chern condition for $L$ and $$\psi(\lambda,\mu)=\sum_{k=0}^{n-1}\bigl(\lambda(a_k)\mu(b_k)-\lambda(b_k)\mu(a_k)\bigr)$$ for all $\lambda,\mu\in D_\gamma(A/S)$. Empty families, with zero sums, are allowed.
