---
{
  "module": "src/Development/AbelianVarietyTheory/Definitions/AutomorphicMembership/ExistsIvDOfDefinite.lean",
  "declarations": [
    "GlobalTheory.LocM.InvFun"
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

## Polarizing fan conventions for toroidal compactifications

[Definition / hypothesis AG.D240](https://andrewodesky.com/rh/lean/GlobalTheory.LocM.InvFun/)

The following conventions specify a polarizing fan, including the condition on self-intersections, in ranks at most $q$ over a ring $O$ with involution $a\mapsto\bar a$. The two cases used here are $O=\mathbb Z$ with the identity involution and $O=\mathcal O_E$ with CM conjugation.

An invariant function $\phi$ assigns a real number to every real-valued function of two variables on $O^n$, for every $n\ge0$. Its value is unchanged by pullback along a surjective $O$-linear map between finite free modules, and its value in rank zero is zero. Consequently $\phi(B)$ is defined for a function $B:X\times X\to\mathbb R$ on a finitely generated $O$-module $X$, by pulling $B$ back along any finite free presentation.

For such $X$, let $\mathcal B(X)$ be the abelian group of integral bilinear forms satisfying $$\beta(x,y)=\beta(y,x),\qquad \beta(ax,y)=\beta(x,\bar a y).$$ Let $\mathcal C(X)$ consist of the real-valued forms pulled back from positive definite symmetric balanced forms along a surjection from $X$ onto a projective $O$-module. Balance means the displayed identity with $\beta$ replaced by a real-valued form.

A cone for $\phi$ on $X$ is a finite ordered list $\gamma_1,\ldots,\gamma_m\in\mathcal B(X)$ satisfying these conditions. Each $\gamma_i$ is nonnegative on the diagonal, and the list extends to an integral basis of $\mathcal B(X)$. For all $c_i\ge0$, $$\phi\!\left(\sum_i c_i\gamma_i\right)=\sum_i c_i\phi(\gamma_i).$$ There are an integer $N>0$ and an integral linear functional $\ell$ on the group of all integral bilinear forms on $X$ such that $$\ell(\gamma_i)=N\phi(\gamma_i),\qquad N\phi(\beta)\le\ell(\beta)$$ for every $\beta\in\mathcal B(X)$ nonnegative on the diagonal. Equality in the latter inequality implies $k\beta=\sum_i n_i\gamma_i$ for some integer $k>0$ and integers $n_i\ge0$.

The polarizing-fan condition in ranks at most $q$ requires the following for every finitely generated projective $O$-module $X$ of rank at most $q$. On $\mathcal C(X)$, $\phi$ is homogeneous for nonnegative scalars and superadditive. On integral balanced forms nonnegative on the diagonal it takes integral values, strictly positive away from zero. Every sublist of a cone is a cone. Every element of $\mathcal C(X)$ is a nonnegative real linear combination of the generators of a cone. There is a finite subset $S\subseteq\mathcal B(X)$ such that every cone can be carried, by pullback under one $O$-linear automorphism of $X$, to a list in $S$.

The no-self-intersection condition requires, for every such $X$, every cone $\gamma_1,\ldots,\gamma_m$, every $O$-linear automorphism $u$ of $X$ and every $i,j$, $$u^*\gamma_i=\gamma_j\quad\Longrightarrow\quad i=j.$$
