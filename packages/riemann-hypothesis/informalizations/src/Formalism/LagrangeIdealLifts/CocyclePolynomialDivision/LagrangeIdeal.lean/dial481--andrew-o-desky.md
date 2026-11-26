---
{
  "module": "src/Formalism/LagrangeIdealLifts/CocyclePolynomialDivision/LagrangeIdeal.lean",
  "declarations": [
    "Formalism.LIFT.lagrangian_ideal_holds",
    "Formalism.LIFT.lagrangian_ideal_integral_holds"
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

## A power in the ideal of two products of linear factors

[Theorem ALG.0692](https://andrewodesky.com/rh/lean/Formalism.LIFT.lagrangian_ideal_holds/)

Let $R$ be a commutative domain, $\ell\in R$, and $S_1,S_2$ disjoint finite subsets of a set $I$. Let $c:I\to R$ and $w:I\times I\to\mathbb N$. Assume $c_a-c_b$ is associated to $\ell^{w(a,b)}$ whenever $a\in S_1$, $b\in S_1\cup S_2$, and $a\ne b$. Set $$M=\max_{a\in S_1}\left(\sum_{b\in S_2}w(a,b)+ \sum_{a'\in S_1\setminus\{a\}}w(a,a')\right),$$ with $M=0$ if $S_1$ is empty. Then, in $R[X]$, $$\ell^M\in\left(\prod_{a\in S_1}(X-c_a),\ \prod_{b\in S_2}(X-c_b)\right).$$

In particular, when $I=\mathbb Z$ and $\ell=p\cdot1_R$ for a prime $p$, take $w(a,b)=v_p(a-b)$ for distinct $a,b$. For a nonzero integer $n$, $v_p(n)$ is the largest nonnegative integer $k$ such that $p^k\mid n$. Under the same association hypothesis, $p^M$ lies in the displayed ideal, with $M$ computed from these weights and $p$ viewed as an element of $R$.
