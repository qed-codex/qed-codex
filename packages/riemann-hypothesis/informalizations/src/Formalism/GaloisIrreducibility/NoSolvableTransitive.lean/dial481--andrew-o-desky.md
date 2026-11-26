---
{
  "module": "src/Formalism/GaloisIrreducibility/NoSolvableTransitive.lean",
  "declarations": [
    "Formalism.GaloisIrreducibility.irred",
    "Formalism.GaloisIrreducibility.lemmaA"
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

## Irreducibility from incompatible power-orbit sizes

[Theorem ALG.0256](https://andrewodesky.com/rh/lean/Formalism.GaloisIrreducibility.irred/)

Let $K$ be algebraically closed and $V$ a finite-dimensional $K$-vector space. Let $P,I$ be sets. For each $v\in P$, choose $T_v\in\operatorname{End}_K(V)$, $F_v\in\operatorname{GL}_K(V)$, $q_v\ge0$, a finite set $I_v\subseteq I$, and finite subsets $O_{v,i}\subseteq K$ for $i\in I$. Suppose $$F_vT_v=T_v^{q_v}F_v,\qquad \operatorname{Roots}(\det(X-T_v))=\sum_{i\in I_v}[O_{v,i}],$$ where $[O]$ is the multiset containing each element of $O$ once. For $i\in I_v$, assume $O_{v,i}$ is stable under $x\mapsto x^{q_v}$ and, for every $x,y\in O_{v,i}$, some iterate sends $x$ to $y$. Assume that for every integer $a$ with $1\le a$ and $2a\le\dim_KV$, there is $v\in P$ for which $a$ is not a sum of a submultiset of $(|O_{v,i}|)_{i\in I_v}$.

Every subspace of $V$ stable under all $T_v$ and all $F_v$ is either $0$ or $V$.

## Dimensions of subquotients from power-map orbits

[Theorem ALG.0445](https://andrewodesky.com/rh/lean/Formalism.GaloisIrreducibility.lemmaA/)

Let $K$ be algebraically closed, $V$ a finite-dimensional $K$-vector space, $\tau\in\operatorname{End}_K(V)$, $F\in\operatorname{GL}_K(V)$, and $q\ge0$ an integer, with $F\tau=\tau^qF$. Let $I$ be finite and let $O_i\subset K$ be finite sets, each stable under $z\mapsto z^q$, such that every element of $O_i$ reaches every other by iterating this map. Suppose the multiset of roots of $\det(X-\tau)$ is $$\sum_{i\in I}[O_i],$$ where $[O_i]$ includes every element once; different sets may overlap. If $W_1\subseteq W_2\subseteq V$ are stable under both $\tau$ and $F$, there is $J\subseteq I$ such that $$\dim_KW_2-\dim_KW_1=\sum_{i\in J}|O_i|.$$
