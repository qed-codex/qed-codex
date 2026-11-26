---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/ExistsLimitRep.lean",
  "declarations": [
    "GlobalTheory.Cong.exists_limit_rep"
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

## A semisimple representation with a prescribed limiting trace

[Theorem AGR.1345](https://andrewodesky.com/rh/lean/GlobalTheory.Cong.exists_limit_rep/)

Let $\ell$ be prime, $\Gamma$ a compact topological group, $a\ge0$, and $x:J\to\Gamma$ a map with dense image. Let $L\subseteq\overline{\mathbb Q}_\ell$ be a finite extension of $\mathbb Q_\ell$, and let $\theta:J\to L$. Let $\mathcal C$ be a set of continuous homomorphisms $\Gamma\to\operatorname{GL}_a(\overline{\mathbb Q}_\ell)$.

For a set $S\subseteq\overline{\mathbb Q}_\ell^{J}$ and $\eta:J\to\overline{\mathbb Q}_\ell$, define the following approximation condition: for every $\varepsilon>0$ there are a finite subset $S_0\subseteq S$ and coefficients $c_\xi\in\overline{\mathbb Q}_\ell$ such that $$\left|P(\eta)-\sum_{\xi\in S_0}c_\xi P(\xi)\right|_\ell\le\varepsilon\qquad\text{for every }P\in\mathbb Z[X_j:j\in J].$$ Assume this condition for $\eta=\theta$ and $S=\{j\mapsto\operatorname{tr}\rho(x_j):\rho\in\mathcal C\}$.

There is a continuous semisimple representation $r:\Gamma\to\operatorname{GL}_a(\overline{\mathbb Q}_\ell)$ such that $$\operatorname{tr}r(x_j)=\theta_j\quad(j\in J).$$ The same approximation condition, now with index set $\Gamma$, holds for $\operatorname{tr}r$ and $\{\operatorname{tr}\rho:\rho\in\mathcal C\}$.
