---
{
  "module": "src/Development/AutomorphicArithmetic/Foundations/Convolution/TraceSplitting/CoreLift.lean",
  "declarations": [
    "UpperTheory.ConvolutionTheory.T.coreLift"
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

## Cyclic spectral lifting from trace and matching inputs

[Theorem AGR.1165](https://andrewodesky.com/rh/lean/UpperTheory.ConvolutionTheory.T.coreLift/)

Assume the source's spectral trace-identity package and geometric matching package. Let $E/F$ be a cyclic Galois extension of prime degree of totally complex number fields, with generator $\sigma$, and let $n\ge1$. On the norm-one adelic groups $\operatorname{GL}_n(\mathbb A_E)^1$ and $\operatorname{GL}_n(\mathbb A_F)^1$, choose Haar measures $\mu_E,\mu_F$. Let $\theta$ be a Galois-twist datum for $\sigma$, including its induced linear operator $U_\theta$ on the cuspidal $L^2$ space over $E$.

Let $V$ be an irreducible closed summand of the cuspidal $L^2$ space over $F$, with infinitesimal-character multisets $\Lambda_\tau$ at every $\tau:F\hookrightarrow\mathbb C$ and spherical Satake multisets $t_v$ outside a finite set of finite places. Define $$\Lambda'_\tau=\Lambda_{\tau|_F},\qquad t'_w=\{\alpha^{f(w/v)}:\alpha\in t_v\},\quad v=w|_F,$$ with multiplicities and residue degree $f(w/v)$. Assume the exclusion condition in the conventions for $(\Lambda',t')$ at every finite set of places. Then there is an irreducible closed cuspidal $L^2$ summand $V'$ over $E$ such that $$U_\theta(V')=V',$$ and $V'$ has infinitesimal characters $\Lambda'$ everywhere and spherical Satake parameters $t'$ outside a finite set.
