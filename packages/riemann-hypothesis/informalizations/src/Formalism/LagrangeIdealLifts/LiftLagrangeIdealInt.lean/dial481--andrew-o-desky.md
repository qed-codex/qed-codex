---
{
  "module": "src/Formalism/LagrangeIdealLifts/LiftLagrangeIdealInt.lean",
  "declarations": [
    "Formalism.LIFT.lift_LagrangeIdealInt",
    "Formalism.LIFT.lift_WBTail"
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

## Replacing a power of a formal parameter by an explicit prime power

[Theorem PHT.0757](https://andrewodesky.com/rh/lean/Formalism.LIFT.lift_WBTail/)

Let $\ell$ be prime and let $A$ be a commutative $\mathbb Z_\ell$-algebra. Choose commuting $\mathbb Z_\ell$-algebra endomorphisms $\varphi_A,\gamma_A$, elements $X,Q\in A$, and $u\in\mathbb Z_\ell^\times$ satisfying $$\varphi_A(X)=XQ,\qquad\gamma_A(X)=X(u+Xt),\qquad\gamma_A(Q)=Q(1+Xt')$$ for some $t,t'\in A$ with $1+Xt'$ a unit. Fix $M\ge0$. For $i=1,2$, let $D_i$ be an $A$-module with the compatible $\mathbb Z_\ell$-module structure, let $N_i\subseteq D_i$ be an $A$-submodule, and let $\varphi_i,\gamma_i$ satisfy the module conditions below.

Let $f:D_1\to D_2$ be $A$-linear, commute with both operators, and satisfy $f(N_1)\subseteq N_2$. Let $s,a\ge0$ with $s\ge1$, $s\ge2$ if $\ell=2$, and $v_\ell(u-1)=s$. If $$X^aN_2\subseteq f(N_1),$$ then $$\ell^{\,2as+v_\ell((2a)!)}N_2\subseteq f(N_1).$$

## A power in the ideal of two products of linear factors

[Theorem ALG.0692](https://andrewodesky.com/rh/lean/Formalism.LIFT.lagrangian_ideal_holds/)

Let $R$ be a commutative domain, $\ell\in R$, and $S_1,S_2$ disjoint finite subsets of a set $I$. Let $c:I\to R$ and $w:I\times I\to\mathbb N$. Assume $c_a-c_b$ is associated to $\ell^{w(a,b)}$ whenever $a\in S_1$, $b\in S_1\cup S_2$, and $a\ne b$. Set $$M=\max_{a\in S_1}\left(\sum_{b\in S_2}w(a,b)+ \sum_{a'\in S_1\setminus\{a\}}w(a,a')\right),$$ with $M=0$ if $S_1$ is empty. Then, in $R[X]$, $$\ell^M\in\left(\prod_{a\in S_1}(X-c_a),\ \prod_{b\in S_2}(X-c_b)\right).$$

In particular, when $I=\mathbb Z$ and $\ell=p\cdot1_R$ for a prime $p$, take $w(a,b)=v_p(a-b)$ for distinct $a,b$. For a nonzero integer $n$, $v_p(n)$ is the largest nonnegative integer $k$ such that $p^k\mid n$. Under the same association hypothesis, $p^M$ lies in the displayed ideal, with $M$ computed from these weights and $p$ viewed as an element of $R$.
