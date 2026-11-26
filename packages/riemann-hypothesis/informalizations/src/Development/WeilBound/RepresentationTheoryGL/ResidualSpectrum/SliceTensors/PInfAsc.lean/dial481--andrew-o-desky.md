---
{
  "module": "src/Development/WeilBound/RepresentationTheoryGL/ResidualSpectrum/SliceTensors/PInfAsc.lean",
  "declarations": [
    "PositivityTheory.Rg.Rs.infAsc_holds"
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

## Infinitesimal characters along a repeated cuspidal induction

[Theorem REP.1409](https://andrewodesky.com/rh/lean/PositivityTheory.Rg.Rs.infAsc_holds/)

Let $E$ be a totally complex number field and let $N,a,d\ge0$. Let $V$ be a discrete automorphic subspace of smooth automorphic functions on $\mathrm{GL}_N(\mathbb A_E)$ in the realization specified in the conventions of ([Cuspidal projection preserves determinant support](https://andrewodesky.com/rh/lean/UpperTheory.V.Z.Tf.GlobalTraceComparison.Pi.pSupp_pf/)), and let $\pi$ be a cuspidal automorphic subspace on $\mathrm{GL}_a(\mathbb A_E)$. Assume the following ascending-induction embedding condition: $N=ad$, and for $0\le i<d$ there are Hecke characters $\nu_i$ with $$\nu_i=|\cdot|^{(a-1)s_i},\qquad s_i=(d-1)/2-i,$$ such that an ambient linear map, injective on $V$ and intertwining the adelic and infinitesimal operators on $V$ in this realization, maps $V$ into its induced automorphic function space from the factors $\pi\otimes\nu_i$.

For every complex embedding $\tau$ and every infinitesimal-character multiset $m$ of $V$ at $\tau$, there is an infinitesimal-character multiset $m_0$ of $\pi$ at $\tau$ with $$m=\bigsqcup_{i=0}^{d-1}(m_0+s_i).$$
