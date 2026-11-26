---
{
  "module": "src/Formalism/FormalGroupWitt/FormalGroupWittProofs/CoeffV.lean",
  "declarations": [
    "Formalism.FG.coeff_bound_vector"
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

## Coefficient bounds for a vector power series functional equation

[Theorem PHT.1071](https://andrewodesky.com/rh/lean/Formalism.FG.coeff_bound_vector/)

Let $K$ be a characteristic-zero ultrametric normed field, let $p$ be prime, let $h$ be a positive integer, and put $q=p^h$. Suppose $|p|<1$ and a ring homomorphism $\sigma:K\to K$ satisfies $$|\sigma(a)-a^q|\le|p|\qquad(|a|\le1).$$ Let $I$ be finite, let $M=(M_{jk})_{j,k\in I}$ have $|M_{jk}|\le1$, and let $\tau$ be any set of variables. Suppose $f_j\in K[[X_t:t\in\tau]]$ have zero constant coefficient and every coefficient of $$f_j(X)-p^{-1}\sum_{k\in I}M_{jk}\,\sigma(f_k)(X^q)$$ has norm at most one, for every $j\in I$. Then for every $j$ and finitely supported multi-index $n:\tau\to\mathbb Z_{\ge0}$ there is an integer $k\ge0$ such that $$q^k\mid n(t)\quad(t\in\tau),\qquad |[X^n]f_j|\,|p|^k\le1.$$
