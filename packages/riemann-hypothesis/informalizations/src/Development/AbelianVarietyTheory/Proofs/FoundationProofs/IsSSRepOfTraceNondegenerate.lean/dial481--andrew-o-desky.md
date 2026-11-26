---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/FoundationProofs/IsSSRepOfTraceNondegenerate.lean",
  "declarations": [
    "GlobalTheory.TraceSemisimple.isSSRep_of_trace_nondegenerate"
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

## Semisimplicity from a nondegenerate trace pairing

[Theorem REP.0264](https://andrewodesky.com/rh/lean/GlobalTheory.TraceSemisimple.isSSRep_of_trace_nondegenerate/)

Let $K$ be a field, $\Gamma$ a group, $n\ge0$, and $\rho:\Gamma\to\operatorname{GL}_n(K)$ a representation. Put $$A=\operatorname{span}_K\{\rho(g):g\in\Gamma\}\subseteq M_n(K).$$ Assume that, for every $x\in A$, $$\bigl(\operatorname{tr}(x\rho(g))=0\text{ for every }g\in\Gamma\bigr)\ \Longrightarrow\ x=0.$$ Then $\rho$ is semisimple: every invariant subspace of $K^n$ has an invariant complementary subspace.
