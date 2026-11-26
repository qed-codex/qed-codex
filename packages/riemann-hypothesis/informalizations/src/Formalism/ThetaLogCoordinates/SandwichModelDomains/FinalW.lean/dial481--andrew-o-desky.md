---
{
  "module": "src/Formalism/ThetaLogCoordinates/SandwichModelDomains/FinalW.lean",
  "declarations": [
    "Formalism.InvariantFactorPaths.INST.Top.coreQp",
    "Formalism.InvariantFactorPaths.INST.Top.sandwichDomain",
    "Formalism.InvariantFactorPaths.INST.Top.sandwichZp"
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

## An explicit denominator between two polynomial Weyl modules

[Theorem REP.1046](https://andrewodesky.com/rh/lean/Formalism.InvariantFactorPaths.INST.Top.sandwichDomain/)

Let $p$ be prime, let $0\le n\le r$ be integers, and let $\nu_1\ge\cdots\ge\nu_n\ge0$ be integers. Let $l\ge0$ be an integer satisfying either $\nu_j\le l$ for every $j$, or $n=r$ and $\nu_i\le\nu_j+l$ for every $i,j$.

Let $O$ be a commutative integral domain in which every integer not divisible by $p$ has unit image. With the modules $\nabla_\nu(O),\Delta_\nu(O)$ of ([Polynomial Weyl modules and row substitutions](https://andrewodesky.com/rh/lean/Formalism.GradedWeylDivisibility.dualWeyl/)), $$p^s\nabla_\nu(O)\subseteq\Delta_\nu(O)\subseteq\nabla_\nu(O),\qquad s=\frac{r(r-1)}2\operatorname{log}_p(l+r-1).$$

## A p-power carries a dual Weyl lattice into a Weyl lattice

[Theorem REP.0941](https://andrewodesky.com/rh/lean/Formalism.InvariantFactorPaths.INST.Top.coreQp/)

Let $p$ be prime, let $0\le n\le r$ be integers, and let $\nu_1\ge\cdots\ge\nu_n\ge0$ be integers. Use ([Polynomial Weyl modules and row substitutions](https://andrewodesky.com/rh/lean/Formalism.GradedWeylDivisibility.dualWeyl/)) for $\nabla_\nu$ and $\Delta_\nu$.

Suppose $\ell\ge0$ is an integer and, for every $f,g\in \nabla_\nu(\mathbb Q_p)$, every monomial $m$ in the support of $f$, every monomial $m'$ in the support of $g$, and every row $i$, the total exponent in row $i$ of $m$ is at most that of $m'$ plus $\ell$. Then $$p^e\nabla_\nu(\mathbb Z_p)\subseteq \Delta_\nu(\mathbb Z_p),\qquad e=\binom r2\left\lfloor\log_p\bigl(\max\{\ell+r-1,1\}\bigr)\right\rfloor.$$

## A prime-power inclusion between polynomial Weyl lattices

[Theorem REP.0996](https://andrewodesky.com/rh/lean/Formalism.InvariantFactorPaths.INST.Top.sandwichZp/)

Let $p$ be prime, let $0\le n\le r$, and let $\nu_1\ge\cdots\ge\nu_n\ge0$ be integers. Let $l\ge0$ be an integer satisfying either $\nu_i\le l$ for every $i$, or $n=r$ and $\nu_i\le\nu_j+l$ for every $i,j$. With the modules of ([Polynomial Weyl modules and row substitutions](https://andrewodesky.com/rh/lean/Formalism.GradedWeylDivisibility.dualWeyl/)) over $\mathbb Z_p$, $$p^{\binom r2\,\lfloor\log_p(l+r-1)\rfloor}\nabla_\nu\subseteq\Delta_\nu.$$
