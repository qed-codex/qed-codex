---
{
  "module": "src/Development/WeilBound/RepresentationTheoryGL/DiscreteSeries/DiscreteSeriesCovers/FdTopB.lean",
  "declarations": [
    "PositivityTheory.RgFd.B.formalDegreeCompactDual"
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

## Formal degree with compact-dual normalization

[Theorem REP.0113](https://andrewodesky.com/rh/lean/PositivityTheory.RgFd.B.formalDegreeCompactDual/)

For every pair $p,q\ge0$, fix a Haar measure $\mu^{\mathrm{cd}}_{p,q}$ on $U(p,q)$. Assume the compact-dual normalization:

1. $\mu^{\mathrm{cd}}_{N,0}$ is a probability measure on $U(N)$.
2. In exponential coordinates at the identity, $\mu^{\mathrm{cd}}_{p,q}$ and $\mu^{\mathrm{cd}}_{p+q,0}$ have the same finite positive density with respect to the respective reference Lebesgue measures on their Lie algebras. Density means the limit of the measure of $\exp(B_t)$ divided by the Lebesgue measure of $B_t$ as $t\downarrow0$.

For a sign vector $\epsilon\in\{+,-\}^N$, let $G_\epsilon$ be the unitary group of the diagonal form with those signs and let $\mu^0_\epsilon$ be its reference Haar measure. Choose nonnegative scalars $s_{N,\epsilon}$. Assume that every coordinate permutation identifying $G_\epsilon$ with $U(p,q)$, with the positive coordinates first, carries $s_{N,\epsilon}\mu^0_\epsilon$ to $\mu^{\mathrm{cd}}_{p,q}$ on every measurable set.

Let $\lambda_1>\cdots>\lambda_N$ satisfy $\lambda_i-(N-1)/2\in\mathbb Z$. Let $\pi$ be a discrete-series representation of $G_\epsilon$ with parameter $\lambda$, acting on a complex Hilbert space, and let $w\ne0$. Then $$\frac{\|w\|^4}{\displaystyle\int_{G_\epsilon}|\langle w,\pi(g)w\rangle|^2\,d(s_{N,\epsilon}\mu^0_\epsilon)(g)}=\frac{\displaystyle\prod_{i<j}|\lambda_i-\lambda_j|}{\displaystyle\prod_{i<j}(j-i)}.$$ Empty products have value one.
