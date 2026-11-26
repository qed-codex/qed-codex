---
{
  "module": "src/Development/AutomorphicArithmetic/Foundations/Convolution/SphericalIdeles/SmoEq.lean",
  "declarations": [
    "UpperTheory.ConvolutionTheory.Sph.smoEq"
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

## Equality of cuspidal subspaces from almost all Satake parameters

[Theorem AGR.1306](https://andrewodesky.com/rh/lean/UpperTheory.ConvolutionTheory.Sph.smoEq/)

Let $K$ be a totally complex number field and $n\ge1$. Let $P,P'$ be irreducible, nonzero, invariant subspaces of smooth cuspidal automorphic forms on $\mathrm{GL}_n(\mathbb A_K)$, in the smooth realization specified in the conventions of ([Cuspidal projection preserves determinant support](https://andrewodesky.com/rh/lean/UpperTheory.V.Z.Tf.GlobalTraceComparison.Pi.pSupp_pf/)). Suppose that at all but finitely many finite places $w$, there is a multiset $B_w$ of nonzero complex numbers which is a Satake parameter for both $P$ and $P'$. Then $$P=P'.$$
