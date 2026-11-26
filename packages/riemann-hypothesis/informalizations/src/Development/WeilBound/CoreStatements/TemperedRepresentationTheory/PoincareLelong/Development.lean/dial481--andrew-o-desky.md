---
{
  "module": "src/Development/WeilBound/CoreStatements/TemperedRepresentationTheory/PoincareLelong/Development.lean",
  "declarations": [
    "PositivityTheory.Tls2.Pl.lelongPolyLimit"
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

## Regularized Poincare–Lelong limit for a polynomial

[Theorem AG.1722](https://andrewodesky.com/rh/lean/PositivityTheory.Tls2.Pl.lelongPolyLimit/)

Assume the linear Poincaré–Lelong limit theorem specified in the conventions below: for a prime affine complex variety, a linear function not identically zero, a compactly supported smooth test function and smooth auxiliary potentials, the divisor integral is the limit of the corresponding regularized logarithmic integrals.

Let $J\subseteq\mathbb C[x_1,\ldots,x_n]$ be prime with $\dim\mathbb C[x]/J=d+1$, and let $p\notin J$. Write $X=V(J)$. Let $f,k,\varphi_1,\ldots,\varphi_d$ be real-valued functions smooth on an open neighborhood of $X$, with $f$ compactly supported and $k>0$ on $X$. Put $dd^c=(i/\pi)\partial\bar\partial$, and interpret integrals on affine varieties by integration on their regular loci, using the finite-projection sheet integral defined in ([Dominated convergence for cutoff sheet integrals](https://andrewodesky.com/rh/lean/GroundTheory.Heights%E2%82%82.Heights.CutOffDominated.full/)) at singular points. Then $$\lim_{\varepsilon\downarrow0}\int_X f\,dd^c\!\left(\frac12\log(|p|^2+\varepsilon k^2)\right)\wedge\bigwedge_{j=1}^{d}dd^c\varphi_j =\sum_W m_W\int_{V(W)}f\,\bigwedge_{j=1}^{d}dd^c\varphi_j,$$ where $W$ runs over the minimal primes of $J+(p)$ and $m_W$ is the length of $(\mathbb C[x]/(J+(p)))_W$ over $\mathbb C[x]_W$.
