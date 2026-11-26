---
{
  "module": "src/Development/WeilBound/RepresentationTheoryGL/HolomorphicDiscreteSeries/LowestKTypeModels/Models.lean",
  "declarations": [
    "PositivityTheory.RgHe.LowestKTypeModel.ofInt"
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

## A nonzero discrete-series coefficient integral gives an intertwiner

[Theorem REP.1489](https://andrewodesky.com/rh/lean/PositivityTheory.RgHe.LowestKTypeModel.ofInt/)

Let $n\ge2$, let $\epsilon\in\{\pm1\}^{n+1}$ and $\epsilon'\in\{\pm1\}^n$, and choose a coordinate embedding $e:U(J_{\epsilon'})\hookrightarrow U(J_\epsilon)$ obtained by adding one positive coordinate. Assume that $\epsilon$ has at least one negative coordinate and that its number of negative coordinates is at most its number of positive coordinates. Let $\lambda_1>\cdots>\lambda_{n+1}$ and $\mu_1>\cdots>\mu_n$ satisfy $$\lambda_i-n/2\in\mathbb Z,\qquad \mu_j-(n-1)/2\in\mathbb Z,$$ $$|\lambda_i-\lambda_j|\ge200(n+1)^3\ (\epsilon_i\ne\epsilon_j),\qquad |\mu_i-\mu_j|\ge200(n+1)^3\ (\epsilon'_i\ne\epsilon'_j).$$ Let $\pi,\sigma$ be any discrete-series representations with these signed parameters on complex Hilbert spaces $H,H'$, and let $\nu$ be any Haar measure on $U(J_{\epsilon'})$. Let $w\in H'$ be a unit vector in the lowest $K$-type subspace of $\sigma$, defined below. If some $a,b\in H$ satisfy $$\int_{U(J_{\epsilon'})}\overline{\langle w,\sigma(h)w\rangle}\,\langle b,\pi(e(h))a\rangle\,d\nu(h)\ne0,$$ then there is a nonzero bounded complex-linear map $j:H'\to H$ with $j\sigma(h)=\pi(e(h))j$ for every $h$.
