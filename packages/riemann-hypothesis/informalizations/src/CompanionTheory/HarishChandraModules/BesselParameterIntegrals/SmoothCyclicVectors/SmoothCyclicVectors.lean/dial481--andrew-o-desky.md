---
{
  "module": "src/CompanionTheory/HarishChandraModules/BesselParameterIntegrals/SmoothCyclicVectors/SmoothCyclicVectors.lean",
  "declarations": [
    "CompanionTheory.D.Upq.Sm.smooth_cyclic_vectors"
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

## Approximation of smooth vectors by translates of a lowest vector

[Theorem REP.1637](https://andrewodesky.com/rh/lean/CompanionTheory.D.Upq.Sm.smooth_cyclic_vectors/)

Let $k,r\ge0$, $n=2r+k+1$, and let $H_0$ be the Hermitian matrix with entries $1$ at $(i,n-1-i)$ when $i<r$ or $n-1-i<r$, entries $1$ on the diagonal $r\le i<r+k$, entry $-1$ at $(r+k,r+k)$, and zero elsewhere. Put $G=\{g:g^*H_0g=H_0\}$. Choose signs $\epsilon_i\in\{\pm1\}$ and strictly decreasing real numbers $\lambda_i$ with $\lambda_i-(n-1)/2\in\mathbb Z$.

Let $\sigma$ be a representation on a complex Hilbert space satisfying the discrete-series realization conditions of ([Recognition from a compact type and a Casimir eigenvalue](https://andrewodesky.com/rh/lean/GlobalTheory.PsCo.PcEF.eq_discreteSeries_of_lowestKType_casimir/)) with parameter $\lambda$ after a unitary change of coordinates taking $H_0$ to $\operatorname{diag}(\epsilon)$. Let $w$ be a unit vector in the sum of the compact subrepresentations of highest weight $\lambda+\rho_n-\rho_c$ after such a change of coordinates, with $\rho_n,\rho_c$ as in ([Recognition from a compact type and a Casimir eigenvalue](https://andrewodesky.com/rh/lean/GlobalTheory.PsCo.PcEF.eq_discreteSeries_of_lowestKType_casimir/)). For every smooth vector $x$, every finite list $D_1,\ldots,D_t$ of ordered products of derivatives $d\sigma(X)$ with $X^*H_0+H_0X=0$, and every $\delta>0$, there are $N\ge0$, $c_i\in\mathbb C$ and $g_i\in G$ such that $$\sum_{j=1}^{t}\left\|D_j\left(x-\sum_{i=1}^{N}c_i\sigma(g_i)w\right)\right\|<\delta.$$ The empty product of derivatives is the identity.
